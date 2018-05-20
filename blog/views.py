from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Articles
from .models import Category


def index(request):
    """主页"""
    return render(request, 'index.html')

def articles(request):
    """文章列表"""
    context = {}
    cates = Category.objects.all()
    cate = request.GET.get('cate', '')
    if cate.isdecimal() and int(cate) > 0:
        # 查看分类下的文章
        articles = Articles.objects.filter(pub_status=True, cate=cate) \
            .order_by('-pub_date')
        context['current_cate'] = int(cate)
    else:
        # 查看全部的文章
        articles = Articles.objects.filter(pub_status=True) \
            .order_by('-pub_date')
        context['current_cate'] = 0
    # context['articles'] = articles
    context['seven_days_hot'] = Articles.get_seven_days_hot()
    context['thirty_days_hot'] = Articles.get_thirty_days_hot()
    context['category'] = cates

    # 分页
    paginator = Paginator(articles, 5)
    page= request.GET.get('page', 1)
    data = paginator.get_page(page)
    context['articles'] = data
    print(data)

    return render(request, 'blog/articles.html', context)


def article_detail(request, pk):
    """文章内容页面"""
    context = {}
    article = get_object_or_404(Articles, pk=pk)
    context['article'] = article
    context['comments'] = article.get_comments_data()
    context['comment_form'] = article.get_comment_form()
    if article.pub_status:
        response = render(request, 'blog/article_detail.html', context)
        article.check_or_set_read_flag(request, response)
        return response
    else:
        if article.author == request.user:
            context['status'] = '[草稿]'
            return render(request, 'blog/article_detail.html', context)
        messages.warning(request, '文章好像飞走了')
        return HttpResponseRedirect(reverse('blog:index'))


def search(request):
    pass