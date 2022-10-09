from django.shortcuts import render
import random

# Create your views here.

# 입력한 숫자가 홀수인지 짝수인지 확인하기
def is_odd_even(request, num):

    if num%2 == 1:
        result = f'{num}은(는) 홀수 입니다.'
    elif num == 0:
        result = f'{num}은(는) 0 입니다.'
    else:
        result = f'{num}은(는) 짝수 입니다.'

    context = {
        'result': result,
    }

    return render(request, 'numbers.html', context)

# 사칙연산 수행하기
def calculate(request, num1, num2):

    result = []
    result.append(f'{num1} + {num2} = {num1 + num2}')
    result.append(f'{num1} - {num2} = {num1 - num2}')
    result.append(f'{num1} * {num2} = {num1 * num2}')
    result.append(f'{num1} // {num2} = {num1 // num2}')

    context = {
        'result': result
    }

    return render(request, 'calculate.html', context)

def previousLife(request):
    return render(request, 'previousLife.html')

def previousLife2(request):

    jobs = ['관제사', '기자', '기술자', '교수', '교사', '과학자', '곤충학자', '관광가이드', '간병인', '간호사', '경찰관', '경호원', '결혼상담원', '장의사', '동물사육사', '문화재보존가', '마술사', '만화가', '모델', '연예인', '미용사', '변호사', '분장사', '소방관', '선장 및 항해사', '성직자', '운동선수', '의사', '약사', '요리사', '작가', '제과제빵사', '화가', '컴퓨터프로그래머', '통역가', '패션디자이너']
    previous_job = random.choice(jobs)
    name = request.GET.get('name')

    context = {
        'name': name,
        'previous_job': previous_job,
    }

    return render(request, 'previousLife2.html', context)

def lipsum(request):
    return render(request, 'lipsum.html')

def lipsum2(request):

    lorem_list = []

    lorem = ['사과', '짜장면', '바나나', '포도', '딸기']

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')

    for _ in range(int(num1)):
        lorems = []
        for _ in range(int(num2)):
            num = random.choice(lorem)
            lorems.append(num)
        lorem_list.append(lorems)

    context = {
        'lorem_list': lorem_list,
    }

    return render(request, 'lipsum2.html', context)