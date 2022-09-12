from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# dummy data

# Create your views here.
def home(request):
    context = {"posts": Post.objects.all()}
    template_name = "blog/home.html"
    return render(request, template_name=template_name, context=context)


class PostListView(ListView):
    model = Post
    # <app>/<model_name>_<viewtype>  #default template name
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
        
    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
    
    
def about(request):
    template_name = "blog/about.html"
    return render(request, template_name=template_name, context={"title": "About"})
