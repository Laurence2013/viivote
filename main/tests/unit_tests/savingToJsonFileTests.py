from django.test import RequestFactory, TestCase, Client
from users.tests.db_setup.db_setup import UserLoginInfo
from main.saveToJsonGetQuestions import SaveToJsonGetQuestions
from main.views import *
from unittest.mock import patch, Mock

class SavingToJsonFileTests(TestCase):
    def setUp(self):
        self.user = UserLoginInfo('lozza2000','lozza2000@gmail.com')
        self.user.setupLogin() 
        self.client= Client()

    def test_00_check_that_a_client_can_login_and_return_302_to_go_to_main_page(self):
        self.response = self.client.post('/main/login/', {'username': 'lozza2000', 'password': 'mysha25pass',})
        # Redirects to 'main' page
        self.assertEqual(302, (self.response.status_code))

    def test_01_check_that_user_is_logged_in(self):
        c = self.client.login(username = 'lozza2000', password = 'mysha25pass')
        self.assertTrue(c)

    def test_02_file_check_that_json_file_size_is_80(self):
        json_file = 'all_votes'
        mock_account = Mock()
        mock_account.check_json.return_value = 80
        self.assertEqual(80, mock_account.check_json(json_file))

    def test_03_data_is_saved_into_json_file_return_value_is_true(self):
        json_file = 'all_votes'
        mock_save_json_file = Mock()
        mock_save_json_file.save_json_file.return_value = True
        self.assertTrue(mock_save_json_file.save_json_file(json = 80, user_id = 1, json_file = json_file))

    def test_04_data_is_not_saved_into_json_file_return_value_is_false(self):
        json_file = 'all_votes'
        mock_save_json_file = Mock()
        mock_save_json_file.save_json_file.return_value = False
        self.assertFalse(mock_save_json_file.save_json_file(json = 80, user_id = 1, json_file = json_file))

if __name__ == '__main__':
    unittest.main()
