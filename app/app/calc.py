def add(x, y):
    return x + y

def subtract(x, y):
    return y - x


from django.test import SimpleTestCase
from rest_framework.test import APIClient

class TestVeiws(SimpleTestCase):
    def test_get_greeting(self):
        client = APIClient()
        res = client.get('/greetings/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.data,
            ["Hello", "Bonjour", "hola"]
        )