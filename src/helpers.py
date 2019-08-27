__author__ = "Paul Schifferer <paul@schifferers.net>"

from jsonpath_rw import parse
from app.common import exceptions


def get_json_value(json, path):
    try:
        expr = parse(path)
        return expr.find(json)[0].value
    except:
        return None


def validate_json_value(json, path, value):
    try:
        actual_value = get_json_value(json, path)
        if actual_value != value:
            return False
    except:
        return False

    return True


def randhex(size=1):
    result = []
    for i in range(size):
        result.append(
            str(random.choice("0123456789ABCDEF"))
            + str(random.choice("0123456789ABCDEF"))
        )
    return "".join(result)
