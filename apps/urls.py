from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('boards/', include('apps.boards.urls')),
    path('stats/', include('apps.stats.urls'))
]
