from django.urls import path

from . import views
from .views import BlogListView

urlpatterns = [
	path('', BlogListView.as_view(), name='blog-home'),
	path('about/', views.about, name='blog-about')
]