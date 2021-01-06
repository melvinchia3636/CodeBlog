from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def user_directory_path(instance, filename): 
    return 'ideas/{1}.{2}'.format(instance.author.id, instance.title, filename.split('.')[-1]) 

class Post(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(max_length=100, default='No Description')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	url = models.URLField(max_length=100, default='No Url')
	image = models.ImageField(upload_to=user_directory_path, default='No Image')

	def __str__(self):
		return self.title
 