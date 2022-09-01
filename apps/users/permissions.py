from rest_framework import permissions
import jwt
from waynehills_D.settings import SECRET_KEY


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    작성자 외 읽기 권한만 부여
    JWT 토큰을 decode, obj의 user와 해당 user가 일치하는지 확인
    """
    message = '작성자만 수정, 삭제가 가능합니다.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            token = request.COOKIES['access']
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            token_user = payload.get('user_id')

            return obj.user == token_user


class IsStaffOrReadOnly(permissions.BasePermission):
    """
    운영 등급 회원(is_staff=True) 에게 모든 권한을 허용, 일반 회원은 읽기만 가능
    운영자 : CRUD
    일반 회원 : R
    """
    message = '운영자만 글 작성이 가능합니다.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_staff

