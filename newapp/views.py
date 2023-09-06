from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Post

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class TelegramPageView(TemplateView):
    template_name = 'telegram.html'

class InstagramPageView(TemplateView):
    template_name = 'instagram.html'

class MyPageView(ListView):
    model = Post
    template_name = 'post.html'

class AdminViews(TemplateView):
    template_name = 'admin.html'