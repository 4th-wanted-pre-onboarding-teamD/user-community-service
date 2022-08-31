from django.db import models


class User(models.Model):
    """
    회원 정보 모델
    """
    GRADES = (('general', '일반'), ('admin', '운영'),)
    SEX = (('M', '남자'), ('F', '여자'),)

    user_id = models.CharField('회원아이디', max_length=30, unique=True)
    name = models.CharField('회원명', max_length=30)
    password = models.CharField('비밀번호', max_length=32)
    grade = models.CharField('회원 등급', max_length=7, choices=GRADES)
    sex = models.CharField('성별', max_length=1, choices=SEX)
    age = models.PositiveIntegerField('나이')
    contact = models.CharField('연락처', max_length=12)
    reg_date = models.DateTimeField('가입일', auto_now_add=True)
    last_login = models.DateTimeField('마지막 접속일')
    withdraw = models.BooleanField('탈퇴여부', default=0)


class Board(models.Model):
    """
    게시판 기본 모델
    """
    title = models.CharField('제목', max_length=30)
    content = models.TextField('내용')
    created_at = models.DateTimeField('등록날짜', auto_now_add=True)
    updated_at = models.DateTimeField('수정날짜', auto_now=True)


class FreeBoard(Board):
    """
    자유 게시판 모델(게시판 기본 모델 상속)
    """
    author_id = models.ForeignKey(User, db_column="author_id", related_name='user')


class AdminBoard(Board):
    """
    운영 게시판 모델(게시판 기본 모델 상속)
    """
    author_id = models.ForeignKey(User, db_column="author_id", related_name='user')


class NoticeBoard(Board):
    """
    공지 게시판 모델(게시판 기본 모델 상속)
    """
    author_id = models.ForeignKey(User, db_column="author_id", related_name='user')