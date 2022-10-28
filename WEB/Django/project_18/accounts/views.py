from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("reviews:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }

    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "reviews:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect("reviews:index")


def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    reviews = user.review_set.all()
    context = {
        "user": user,
        "reviews": reviews,
    }
    return render(request, "accounts/detail.html", context)
