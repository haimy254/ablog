from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),
    path('article/<int:pk>', ArticleView.as_view(), name='articles'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
