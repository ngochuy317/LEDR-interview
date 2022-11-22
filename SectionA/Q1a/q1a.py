# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from Q1a.constants import (
    digit_text,
    length_of_val_to_suffix
)

def convert_str_to_num(string_val: str) ->int:
    """
    Convert string number to number.
    Parameters:
        string_val (str): A number in string
    Returns:
        int_val (int): A number
    """
    try:
        int_val = int(string_val)
        return int_val
    except ValueError as e:
        print(e)

def one_digit_to_list_of_word(num: int) -> list:
    """
    Convert one digit to list of words.
    Parameters:
        num (int): One digit number
    Returns:
        word (list): A list of words
    """
    word = [digit_text.get(num)]
    return word

def two_digits_to_list_of_word(num: int) -> list:
    """
    Convert two digits to list of words.
    Parameters:
        num (int): Two digits number
    Returns:
        word (list): A list of words
    """
    word = []
    if digit_text.get(num):
        word.append(digit_text.get(num))
    else:
        word.append(digit_text.get((num//10)*10))
        word.append(digit_text.get(num%10))
    return word

def three_digits_to_list_of_word(num: int) -> list:
    """
    Convert three digits to list of words.
    Parameters:
        num (int): Three digits number
    Returns:
        word (list): A list of words
    """
    word = []
    word = one_digit_to_list_of_word(num // 100)
    word.append("Hundred")
    num = num % 100
    word.extend(two_digits_to_list_of_word(num))
    return word

def factory_digit_list_of_word(num: int) -> list:
    """
    Method map to the function handle number by its value.
    Parameters:
        num (int): Three digits number
    Returns:
        word (list): A list of words
    """
    word = []
    if num <= 20:
        word = one_digit_to_list_of_word(num)
    elif num <= 99:
        word = two_digits_to_list_of_word(num)
    elif num <= 999:
        word = three_digits_to_list_of_word(num)
    return word
    


def main(number):
    len_num = len(number)
    if len_num > 9:
        print("number must be less than 999,999,999")
    else:
        no_loop = len_num // 3

        num = convert_str_to_num(number)
        word = []
        for i in range(no_loop + 1, 0, -1):
            temp_num = num // (pow(1000, i -1))
            if temp_num:
                word.extend(x(temp_num))
                if length_of_val_to_suffix.get(i -1):
                    word.append(length_of_val_to_suffix.get(i -1))
            
            num = num % (pow(1000, i -1))
       
        full_word = " ".join(word)
        print(full_word)
        return(full_word)


if __name__ == '__main__':
    number = input("input your number: ")
    main(number)
