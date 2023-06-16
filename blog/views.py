from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import * 
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'articles_detail.html'