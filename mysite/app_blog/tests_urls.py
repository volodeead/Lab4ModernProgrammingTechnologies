# app_blog/tests_urls.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_blog.views import HomePageView  # Імпортуйте клас HomePageView

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePageView)


