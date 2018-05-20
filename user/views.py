from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import LoginForm


def login(request):
    """登录操作"""
    context = {}
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        next = request.POST.get('next_url')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            # messages.success(request, '登录成功')
            if next:
               return redirect(next)
            return redirect(reverse('blog:index'))

        else:
            # 登录表单错误
            # login_form.add_error(None, "用户名或错误")
            context['login_form'] = LoginForm(request.POST)
    else:
        # POST 之外其他请求
        next = request.GET.get('next_url')
        print(next)
        context['login_form'] = LoginForm()
        context['next_url'] = next
    return render(request, 'user/login.html', context)


@login_required
def logout(request):
    """注销操作"""
    referer = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        auth.logout(request)
        if referer:
            return redirect(referer)
    return redirect('/')
