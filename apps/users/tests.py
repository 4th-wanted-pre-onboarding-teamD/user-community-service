from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class TestUser(APITestCase):
    '''
        users app의 API 3개(회원가입, 로그인, 회원탈퇴) unit test
    '''
    def setUp(self):
        self.user = User(
            id       = 1,
            username = "wanted",
            password = make_password("123"),
            name     = "aaa",
            email    = "aaa@gmail.com",
            phone    = "010-1111-2222"
        )
        self.user.save()
        

    # 회원가입
    def test_register_success(self):
        
        self.user_data = {
            "username"      : "wantedtest",
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "phone"         : "010-1111-2222"
            }

        self.register_url = "/api/users/register"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 회원가입 증복아이디 체크 실패
    def test_register_id_ckeck_fail(self):
        
        self.user_data = {
            "username"      : "wanted", # 중복아이디
            "password"      : "111222333",
            "password_check": "111222333",
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "phone"         : "010-1111-2222"
            }

        self.register_url = "/api/users/register"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    # 회원가입시 패스워드 확인 실패
    def test_register_password_check_fail(self):
        
        self.user_data = {
            "username"      : "wantedtest",
            "password"      : "111222333",
            "password_check": "111111111", # 패스워드 확인 오류
            "name"          : "홍길동",
            "email"         : "abc@gmail.com",
            "phone"         : "010-1111-2222"
            }

        self.register_url = "/api/users/register"
        self.response = self.client.post(self.register_url, data = self.user_data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    # 로그인
    def test_login_success(self):
        self.login_url = "/api/users/login"
        data= {
                "username": "wanted",
                "password": "123",
            }
        response= self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 비밀번호 불일치
    def test_password_fail(self):
        self.login_url = "/api/users/login"
        data= {
                "username": "wanted",
                "password": "133",
            }
        response= self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {"detail": "No active account found with the given credentials"})

    # 회원탈퇴
    def test_withdraw_success(self):
        self.withdraw_url = "/api/users/withdraw"

        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')

        response= self.client.delete(self.withdraw_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

