from django import template

register = template.Library()

@register.simple_tag
def select_check(request, key, value):
    return 'selected="selected"' if request.GET.get(f'{key}') == value else ''

@register.simple_tag
def value_check(request, key):
    value = request.GET.get(key)
    if value == None:
        return "value=0"
    else:
        return f'value={value}'