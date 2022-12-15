guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  n = None
  while True:
    if n is not None:
      line_data = n.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")

    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    n = yield name, age


guest_generator = read_guestlist('guest_list.txt')


i=0
for guest in guest_generator:
  if i < 10:
    print(guest)
    i += 1
  else:
    break

print(guest_generator.send('Jane,35'))
print(guests)

print(next(guest_generator))
print(next(guest_generator))
print(next(guest_generator))
print(next(guest_generator))


drinks_generator = (name for name, age in guests.items() if age >= 21 )

for i in drinks_generator:
    print(i)


def Table_1():
  food = 'Chicken'
  table = 1
  for i in range(1,6):
    seat = i
    yield food, table, seat

def Table_2():
  food = 'Beef'
  table = 2
  for i in range(1,6):
    seat = i
    yield food, table, seat


def Table_3():
  food = 'Fish'
  table = 3
  for i in range(1,6):
    seat = i
    yield food, table, seat

fish_table = Table_3()
for i in range(5):
  print(next(fish_table))

def all_tables():
  yield from Table_1()
  yield from Table_2()
  yield from Table_3()

tables = all_tables()
print(next(tab))
print(next(tab))


def table_assigner(guests, all_tables):
   for guest, table in zip(guests, all_tables):
       yield guest, table

assign = table_assigner(guests, tab)


assign = ((guest, table) for guest, table in zip(guests, tab))
