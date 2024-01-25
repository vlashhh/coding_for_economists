def add_one(num):
  return num + 1

print(add_one(5))

def add_one_str():
  print(6)

print(add_one_str())

res = add_one(5)
res_str = add_one_str()

print(res, res_str)

def add_one_return_both(num1):
  return num1, num1 + 1

print(add_one_return_both(5))

def add_two_nums(num1, num2):
  res = num1 + num2
  return num1,num2,res

print(add_two_nums(5,6))

def exponentiate(num, exponent = 2):
  return num ** exponent

print(exponentiate(5,2) == exponentiate(5))

print(exponentiate(exponent=1, num =2 ))

def add_nums(*nums):
  res = 0

  for num in nums:
    res += num
  return res



print(add_nums(1,2,3,4,5))

def cast_listitems_to_str(list_of_objects):
  listik = []
  for i in list_of_objects:
    listik.append(str(i))
  return listik

print(cast_listitems_to_str([1,2,3,4,5]))

def square(x):
  """
  Returns the square of x

  Parameters:
  ------------------
  x: int or float or double
  
  Returns:
  square_x: int or float or double 
  """
  return x ** 2

square_lambda = lambda x: x ** 2

print(square(5) == square_lambda(5))