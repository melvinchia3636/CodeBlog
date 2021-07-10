from django.db import models
from colorfield.fields import ColorField

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Language(models.Model):
	name = models.CharField(max_length=100)
	color = ColorField(default="#FFFFFF")

	def __str__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
	icon = models.URLField()
	desc = models.TextField()
	language = models.ForeignKey(Language, null=True, on_delete=models.SET_NULL)
	star = models.IntegerField(default=0)
	fork = models.IntegerField(default=0)
	repo = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name