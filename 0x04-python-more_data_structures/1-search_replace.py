#!/usr/bin/python3


def search_replace(my_list, search, replace):
    return [replace if s == search else s for s in my_list]
