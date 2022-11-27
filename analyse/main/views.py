from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import RegisterUserForm
from .models import Price


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


def faqs(request):
    return render(request, "main/faqs.html")


def search(request):
    if request.method == "POST":
        name = request.POST["name"]
        items = analyse(name)
        return render(
            request,
            "main/search.html",
            {"items": items, "search": name, "len": len(items), "phone": True},
        )
    return render(request, "main/search.html")


def analyse(name):
    result = Price.objects.filter(name__icontains=name)
    return [r for r in result]
