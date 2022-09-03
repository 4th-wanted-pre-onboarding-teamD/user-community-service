from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, max_length=159)
    password = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})
    password_check = serializers.CharField(write_only=True, max_length=128, style={'input_type': 'password'})
    name = serializers.CharField(write_only=True, max_length=10)
    email = serializers.EmailField(write_only=True)
    gender = serializers.ChoiceField(write_only=True, choices=User.GENDER_CHOICES, required=False,
                                     allow_null=True)
    age = serializers.IntegerField(write_only=True, min_value=1, required=False, allow_null=True)
    phone = serializers.CharField(write_only=True, required=False, allow_null=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise ValidationError({'username', '이미 존재하는 아이디입니다.'})
        if attrs['password'] != attrs['password_check']:
            raise ValidationError({'password', '비밀번호와 비밀번호 확인이 일치하지 않습니다.'})
        return attrs

    def create(self, validated_data):
        # 사용자 생성
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            name=validated_data['name'],
            email=validated_data['email'],
        )

        # 추가정보 저장
        user.gender = validated_data.get('gender', None)
        user.age = validated_data.get('age', None)
        user.phone = validated_data.get('phone', None)
        user.save()

        # 토큰 발급 후 반환
        refresh = RefreshToken.for_user(user)
        return {
            'access': refresh.access_token,
            'refresh': refresh
        }
