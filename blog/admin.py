from django.contrib import admin

from .models import Post
from .forms import PostForm

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    fields = ["title", "snippet", "author", "image", "body", "tags", "status"]
    # class Media:
    #     js = (
    #         "//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
    #         "js/selectize-js/src/selectize.js",
    #         "js/app.js"
    #     )

admin.site.register(Post, PostAdmin)