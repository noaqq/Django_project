from django.urls import include, path

from . import views

urlpatterns = [
    path("register", views.register_user, name="register_user"),
    path("login", views.login_user, name="login_user"),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("search", views.search, name="search"),
    path("faqs", views.faqs, name="faqs"),
    path("logout", views.logout_user, name="logout_user"),
]
