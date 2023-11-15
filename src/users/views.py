from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import (
    SignInRequestSerializer,
    SignInResponseSerializer,
    TokenRefreshRequestSerializer,
    TokenRefreshResponseSerializer,
    UserSignUpSerializer,
)


class SignUpAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="사용자 회원가입",
        request_body=UserSignUpSerializer,
        responses={
            status.HTTP_201_CREATED: UserSignUpSerializer,
            status.HTTP_400_BAD_REQUEST: "error",
        },
    )
    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            data=UserSignUpSerializer(user).data,
            status=status.HTTP_201_CREATED,
        )


class SignInAPIView(TokenObtainPairView):
    @swagger_auto_schema(
        operation_summary="사용자 로그인",
        request_body=SignInRequestSerializer,
        responses={
            status.HTTP_200_OK: SignInResponseSerializer,
            status.HTTP_400_BAD_REQUEST: "error",
            status.HTTP_401_UNAUTHORIZED: "unauthorized",
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshAPIView(TokenRefreshView):
    @swagger_auto_schema(
        operation_summary="사용자 토큰 리프레시",
        request_body=TokenRefreshRequestSerializer,
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
            # TODO : other response.
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
