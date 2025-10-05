import random
print(random.randint(5, 20))  # line 1
#Get a number from 5 to 20. The min is 5 and max is 20.
print(random.randrange(3, 10, 2))  # line 2
#Start from 0, step is 2 until -10, it is a random number
#min: -8 max: 0
#4 will not be created because it is not in the range
print(random.uniform(2.5, 5.5))  # line 3
#Get a float number from 2.5 to 5.5
#min: nearby2.5, max: nearby 5.5
print(random.randint(1,100))
