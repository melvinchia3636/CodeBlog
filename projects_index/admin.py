from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
	list_display = ("proj_id", "name", "category", "image")

admin.site.index_title = "Administration Index"
admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(Category)