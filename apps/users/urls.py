from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from . import views

urlpatterns = [
    path('login', views.CustomTokenObtainPairView.as_view()),
    path('login/refresh', TokenRefreshView.as_view()),
    path('login/verify', TokenVerifyView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('withdraw', views.WithdrawalView.as_view()),
]
