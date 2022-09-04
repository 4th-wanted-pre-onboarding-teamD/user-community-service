from django.conf import settings
from rest_framework.permissions import BasePermission, SAFE_METHODS
import jwt


class IsAuthenticated(BasePermission):
    """
    로그인 한 유저(액세스 토큰 있는) 접근 가능
    ERR01
    """
    message = "[Access Denied: ERR01] 접근 권한이 없습니다."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsAdminUser(BasePermission):
    """
    운영 등급 회원에게만 모든 권한 허용 (is_staff=True)
    운영자 : CRUD
    일반 회원 : X
    ERR02
    """
    message = "[Access Denied: ERR02] 접근 권한이 없습니다."

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(BasePermission):
    """
    작성자 외 읽기 권한만 부여
    JWT 토큰을 decode, obj의 user와 해당 user가 일치하는지 확인
    ERR03
    """
    message = "[Access Denied: ERR03] 게시글 수정, 삭제 권한이 없습니다."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            token = request.headers.get('Authorization').split(" ")[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
            token_user = payload.get('user_id')

            return obj.user.id == token_user


class IsStaffOrReadOnly(BasePermission):
    """
    운영 등급 회원(is_staff=True) 에게 모든 권한을 허용, 일반 회원은 읽기만 가능
    운영자 : CRUD
    일반 회원 : R
    ERR04
    """
    message = "[Access Denied: ERR04] 게시글 수정, 삭제 권한이 없습니다."

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
