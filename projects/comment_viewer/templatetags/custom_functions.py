from django import template

register = template.Library()

@register.simple_tag
def next_comment(result):
	try:
		return next(result)
	except:
		return None