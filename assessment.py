"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
    """Determines if the string provided is my hometown: Charlotte
    
        >>> is_hometown("Charlotte")
        True

        >>> is_hometown("San Francisco")
        False

        >>> is_hometown(123456)
        Bad input. String expected.
    """

    #Confirms input is a string before comparing to catch bad data
    if isinstance(town_name, basestring):
        return town_name == "Charlotte"
    else:
        print "Bad input. String expected."



#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

def combine_names(first_name, last_name):
    """Reads in the first and last name as arguments and returns the
    concatenation of the two 

    >>> combine_names("Bruce", "Banner")
    'Bruce Banner'

    >>> combine_names("Peter", "")
    Bad input. Last name not provided.

    >>> combine_names("", "Wanye")
    Bad input. First name not provided.
    """

    #Checks that the first then last names are strings and not empty
    if (isinstance(first_name, basestring) and first_name):
        if (isinstance(last_name, basestring) and last_name):
            return first_name + " " + last_name
        else:
            print "Bad input. Last name not provided."
    else:
        print "Bad input. First name not provided."



#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

def user_introduction(town_name, first_name, last_name):
    """Uses user input to greet user by full name and compare hometowns
    to the author.

    >>> user_introduction("Charlotte", "Steph", "Curry")
    Hi, Steph Curry. We're from the same place!

    >>> user_introduction("Brooklyn", "Steven", "Rogers")
    Hi, Steven Rogers. Where are you from?
     """

    #Can skip checking for stringyness since the other functions handle that
    if is_hometown(town_name):
        print("Hi, " + combine_names(first_name, last_name) + 
            ". We're from the same place!")
    else:
        print("Hi, " + combine_names(first_name, last_name) +
            ". Where are you from?")



###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit in ["strawberry", "cherry", "blackberry"]:
        return True
    return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit):
        return 0
    return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    return lst + [num]



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, state, tax_percent = 0.05):

    price_with_tax = base_price * (1 + tax_percent)
    price_after_fees = price_with_tax

    #Check state code to add any extra fees
    if state == "CA":
        price_after_fees *= 1.03
    elif state == "PA":
        price_after_fees += 2
    elif state == "MA":
        if base_price > 100:
            price_after_fees += 3
        else:
            price_after_fees += 1

    #Check tax_percent to match docstring formatting (150 instead of 150.0)
    if tax_percent != 0:
        return float("%.1f" % price_after_fees)
    else:
        return price_after_fees


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def append_multiple_to_list(lst, *arguments):
    """Takes a list and an unknown number of additional arguments, and appends
    those arguments to the list

    >>> append_multiple_to_list([1, 2, 3], 4, 5, 6)
    [1, 2, 3, 4, 5, 6]

    >>> append_multiple_to_list([1, 2, 3], 4, [5, 6])
    [1, 2, 3, 4, [5, 6]]
     """

    for argument in arguments:
        lst += [argument]
    return lst

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def outer_function(word):
    """Takes in a word and then calls a nested inner funtion to return that word
    times 3. Returns both the original word and the result of the inner funciton

    >>> outer_function("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')
     """

    def inner_function(word):
        return word * 3
    return (word, inner_function(word))


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
