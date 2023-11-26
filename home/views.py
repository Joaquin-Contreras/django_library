from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from home.forms import CustomUserCreationForm

# Create your views here.
# @login_required
def root(request):
    return render(request, "index.html")

def signup(request):

    if request.method == "GET":
        return render(request, "signup.html", {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # try:
                print(request.POST)
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], dni=request.POST['dni'])

                print(user)

                user.save()
                login(request, user)
                return redirect("home")
            # except:
            #     return render(request, "signup.html", {
            #         'form': UserCreationForm,
            #         'error': "User already exists"
            #         })

        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': "Passwords don't match"
            })






