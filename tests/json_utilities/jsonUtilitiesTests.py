from core.json_utils.saveToJsonGetQuestions import SaveToJsonGetQuestions
from django.test import TestCase

class JsonUtilitiesTests(TestCase):
    def setUp(self):
        self._save_to_json  = SaveToJsonGetQuestions('all_votes', 1)

    def test_00_sample(self):
        test = self._save_to_json.test_check_json()
        print(dir(test))
