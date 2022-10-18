from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm  # 회원 가입
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm  # 로그인 기능
from django.contrib.auth import login as auth_login

# login 함수를 가져와야 하는데 이름이 겹치기 때문에 auth_login으로 변경

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def index(request):
    users = get_user_model().objects.order_by("pk")
    context = {
        "users": users,
    }

    return render(request, "accounts/index.html", context)


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }

    return render(request, "accounts/detail.html", context)


def login(request):
    if request.method == "POST":
        # AuthenticationForm은 ModelForm이 아님
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 form에서 인증된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            return redirect("main:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)
