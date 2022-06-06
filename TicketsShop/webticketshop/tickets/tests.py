from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class ticketTestClass(TestCase):

    def setUP(self):
        self.login_url = 'main/login'
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')

    def test_ticket_add_invalid_not_admin(self):
        form_data = {'title': "randomtitle1", 'description': "randomdescription", 'category': "2"}
        self.client.login(fusername='testuser', password='12345')
        response = self.client.post("/add-ticket", data=form_data)
        self.assertEqual(response.status_code, 404)

    def test_tickets_not_available_unauthorized(self):
        response = self.client.get("/tickets")
        self.assertEqual(response.status_code, 404)