class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
    def __str__(self):
        return f"{self.name} got marks {self.marks}"

s1=student("salma",22)
s2=student("mallu",23)
print(s1+s2)
print(s1)
print(s2)
