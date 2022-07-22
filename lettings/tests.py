from django.test import Client, TestCase
from django.urls import reverse
import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
class TestLettings(TestCase):
    """Class to test the lettings URL and title."""

    client = Client()
    url_index = reverse("lettings:index")
    url_letting = reverse("lettings:letting", args=[1])

    def test_lettings_index_url_and_title(self):
        response = self.client.get(self.url_index)
        assert response.status_code == 200
        assert "<title>Lettings</title>" in response.content.decode()

    def test_lettings_letting_url_and_title(self):
        address = Address.objects.create(
            number="1901",
            street="W Madison St",
            city="Chicago",
            state="IL",
            zip_code="60612",
            country_iso_code="USA",
        )
        letting = Letting.objects.create(title="United Center", address=address)
        response = self.client.get(self.url_letting)
        assert response.status_code == 200
        assert "<title>United Center</title>" in response.content.decode()
