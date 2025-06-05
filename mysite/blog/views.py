# from django.shortcuts import render
from django.views import generic

# from .models import Post
# Create your views here.

# Hardcoded blog data (simulating database records)
BLOG_POSTS = [
    {
        'title': 'Можлива причина дивної ходьби: У пінгвінів немає колін?',
        'slug': 'penguin-knees',
        'author': '',
        'status': 'Publish',
        'created_at': '23 лютого 2025 р. 15:00',
        'updated_at': '23 лютого 2025 р. 15:00',
        'content': [
            {"type": "paragraph", "text": "Багато хто вважає, що у пінгвінів немає колін, але це не так."},

            {"type": "header", "text": "Чому пінгвіни так ходять?"},
            {"type": "paragraph", "text": "Багато хто вважає, що у пінгвінів немає колін, але це не так."},
            {"type": "image", "url": "https://example.com/penguin.jpg", "caption": "Пінгвін на льоду"},
            {"type": "list", "items": [
                "Їхні ноги дуже короткі.",
                "Спеціальний механізм ходьби зберігає енергію.",
                "Центр ваги знаходиться близько до землі."
            ]},
            {"type": "quote", "text": "Пінгвіни – це унікальні птахи, які адаптувалися до холодного клімату.", "author": "Дослідник Антарктиди"}
        ],
    },
    {'title': 'Чи є коліна у качок? Як качки висиджують яйця, якщо у них немає колін?',
     'slug': 'duck-knees',
     'author': '',
     'content': 'This is the content for post 1.',
     'status': 'Publish',
     'created_at': '23 лютого 2025 р. 17:00',
     'updated_at': '23 лютого 2025 р. 17:00'},
    {'title': 'Як курка не падає на двох ногах? Чи є у курки коліна?',
     'slug': 'chicken-knees',
     'author': '',
     'content': 'This is the content for post 1.',
     'status': 'Publish',
     'created_at': '23 лютого 2025 р. 19:00',
     'updated_at': '23 лютого 2025 р. 19:00'},
    {'title': 'Так багато запитань і так мало відповідей...',
     'slug': 'answers',
     'author': '',
     'content': 'This is the content for post 1.',
     'status': 'Publish',
     'created_at': '23 лютого 2025 р. 21:30',
     'updated_at': '23 лютого 2025 р. 21:30'},
]


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

        return context  #???


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = "contact.html"
