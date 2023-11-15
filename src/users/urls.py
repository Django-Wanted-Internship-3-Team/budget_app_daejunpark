from django.urls import path

from users.views import SignInAPIView, SignUpAPIView, TokenRefreshAPIView

urlpatterns = [
    path("signup/", view=SignUpAPIView.as_view(), name="signup"),
    path("signin/", view=SignInAPIView.as_view(), name="signin"),
    path("token-refresh/", view=TokenRefreshAPIView.as_view(), name="token-refresh"),
]
