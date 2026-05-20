def countdown(num):
    while num >0:
        yield num
        num = num - 1

count=countdown(5)

print(next(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))

def even_number(num):
    i = 0
    while i < num:
        if i % 2 == 0:
            yield i
        i=i+1


even=even_number(10)
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))
print(next(even))