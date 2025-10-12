"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elasped_bake_time):
    """Calculate the remaining bake time in minutes.
    
    :param time_passed: int - The number of minutes the lasagna has been baking.
    :return: int - The number of minutes remaining.
    """
    time_passed = EXPECTED_BAKE_TIME - elasped_bake_time
    return(time_passed)

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Define the preparation_time_in_minutes() function that takes the number_of_layers you want to add to the lasagna as an argument and
    returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.
    """
    added_layers = PREPARATION_TIME * number_of_layers
    return(added_layers)

#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elasped_bake_time):
    """Define the elapsed_time_in_minutes() function that takes two parameters as arguments:
    number_of_layers (the number of layers added to the lasagna)
    elapsed_bake_time (the number of minutes the lasagna has spent baking in the oven already).
    This function should return the total minutes you have been in the kitchen cooking — your preparation time layering + the time the
    lasagna has spent baking in the oven.
    """
    
    total_minutes = preparation_time_in_minutes(number_of_layers) + elasped_bake_time
    return(total_minutes)
    

total_bake_time = elapsed_time_in_minutes(3, 20)
print(total_bake_time)

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
