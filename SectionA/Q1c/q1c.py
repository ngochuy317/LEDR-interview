# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


def parenthesis_check(seq: str) -> bool:
    """
    Method check parenthesis is valid or not
    Parameters:
        seq (str): parenthesis sequence
    Returns:
        boolean: True if parenthesis is valid else False
    """
    
    seq = seq.replace(" ", "")
    while True:  
        if '()' in seq :  
            seq = seq.replace ('()', '' )
        elif '{}' in seq :  
            seq = seq.replace ('{}', '' )
        elif '[]' in seq :  
            seq = seq.replace ('[]', '' )
        else:
            return not bool(seq)
