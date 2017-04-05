from django.test import TestCase
from home.views import home
from django.core.urlresolvers import resolve


class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, home)
