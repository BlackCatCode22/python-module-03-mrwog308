########################################################
#                                                      #
#   Write a program which repeatedly reads integers    #  
#   until the user enters “done”. Once “done” is       #
#   entered, print out the min, and max                #
#   of the integers. If the user enters anything       #
#   other than an integer, detect their mistake using  #
#   try and except and print an error message and      #
#   skip to the next integers. (work_ex_5_2)           #
#                                                      #
########################################################

numlist = []

while True:
    
    input = input("\n  Enter a number or 'done' to finish: ")

    if input == "done":
        break

    try:
        num = float(input)
        numlist.append(num)
    except ValueError:
        
        print("\n Invalid input, enter a number or 'done' to end.\n")

if numlist:
    print("\n The maximum is: ", max(numlist))
    print("\n The minimum is: ", min(numlist))
else:
    print("\n No numbers were entered.")