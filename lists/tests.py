from django.urls import resolve
# django.core.urlresovers는 삭제됨
from django.test import TestCase
from .views import home_page
# 패키지의 현재 위치를 나타내기 위해 .을 사용


class HomPageTest(TestCase):
	def test_root_rul_resolves_to_home_page_view(self):
		# "/"사이트 루트가 호출 시 resolve를 실행해서, home_page라는 함수 호출
		found = resolve('/')
		self.assertEqual(found.func, home_page)
