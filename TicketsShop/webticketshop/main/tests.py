from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class MainTestClass(TestCase):

    def setUP(self):
        self.login_url = 'main/login'
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')

    def test_registration(self):
        form_data = {'username': "testuser2", 'first_name': "blabla", 'last_name': "blabl", 'email': "blabla@gmail.com",
                     'password1': "denfit3841", 'password2': "denfit3841"}
        response = self.client.post("/main/register", data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        form_data = {'username': "testuser2",'password1': "denfit3841", 'password2': "denfit3841"}
        response = self.client.post("/main/login", data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)