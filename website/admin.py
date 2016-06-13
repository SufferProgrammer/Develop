from django.contrib import admin
from django.utils import timezone
from website.models import Post
from django.contrib.admin import AdminSite

class adminLayout(admin.ModelAdmin):
	fieldsets = [
		('Title',		{'fields':['Title']}),
		('Post Data',		{'fields':['Content']}),
		('Created Date',	{'fields':['Created']}),
	]
	list_display = ('Title', 'Created', 'recent_Created')
	list_filter = ['Created']
	search_fields = ['Content']

admin.site.index_title = "Admin"
admin.site.site_title = "Admin"
admin.site.site_header = "Admin Dashboard"
admin.site.register(Post, adminLayout)

