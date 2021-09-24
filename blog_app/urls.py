from django.urls import path

from . import views
from .views import BlogListView, BlogDetailView

urlpatterns = [
	path('', BlogListView.as_view(), name='blog-home'),
	path('post/<int:pk>/', BlogDetailView.as_view(), name='blog-details'),
	path('about/', views.about, name='blog-about')
]