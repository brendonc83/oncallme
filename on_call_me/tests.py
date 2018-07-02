from django.test import TestCase, Client, RequestFactory
from on_call_me.models import User
import os


class LoginPageTest(TestCase):

    def setUp(self):

        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(
            username='U009835', email='U09835@someemail.com', password=os.environ.get('TEST_PWD'), is_staff='True')

    def test_login_view(self):

        request = self.client.get('/accounts/login/')
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'on_call_me/login.html')

    def test_login_successful(self):

        logged_in = self.client.login(username='U009835', password=os.environ.get('TEST_PWD'))
        self.assertTrue(logged_in)

        """Access a page that requires a user to be authenticated"""
        self.client.get('index/')
        self.assertTemplateUsed('on_call_me/index.html')





