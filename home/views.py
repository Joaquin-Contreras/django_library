from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from home.forms import CustomUserCreationForm


# get_user_model is use to get the personalize user_model
User = get_user_model()


# @login_required
def root(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": CustomUserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # user_creation_form = CustomUserCreationForm(data=request.POST)
            # if user_creation_form.is_valid():
            #     user_creation_form.save()
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                    dni=request.POST["dni"],
                )
                user.save()
                # user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
                login(request, user)
                return redirect("home")
            except:
                return render(
                    request,
                    "signup.html",
                    {"form": CustomUserCreationForm(), "error": "User already exists"},
                )

        return render(
            request,
            "signup.html",
            {"form": CustomUserCreationForm(), "error": "Passwords don't match"},
        )
