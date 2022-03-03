"""
Assignment: Set Assignment
Program: set_membership.py
Author: Colby Boell
Last date modified: 03/03/2022

The purpose of this program is to pass a set and a value into in_set function to see if the
value is within the set then print out if it was in the set or not.
"""


# function to see if value is in set.
def in_set(the_set, the_value):
    check_set = the_value in the_set
    return check_set


# main where we call the function
if __name__ == '__main__':
    # variables
    test_set = {'banana', 'apple', 'cherry'}
    test_value = 'apple'

    # if statement to print out appropriate result
    if in_set(test_set, test_value):
        print(f'The value {test_value} is in the set {test_set}')
    else:
        print(f'The value {test_value} is not in the set {test_set}')

"""
Tests:
1.)
variables:
test_set = {'banana', 'apple', 'cherry'}
test_value = 8
result:
The value 8 is not in the set {'cherry', 'apple', 'banana'}

2.)
variables:
test_set = {'banana', 'apple', 'cherry'}
test_value = 'chapstick'
result:
The value chapstick is not in the set {'apple', 'banana', 'cherry'}

3.)
variables:
test_set = {'banana', 'apple', 'cherry'}
test_value = 'apple'
result:
The value apple is in the set {'banana', 'apple', 'cherry'}
"""
