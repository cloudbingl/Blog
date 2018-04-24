from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

from .models import Articles
from .models import Category
from comment.models import Comments


class BlogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_user(
            username='test_admin',
            password='admintest',
            email='test_admin@gmail.com'
        )

        cls.cate_python = Category.objects.create(name='Python')

        cls.article_test = Articles.objects.create(
            title='测试的标题',
            detail='测试的内容',
            cate=cls.cate_python,
            author=cls.admin
        )

    def test_category_create(self):
        """测试创建文章分类"""
        cate = Category()
        cate.name = 'JAVA'
        cate.save()

    def test_articles_create(self):
        """测试创建文章"""
        Articles.objects.create(
            title='标题测试',
            detail='内容测试',
            author=self.admin,
            cate=self.cate_python
        )

        article = Articles.objects.get(title='标题测试')
        self.assertEqual(article.detail, '内容测试')

    def test_home(self):
        """测试访问首页"""
        response = self.client.get(reverse('blog:index'))
        self.failUnlessEqual(response.status_code, 200)

    def test_articles(self):
        """测试访问文章列表"""
        response = self.client.get(reverse('blog:articles'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['articles'],
                                 ['<Articles: 测试的标题>'])

    def test_article_not_found(self):
        """测试访问不存在的文章"""
        response = self.client.get(reverse('blog:article', args=[10]))
        self.assertEqual(response.status_code, 404)

    def test_article(self):
        """测试访问已存在的文章"""
        article = Articles.objects.get(title='测试的标题')
        response = self.client.get(
            reverse('blog:article', args=[str(article.id)]))
        self.assertEqual(response.status_code, 200)

    def test_article_not_pub(self):
        """访问未发布的文章"""
        Articles.objects.create(
            title='未发布的文章',
            detail='未发布的文章内容',
            author=self.admin,
            cate=self.cate_python,
            pub_status=False
        )
        article = Articles.objects.get(title='未发布的文章')
        response = self.client.get(reverse('blog:article', args=[article.id]))
        self.assertEqual(response.status_code, 302)


class CommentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_user(
            username='test_admin',
            password='admintest',
            email='test_admin@gmail.com'
        )

        cls.cate_python = Category.objects.create(name='Python')

        cls.article_test = Articles.objects.create(
            title='测试的标题',
            detail='测试的内容',
            cate=cls.cate_python,
            author=cls.admin
        )

        ct = ContentType.objects.get_for_model(Articles)
        cls.comment_test = Comments.objects.create(
            content_type=ct,
            object_id=cls.article_test.id,
            cmt_detail='已存在的测试评论',
            cmt_user=cls.admin
        )

    def test_add_comment(self):
        c = Client()
        r = c.login(username='test_admin', password='admintest')
        self.assertTrue(r)
        ct = ContentType.objects.get_for_model(Articles)
        response = c.post(
            reverse('comment:add_comment'),
            {
                'content_type': ct,
                'object_id': self.article_test.id,
                'detail': '测试添加评论',
                'reply_comment': '0'
            }
        )
        self.assertEqual(response.status_code, 200)

    def test_comments(self):
        article = Articles.objects.get(title='测试的标题')

        response = self.client.get(reverse('blog:article', args=[article.id]))
        self.assertQuerysetEqual(
            response.context['comments'], ['<Comments: 已存在的测试评论>']
        )


class ReadTest(TestCase):
    pass
