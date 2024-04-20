#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """_summary_
        Args:
            my_list: list
            search : number  to find in the list to replace it.
            replace: nem number that user want in the list.
        Returns:
            _type_: list : new list with replaced numbers.
    """
    new_list = []
    for i in range(len(my_list)):
        if  my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
