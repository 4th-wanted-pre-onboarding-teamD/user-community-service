from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import UserLog

# Create your views here.
class LoginLogGenderStatisticsView(APIView):
    def get(self, request):
        male_cnt = UserLog.objects.filter(user__gender="Male").count()
        female_cnt = UserLog.objects.filter(user__gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)