from django.urls import path

from .views import PostList, post_detail, PostCreateView, PostUpdateView

urlpatterns = [
    path("list/", PostList.as_view(), name="post-list"),
    path("detail/<int:pk>/", post_detail, name="post-detail"),

    path("create/", PostCreateView.as_view(), name="post-create"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="post-update"),
]