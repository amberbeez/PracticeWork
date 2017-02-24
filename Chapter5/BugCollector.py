_author_ = "amber buckley"
# description: design a program that keeps a running tally of bugs collected for up to 7 days
#
#  still need to add variables. local
# function Boolean is_valid_integer(number_of_bugs)
# declare boolean
#   is_valid = is number_of_bugs a valid integer?
#   return is_valid
# end function
def is_valid_integer(number_of_bugs):
    try:
        val = str(number_of_bugs)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

# Function integer get_bugs_collected()
# declare
# for counter = 1 To 7
#   display "How many bugs did you collect today?"
#   input number_of_bugs
#   set total_bugs = total + number_of_bugs
#   while Not is_valid
#       display "Please add a number"
#       input number_of_bugs
#       is_valid = is_valid_integer(number_of_bugs)
#   end while
#   total = number_of_bugs + i
#   return input_bugs
# End function
def get_bugs_collected(): #get number of bugs from each day and tally the total
    total = 0
    for i in range(0, 7):
        number_of_bugs = int(input("How many bugs did you collect today (day" + str(i + 1) + ")?"))
        is_valid = is_valid_integer(number_of_bugs)
        while not is_valid:
            number_of_bugs = input("Please enter a number.")
            is_valid = is_valid_integer(number_of_bugs)
    total += number_of_bugs + i
    return total

# update module:  # needs sum
number_of_bugs = 0
counter = 0
total_bugs = 0
def bug_collector_count():
    print("This program will add up how many bugs you collected in 7 days."
    "Have fun out there!")
    total = get_bugs_collected()
    print("You collected", total, "bugs this week.")
bug_collector_count()
