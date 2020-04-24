from django.test import TestCase

# Create your tests here.
class PlustestCase(TestCase):

    def test_over_ten(self):
        self.assertEqual(1 + 4, 5)