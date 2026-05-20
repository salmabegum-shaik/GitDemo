#with read and write mode
with open("test.txt", "r+") as file:

    data = file.read()

    print("Old Data:", data)

    file.write("\nPyTest")

with open("test.txt",'w+') as file:
    data = file.read()
    print("old data",data)
    file.write("\n cocococococlaaaaaa")


with open("demo.txt", "a+") as file:

    file.write("\nSelenium")

    file.seek(0)

    data = file.read()

    print(data)
#checking if file exist or not
import os
if os.path.exists("test.txt"):
    print("file exist")