class calculator:
    num = 100

    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b
        print("iam called automatically when object is created")
    def getdata(self):
        print("alhamdulillah")
    def summation(self):
        return self.firstnumber+self.secondnumber+calculator.num


obj=calculator(2,3)
print(obj.summation())
obj.getdata()
print(obj.num)


obj1=calculator(4,6)
print(obj1.summation())
obj.getdata()
print(obj.num)
