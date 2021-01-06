from django import template

register = template.Library()

@register.simple_tag
def getdatetime(o):
	return o.strftime('%d %b %Y')