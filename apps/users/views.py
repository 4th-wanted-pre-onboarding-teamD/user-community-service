from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer
from .signals import sig_user_logged_in, CustomTokenObtainPairSerializer
from .models import UserLog

# Create your views here.
class RegisterView(CreateAPIView):
    """ 회원가입 뷰 - 사용자를 생성합니다. """

    serializer_class = RegisterSerializer


class WithdrawalView(DestroyAPIView):
    """ 회원탈퇴 뷰 - 요청을 보낸 사용자를 삭제합니다. """

    permission_classes = [IsAuthenticated]

    def get_object(self):
        """ 요청을 보낸 사용자를 찾아 반환합니다. """

        return self.request.user

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    class Meta:
        model = UserLog
        fields = ["username", "login_date"]