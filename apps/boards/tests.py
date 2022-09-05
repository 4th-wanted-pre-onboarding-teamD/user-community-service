

from django.contrib.auth.hashers import make_password

from rest_framework                  import status
from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models  import User
from apps.boards.models import FreeBoard, NoticeBoard, OperationBoard


class TestNoticeBoard(APITestCase):
    '''
        공지게시판 TEST Code
    '''
    # Test시작전 필요한 임시 데이터 생성
    def setUp(self):
        self.user = User.objects.create(
            id       = 1,
            username = "wanted",
            password = make_password("123"),
            name     = "aaa",
            email    = "aaa@gmail.com",
            phone    = "010-1111-2222",
            is_staff = True
        )
        self.notice = NoticeBoard.objects.create(
            id      = 1,
            user_id = 1,
            title   = "공지사항 제목 1",
            content = "공지사항 내용 1"
        )
        self.notice_url = "/api/boards/notice"

    # Test를 위해 생성했던 임시 데이터 삭제
    def tearDown(self):
        User.objects.all().delete()
        NoticeBoard.objects.all().delete()


    # 공지사항 리스트 조회
    def test_notice_list_success(self):
        self.response = self.client.get(self.notice_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 공지사항 상세페이지 조회
    def test_notice_detail_success(self):

        self.response = self.client.get(f'{self.notice_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 공지사항 글 작성
    def test_notice_create_success(self):
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "공지사항추가 제목 2",
            "content": "공지사항추가 내용 2"
        }

        self.response = self.client.post(self.notice_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 공지사항 글 업데이트
    def test_notice_update_success(self):
        
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title": "공지사항 제목1 수정",
            "content": "공지사항 내용1수정",
        }

        self.response = self.client.put(f'{self.notice_url}/1', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


    # 공지사항 작성글 삭제
    def test_notice_delete_success(self):
        
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.delete(f'{self.notice_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)


class TestFreeBoard(APITestCase):
    '''
        자유게시판 TEST Code
    '''
    # Test시작전 필요한 임시 데이터 생성
    def setUp(self):
        self.user = User.objects.create(
            id       = 1,
            username = "wanted",
            password = make_password("123"),
            name     = "aaa",
            email    = "aaa@gmail.com",
            phone    = "010-1111-2222",
            is_staff = False  # 일반유저
            )
        self.user1 = User.objects.create(
            id       = 2,
            username = "wanted1",
            password = make_password("123"),
            name     = "aaa1",
            email    = "aaa1@gmail.com",
            phone    = "010-1111-3333",
            is_staff = False  # 일반유저
            )    
        self.free = FreeBoard.objects.create(
            id      = 1,
            user_id = 1,
            title   = "자유게시판 제목 1",
            content = "자유게시판 내용 1"
        )
        self.free_url = "/api/boards/free"

    # Test를 위해 생성했던 임시 데이터 삭제
    def tearDown(self):
        User.objects.all().delete()
        FreeBoard.objects.all().delete()


    # 자유게시판 리스트 조회(로그인 했을경우)
    def test_free_list_login_success(self):
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.get(self.free_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    

    # 자유게시판 리스트 조회(로그인 안했을경우)
    def test_free_list_success(self):
        self.response = self.client.get(self.free_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


    # 자유게시판 상세페이지 조회(로그인했을경우)
    def test_free_detail_signin_success(self):
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.get(f'{self.free_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 상세페이지 조회(로그인안했을경우)
    def test_free_detail_signin_success(self):

        self.response = self.client.get(f'{self.free_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 글 작성(로그인했을경우)
    def test_free_create_login_success(self):
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "자유게시판 추가 제목 2",
            "content": "자유게시판 추가 내용 2"
        }

        self.response = self.client.post(self.free_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 자유게시판 글 작성 실패(로그인 안했을경우)
    def test_free_create_fail(self):
        data = {
            "title"  : "자유게시판 추가 제목 2",
            "content": "자유게시판 추가 내용 2"
        }

        self.response = self.client.post(self.free_url, data, format='json')
        
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 자유게시판 글 업데이트성공(본인의 글인 경우)
    def test_free_update_login_success(self):
        
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "자유게시판 추가 제목 2",
            "content": "자유게시판 추가 내용 2"
        }

        self.response = self.client.put(f'{self.free_url}/1', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 글 업데이트실패(본인글이 아닌 경우)
    def test_notice_update_success(self):
        self.refresh = RefreshToken.for_user(self.user1)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title": "공지사항 제목1 수정",
            "content": "공지사항 내용1수정",
        }

        self.response = self.client.put(f'{self.free_url}/1', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': '[Access Denied: ERR03] 게시글 수정, 삭제 권한이 없습니다.'})

    # 자유게시판 작성글 삭제(본인글인경우)
    def test_free_delete_success(self):
        
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.delete(f'{self.free_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    # 자유게시판 작성글 삭제(본인글이 아닌경우)
    def test_free_delete_fail(self):
        
        self.refresh = RefreshToken.for_user(self.user1)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.delete(f'{self.free_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': '[Access Denied: ERR03] 게시글 수정, 삭제 권한이 없습니다.'})


class TestOperationBoard(APITestCase):
    '''
        관리자 게시판 TEST Code
    '''
    # Test시작전 필요한 임시 데이터 생성
    def setUp(self):
        self.operation_user = User.objects.create(
            id       = 1,
            username = "wanted",
            password = make_password("123"),
            name     = "aaa",
            email    = "aaa@gmail.com",
            phone    = "010-1111-2222",
            is_staff = True  # 관리자
            )
        self.general_user = User.objects.create(
            id       = 2,
            username = "wanted1",
            password = make_password("123"),
            name     = "aaa1",
            email    = "aaa1@gmail.com",
            phone    = "010-1111-3333",
            is_staff = False  # 일반유저
            )
        self.operation_user_1 = User.objects.create(
            id       = 3,
            username = "wanted2",
            password = make_password("123"),
            name     = "aaa2",
            email    = "aaa2@gmail.com",
            phone    = "010-1111-2222",
            is_staff = True  # 두번째 관리자
            )        
        self.free = OperationBoard.objects.create(
            id      = 1,
            user_id = 1,
            title   = "관리자 게시판 제목 1",
            content = "관리자 게시판 내용 1"
        )
        self.operation_url = "/api/boards/operation"

    # Test를 위해 생성했던 임시 데이터 삭제
    def tearDown(self):
        User.objects.all().delete()
        FreeBoard.objects.all().delete()


    # 관리자 게시판 리스트 조회(관리자 로그인 했을경우)
    def test_operation_list_login_oper_success(self):
        self.refresh = RefreshToken.for_user(self.operation_user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.get(self.operation_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    

    # 관리자 게시판 리스트 조회(일반 유저 로그인)
    def test_operation_list_general_fail(self):
        self.refresh = RefreshToken.for_user(self.general_user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.get(self.operation_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(),  {'detail': '[Access Denied: ERR02] 접근 권한이 없습니다.'})

    # 관리자 게시판 리스트 조회(비 로그인)
    def test_operation_list_fail(self):
        self.response = self.client.get(self.operation_url, format='json')

        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 관리자 상세페이지 조회(관리자 로그인했을경우)
    def test_operation_detail_signin_success(self):
        self.refresh = RefreshToken.for_user(self.operation_user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.get(f'{self.operation_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 관리자 글 작성(관리자 로그인했을경우)
    def test_operation_create_login_success(self):
        self.refresh = RefreshToken.for_user(self.operation_user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "관리자 게시판 추가 제목 2",
            "content": "관리자 게시판 추가 내용 2"
        }

        self.response = self.client.post(self.operation_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 관리자 글 업데이트성공(본인의 글인 경우)
    def test_operation_update_login_success(self):
        
        self.refresh = RefreshToken.for_user(self.operation_user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "관리자 게시판 수정 제목 2",
            "content": "관리자 게시판 수정 내용 2"
        }

        self.response = self.client.put(f'{self.operation_url}/1', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 관리자 글 업데이트실패(본인글이 아닌 경우)
    def test_operation_update_fail(self):
        self.refresh = RefreshToken.for_user(self.operation_user_1)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "관리자 게시판 수정 제목 2",
            "content": "관리자 게시판 수정 내용 2"
        }

        self.response = self.client.put(f'{self.operation_url}/1', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': '[Access Denied: ERR03] 게시글 수정, 삭제 권한이 없습니다.'})

    # 관리자 작성글 삭제(본인글인경우)
    def test_operation_delete_success(self):
        
        self.refresh = RefreshToken.for_user(self.operation_user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.delete(f'{self.operation_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    # 관리자 작성글 삭제(본인글이 아닌경우)
    def test_operation_delete_fail(self):
        
        self.refresh = RefreshToken.for_user(self.operation_user_1)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.delete(f'{self.operation_url}/1', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': '[Access Denied: ERR03] 게시글 수정, 삭제 권한이 없습니다.'})
        