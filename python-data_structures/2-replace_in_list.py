#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list
if idx >= len(my_list) or idx < 0:
    return my_list
my_list[idx] = element
return my_list
