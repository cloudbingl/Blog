from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    referer = request.META.get('HTTP_REFERER')
    context = {}
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return redirect('/admin')
        # return render(request, 'user/login.html', context)

    if request.method == 'POST':
        login_name = request.POST.get('username', '').strip()
        login_pwd = request.POST.get('password', '').strip()
        # login_referer = request.POST.get('referer', referer).strip()
        user = authenticate(username=login_name, password=login_pwd)
        if user is not None:
            auth.login(request, user)
            messages.success(request, '登录成功')
            http_rd = redirect('/admin')
            if referer:
                http_rd = redirect(referer)
            return http_rd
        else:
            messages.warning(request, '用户名或密码错误')

        return redirect(referer)


@login_required
def logout(request):
    referer = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        auth.logout(request)
        if referer:
            return redirect(referer)
    return redirect('/')
