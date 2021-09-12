from django.shortcuts import render

blog_posts = [
	{
		'name': 'Harsh',
		'title': 'Blog Post #1',
		'content': 'Hi everybody How is it going !!',
		'date_posted': '11th september, 2021',
	},
	{
		'name': 'Some Name',
		'title': 'Blog Post #2',
		'content': 'THis is some content !!',
		'date_posted': '9th september, 2021',
	}
]

def home(request):
	# context passes the data to the templates
	context = {
		'blog_posts': blog_posts,
	}
	return render(request, 'blog_app/home.html', context)

def about(request):
	return render(request, 'blog_app/about.html', { 'title': 'About' })
