from  oops   import  calculator


class child(calculator):
    num2 = 100
    def __init__(self):
        calculator.__init__(self,2,10)

    def getCompletedata(self):
        return self.num2+self.num+self.summation()

obj=child()
print(obj.getCompletedata())