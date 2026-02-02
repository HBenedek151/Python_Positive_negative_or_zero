"""
Production code - This is the application code that we are testing.
This module contains the business logic for categorizing numbers.
"""


def categorize_number(number):
    if number > 0:
        return "Pozitive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

    # TODO: Írd meg az implementációt!

