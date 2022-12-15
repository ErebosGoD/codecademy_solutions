def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0:
      counter += 1
  return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))



def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append(f"Hello, {name}")
  return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))



def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))



def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))



def exponents(bases,powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))