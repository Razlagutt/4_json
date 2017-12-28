import sys
import json
import pprint


def load_data(filepath):
    with open(filepath, "r") as data:
        return json.loads(data.read())


def pretty_print_json(data):
    pprint.pprint(data)


if __name__ == '__main__':
    pretty_print_json(
        load_data(sys.argv[1]))
