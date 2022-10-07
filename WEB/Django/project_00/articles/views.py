from django.shortcuts import render
import random

# Create your views here.
def index(request):

    names = ['주세환', '오진수', '임수경', '조병진', '차화영', '최근영', '김선교']

    name = random.choice(names)

    # context 안에 있는 데이터들을 templates로 보내서 templates에서 활용할 수 있게 함
    context = {
        # 변수명: 값
        'name': name,
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }

    return render(request, 'index.html', context)

def welcome(request, name):
    # 사람들이 /welcome/본인이름 을 입력하면, 환영 인사와 이름을 동시에 보여준다.
    context = {
        'name': name,
        'greetings': [
            'hello',
            'hi',
            'guten tag',
            'bon jour',
        ],

        'images': [
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
            'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
        ],
    }

    return render(request, 'welcome.html', context)
