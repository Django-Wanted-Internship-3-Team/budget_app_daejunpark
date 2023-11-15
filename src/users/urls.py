from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import SignUpAPIView

urlpatterns = [
    path("signup/", view=SignUpAPIView.as_view(), name="signup"),
    path("signin/", view=TokenObtainPairView.as_view(), name="signin"),
]
