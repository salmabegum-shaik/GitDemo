class destruct:
    def __init__(self,name):
        self.name=name
        print(f" object {self.name} created ")
    def show(self):
        print(f"the show method for object {self.name}")
    def __del__(self):
        print(f"object {self.name} deleted")

d1=destruct("salma")
d1.show()
del d1
d1.show()
# d1



