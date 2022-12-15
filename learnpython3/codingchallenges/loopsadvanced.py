def larger_sum(lst1,lst2):
  sum_1 = 0
  sum_2 = 0
  for num in lst1:
    sum_1 += num
  for num in lst2:
    sum_2 += num
  return lst1 if sum_1 >= sum_2 else lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))



def over_nine_thousand(lst):
  sum = 0
  while sum <= 9000:
    for num in lst:
      sum += num
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))



def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
    else:
      continue
  return max

print(max_num([50, -10, 0, 75, 20]))



def same_values(lst1, lst2):
  same_values = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      same_values.append(index)
  return same_values

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))