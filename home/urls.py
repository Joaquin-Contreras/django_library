from django.urls import path
from . import views

urlpatterns = [
    path("", views.root, name="home"),
    path("signup/", views.signup, name="signup")
    # path("login/"),
]
