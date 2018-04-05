from django.shortcuts import render

from .models import Articles
# Create your views here.
def index(request):
    return render(request, 'index.html')


def articles(request):
    context = {}
    articles = Articles.objects.filter(pub_status=True).order_by('-pub_date')
    context['articles'] = articles
    return render(request, 'blog/articles.html', context)

def article_detail(request, pk):
    context = {}
    return render(request, 'blog/article_detail.html', context)