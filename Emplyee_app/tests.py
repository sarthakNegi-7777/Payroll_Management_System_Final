from django.test import TestCase

class MyTemplateTests(TestCase):
    def test_my_template(self):
        # Assuming you have a user created for testing
        self.client.login(username='PrincePandey123', password='Princepandey')
        response = self.client.get('add_emp')
        self.assertTemplateUsed(response, 'add_emp.html')
