"""
Name: (put your name here)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    grades[0]=input("Give me the next grade in [0 to 10]:")
    grades[1]=input("Give me the next grade in [0 to 10]:")
    grades[2]=input("Give me the next grade in [0 to 10]:")
    grades[3]=input("Give me the next grade in [0 to 10]:")
    grades[4]=input("Give me the next grade in [0 to 10]:")
    for idx in range(len(grades)):
        if all(num.isdigit() for num in grades):
            grade_test = list(map(int, grades))
            if all(0<=g<=10 for g in grade_test):
                grades[idx]=grade_test
            else:
                print("Error in read_five_ints: input string is not for an integer")
        exit() 
                


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    pass

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    pass


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
