from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import MemberModel
from knowbase.utils import md5


def basic(request):
    return render(request, 'member/basic.html')


def lists(request):
    members = list(MemberModel.objects.values('id', 'username', 'age', 'sex'))
    return JsonResponse(members, safe=False)


def index(request):
    return render(request, 'member/index.html')


def manage(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    member = MemberModel.objects.create(
        username=username,
        password=md5(password),
        age=age,
        sex=sex
    )
    context = {
        'id': member.pk,
        'username': member.username,
        'age': member.age,
        'sex': member.sex
    }

    return JsonResponse(context)


def delete(request, id):
    MemberModel.objects.filter(pk=id).delete()
    context = {
        'status': 200,
        'message': 'OK'
    }
    return JsonResponse(context)


def get(request, id):
    member = MemberModel.objects.get(pk=id)
    context = {
        'id': member.pk,
        'username': member.username,
        'age': member.age,
        'sex': member.sex
    }
    return JsonResponse(context)


def put(request, id):
    # 如果以查询字符串的方式进行提交的话需要导入urllib
    # 模块中的parse_qs函数,然后再解析HTTP的请求体
    # from urllib.parse import parse_qs
    # body = request.body
    # parsed_qs = parse_qs(body)
    # print(parsed_qs)
    import json
    data = json.loads(request.body)
    username = data.get('username')
    age = data.get('age')
    sex = data.get('sex')
    MemberModel.objects.filter(pk=id).update(
        username=username,
        age=age,
        sex=sex,
    )
    context = {
        'status': 200,
        'message': 'OK',
        'data': {
            'id': id,
            'username': username,
            'age': age,
            'sex': sex
        }
    }
    return JsonResponse(context)


#########################################################

from django.views import View


class MemberView(View):

    # INSERT
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        member = MemberModel.objects.create(
            username=username,
            password=md5(password),
            age=age,
            sex=sex
        )
        context = {
            'id': member.pk,
            'username': member.username,
            'age': member.age,
            'sex': member.sex
        }

        return JsonResponse(context)

    # DELETE
    def delete(self, request, id):
        MemberModel.objects.filter(pk=id).delete()
        context = {
            'status': 200,
            'message': 'OK'
        }
        return JsonResponse(context)

    # UPDATE
    def put(self, request, id):
        # 如果以查询字符串的方式进行提交的话需要导入urllib
        # 模块中的parse_qs函数,然后再解析HTTP的请求体
        # from urllib.parse import parse_qs
        # body = request.body
        # parsed_qs = parse_qs(body)
        # print(parsed_qs)
        import json
        data = json.loads(request.body)
        username = data.get('username')
        age = data.get('age')
        sex = data.get('sex')
        MemberModel.objects.filter(pk=id).update(
            username=username,
            age=age,
            sex=sex,
        )
        context = {
            'status': 200,
            'message': 'OK',
            'data': {
                'id': id,
                'username': username,
                'age': age,
                'sex': sex
            }
        }
        return JsonResponse(context)

    # SELECT ... WHERE
    def get(self, request, id):
        member = MemberModel.objects.get(pk=id)
        context = {
            'id': member.pk,
            'username': member.username,
            'age': member.age,
            'sex': member.sex
        }
        return JsonResponse(context)
