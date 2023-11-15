from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SignInAPITestCase(APITestCase):
    viewname = "signin"

    @classmethod
    def setUpTestData(cls):
        # create user
        cls.username = "user"
        cls.password = "SNFae@12%"
        cls.user = get_user_model().objects.create(username=cls.username)
        cls.user.set_password(cls.password)
        cls.user.save()

    def test_matched_viewname(self):
        reverse(self.viewname)

    def test_signin_success(self):
        response = self.client.post(
            reverse(self.viewname),
            data={"username": self.username, "password": self.password},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # response contain tokens
        self.assertIsNotNone(response.data.get("refresh", None))
        self.assertIsNotNone(response.data.get("access", None))

    def test_signin_unregistered_user(self):
        username = "user1"

        self.assertNotEqual(self.username, username)

        response = self.client.post(
            reverse(self.viewname),
            data={"username": username, "password": "asdfj"},
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_signin_invalid_password(self):
        password = "asdfnsfdlj!@#9"

        self.assertNotEqual(self.password, password)

        response = self.client.post(
            reverse(self.viewname),
            data={"username": self.username, "password": password},
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
