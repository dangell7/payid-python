import re

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

def get_included_object(obj):
    try:
        rel = obj['_included'][0]['rel']
        data = obj['_included'][0]['data']
        return rel, data
    except:
        return None


def has_included_objects(obj):
    return '_included' in obj

import json

def read_json(path):
    with open(path) as json_file:
        return json.load(json_file)
