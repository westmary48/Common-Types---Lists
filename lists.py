import random

my_randoms = [1, 3, 1, 2, 4, 2, 5, 4, 2, 5]

my_new_list = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]

"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 10)

# Iterate from 1 to 10
for number in num_list:
  contains = False
  for ranNum in my_randoms:
    if ranNum == number:
      containes = True
for number in numbers_1_to_10:
    the_numbers_match = False
    print(f'{number} is not on the random list {number}')

# for number in my_randoms:
#     the_numbers_match = True
#     print(f'{number} is on the random list')

# Iterate your random number list here
for number in my_randoms:
  the_numbers_match = False

    # Do the two numbers match? Change the boolean.

  print(f'{number} is in the random list')