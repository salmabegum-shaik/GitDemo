class father:
    def house(self):
        print("Father's house")
class son(father):
    def bike(self):

        print("Son's bike")
class daughter(father):
    def car(self):
        print("Daughter's car")

s1 = son()
d1 = daughter()
s1.house()
s1.bike()
d1.house()
d1.car()