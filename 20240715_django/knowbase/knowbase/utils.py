import hashlib
from django.shortcuts import redirect


def md5(string):
    md5 = hashlib.md5()
    md5.update(string.encode())
    return md5.hexdigest()


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not ('backend' in request.session.keys()):
            return redirect('/backend/login/?returnurl=' + request.path)
        else:
            return func(request, *args, **kwargs)

    return wrapper
