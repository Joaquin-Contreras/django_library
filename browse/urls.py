from django.urls import path
from . import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path("", views.search_home, name="search_home"),
]
