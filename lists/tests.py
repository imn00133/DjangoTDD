from django.urls import resolve
# django.core.urlresovers는 삭제됨
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page
# 패키지의 현재 위치를 나타내기 위해 .을 사용


class HomePageTest(TestCase):
	def test_root_rul_resolves_to_home_page_view(self):
		# "/"사이트 루트가 호출 시 resolve를 실행해서, home_page라는 함수 호출
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		# 요청 객체 생성
		response = home_page(request)
		# home_page 뷰에 전달해서 응답을 취득. HttpResponse라는 클래스의 인스턴스
		# 하위는 <html>로 시작해서</html>로 끝나는 것과 title 이름 확인 response.content는 byte형 데이터이다.
		# self.assertTrue(response.content.startswith(b'<html>'))
		# 이런식으로 하는 것은 상수 테스트임으로 사용하지 않고, 구현 결과물을 비교하도록 한다.
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)
