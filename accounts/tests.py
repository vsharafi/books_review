from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class SignUpTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     cls.user = CustomUser.objects.create(username='naz', age=22, password='<PASSWORD>')
    #

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_page_form(self):
        user = get_user_model().objects.create_user('naz', age='22')
        # response = self.client.post(reverse('signup'), {'username': 'naz', 'age': '22', 'password': 'Va@12345'})
        # response2 = self.client.post(reverse('login'), {'username': 'naz', 'password': 'Va@12345'})
        #
        # res = self.client.get(reverse('home'))
        # self.assertContains(res, 'naz')
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'naz')
        self.assertEqual(get_user_model().objects.all()[0].age, 22)


