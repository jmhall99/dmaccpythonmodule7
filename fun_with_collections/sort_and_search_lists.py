"""
Program: basic_lists.py
Author: Jeremy Hall
Last date modified: 10/9/2021

The purpose of this program is to pass a number into a function and then that function calls a second
function and then passes the input back to the calling function.
"""

def sort_list(incomingList):
    """
    i was instructed to add this docstring to the function.  I don't know what it is and I dont believe
    its been covered or even mentioned up to this point.

    use reST style.
    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises key/Error: raises an exception
    """

    #receives the incoming list
    myList = incomingList

    #sorts the list
    myList.sort()

    print(id(incomingList))
    print(id(myList))

    # these 2 print statement generate the same output.
    # Therefore both lists are referencing the SAME list in memory.
    # because of this we do NOT need to return the list.


def search_list(whatFor):
    """
    i was instructed to add this docstring to the function.  I don't know what it is and I dont believe
    its been covered or even mentioned up to this point.

    use reST style.
    :param parameter_1: this is what the first parameter represents
    :param parameter_2: this is what the second parameter represents
    :returns: this is what is returned
    :raises key/Error: raises an exception
    """

    # hardcode a list here since we arent passing in a list this time,
    # instead we are passing in what we are searching for  (per the instructions in the video)

    anotherList = ['f', 'c', 'b', 'd', 'g', 'a', 'e']

    # receive the incoming value to search for
    searchValue = whatFor

    # search the list for that value.
    for i in range(len(anotherList)):
        if anotherList[i] == searchValue:
            # we do need to return the list as the list doesnt exist outside of this function.
            # since we didnt pass the list into the function this time.
            return True
    return False

if __name__ =='__main__':      #again this file is not MAIN.  I still/again don't understand this.

    #hardcode a list
    myList = ['f', 'c', 'b', 'd', 'g', 'a', 'e']

    sort_list(myList)

    #search_list(myList)
    print(search_list('a'))
    print(search_list('z'))