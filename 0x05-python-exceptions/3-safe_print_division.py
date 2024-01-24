#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Returns the division of a by b."""

    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))

    return div
