from core.json_utils.saveToJsonGetQuestions import SaveToJsonGetQuestions
from django.conf import settings
from django.test import TestCase
from unittest.mock import Mock, patch

class JsonUtilitiesTests(TestCase):
    def setUp(self):
        self._base_dir      = settings.BASE_DIR
        self._file_dir      = self._base_dir + '/static/json/tests/all_votes.json'

    def test_00_test_json_file_is_the_same(self):
        save_to_json    = SaveToJsonGetQuestions('all_votes', 1)
        test_json_file  = save_to_json.test_check_json()
        self.assertEqual(self._file_dir, test_json_file)

    @patch('core.json_utils.saveToJsonGetQuestions.SaveToJsonGetQuestions.save_json_file', return_value = True)
    def test_01_set_return_as_true(self, mock_save_json_file):
        save_to_json  = SaveToJsonGetQuestions('all_votes', 1)
        value = save_to_json.save_json_file()
        self.assertTrue(value)

    
    @patch('core.json_utils.saveToJsonGetQuestions.SaveToJsonGetQuestions.save_json_file', return_value = False)
    def test_02_set_return_as_false(self, mock_save_json_file):
        save_to_json  = SaveToJsonGetQuestions('all_votes', 1)
        value = save_to_json.save_json_file()
        self.assertFalse(value)

if __name__ == '__main__':
    unittest.main()
