from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from models import Post

def index(request):
	post = Post.objects.filter(Created__lte=timezone.now()).order_by('Created')
	return render(request, 'website/index.htm', {'post' : post})
