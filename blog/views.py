from django.shortcuts import redirect, render

from .models import Post
from .forms import PostForm

from django.views.generic import CreateView, UpdateView, ListView
# Create your views here.


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = "blog/post-create.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        status = request.POST.get("status")

        if form.is_valid():
            post = form.save(commit=False)
            post.status = status
            post.save()
            form.save_m2m()
            return redirect("post-detail", pk=post.pk)
        return render(request, self.template_name, {"form": form})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post-update.html" 

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return self.model.objects.filter(pk=pk)


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        status = request.POST.get("status", self.object.status)

        if form.is_valid():
            post = form.save(commit=False)
            post.status = status
            post.save()
            form.save_m2m()
            return redirect("post-update", pk=post.pk)
        return render(request, self.template_name, {"form": form})


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.PostStatus.published)
    paginate_by = 10
    template_name = "blog/post-list.html"
    context_object_name = "posts"

    
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm(instance=post)
    form.fields.get("body").ReadOnly = True
    return render(request, "blog/post-detail.html", {"post": post, "form": form})