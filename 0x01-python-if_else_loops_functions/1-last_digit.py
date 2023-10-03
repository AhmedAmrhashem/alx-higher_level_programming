#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_to_string = str(number)
i = len(num_to_string)
if num_to_string[i-1] > '5':
    print(f"Last digit of {num_to_string} is {num_to_string[i-1]} and is greater than 5")
elif num_to_string[i-1] == '0':
    print(f"Last digit of {num_to_string} is {num_to_string[i-1]} and is zero")
else:
    print(f"Last digit of {num_to_string} is {num_to_string[i-1]} and is less than 6 and not 0")

