cheeses = ['cheddar', 'swiss', 'Gouda']
number = [42, 123]
empty = []

print(cheeses, number, empty)

print(number[1])

for cheese in cheeses:
  print(cheese)

for i in range(len(number)):
  number[i] = number[i] * 2

print(number[1])


a = [1,2,3]
b = [4,5,6]

c = a + b

print(c)

# slices

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t)
t[1:2] = ['x', 'y']
print(t)

#append
t = ['a', 'b', 'c', 'd', 'e', 'f']
t.append('g')
print(t)

#extend adds list to other list and you tell it where to start based of input of
t1 = ['h', 'b', 'c', 'd', 'e', 'f']
t2 = ['g', 'h']
print(t1)
print(t2)
t1.extend(t2)
print(t1)

# sort from low to high

numbers = [2, 5, 6, 7, 8, 9]
numbers.sort()
print(numbers)

#pop deletes the index
t = ['a', 'b', 'c', 'd', 'e', 'f']
x = t.pop(1)
print(x)
print(t)

#del deletes the index of the value you want to delete
z = ['z', 'b', 'c', 'd', 'e', 'f']
del z[3]
print(z)

# remove it removes the element you want to remove
z = ['a', 'b', 'c', 'd', 'e', 'f']
z.remove('c')
print(z)

# if you want to remove more than 1 element
# 1 is the index where you start 5 is how many elements you remove
z = ['j', 'b', 'c', 'd', 'e', 'f']
del z[1:5]
print(z)


#map filter and reduce

# add all numbers
d = [2, 5, 6, 7, 8, 9]

# def add_all(numbers_to_add):
#     total = 0
#     for numbers in numbers_to_add:
#       total += numbers
#     return total

# print(numbers)

sum(d)
print(d)



