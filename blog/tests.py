from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Articles
from .models import Category

class ArticlesTestCase(TestCase):
    def setUp(self):
        article = Articles.objects.create(title='标题测试', detail='内容测试')
        article.author = User.objects.get(username='bing')
        article.cate = Category.objects.get(name='Python')
        article.save()

    def test_articles_create(self):
        article = Articles.objects.get(title='标题测试')
        self.assertContains(article.detail, '内容测试')