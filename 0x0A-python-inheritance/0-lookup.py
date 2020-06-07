#!/usr/bin/python3
"""
function that returns the list of available attributes and methods
"""


def lookup(obj):
    """
    function that returns the list of available attributes and methods
    """
    return sorted(dir(obj))
