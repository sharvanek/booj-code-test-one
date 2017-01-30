def eqindex(data):
    """
    Calculte the equlibrium indicies (if any) of a interger list of undetermined
    length
    :param data: Integer list
    :return:
    """
    # EquilibriumIndexTest.py gives a list of intergers. Assume this is the case
    # Declare a list that holds the equilibrium indicies for an interger list
    # Empty list signifies there were not any equilibrium indicies
    equilibIndexlist = []

    # Care about indicies and thus need to iterate through the list using them
    for i in range(len(data)):
        # Check sums of elements below and above index
        # If there are no elements above/below index, the sum is 0 respectively
        if sum(data[:i]) == sum(data[i+1:]):
            # If the sums are equal then the index is an equilib index
            equilibIndexlist.append(i)
    return equilibIndexlist
