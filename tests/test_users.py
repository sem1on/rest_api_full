import allure
import pytest

from config.base_test import BaseTest

@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.regretion
    @allure.title("Create user")
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_username(user.username)
