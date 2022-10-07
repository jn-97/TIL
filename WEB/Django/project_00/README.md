# Django CRUD

## 1. 가상환경 및 Django 설치

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 '.gitignore'로 설정을 해둔다.

```bash
$ python -m venv venv
$ source venv/Scripts/activate
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

### 3. Django 프로젝트 생성

```bash
$ django-admin startproject pjt .
```

## 2. articles app

### 1. app 생성

```
python manage.py startapp articles
```

### 2. app 등록

### 3. urls.py 설정

## 3. CRUD (Model 정의)

### 1. 클래스 정의

### 2. 마이그레이션 파일 생성

### 3. DB 반영('python manage.py makemigrations -> migrate')

## 4. CRUD 기능 구현

### 1. 게시글 생성
> 사용자에게 HTML form 제공, 입력한 데이터를 처리

#### 1. HTML Form 제공
> http://localhost:8000/articles/new/

#### 2. 입력받은 데이터 처리
> http://localhost:8000/articles/create/