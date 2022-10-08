from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')

def pong(request):

    # print(request)
    # <WSGIRequest: GET '/pong/?ball=김지연'>

    # print(dir(request))
    # request의 객체 안에 뭐가 들어있는지 확인할 수 있음

    # print(request.GET)
    # <QueryDict: {'ball': ['john']}>

    # print(request.GET.get('ball'))
    # 김지연

    ball = request.GET.get('ball')
    context = {
        'name': ball,
    }

    return render(request, 'pong.html', context)
    # return render(request, 'pong.html', {'name': request.GET.get('ball')})