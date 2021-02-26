from django import template

register = template.Library()

@register.filter
def get_range(lst):
    return range(1, len(lst)+1)