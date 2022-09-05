from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import NoticeBoard, FreeBoard, OperationBoard
from .serializers import NoticeBoardSerializer, FreeBoardSerializer, OperationBoardSerializer
from .permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly, IsAuthenticated, IsAdminUser


class NoticeBoardView(ListCreateAPIView):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]

    def perform_create(self, serializer):
        # 현재 요청한 유저를 작성자로 설정
        serializer.save(user=self.request.user)


class NoticeBoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = NoticeBoard.objects.all()
    serializer_class = NoticeBoardSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly, IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit += 1  # 조회수 1 증가
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FreeBoardView(ListCreateAPIView):
    queryset = FreeBoard.objects.all()
    serializer_class = FreeBoardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 현재 요청한 유저를 작성자로 설정
        serializer.save(user=self.request.user)


class FreeBoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = FreeBoard.objects.all()
    serializer_class = FreeBoardSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit += 1  # 조회수 1 증가
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OperationBoardView(ListCreateAPIView):
    queryset = OperationBoard.objects.all()
    serializer_class = OperationBoardSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        # 현재 요청한 유저를 작성자로 설정
        serializer.save(user=self.request.user)


class OperationBoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = OperationBoard.objects.all()
    serializer_class = OperationBoardSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.hit += 1  # 조회수 1 증가
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
