from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post) 
#resgisters the Post model, so that it can be accessed in admin