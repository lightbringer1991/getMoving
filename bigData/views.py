from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from .models import Tile, Tile_Data, Category, Postcode
from django.core.serializers import serialize
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

import json


def index(request):
    return (HttpResponse("Dashboard Development Home Page"))


def jsonp(request, tileid, callback):
    tile = Tile_Data.objects.get(id=tileid)
    pydata = tile.data

    response = callback + u'('
    response += json.dumps(pydata)
    response += u');'

    return HttpResponse(response, content_type="application/javascript")


def serverDemo(request):
    template = loader.get_template('bigData/serverDemo.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def MyBallarat(request):
    tile_list = Tile.objects
    print(tile_list)

    tile_categories = Category.objects.order_by('name')
    tile_data_list = Tile_Data.objects.order_by('name')
    template = loader.get_template('bigData/MyBallarat.html')
    context = RequestContext(request, {'tile_list': tile_list, 'tile_data_list': tile_data_list,
                                        'tile_categories': tile_categories})
    # return HttpResponse("test")
    return HttpResponse(template.render(context))


def TileTab(request):
    template = loader.get_template('bigData/TileTab.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def melTest(request):
    tile_list = Tile.objects.order_by('title')
    template = loader.get_template('bigData/melTest.html')
    context = RequestContext(request, {'tile_list': tile_list})
    return HttpResponse(template.render(context))


def MTest(request):
    tile_list = Tile.objects.order_by('title')
    template = loader.get_template('bigData/MTest.html')
    context = {'tile_list': tile_list, }
    return HttpResponse(template.render(context))


def tile(request):
    template = loader.get_template('bigData/tile.html')
    context = template.Context({'bgcolour': 'Green'})
    return template.render(context)


def tile1_content(request):
    template = loader.get_template('bigData/tile1_content.html')
    context = template.Context({'bgcolour': 'Green'})
    return template.render(context)


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form.save()
        return HttpResponseRedirect('bigData/MyBallarat.html')
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('register.html', args)


def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/MyBallarat')
    else:
        return HttpResponseRedirect('/invalid')


def loggedin(request):
    return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/MyBallarat')


def ajax_return(request):
    if request.method == 'GET':
        requested_tile = request.GET.get('tile_id')
        tile = Tile.objects.get(id=requested_tile)
        tile_data_list = Tile_Data.objects.filter(tile_tiledata__tileId=requested_tile)
        return render_to_response("ajax_request.html", {'tile': tile, 'tile_data_list': tile_data_list})


def get_tile(request):
    if request.method == 'GET':
        data = Postcode.objects.filter(postcode__in=request.GET.getlist('postCodes[]'))
        tileType = request.GET.get('type')
        # return HttpResponse('<span>test tile content</span>', status=201)
        return render_to_response("tile_" + tileType + ".html", {
            'tile_data_list': [{
                'name': 'Emergency Alerts',
                'data': [{
                    'link': 'test link',
                    'location': 'test location',
                    'type': 'test type',
                    'size': 'test size',
                    'status': 'test status',
                    'title': 'test title',
                }]
            }],
            'category': request.GET.getlist('type'),
        });
    else:
        return HttpResponse(status=405)


def get_postcode(request):
    if request.method == 'GET':
        postcode = Postcode.objects.filter(postcode=request.GET.get('code'))[0]
        return HttpResponse(serialize('json', [postcode], fields=('postcode', 'latitude', 'longitude')), status=201)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def get_template(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        template_name = data['templateName']
        print(request.GET.iteritems())
        for key, value in request.GET.iteritems():
            print(value)
        return render_to_response(template_name + ".html", {'data': data['data']})
    else:
        return HttpResponse(status=405)
