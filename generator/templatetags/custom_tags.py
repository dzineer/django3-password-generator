from django import template

register = template.Library()

@register.filter(name='arange')
def arange(min=1):
    return range(min)
