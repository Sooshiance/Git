from django.urls import reverse
from faker import Faker
from rest_framework.test import APITestCase


class TestRegister(APITestCase):
    def setUp(self):
        super().setUp()

        self.english_faker = Faker("en-US")

        self.password = self.english_faker.password()

        self.register_url = reverse("register")

    def test_create_user_success(self) -> None:
        payload = {
            "username": self.english_faker.user_name(),
            "email": self.english_faker.safe_email(),
            "password": self.password,
        }

        response = self.client.post(
            self.register_url,
            data={**payload},
            format="json",
        )

        print("\n")
        print("=" * 50)
        print(response.data)

    def test_create_user_fail(self) -> None:
        pass


class TestToken(APITestCase):
    def setUp(self):
        super().setUp()

        self.token_url = reverse("token")


class TestProfile(APITestCase):
    def setUp(self):
        super().setUp()

        self.profile = reverse("profile")
