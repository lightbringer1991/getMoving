from django import template

register = template.Library()


@register.filter
def listify(values, maxitems=4):
    sercomma = ','
    l = len(values)
    if l == 0:
        return ''
    elif l == 1:
        return values[0]
    elif l == 2:
        return values[0] + ' and ' + values[1]
    elif l <= maxitems:
        return ', '.join(values[:l-1]) + sercomma + ' and ' + values[-1]
    else:
        andmoretxt = ' and %d more' % (l - maxitems)
        return ', '.join(values[:maxitems]) + andmoretxt


@register.filter
def to_js_array(values):
    return '[' + ', '.join(map(str, values)) + ']'
