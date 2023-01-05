#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    list = [1, 2, 3, 4, 5]
idx = 5
idx = 3
idx = 4
idx = 0
new_list = delete_at(list, idx)
print(new_list)
print(list)
