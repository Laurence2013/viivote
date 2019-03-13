from main.save_data_to_json import Save_Data_To_Json
from core.utilities.general_utils import General_Utils
from django.conf import settings

class SaveToJsonGetQuestions:
    __slots__ = ('_get_json', '_base_dir', '_gen_utils', '_json_file', '_user_id')

    def __init__(self, json_file, user_id):
        self._get_json  = Save_Data_To_Json()
        self._base_dir  = settings.BASE_DIR
        self._gen_utils = General_Utils()
        self._json_file = json_file
        self._user_id   = user_id

    def check_json(self):
        return self._base_dir + '/static/json/'+ self._json_file +'.json'

    def save_json_file(self, **kwargs):
        if kwargs.get('json') != 0 or kwargs.get('json') == 0:
            get_q = self._gen_utils.get_questions(kwargs.get('user_id'))
            self._get_json.save_json(get_q, kwargs.get('json_file'))
            return True
        return False

    '''
    For now here contains all the tests that interact with the system
    '''
    
    def test_check_json(self):
        return self._base_dir + '/static/json/tests/'+ self._json_file +'.json'
