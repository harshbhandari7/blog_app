from django.shortcuts import render
from .models import Post

def home(request):
	# context passes the data to the templates
	context = {
		'blog_posts': Post.objects.all(),  #objects stored in the data base
	}
	return render(request, 'blog_app/home.html', context)

def about(request):
	return render(request, 'blog_app/about.html', { 'title': 'About' })
