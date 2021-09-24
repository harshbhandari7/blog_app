from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

def home(request):
	# context passes the data to the templates
	context = {
		'blog_posts': Post.objects.all(),  #objects stored in the data base
	}
	return render(request, 'blog_app/home.html', context)

# posts list view
class BlogListView(ListView):
	model = Post
	template_name = 'blog_app/home.html'  # <app_name>/<model>_<view_type>.html
	context_object_name = 'blog_posts'
	ordering = ['-date_posted']

def about(request):
	return render(request, 'blog_app/about.html', { 'title': 'About' })
