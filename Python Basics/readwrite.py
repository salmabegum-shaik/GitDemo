file = open('test.txt')
# #print(file.read())
# print(file.read(2))
# print(file.readline())
# print(file.readline())
# print(file.read())
#file.close()

'''print line by line using read line method'''

# line = file.readline()
#
#
# while  line !='':
#     print(line)
#     line=file.readline()
#
# file.close()

for line in file.readlines():
    print(line)



