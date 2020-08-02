
import pandas as pd
import json

class CachedProperty(object):
    """
    A property that is only computed once per instance and then replaces
    itself with an ordinary attribute. Deleting the attribute resets the
    property.

    Taken from https://github.com/bottlepy/bottle/blob/master/bottle.py
    """

    # TODO: allow refresh

    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self

        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


cached_property = CachedProperty


def read_json(path):
    with open(path) as json_file:
        return json.load(json_file)


def save_json(path, data):
    with open(path, 'w') as json_file:
        return json.dump(data, json_file, indent=4, sort_keys=True)


def read_csv(csv_path):
    df = pd.read_csv(csv_path)
    df = df.applymap(str)
    df = df.replace({'nan': None})
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df


def save_csv(path, data):
    with open(path, 'w') as json_file:
        return json.dump(data, json_file, indent=4, sort_keys=True)
