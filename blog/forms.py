from django import forms

from .models import Post, Comment
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.models


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','header_image','category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),


        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {

            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = django.contrib.auth.models.User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


