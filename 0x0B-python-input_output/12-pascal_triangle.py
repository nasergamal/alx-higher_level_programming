#!/usr/bin/python3
'''pascal trianlge challenge'''


def pascal_triangle(n):
    '''defining pascal triangle'''
    plist = []
    if n <= 0:
        return plist
    for i in range(n):
        li = []
        li.append(1)
        for m in range(1, i):
            li.append(plist[i - 1][m - 1] + plist[i - 1][m])
        if len(li) == i:
            li.append(1)
        plist.append(li)
    return plist
