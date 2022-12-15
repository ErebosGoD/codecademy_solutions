from stacks import Stack
print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks += [left_stack, middle_stack, right_stack]

#Set up the Game
number_of_disks = int(input("\nHow many disks do you want to play with?\n"))

while number_of_disks < 3:
  number_of_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(number_of_disks, 0, -1):
  left_stack.push(i)
number_of_optimal_moves = (2 ** number_of_disks) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(number_of_optimal_moves))

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name_of_stack = stacks[i].get_name()
      first_letter = choices[i]
      print(f"Enter {first_letter} for {name_of_stack}")
    user_input = input('')
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

#Play the Game
number_of_user_moves = 0
while right_stack.get_size() != number_of_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      number_of_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(number_of_user_moves, number_of_optimal_moves))