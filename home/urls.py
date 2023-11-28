from django.urls import path
from . import views
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path("", views.root, name="home"),
    path("signup/", views.signup, name="signup"),
    path("accounts/login/", views.login_view, name='login'),
    path("accounts/logout/", logout_then_login, name="logout")
]
