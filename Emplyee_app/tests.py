from django.test import TestCase

class MyTemplateTests(TestCase) :
    def test_my_template(self) :
        # Assuming you have a user created for testing
        self.client.login(username='SarthakNegi', password='sarthak_123')
        response = self.client.get('add_emp')
        self.assertTemplateUsed(response, 'add_emp.html')
        