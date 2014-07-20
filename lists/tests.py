from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from lists.views import Home

class HomeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/lists/')
        self.assertEqual(found.func, Home.get())

    def test_home_page_displays_list_of_lists(self):
        request = HttpRequest()
        test_home = Home()
        response = test_home.get(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b"<title>Teacher\'s List</title>", response.content)
        self.assertIn(b"<h1>Teacher\'s List</h1>", response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

