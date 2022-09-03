from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer


# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class WithdrawalView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
