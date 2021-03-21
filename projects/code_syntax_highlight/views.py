from django.shortcuts import render
from django.http import HttpResponse
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles, get_style_by_name
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer, guess_lexer, get_lexer_by_name
from django.views.decorators.csrf import csrf_exempt

def home(response):
	#preview = (highlight(code, PythonLexer(), HtmlFormatter(full=True, style=i)) for i in get_all_styles())
	return render(response, 'code-syntax-highlight/main.html', {'lexer_list': get_all_lexers(), 'style_list': get_all_styles(), 'preview': get_all_styles(), 'title': 'Code Syntax Highlighter'})


def get_preview(response, theme=None):
	code = '''
#'''+theme+'''

from some_module import some_function
import some_module as module_name

@decorator(param=1)
def f(x):
	""" Syntax Highlight Demo
	@param x Parameter"""
	s = ("Test", 2+3, {'a':'b'}, x) #Comment

class Foo:
	def __init__(self):
		byte_string = 'newline:\\n also newline:\\x0a'
		text_string = u"Cyrillic Я is \\u042f."
		self.makeSense(whatever=1)
		print(some_function())

	def makeSense(self, whatever)
		self.sense = whatever
x = len('abc)
print(f.__doc__)'''
	return HttpResponse(highlight(code, PythonLexer(), HtmlFormatter(full=True, style=theme)))


@csrf_exempt
def get_formatted_code(response):
	if response.POST:
		return HttpResponse(highlight(response.POST['text'], get_lexer_by_name(response.POST['lexer']), HtmlFormatter(full=True, style=response.POST['style'])))