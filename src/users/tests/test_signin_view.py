from django.urls import reverse
from rest_framework.test import APITestCase


class SignInAPITestCase(APITestCase):
    viewname = "signin"

    def test_no_api_matched_fail(self):
        reverse(self.viewname)
