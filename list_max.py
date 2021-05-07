"""
Name: Masud Hussain
Course: CS162
Assignment: 6A
"""


def list_max(a_list):

    """
    Compares the first item to the second item in the list.
    If the first item is greater than the second then it removes the second item.
    If the second item is greater than the first then the first item is removed.
    The list_max() function is called recursively to run through the list.

    Once the list only contains 1 item, it returns the item from the list.

    :param a_list:
    :return: Max value in list
    """

    if len(a_list) == 1:
        return a_list[0]

    if a_list[0] > a_list[1]:
        a_list.pop(1)
    else:
        a_list.pop(0)
    return list_max(a_list)
