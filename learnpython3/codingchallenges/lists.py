def append_size(list):
    list.append(len(list))
    return list

print(append_size([23, 42, 108]))



def append_sum(list):
  list.append(list[-1] + list[-2])
  list.append(list[-1] + list[-2])
  list.append(list[-1] + list[-2])
  return list

print(append_sum([1, 1, 2]))


def larger_list(list1,list2):
  if len(list1) >= len(list2):
    return list1[-1]
  else:
    return list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))



def more_than_n(list, item, n):
  return list.count(item) > n

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))



def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList = sorted(unsorted)
  return sortedList

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))