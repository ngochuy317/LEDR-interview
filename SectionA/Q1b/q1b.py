# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

def transpose(lst: list) -> list:
    """
    Transpose 2D array.
    Example:
        lst = [
            ['L', 'E', 'D', 'R'],
            ['T', 'E', 'C', 'H']
        ]
        transpose_lst = transpose(lst)
        transpose_lst = [
            ['T', 'L'],
            ['E', 'E'],
            ['C', 'D'],
            ['H', 'R']
        ]
    Parameters:
        lst (list): 2D array
    Returns:
        transpose_lst (list): A the list has been transposed
    """
    transpose_lst = []
    for i in range(len(lst[0])):
        temp = []
        for j in range(len(lst)):
            temp.append(lst[j][i])
        transpose_lst.append(temp)
    
    return transpose_lst

