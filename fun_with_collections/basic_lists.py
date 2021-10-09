"""
Program: basic_lists.py
Author: Jeremy Hall
Last date modified: 10/9/2021

The purpose of this program is to pass a number into a function and then that function calls a second
function and then passes the input back to the calling function.
"""

def get_input():
    """
    i was instructed to add this docstring to the function.  I don't know what it is and I dont believe
    its been covered or even mentioned up to this point.

    use reST style.
    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises key/Error: raises an exception
    """

    #prompt user for input.  no validation needed
    user_input = input("Please enter a score:")

    try:
    # cast input to proper type
        user_input = int(user_input)
    # throw exception for non-numeric
    except:
        print("integers only please")
    # return that input as a string.
    finally:
        return user_input


def make_list(num):
    """
    i was instructed to add this docstring to the function.  I don't know what it is and I dont believe
    its been covered or even mentioned up to this point.

    use reST style.
    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises key/Error: raises an exception
    """

    #define a list
    my_list = []

    # pass in num.  Use it to call "get_input" that many times.
    call_function_amount = num

    for x in range(call_function_amount):
        # append user input to the list
        my_list.append(get_input())
    # return the list
    return my_list

if __name__ =='__main__':      #this file is not MAIN.  I still don't understand this.

    print(make_list(1))
    print(make_list(2))
    print(make_list(3))