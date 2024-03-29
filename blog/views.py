from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from .models import * 
from .forms import *
from django.urls import reverse_lazy
# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date'] #displays according to the order, the last one to be displayed will be at the top

class ArticleView(DetailView):
    model = Post
    template_name = 'articles_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

