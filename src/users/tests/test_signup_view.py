from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SingUpAPITestCase(APITestCase):
    viewname = "signup"

    def test_signup_success(self):
        """사용자 회원가입 성공 테스트 케이스"""

        username = "user"
        password = "asdfn@1#2"

        response = self.client.post(
            path=reverse(self.viewname),
            data={"username": username, "password": password},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # response no show user password
        self.assertIsNone(response.data.get("password", None))

        # password check
        user = get_user_model().objects.get(username=username)
        self.assertTrue(user.check_password(password))

    def test_signup_simple_password_error(self):
        """사용자 회원가입시 간단한 비밀번호 방지 테스트 케이스"""
        response = self.client.post(
            path=reverse(self.viewname),
            data={"username": "user", "password": "12345678"},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_duplicated_username_error(self):
        """사용자 회원가입시 중복 사용자이름 방지 테스트 케이스"""

        username = "user"

        # create user
        get_user_model().objects.create(username=username)

        response = self.client.post(
            path=reverse(self.viewname),
            data={"username": username, "password": "asdfjwn!32S@"},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
