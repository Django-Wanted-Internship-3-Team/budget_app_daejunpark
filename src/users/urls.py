from django.urls import path

from users.views import SignUpAPIView

urlpatterns = [
    path("signup/", view=SignUpAPIView.as_view(), name="signup"),
]
