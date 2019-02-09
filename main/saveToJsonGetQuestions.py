from main.save_data_to_json import Save_Data_To_Json
from core.utilities.general_utils import General_Utils
from django.conf import settings

class SaveToJsonGetQuestions:
    __get_json  = Save_Data_To_Json()
    __base_dir  = settings.BASE_DIR
    __gen_utils = General_Utils()

    def check_json(self, json_file):
        return self.__base_dir + '/static/json/'+ json_file +'.json'

    def save_json_file(self, **kwargs):
        if kwargs.get('json') != 0 or kwargs.get('json') == 0:
            get_q = self.__gen_utils.get_questions(kwargs.get('user_id'))
            self.__get_json.save_json(get_q, kwargs.get('json_file'))
            return True
        return False
