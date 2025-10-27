from django.shortcuts import render,redirect
from testing.models import Category,Article
from django.http import HttpResponse


def index(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'index.html', context)


def migrations(request, id):
    if request.method == 'GET':
        object = Category.objects.get(pk=id)
        category = Category.objects.all()
        context = {
            'category': category,
            'object': object
        }
        return render(request, 'migrations.html', context)
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        Article.objects.filter(category_id=id).update(category_id=category_id)
        return redirect('/')
