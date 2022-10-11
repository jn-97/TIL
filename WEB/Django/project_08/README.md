# 회원가입 기능 개발 과정

1. accounts app 생성 및 등록
- auth와 관련한 경로나 키워드들을 Django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장

2. settings.py 에서 AUTH_USER_MODEL 정의 (커스텀 USER MODEL: 추후 수정 용이)

```python 
AUTH_USER_MODEL = 'accounts.User'
```

3. db.sqlite3 에서 기본 설정 모델인 auth_user 모델을 가져와서 클래스 상속

> accounts > models.py
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

4. bash에서 user 생성 후 db.sqlite3 > accounts_user 에서 생성되었나 확인

```bash
$ python manage.py createsuperuser
Username: admin
Email address: kjo5395@naver.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

5.

```bash
pip install django-extensions
pip install ipython # shell_plus 간편하게 사용
pip freeze > requirements.txt
```

6. django-extensions 앱 등록

```python 
INSTALLED_APPS = [
    'accounts',
    'django_extensions',
]
```

7. shell 실행

```bash
python manage.py shell_plus
```
  1. user 생성

  ```bash
  Article.objects.create(title='제목1', content='내용1')
  User.objects.create_user('hong', 'hong@gmail.com', '1234') 
  # create_user 사용하면 암호화 된 채로 저장
  ```

  2. user 인증

  ```bash
  from django.contrib.auth import authenticate
  authenticate(username='admin', password='1234')
  ```

8. urls.py 정의

> accounts > urls.py
```python 
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
]
```

9. views.py 정의

> accounts > views.py
```python
from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')
```

10. templates 정의

> accounts > templates > accounts > signup.html

11. signup.html에 form을 입력하기 위한 views.py 정의

> accounts > views.py
```python
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    form = UserCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)
```

12. signup.html 작성

> accounts > signup.html
```python
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}

<h1>회원가입</h1>
<form action="" method="POST">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% bootstrap_button button_type="submit" content="OK" %}
</form>

{% endblock body %}
```

13. views.py 작성

> accounts > views.py
```python
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    # POST 요청 처리
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)
```

14. forms.py 작성

> accounts > forms.py
```python 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = '__all__'
```

15. views.py 수정

> accounts > views.py
```python
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    # POST 요청 처리
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/signup.html', context)
```

16. forms.py 수정

> accounts > forms.py
```python 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username',)
```

17. admin.py 정의

> accounts > admin.py
```python
from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
```

18. admin.py 수정

> accounts > admin.py
```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(get_user_model, UserAdmin)
```

19. forms.py 수정

> accounts > forms.py
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username',)
```

20. detail.html url 생성 

> accounts > urls.py
```python
path('<int:pk>/', views.detail, name="detail")
```

21. detail.html views.py 정의

> accounts > views.py
```python
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

def detail(request, pk):

    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user,
    }

    return render(request, 'accounts/detail.html', context)
```

22. detail.html 생성

> accounts > templates > accounts > detail.html
```python
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}

<h1>{{ user.username }}님의 프로필</h1>

{% endblock body %}
```