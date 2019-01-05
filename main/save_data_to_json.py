import os
import json
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder

class Save_Data_To_Json:
    def __init__(self):
        self.__base_dir = settings.BASE_DIR

    def get_json_file(self, get_json):
        main_json_file = self.__base_dir + '/static/json/'+ get_json +'.json'
        try:
            main_json_file_size = os.path.getsize(main_json_file)
            if main_json_file_size > 0:
                with open(main_json_file) as json_file:
                    get_main_json = json.load(json_file)
        except FileNotFoundError as e:
            # Log this to file
            print(e)
        return get_main_json

    def save_json(self, save_file_to_json, get_json):
        main_json_file = self.__base_dir + '/static/json/'+ get_json +'.json'     
        json_file = json.dumps(save_file_to_json, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
        with open(main_json_file, 'w') as f:
            f.write(json_file)

