# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals


def int_to_string(int_val: int) -> str:
    """
    Convert int to string. If number is only have one digit,
    leading zero will be added.
    Parameters:
        int_val (int): integer value
    Returns:
        str_val (str): string value
    """
    if 0 <= int_val < 10:
        str_val = f"0{int_val}"
    else:
        str_val = str(int_val)
    return str_val


def serial_number_to_data(list_serial_number: list) -> list:
    """
    Convert serial number to data.
    Parameters:
        list_serial_number (list): list of serial number
    Returns:
        data (list): list of data
    """
    data = []
    for idx, ele in enumerate(list_serial_number):
        first_chr = ele[0]
        last_chr = ele[-1]
        data.append(first_chr + last_chr + int_to_string(idx + 1))
    return data
