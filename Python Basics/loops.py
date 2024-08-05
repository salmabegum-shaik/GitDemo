greeting='morning'
if greeting=='morning':
    print("condition matched")
else:
    print("condition unmatched")
print("if condition completed")


sum =0
for j in range(1,6):
    sum = sum+j
print(sum)

for i in range(1,10,2):
    print(i)

print("*******************")
for m in range(10):
    print(m)

print("***********************")
it=4
while it>1:
    print(it)
    it=it-1
print("**********hui*************")
it=4
while it>1:
    if it != 3:
      print(it)

    it=it-1

print("**********huiiii*************")
it=4
while it>1:
    if it == 3:
        break
    print(it)

    it=it-1
print("**********huiiii*************")
it=10
while it>1:
    if it == 5:
        it = it - 1
        continue

    if it == 3:
        break
    print(it)
    it = it - 1