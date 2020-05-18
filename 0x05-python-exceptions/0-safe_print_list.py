#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list[0:x]:
            print(i, end='')
    except IndexError:
        print("Error")
    print()
    return x
'''Create by adonis7ejeda'''
