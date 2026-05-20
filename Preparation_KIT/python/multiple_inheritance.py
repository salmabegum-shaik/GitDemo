class mother:
    def __init__(self,jewellery):
        self.jewellery=jewellery
    def show(self):
        print("mothers jewellery",self.jewellery)
class father:
    def __init__(self,house):
        self.house=house
    def display(self):
        print("fathers house",self.house)
class child(father,mother):
    def __init__(self,bike,house,jewellery):
       father.__init__(self,house)
       mother.__init__(self,jewellery)
       self.bike=bike
    def assets(self):
        print("the assets of mine",self.bike)
c1=child("suzuki","bungalow","necklace")
c1.display()
c1.show()
c1.assets()
