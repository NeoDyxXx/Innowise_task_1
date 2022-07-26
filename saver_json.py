import json

class JSONSaver:
    def __call__(self, result_list: list, path_of_file: str):
        with open(path_of_file + '.json', 'w') as file:
            json.dump(result_list, file)