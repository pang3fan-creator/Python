from django.shortcuts import render


def basic(request):
    return render(request, 'request/basic.html')

def headers(request):
    return render(request, 'request/headers.html')

def parameters(request):
    context = {
        'print':request.GET.get('print'),
        'uri':request.GET.get('uri'),
        'page':request.GET.get('page')
    }

    return render(request, 'request/parameters.html',context)


def headers(request):
    context = {
        # META是区分大写的
        'server_protocol':request.META['SERVER_PROTOCOL'],
        'request_method':request.META['REQUEST_METHOD'],
        'content_type':request.META.get('CONTENT_TYPE'),
        # headers是不区分大小写的
        'user_agent':request.headers['User-Agent'],
        'language':request.headers.get('ACCEpt-Language')
    }
    return render(request, 'request/headers.html',context)


def body(request):
    return render(request, 'request/body.html')


def register(request):
    #获取请求方式 -- "POST"/"GET"
    method = request.method
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    sex = request.POST.get('sex','0')
    hobby = request.POST.getlist('hobby')

    context = {
        'method': method,
        'data': {
            'username': username,
            'password': password,
            'password2': password2,
            'sex': int(sex),
            'hobby': hobby
        },
        # 根据返回值来查看是否进行了文件上传
        'is_uploaded':bool(request.FILES.get('attachment'))
    }

    if method == 'POST':
        # 只有在文件上传的情况下才将相关的信息附加到字典
        if context['is_uploaded']:
            context.update({
                'uploaded_file':{
                    'name':request.FILES.get('attachment').name,
                    'size':request.FILES.get('attachment').size,
                    'content_type':request.FILES.get('attachment').content_type
                }
            })

    return render(request, 'request/register.html',context)
