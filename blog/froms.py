from django import forms
from .models import *

class PostForm(forms.ModekForms):
    class Meta:
        model = Post
        fields = ('title','title_tag','author', 'body')
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.TextInput(attrs={'class': 'form-control'}),

        }
