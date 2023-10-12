#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return (str)
    y = str[n]
    newStr = str.replace(y, '')
    return (newStr)
