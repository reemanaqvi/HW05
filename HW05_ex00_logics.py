# #!/usr/bin/env python
# # HW05_ex00_logics.py
# ##############################################################################

# def even_odd():
#     """ Print even or odd:
#         Takes one integer from user
#             accepts only non-word numerals
#             must validate
#         Determines if even or odd
#         Prints determination
#         returns None
   
#  # """
#     while True:
#         ui = raw_input("Enter a number: ")
#         try:
#             int_ui = int(ui)
#         except:
#             print "Enter non-word numerals only!"
#         else:
#             break
#     if int_ui%2 ==1:
#         print "Odd number"
#     else:
#         print "Even number"
#         pass

def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    
    n=1
    while n<=100:
        if n%10 == 0:
            print n
        else:
            print n,
        n +=1
   


# def find_average():
#     """ Takes numeric input (non-word numerals) from the user, one number
#     at a time. Once the user types 'done', returns the average.
#     """
#     numbers = 0
#     sumOfNumbers = 0
#     while True:
#         ui = raw_input("Enter first number or 'done' to calculate average: ")
#         if ui == 'done':
#             break
#         else:
#             try:
#                 int_ui = int(ui)
#             except:
#                 print "Numerals please!"
#             else:
#                 numbers +=1
#                 sumOfNumbers +=int_ui
#         average = float(sumOfNumbers)/float(numbers)
#     print average
        

    

# ##############################################################################
def main():
#     """ Calls the following functions:
#         - even_odd()
#         - ten_by_ten()
#     Prints the following function:
#         - find_average()
#     """
#     even_odd()
    ten_by_ten()
#     find_average()

if __name__ == '__main__':
    main()
