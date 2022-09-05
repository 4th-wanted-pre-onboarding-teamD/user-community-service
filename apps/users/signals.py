import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import UserLoginLog
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserLogSerializer
from ipware.ip import get_client_ip

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    log = UserLoginLog()
    log.user = user
    log.ip_address = get_client_ip(request)
    log.user_agent = request.META['HTTP_USER_AGENT']
    log.save()

def create_user_log(user):
    """ 
	로그인 시 유저로그 생성 
	input :
	    UserLog모델에서 받아오는 값 serializing
	output :
		None
    """
    request_data = {"user" : user.id}
    user_log_serializer = UserLogSerializer(data=request_data)
    user_log_serializer.is_valid(raise_exception=True)
    user_log_serializer.save()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        create_user_log(user)
        token['username'] = user.username
        return token