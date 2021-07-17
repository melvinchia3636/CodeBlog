from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
	list_display = ("__str__", "language", "category", "desc", "star", "fork", "created_at", "license")

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)
admin.site.register(Category)