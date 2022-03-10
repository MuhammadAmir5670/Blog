from curses import meta
from django import forms

from taggit.forms import TagWidget

from .models import Post


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ["title", "snippet", "image", "body", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post Title Here."}),
            "snippet": forms.Textarea(attrs={"rows": 1, "placeholder": "short description about the post."}),
            "tags": TagWidget(attrs={"class": "input-tags"}),
            "status": forms.RadioSelect()
        }
    
    class Media:
        css = {
            "all": (
                "vendor/bootstrap-tags/dist/bootstrap-tagsinput.css",
                "vendor/bootstrap-tags/examples/assets/app.css"
            )
        }