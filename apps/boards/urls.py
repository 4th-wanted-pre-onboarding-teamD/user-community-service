from django.urls import path

from . import views

urlpatterns = [
    path('notice', views.NoticeBoardView.as_view()),
    path('notice/<int:pk>', views.NoticeBoardDetailView.as_view()),
    path('free', views.FreeBoardView.as_view()),
    path('free/<int:pk>', views.FreeBoardDetailView.as_view()),
    path('operation', views.OperationBoardView.as_view()),
    path('operation/<int:pk>', views.OperationBoardDetailView.as_view())
]
