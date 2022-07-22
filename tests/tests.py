from django.test import Client, TestCase
from django.urls import reverse


class TestHomepage(TestCase):
    """Class to test the homepage URL and title."""

    def test_homepage_url_and_title(self):
        client = Client()
        response = client.get(reverse("index"))
        assert response.status_code == 200
        assert "<title>Holiday Homes</title>" in response.content.decode()
