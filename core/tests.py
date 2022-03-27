from django.test import TestCase


class ViewTestCase(TestCase):
    def test_home_view(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        
