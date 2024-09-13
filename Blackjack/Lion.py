# def add(num1, num2):
#   return num1 + num2

def add(*numbers):
  return sum(numbers)

sum_1 = add(1,2,3,4,5,6)

print(sum_1)


def add(*input):
  return input

str_1 = add('hiy')