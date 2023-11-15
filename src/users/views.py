from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSignUpSerializer


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
