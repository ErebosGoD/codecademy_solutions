import csv
from collections import namedtuple

# Code for Checkpoint 1 goes here.
tree = namedtuple("tree", ["index", "width", "height", "volume"]) 

with open('codecademy/learnadvancedpython3/functionalprogramming/trees.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader) 
  mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)
  trees = tuple(mapper)
  print(trees)