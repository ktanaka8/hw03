"""
Name: Kathryn Tanaka
Peers: Mathieu Zhang (uncle)
References: Pythong Tutor code visualizer
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
    
    PARAMS:
        - u_grades: user input of any digit from 1-10
    RETURNS:
        - grades: int of initial u_grade string
    
    """
    for idx in range(len(grades)):
        u_grades=input("Give me the next grade in [0 to 10]:") #gets user-input grade as a string
        if u_grades.isdigit(): #checks that there are only digits in the string
            u_grades=int(u_grades) #casts digits as integers
            if 0 <= u_grades <= 10: #checks that the user-input grade is within range
                grades[idx]=u_grades #stores values in the corresponding places in the list
            else:
                print("Error in read_five_ints: input integer outside of range") #if values are not in range, print error message
                exit()
        else:
            print("Error in read_five_ints: input string is not for an integer") #if input is not 100% digits, print error message
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
    
    PARAMS:
        - operation: user choice of a, b, or c
    RETURNS:
        - avg: value of the user-input choice after performing an operation on it
    """
    operation=input("Pick 'a' for mean, 'b' for median, 'c' for mode: ") #get user input on which operation to perform
    if operation == 'a':
        print("picked: Mean") #print which operation the user chose
        avg = statistics.mean(grades) #assign variable 'avg' to the average value of input grades
        return avg
    elif operation == 'b':
        print("picked: Median") #print which operation the user chose
        avg = statistics.median(grades) #assign variable 'avg' to the median value of input grades
        return avg
    elif operation == 'c':
        print("picked: Mode") #print which operation the user chose
        avg = statistics.mode(grades) #assign variable 'avg' to the mode value of input grade
        return avg
    else:
        print("Error in pick_averaging_method: incorrect option picked") #if user input is not 'a', 'b', 'c' then print error message
        exit()

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    PARAMS:
        - pick: user input of 1 or 2
    RETURNS:
        - average
    """
    pick=str(input("Pick '1' for print average, or '2' for plot average: ")) #asks user to pick 1 or 2
    if pick == '1':
        print_list_and_average(average) #if 1 is picked, the entire list and its average is printed
    elif pick == '2':
        plot_grades(average) #if 2 is picked, the value obtained by operation user picked earlier will be marked by a carat in a list of the numbers
    else:
        print("Error in pick_visualization: incorrect option picked") #if user picked something other than 1 or 2, print error message
        exit()


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
