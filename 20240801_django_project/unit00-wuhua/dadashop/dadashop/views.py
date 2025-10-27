from django.http import HttpResponse


def index(request):
    print(request.POST)
    # uname = request.POST.get('uname')
    return HttpResponse('hello')
