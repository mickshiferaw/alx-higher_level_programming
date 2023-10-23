#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        abc = fct(*args)
        return (abc)
    except Exception as ex:
        print("Exception: {}".format(ex))
        return (None)
