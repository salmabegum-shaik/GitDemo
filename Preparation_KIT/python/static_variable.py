class stat:
    company_name="capgemini"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        # self.company_name = "altran" #here instance variable is creted which will overshadow the class variable
        print(f"the employee name {self.name}, the employee age {self.age} the employee works in {self.company_name}")


s1=stat("salma",27)
s1.display()
s1.company_name = "TCS"
# you are not changing the class variable. Instead, you are creating a new
# instance variable called company_name that
# shadows the class variable for that particular object (s1).
s1.display()
s2=stat("sasalala",27)
s2.display()
print(s1.company_name)
stat.company_name = "WIPRO"
print(s1.company_name)
print(s2.company_name)
s3=stat("shama",27)
s3.display()
print(s3.company_name)

print("######### various places to declare static variable #######")

class Employee:
    company = "TCS"
    def __init__(self,name,job):
        self.name=name
        self.job = job
        Employee.Manager= "Neha"
    def display(self):
        print(f"Employee details \t {self.name},\t {self.job},\t{self.Manager}")
    @classmethod
    def newmanager(cls):
        cls.L1_manager="sanjay"
        print(f"employee L1 namagaer {cls.L1_manager}, and main manager {Employee.Manager}")


    @staticmethod
    def stats():
        Employee.HR="Namratha"

        print(f"employee L1 namagaer {Employee.L1_manager}, and main manager {Employee.Manager} and Hr is {Employee.HR}")

e1=Employee("salma","spftware")
e1.display()
e1.newmanager()
e1.stats()
