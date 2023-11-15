from django.urls import reverse
from rest_framework.test import APITestCase


class SignInAPITestCase(APITestCase):
    viewname = "signin"

    def test_matched_viewname(self):
        reverse(self.viewname)
