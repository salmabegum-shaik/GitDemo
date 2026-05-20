class father:
    def __init__(self,house,car):
        self.house=house
        self.car=car

    def show(self):
        print("the fathers house",self.house)
        print("the fathers car",self.car)
class child(father):
    def __init__(self,house,car,bike): #here we must pass the parent constructor parameters
        super().__init__(house, car)
    # def __init__(self,bike):
        # super().__init__("bungalow","honda") #here we are gard coding the values so we dont need to pass the house
        # and car parameter insdie the child constructor
        self.bike=bike
    def display(self):
        print("the child's bike is",self.bike)

c1=child("bungalow","lamborgini","suzuki")
c1.display()
c1.show()

