#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    store = 0
    if my_list == None:
        return None
    else:
        for i in range(length):
            if my_list[i] > store:
                store = my_list[i]
        return store

