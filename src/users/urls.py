from django.urls import path

from users.views import SignInAPIView, SignUpAPIView

urlpatterns = [
    path("signup/", view=SignUpAPIView.as_view(), name="signup"),
    path("signin/", view=SignInAPIView.as_view(), name="signin"),
]
