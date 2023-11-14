from django.urls import reverse
from rest_framework.test import APITestCase


class SingUpAPITestCase(APITestCase):
    viewname = "signup"

    def test_no_view_failure(self):
        """지정된 view가 없는 실패 테스트 케이스"""
        self.client.post(path=reverse(self.viewname))
