from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

def home(request):
	# context passes the data to the templates
	context = {
		'blog_posts': Post.objects.all(),  #objects stored in the data base
	}
	return render(request, 'blog_app/home.html', context)

# posts list view
class BlogListView(ListView):
	model = Post  # this ia a model, not request type check model.py
	template_name = 'blog_app/home.html'  # <app_name>/<model>_<view_type>.html
	context_object_name = 'blog_posts'
	ordering = ['-date_posted']
	paginate_by = 5  # will show 3 items per page

class BlogDetailView(DetailView):
	model = Post

class BlogCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.name = self.request.user
		return super().form_valid(form)

	# below func checks if the user is editing it's own post or not
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.name:
			return True
		else:
			return False

# template for delete view is post_confirm_delete.html
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'  # redirects to home page after successful deletion

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.name:
			return True
		else:
			return False


# about view
def about(request):
	return render(request, 'blog_app/about.html', { 'title': 'About' })
