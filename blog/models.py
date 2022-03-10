from distutils import text_file
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from django.contrib.auth.models import User

from django_editorjs_fields import EditorJsJSONField 
from taggit.managers import TaggableManager

from .utils import count_words, read_time

# Create your models here.

class Post(models.Model):

    class PostStatus(models.TextChoices):
        drafted = "DRAFTED", "draft"
        published = "PUBLISHED", "publish"

    title = models.CharField(max_length=250, null=False, blank=False)
    snippet = models.TextField(null=True, blank=False)
    slug = models.SlugField(editable=False, unique_for_month="published_on")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True)
    body = EditorJsJSONField()
    image = models.ImageField(upload_to="blog/", null=False, blank=False)
    tags = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(editable=False, default=timezone.now, null=False, blank=False)
    status = models.CharField(max_length=10, choices=PostStatus.choices, default=PostStatus.drafted)
    count_words = models.CharField(editable=False, max_length=50, default=0)
    read_time = models.CharField(editable=False, max_length=50, default=0)
    deleted = models.BooleanField(editable=False, default=False)

    class Meta:
        ordering = ("-published_on",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        self.count_words = count_words(self.body)
        self.read_time = read_time(self.body)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.title}"


class Comment(models.Model):

    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=254)
    comment = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Comment-detail", kwargs={"pk": self.pk})
