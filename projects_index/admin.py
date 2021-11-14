from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
	def languages(self, item):
		return [i.name for i in item.language.all()]
	list_display = ("proj_id", "name", "category", "image", "languages")

admin.site.index_title = "Administration Index"
admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(Category)