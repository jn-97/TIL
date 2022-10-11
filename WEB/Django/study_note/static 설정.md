- static 파일은 templates 파일처럼 고정임

1. articles > static 폴더 생성 후 이미지 파일 추가

2. articles > html 파일 설정

```html
<body>
  
{% load static %}
<img src="{% static 'images/img.jpeg' %}" alt="">

</body>
```

3. static 파일 안에 images, css 등 폴더 추가 후 경로 설정 가능