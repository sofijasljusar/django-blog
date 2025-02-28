# from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.


class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one
    """
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ContactView(generic.TemplateView):
    template_name = "contact.html"



