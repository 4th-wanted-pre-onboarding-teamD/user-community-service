from rest_framework.generics import CreateAPIView, DestroyAPIView

from .serializers import RegisterSerializer


# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class WithdrawalView(DestroyAPIView):
    def get_object(self):
        return self.request.user
