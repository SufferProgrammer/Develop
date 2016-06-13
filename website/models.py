from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
	Title = models.CharField(max_length = 20)
	Content = models.TextField()
	Created = models.DateTimeField('Created')

	def __str__(self):
		return self.Title
	
	def recent_Created(self):
		return self.Created >= timezone.now() - datetime.timedelta(days=1)

	recent_Created.admin_order_field = 'Created'
        recent_Created.boolean = True
        recent_Created.short_description = 'Created recently'

