from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from . import views

urlpatterns = [
    path('gender/login', views.LoginLogGenderStatisticsView.as_view()),
    path('age/login', views.LoginLogAgeStatisticsView.as_view()),
    path('gender/users', views.UserGenderStatisticsView.as_view()),
    path('age/users', views.UserAgeStatisticsView.as_view()),
    path('gender/notice', views.NoticeBoardGenderStatisticsView.as_view()),
    path('age/notice', views.NoticeBoardAgeStatisticsView.as_view()),
    path('gender/free', views.FreeBoardGenderStatisticsView.as_view()),
    path('age/free', views.FreeBoardAgeStatisticsView.as_view()),
    path('gender/operation', views.OperationBoardGenderStatisticsView.as_view()),
    path('age/operation', views.OperationBoardAgeStatisticsView.as_view()),
]
