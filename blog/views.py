from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Articles
from .models import Category


def index(request):
    """主页"""
    return render(request, 'index.html')


def articles(request):
    """文章列表"""
    context = {}
    cates = Category.objects.all()
    cate = request.GET.get('cate', None)
    if cate is not None:
        articles = Articles.objects.filter(pub_status=True,cate=cate)\
                                   .order_by('-pub_date')
    else:
        articles = Articles.objects.filter(pub_status=True)\
                                   .order_by('-pub_date')
    context['articles'] = articles
    context['category'] = cates
    return render(request, 'blog/articles.html', context)


def article_detail(request, pk):
    """文章内容页面"""
    context = {}
    article = get_object_or_404(Articles, pk=pk)
    context['article'] = article
    if article.pub_status:
        response = render(request, 'blog/article_detail.html', context)
        article.check_or_set_read_flag(request, response)
        return response
    if article.author == request.user:
        context['status'] = '[草稿]'
        return render(request, 'blog/article_detail.html', context)
    messages.warning(request, '文章好像飞走了')
    return HttpResponseRedirect(reverse('blog:index'))
