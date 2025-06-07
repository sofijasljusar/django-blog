# from django.shortcuts import render
import requests
from django.views import generic

# from .models import Post
# Create your views here.

# Hardcoded blog data (simulating database records)
BLOG_POSTS = requests.get('https://api.npoint.io/ce3b8ba44b768e2a827e').json()


# class PostList(generic.ListView):
class PostList(generic.TemplateView):
    """
    Return all posts that are with status 1 (published) and order from the latest one
    """
    # queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = BLOG_POSTS
        return context


# class PostDetail(generic.DetailView):
class PostDetail(generic.TemplateView):
    # model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get('slug')  # Get the post slug from the URL
        post = next((p for p in BLOG_POSTS if p["slug"] == slug), None)  #???
        if post:
            context["post"] = post
        else:
            context["post"] = {"title": "Not Found", "content": "This post does not exist."}

        return context  # ???


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = "contact.html"
