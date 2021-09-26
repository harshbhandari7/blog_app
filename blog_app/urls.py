from django.urls import path

from . import views
from .views import (
	BlogListView,
	BlogDetailView,
	BlogCreateView,
	BlogUpdateView,
	BlogDeleteView,
	UserBlogListView,
)

urlpatterns = [
	path('', BlogListView.as_view(), name='blog-home'),
	path('post/<int:pk>/', BlogDetailView.as_view(), name='blog-details'),
	path('post/new/', BlogCreateView.as_view(), name='blog-create'),
	path('post/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
	path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
	path('post//<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
	path('user/<str:username>/', UserBlogListView.as_view(), name='user-blog-details'),
	path('about/', views.about, name='blog-about')
]