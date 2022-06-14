from django.contrib import admin
from .models import Post
from .models import Journal

# В этой части регистрируем модели.
admin.site.register(Journal)
admin.site.register(Post)