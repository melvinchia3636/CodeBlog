from django.db import models
from colorfield.fields import ColorField
from django.utils.crypto import get_random_string
import string

def project_image_path(instance, filename):
    return 'project_{0}.{1}'.format(instance.proj_id, filename.split(".")[-1])

class Category(models.Model):
	name = models.CharField(max_length=100)
	short_name = models.CharField(max_length=2)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Project(models.Model):
	proj_id = models.CharField(max_length=5, default=get_random_string(5, allowed_chars=string.ascii_uppercase+string.digits))
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
	language = models.ManyToManyField(Language)
	image = models.ImageField(upload_to = project_image_path)
	color = ColorField(default="#FFFFFF")

	def __str__(self):
		return self.name