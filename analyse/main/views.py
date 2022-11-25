from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import RegisterUserForm


# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, ("Вы зарегистрировались как " + username))
            return redirect("index")
    else:
        form = RegisterUserForm()
    return render(request, "main/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.success(request, "Логин или пароль неверны")
            return render(request, "main/login.html")
    else:
        return render(request, "main/login.html")


def index(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")
