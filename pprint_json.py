import sys
import json
import pprint


def load_data(file_path):
    with open(file_path, 'r') as json_file:
        return json.loads(json_file.read())


def pretty_print_json(data_json):
    pprint.pprint(data_json)


if __name__ == '__main__':
    pretty_print_json(
        load_data(sys.argv[1]))
