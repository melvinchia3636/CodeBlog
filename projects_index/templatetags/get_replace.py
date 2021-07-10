from django import template

register = template.Library()

@register.simple_tag
def replace(r, f, t):
	return r.replace(f, t)