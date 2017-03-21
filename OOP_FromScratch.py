class pet:
    number_of_legs = 0

    def sleep(self):
        print("zzzzz")

    def count_legs(self):
        print("I have %s legs." % self.number_of_legs)

class dog(pet):
    def bark(self):
        print("woof")

foxy = dog()
foxy.sleep()
foxy.number_of_legs = 4
foxy.count_legs()