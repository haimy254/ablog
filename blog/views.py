from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import * 
from .forms import *
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'articles_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'