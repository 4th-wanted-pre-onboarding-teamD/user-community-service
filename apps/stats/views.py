from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.generic import View
from rest_framework import status

from apps.users.models import UserLog, User
from apps.boards.models import NoticeBoard, FreeBoard, OperationBoard

class UserGenderStatisticsView(APIView):
    """
    유저의 남녀 수를 확인합니다.
    """
    def get(self, request):
        male_cnt = User.objects.filter(gender="Male").count()
        female_cnt = User.objects.filter(gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)


class UserAgeStatisticsView(APIView):
    """
    유저의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        for i in range(1, 10):
            age_num = (
                User.objects
                .filter(age__gte=i * 10, age__lt=i * 10 + 10)
                .distinct()
                .count()
            )
            age_key = str(i * 10) + '대'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)


class LoginLogGenderStatisticsView(APIView):
    """
    로그인 로그에서 남녀의 분포를 확인합니다.
    """
    def get(self, request):
        male_cnt = UserLog.objects.filter(user__gender="Male").count()
        female_cnt = UserLog.objects.filter(user__gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)


class LoginLogAgeStatisticsView(APIView):
    """
    로그인 로그에서의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        for i in range(1, 10):
            age_num = (
                UserLog.objects.select_related("user")
                .filter(user__age__gte=i * 10, user__age__lt=i * 10 + 10)
                .distinct()
                .values_list("user")
                .count()
            )
            age_key = str(i * 10) + '대'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)


class NoticeBoardGenderStatisticsView(APIView):
    """
    공지사항 게시판에서 남녀의 분포를 확인합니다.
    """
    def get(self, request):
        male_cnt = NoticeBoard.objects.filter(user__gender="Male").count()
        female_cnt = NoticeBoard.objects.filter(user__gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)


class NoticeBoardAgeStatisticsView(APIView):
    """
    공지사항 게시판에서의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        for i in range(1, 10):
            age_num = (
                NoticeBoard.objects.select_related("user")
                .filter(user__age__gte=i * 10, user__age__lt=i * 10 + 10)
                .distinct()
                .values_list("user")
                .count()
            )
            age_key = str(i * 10) + '대'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)


class FreeBoardGenderStatisticsView(APIView):
    """
    자유 게시판에서 남녀의 분포를 확인합니다.
    """
    def get(self, request):
        male_cnt = FreeBoard.objects.filter(user__gender="Male").count()
        female_cnt = FreeBoard.objects.filter(user__gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)


class FreeBoardAgeStatisticsView(APIView):
    """
    자유 게시판에서의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        for i in range(1, 10):
            age_num = (
                FreeBoard.objects.select_related("user")
                .filter(user__age__gte=i * 10, user__age__lt=i * 10 + 10)
                .distinct()
                .values_list("user")
                .count()
            )
            age_key = str(i * 10) + '대'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)


class OperationBoardGenderStatisticsView(APIView):
    """
    운영 게시판에서 남녀의 분포를 확인합니다.
    """
    def get(self, request):
        male_cnt = OperationBoard.objects.filter(user__gender="Male").count()
        female_cnt = OperationBoard.objects.filter(user__gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)


class OperationBoardAgeStatisticsView(APIView):
    """
    운영 게시판에서의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        for i in range(1, 10):
            age_num = (
                OperationBoard.objects.select_related("user")
                .filter(user__age__gte=i * 10, user__age__lt=i * 10 + 10)
                .distinct()
                .values_list("user")
                .count()
            )
            age_key = str(i * 10) + '대'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)