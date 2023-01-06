#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
