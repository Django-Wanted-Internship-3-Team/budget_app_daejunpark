from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView


class SignUpAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="사용자 회원가입",
    )
    def post(self, request):
        return Response()
