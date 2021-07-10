from codeblog.wsgi import *
import requests
from projects_index.models import *

add_project = lambda: [Project.objects.create(name=i['name'].replace('-', ' ').title(), icon="https://www.google.com", desc=i['description'] if i['description'] else "", language=Language.objects.get(name=i['language'])) for i in requests.get('https://api.github.com/users/melvinchia3636/repos?per_page=100&sort=updated').json() if i['language']]

#add_project()

for i in requests.get('https://api.github.com/users/melvinchia3636/repos?per_page=100&sort=updated').json():
	try:
		data = Project.objects.get(name=i['name'].replace('-', ' ').title())
		data.repo = i["html_url"]
		data.save()
	except:
		pass