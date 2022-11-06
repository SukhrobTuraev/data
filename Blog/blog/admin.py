from django.contrib import admin
from .models import Post
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', ]
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title', )

admin.site.register(Post,BlogAdmin)
