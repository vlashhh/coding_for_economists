import random

random_number = random.randint(20, 34)
print(random_number)

random_number = 22
if random_number < 25:
  print("The number is less than 25")
elif random_number < 30:
  print("The number is less than 30")
else:
  print("The number is less than 34")


a = random.randint(0,10)
b = random.randint(10,20)

if a < 9:
  print(f"a is equal to: {a}"")
  if b < 19:
    print(f"b is smaller than 19")