from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from home.forms import LoginForm  # , CustomUserCretionForm
from django.contrib import messages


# get_user_model is use to get the personalized user_model
User = get_user_model()


# @login_required
def root(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        if request.POST.get("password1") == request.POST.get("password2"):
            if request.POST.get("email1") == request.POST.get("email2"):
                # user_creation_form = CustomUserCreationForm(data=request.POST)
                # if user_creation_form.is_valid():
                #     user_creation_form.save()
                try:
                    user = User.objects.create_user(
                        email=request.POST.get("email1"),
                        username=request.POST.get("username"),
                        first_name=request.POST.get("first_name"),
                        last_name=request.POST.get("last_name"),
                        dni=request.POST.get("dni"),
                        password=request.POST.get("password1"),
                    )
                    user.save()
                    # user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
                    # login(request, user)
                    return redirect("login")
                except:
                    return render(request, "signup.html", {"error": "error"})
            return render(request, "signup.html", {"error": "Email's doesn't match"})
        return render(request, "signup.html", {"error": "Password's doesn't match"})


def login_view(request):
    form = LoginForm()

    if request.method == "GET":
        return render(request, "registration/login.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Hi {username.title()}, welcome back!")
                return redirect("home")

        messages.error(request, f"Invalid username or password")
        return render(request, "registration/login.html", {"form": form})
