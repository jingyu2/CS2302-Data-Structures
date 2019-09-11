"""
@author: Jing Jing Yu

Created on: Thu, Sep 5, 2019
Assignment: Lab 1 option B - Password Cracking
Class: CS 2302 Data Structure
Section: MW 1:30 pm - 2:50 pm
Instructor: Diego Aguirre

Overview: A file contains 100 accounts information, the information
included username, salt value, and hashed password,
in the format of <username>, <salt value>, <hashed password>. Find the
real password that contains only number, and between 3 tp 7 characters long
"""

import hashlib
import time


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def check_pass(password):
    fr = open('password.txt', 'r')

    for cur_line in fr:
        # Split the file, text_line[0] is username, text_line[1] is salt value, text_line[2] is hashed string
        text_line = cur_line.split(',')
        # Get a new hashed string by using hash_with_sha256() method with password and salt value
        new_line = hash_with_sha256(password + str(text_line[1]))
        # If the new hashed string is the same as the one in file, then we found the password!!
        if new_line == text_line[2].rstrip():
            print(text_line[0], ':', password)
    fr.close()


# This method is to find all possible combinations of password
# The possible combinations are at least 3 characters long, and at most 7 characters long
# The password contains only numbers from 0 t0 9
# All the possible combinations are from 000 - 9999999
def find_combo(size, pass_list):
    if size == 0:
        check_pass(pass_list)
    else:
        for i in range(0, 10):
            find_combo(size-1, pass_list + str(i))


# The length of the password will be between 3-7
def find_len(min_len, max_len):
    for n in range(min_len, max_len):
        # Call method, find_combo(), to find all possible combination n characters long
        find_combo(n, '')


def main():

    start = time.time()

    # The length of the password will be between 3-7
    find_len(3, 8)

    end = time.time()

    print('The program took', end - start, 'seconds')

main()