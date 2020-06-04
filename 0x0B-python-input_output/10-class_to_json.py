#!/usr/bin/python3
"""Returns the dictionary description"""


def class_to_json(obj):
    """Returns the dictionary description"""
    my_dic = {}
    for key in obj.__dict__:
        my_dic[key] = obj.__dict__[key]
    return my_dic
