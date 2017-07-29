from django.conf.urls import include, url
from django.contrib import admin

from bigData import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'getMoving.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), url(r'^$', views.index, name='index'),
    url(r'^cityDevelopment/', views.jsonp, {'tileid': 6, 'callback': 'eqfeed_callback'}),
    url(r'^publicToilets/', views.jsonp, {'tileid': 13, 'callback': 'ptfeed_callback'}),
    url(r'^childcareCenters/', views.jsonp, {'tileid': 20, 'callback': 'ccfeed_callback'}),
    url(r'^drinkingFountains/', views.jsonp, {'tileid': 19, 'callback': 'dffeed_callback'}),
    url(r'^cctvCameras/', views.jsonp, {'tileid': 23, 'callback': 'cctvfeed_callback'}),
    url(r'^educationFacilities/', views.jsonp, {'tileid': 15, 'callback': 'effeed_callback'}),
    url(r'^aquaticFacilities/', views.jsonp, {'tileid': 22, 'callback': 'affeed_callback'}),
    url(r'^serverDemo/', views.serverDemo, name='serverDemo'),
    url(r'^MyBallarat/', views.MyBallarat, name='MyBallarat'),
    url(r'^ajax_request', views.ajax_return),
    url(r'^melTest/', views.melTest, name='melTest'),
    url(r'^MTest/', views.MTest, name='MTest'),
    url(r'^TileTab/', views.TileTab, name='TileTab'),
	url(r'^register/', views.register_user, name='register_user'),
    url(r'^MyBallarat/', views.MyBallarat, name='MyBallarat'),
    url(r'^melTest/', views.melTest, name='melTest'),
	url(r'^login/', views.login_view),
	url(r'^auth/$', views.auth_view),
	url(r'^auth/loggedin/$', views.loggedin),
	url(r'^logout/$', views.logout_view),
	url(r'^invalid/$', views.invalid_login),
    url(r'^admin/', include(admin.site.urls)),

]
