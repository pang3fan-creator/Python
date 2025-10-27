from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def responseHTML(request):
    return HttpResponse('HTML')


def responseText(request):
    return HttpResponse('Text')


def responseCSS(request):
    return render(request,'response/responseCSS.html')


def responseJS(request):
    return render(request,'response/responseJS.html')


def responseJSON(request):
    return HttpResponse('JSON')


def redirectToBaidu(request):
    return HttpResponse('RedirectToBaidu')

def redirectToSina(request):
    return HttpResponse('RedirectToSina')

def headers(request):
    return render(request,'response/headers.html')


def badRequest(request):
    return HttpResponse('BadRequest')


def notFound(request):
    return HttpResponse('NotFound')


def serverError(request):
    return HttpResponse('ServerError')
