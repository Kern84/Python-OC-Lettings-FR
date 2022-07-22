from django.test import Client, TestCase
from django.urls import reverse
import pytest
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.mark.django_db
class TestProfiles(TestCase):
    """Class to test the profiles URL and title."""

    client = Client()
    url_index = reverse("profiles:index")
    url_profile = reverse("profiles:profile", args=["MJ"])

    def test_profiles_index_url_and_title(self):
        response = self.client.get(self.url_index)
        assert response.status_code == 200
        assert "<title>Profiles</title>" in response.content.decode()

    def test_profiles_profile_url_and_title(self):
        user = User.objects.create(
            username="MJ",
            first_name="Michael",
            last_name="Jordan",
            email="michael@email.fr",
        )
        profile = Profile.objects.create(user=user, favorite_city="Chicago")
        response = self.client.get(self.url_profile)
        assert response.status_code == 200
        assert "<title>MJ</title>" in response.content.decode()
