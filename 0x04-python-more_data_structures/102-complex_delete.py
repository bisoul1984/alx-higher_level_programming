#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for valu_dic in list_keys:
        if value == a_dictionary.get(valu_dic):
            del a_dictionary[valu_dic]

    return (a_dictionary)
