from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from home.models import Post

# Create your views here.
USER = get_user_model()

def search_home(request):
    POSTS = Post.objects.all()
    return render(request, 'index.html', {"posts":POSTS})
