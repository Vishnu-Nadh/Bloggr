from django.shortcuts import render
from .models import Post

# dummy data

# Create your views here.
def home(request):
    context = {"posts": Post.objects.all()}
    template_name = "blog/home.html"
    return render(request, template_name=template_name, context=context)


def about(request):
    template_name = "blog/about.html"
    return render(request, template_name=template_name, context={"title": "About"})
