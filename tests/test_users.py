from config.base_test import BaseTest


class TestUsers(BaseTest):

    def test_create_user(self):
        user = self.api_users.create_user()
