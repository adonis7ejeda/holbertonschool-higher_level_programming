#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers"""
    if list_of_integers:
        if(list_of_integers[0] > list_of_integers[1]):
            return list_of_integers[0]
        elif(list_of_integers[-1] > list_of_integers[-2]):
            return list_of_integers[-1]
        else:
            return(max(list_of_integers))
    return None
