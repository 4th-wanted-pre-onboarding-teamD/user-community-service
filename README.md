# 01_WayneHills_D - 커뮤니티 API 서버
원티드 프리온보딩 백엔드 기업 과제

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 기술 스택](#프로젝트-기술-스택)
3. [개발 기간](#개발-기간)
4. [팀 구성](#팀-구성)
5. [역할](#역할)
6. [ERD](#ERD)
7. [API 목록](#API-목록)
8. [프로젝트 시작 방법](#프로젝트-시작-방법)


<br>


## 프로젝트 개요
사용자들이 글로 소통할 수 있는 일반 커뮤니티로
- 회원가입, 로그인, 탈퇴 등의 유저 기능
- 게시글 CRUD 기능
- 커뮤니티 이용 통계

을 제공하는 Django 기반 API 서버입니다. 


<br>

## 과제 요구사항 분석
### 1. 회원가입 / 탈퇴, 로그인 등 유저 기능 구현
- 로그인은 JWT를 활용한 토큰 인증 방식으로 구현
- 회원가입, 탈퇴

### 2. 공지 게시판, 자유 게시판, 운영 게시판 CRUD
- 각 게시판별 전체 글 조회, 글 작성, 수정, 특정 글 조회, 삭제 기능

### 3. 게시판별 권한 설정
- 유저는 **일반 유저** 와 **운영 유저** 가 존재 (추후 확장 가능)
- 유저별 게시판 접근 권한

| 게시판 | 유저 | 생성\(C\) | 조회\(R\) | 수정(U) | 삭제(D) |
| --- | --- | --- | --- | --- | --- |
| 공지 게시판 | 비로그인 유저 | :x: | :o: | :x: | :x: |
| - | 일반 유저 | :x: | :o: | :x: | :x: |
| - | 운영 유저 | :o: | :o: | :o: | :o: |
| 자유 게시판 | 비로그인 유저 | :x: | :o: | :x: | :x: |
| - | 일반 유저 | :o: | :o: | :o: | :o: |
| - | 운영 유저 | :o: | :o: | :o: | :o: |
| 운영 게시판 | 비로그인 유저 | :x: | :x: | :x: | :x: |
| - | 일반 유저 | :x: | :x: | :x: | :x: |
| - | 운영 유저 | :o: | :o: | :o: | :o: |

### 4. 사용자 이용 통계
- 사용자의 로그인 기록을 토대로 이용 내역 통계

<br>

## 프로젝트 기술 스택

### Backend
<section>
<img src="https://img.shields.io/badge/Django-092E20?logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20?logo=Django&logoColor=white"/>
</section>

### DB
<section>
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=MySQL&logoColor=white"/>
</section>

### Tools
<section>
<img src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white"/>
<img src="https://img.shields.io/badge/Discord-5865F2?logo=Discord&logoColor=white">
<img src="https://img.shields.io/badge/Postman-FF6C37?logo=Postman&logoColor=white">
</section>
<!-- | 백엔드 | DB   |  Tools   |
| ---- | ------ | --- |
|      |        |    | -->


<br>


## 개발 기간
- 2022/08/31~2022/09/05


<br>


## 팀 구성
| 김현수 | 유혜선 | 임한구 |  최보미  |
| ------ | ------ | ------ | --- |
| [Github](https://github.com/HyeonsooKim) | [Github](https://github.com/Hyes-y)   | [Github](https://github.com/nicholas019/)   |  [Github](https://github.com/BomiChoi)   |


<br>


## 역할
### 김현수
1. 로그인 로그 기록 기능 추가
2. 성별/나이별/시간대별 통계자료 API 기능 작성
### 유혜선
1. 유저별 접근 권한 설정 관련 Permissions 작성
2. 게시판 API에 권한 설정

### 임한구
1. Unit Test Code 구현
     - APITestCase 클래스 사용
     - Board CRUD + permission 기능에 대한 Test Code
2. 구현부분
     - users app API 3종(로그인, 회원가입, 회원탈퇴)
     - boards app API 3종(공지사항게시판, 자유게시판, 관리자게시판)
3. users APP Test Case(6종)
     - 회원가입 성공, 회원가입 실패(중복아이디체크, 패스워드 확인실패)
     - 로그인 성공, 로그인 실패(패스워드 불일치)
     - 회원탈퇴 성공
4. boards APP Test Case(23종)
     - **공지사항게시판** : 리스트 조회성공(비로그인), 상세페이지 조회 성공(비로그인), 글작성 성공(로그인), 글 업데이트 성공(본인글), 작성글 삭제(본인글)
     - **자유게시판** : 리스트 조회 성공(로그인, 비로그인), 상세페이지 조회 성공(로그인, 비로그인), 글작성 성공(로그인), 글작성실패(비로그인), 글 업데이트 성공(본인글), 글업데이트 실패(본인글이 아닌경우), 글삭제성공(본인글), 글삭제 실패(본인글이 아닌경우)
     - **관리자게시판** : 리스트 조회 성공(관리자로그인), 리스트 조회 실패(일반유저로그인, 비로그인), 상세페이지 조회 성공(관리자 로그인), 글작성 성공(관리자 로그인), 글 업데이트 성공(본인글), 글업데이트 실패(본인글이 아닌경우), 글삭제성공(본인글), 글삭제 실패(본인글이 아닌경우)

### 최보미
1. 로그인/회원가입/회원탈퇴 API 작성
    - simplejwt 사용
    - 회원가입 시 중복 아이디, 비밀번호 일치 검증
    - 회원탈퇴 시 현재 요청한 유저를 삭제
2. 각 게시판별로 CRUD API 작성
    - 요청한 유저를 작성자 필드에 저장
    - DetailView에 GET 요청을 보낼 경우 조회수 1 증가


<br>


## ERD
![](https://i.imgur.com/2bgYJbN.png)


<br>


## API 목록
https://documenter.getpostman.com/view/17766148/VUxVqjXV


<br>


## 프로젝트 시작 방법
1. 로컬에서 실행할 경우
```bash
# 프로젝트 clone(로컬로 내려받기)
git clone -b develop --single-branch https://github.com/4th-wanted-pre-onboarding-teamD/01_WayneHills_D.git

cd 01_WayneHills_D

# 가상환경 설정
python -m venv ${가상환경명}
source ${가상환경명}/bin/activate
# window (2 ways) 
# 1> ${가상환경명}/Scripts/activate
# 2> activate

# 라이브러리 설치
pip install -r requirements.txt
# 실행
python manage.py runserver
```

<br>