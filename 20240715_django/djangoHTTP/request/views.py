from django.shortcuts import render


def basic(request):
    return render(request, 'request/basic.html')


def headers(request):
    return render(request, 'request/headers.html')


def parameters(request):
    context = {'print': request.GET.get('print'),
               'uri': request.GET.get('uri'),
               'page': request.GET.get('page')}

    return render(request, 'request/parameters.html', context)


def headers(request):
    return render(request, 'request/headers.html')


def body(request):
    return render(request, 'request/body.html')


def register(request):
    print(request)
    print(type(request))
    print(request.POST)
    print(type(request.POST))
    # 获取请求方式 -- "POST"/"GET"
    method = request.method
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    sex = request.POST.get('sex', '0')
    hobby = request.POST.getlist('hobby')
    context = {'method': method,
               'data': {'username': username,
                        'password': password,
                        'password2': password2,
                        'sex': int(sex),
                        'hobby': hobby}}
    return render(request, 'request/register.html', context)
