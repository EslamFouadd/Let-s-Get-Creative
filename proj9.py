# Define functions to represent sets using set-builder notation

def natural_numbers_less_than_4():
    """Returns the set of natural numbers less than 4."""
    return {x for x in range(1, 4)}

def natural_numbers_greater_than_or_equal_to_7():
    """Returns the set of natural numbers greater than or equal to 7."""
    return {x for x in range(7, float('inf'))}

def multiples_of_5_greater_than_0():
    """Returns the set of multiples of 5 greater than 0."""
    return {5 * x for x in range(1, float('inf'))}

def first_five_odd_natural_numbers():
    """Returns the set of the first five odd natural numbers."""
    return {2 * x + 1 for x in range(5)}

def first_five_even_natural_numbers():
    """Returns the set of the first five even natural numbers."""
    return {2 * x for x in range(1, 6)}

# Example sets using set-builder notation

set_a = natural_numbers_less_than_4()
set_b = natural_numbers_greater_than_or_equal_to_7()
set_c = multiples_of_5_greater_than_0()
set_d = first_five_odd_natural_numbers()
set_e = first_five_even_natural_numbers()

# Print the elements of each set

print("Elements of Set A:", set_a)
print("Elements of Set B:", set_b)
print("Elements of Set C:", set_c)
print("Elements of Set D:", set_d)
print("Elements of Set E:", set_e)
