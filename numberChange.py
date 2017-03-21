class ChangeNumber:

    def __init__(self, __number):
        self.__number = 0

    def add_five(self, num):
        self.__number = num
        return self.__number + 5

    def multiply(self, added):
        self.__added = added
        return self.__added * 3.18

    def getReal(self, prompt):
        value = ""
        valid_real = 0.0
        while not valid_real(value):
            print(value, "is not a number." + "Please try again.")
            value = input(prompt)
        return self.float(prompt)

def numberPlay():
    maths = ChangeNumber(0)
    numValue = getReal(0)
    multip = 0.0
    num = float(input("Please enter a number. \n"))
    numValue = numValue.getReal(num)
    added = maths.add_five(num)
    multip = maths.multiply(added)
    print("The new value is ", multip)

numberPlay()




# add to module:
# num = getReal("Please enter a number. \n")

#def getReal(prompt)
 # value = ""

#  value = input(prompt)
#  while not valid_real(value):
#    print(value, "is not a number. Please try again.")
#    value = input(prompt)
#  return float(value)
