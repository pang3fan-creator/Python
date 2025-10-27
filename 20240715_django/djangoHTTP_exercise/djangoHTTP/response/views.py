from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
import json

# Create your views here.

def responseHTML(request):
    html = '''
    <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Hello</title>
        </head>
        <body>	
            <h1>Django Response Object</h1>
        </body>
        </html>
    '''
    return HttpResponse(html,content_type='text/html')


def responseText(request):
    html = '''
        <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Hello</title>
            </head>
            <body>	
                <h1>Django Response Object</h1>
            </body>
            </html>
    '''
    headers = {
        'powerby':'AID2405',
        'copyright':'Tedu'
    }
    return HttpResponse(html,content_type='text/plain',status=200,headers = headers)


def responseCSS(request):
    return render(request,'response/responseCSS.html')


def responseJS(request):
    return render(request,'response/responseJS.html')


def responseJSON(request):
    users =  [
        {'id':1,'username':'Tom','age':21},
        {'id':2,'username':'Rose','age':26},
        {'id':3,'username':'Ben','age':19},
        {'id':6,'username':'Ali','age':22},
    ]
    return HttpResponse(json.dumps(users),content_type='application/json')


def responseJSON1(request):
    users = [
        {'id': 1, 'username': 'Tom', 'age': 21},
        {'id': 2, 'username': 'Rose', 'age': 26},
        {'id': 3, 'username': 'Ben', 'age': 19},
        {'id': 6, 'username': 'Ali', 'age': 22},
    ]
    return JsonResponse(users,safe=False)

def redirectToBaidu(request):
    return HttpResponseRedirect('http://www.baidu.com')

def redirectToSina(request):
    return redirect('http://www.sina.com.cn')

def headers(request):
    return render(request,'response/headers.html')


def badRequest(request):
    return HttpResponse('BadRequest')


def notFound(request):
    return HttpResponse('NotFound')


def serverError(request):
    return HttpResponse('ServerError')
