from django.test import TestCase
from django.contrib.auth.models import User


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_user(
            username='test_admin',
            password='testadmin',
            email='admin@gmail.com'
        )

        cls.user = User.objects.create_user(
            username='test_user',
            password='testuser',
            email='user@gmail.com',
            is_staff=False,
            is_active=True,
            is_superuser=False
        )

    def test_admin_login(self):
        login_status = self.client.login(username='test_admin', password='testadmin')
        self.assertTrue(login_status)
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)

    def test_admin_modal_login(self):
        pass


    def test_user_login(self):
        login_status = self.client.login(username='test_user',
                                         password='testuser')
        self.assertTrue(login_status)
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)

    def test_user_modal_login(self):
        pass
