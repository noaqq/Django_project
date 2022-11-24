from django.urls import include, path

from . import views

urlpatterns = [
    path("register", views.register_user, name="register_user"),
    path("login", views.login_user, name="login_user"),
    path("index", views.index, name="index"),
]
