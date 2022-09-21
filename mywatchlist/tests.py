from django.test import TestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_mywatchlist, show_xml, show_json

# Create your tests here.
class TestUrls(TestCase):

    def setUp(self):
        self.urlToViewHtml = reverse(
            'mywatchlist:show_mywatchlist'
        )
        self.urlToViewJson = reverse(
            'mywatchlist:show_json'
        )
        self.urlToViewXML = reverse(
            'mywatchlist:show_xml'
        )

    def test_my_wish_list_urls_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewHtml
            ).func,
            show_mywatchlist
        )
        
    def test_my_wish_list_xml_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewJson
            ).func,
            show_json
        )

    def test_my_wish_list_json_resolve(self):
        self.assertEqual(
            resolve(
                self.urlToViewXML
            ).func,
            show_xml
        )