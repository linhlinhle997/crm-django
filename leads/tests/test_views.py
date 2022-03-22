from django.shortcuts import reverse
from django.test import TestCase

# Create your tests here.
class LandingPageTest(TestCase):
    def test_get(self):
        # TODO some sort of test
        response = self.client.get(reverse("landing-page"))
        # print(response.content)
        # print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")