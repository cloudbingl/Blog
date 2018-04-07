from django.shortcuts import render

from .models import Articles
from .models import Category


def index(request):
    return render(request, 'index.html')


def articles(request):
    context = {}
    cates = Category.objects.all()
    cate = request.GET.get('cate', '')
    print(cate)
    if cate:
        articles = Articles.objects.filter(pub_status=True, cate=cate).order_by('-pub_date')
    else:
        articles = Articles.objects.filter(pub_status=True).order_by('-pub_date')
    context['articles'] = articles
    context['category'] = cates
    return render(request, 'blog/articles.html', context)

def article_detail(request, pk):
    context = {}
    return render(request, 'blog/article_detail.html', context)