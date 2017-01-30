def truebooj(number):
    """
    Determine if a number is divisible by 3, 5, or 10 or a combination thereof
    :param number: Integer
    :return:
    """
    # Create strings that will hold the values True, Booj, TrueBooj
    # Set all strings to empty as it will need to be seen which ones are not
    divisibleBy3 = ''
    divisibleBy5 = ''
    divisibleBy10 = ''
    # A number can be divisible by more than one number
    # Need to be separate if for each check
    # See if the number is divisible by 3
    if number % 3 == 0:
        divisibleBy3 = 'True'
    # See if the number is divisible by 5
    if number % 5 == 0:
        divisibleBy5 = 'Booj'
    # See if the number is divisible by 10
    if number % 10 == 0:
        divisibleBy10 = 'TrueBooj'
    # Create a list to join the list of strings that are nonempty
    divisibleByList = [divisibleBy3, divisibleBy5, divisibleBy10]
    # Check if list does not contain all empty strings
    if any(divisibleByList):
        # Join string in list that are nonempty and return that string
        return '\n'.join(filter(None, divisibleByList))
    else:
        # If number isn't divisible by 3, 5, 10 return the number
        return str(number)
