import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestHomePage:
    def test_homepage_url(self, client):
        url = reverse("blog:home")
        response = client.get(url)
        assert response.status_code == 200

    def test_post_htmx_fragment(self, client):
        headers = {"HTTP_HX-Request": "true"}
        response = client.get(reverse("blog:home"), **headers)
        assertTemplateUsed(response, "blog/components/post-list-elements.html")
