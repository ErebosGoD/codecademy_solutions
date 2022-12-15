import random

name = input("What is your name? ")
question = input("What is your question? ")
answer = ""
random_number = random.randint(1,9)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if name != "" and question != "":
  print(name + " asks: "+ question)
  print("Magic 8-Balls's answer: " + answer)
elif name != "" and question == "":
  print("You did not ask a question")
elif name == "" and question != "":
  print("Question: "+ question)
  print("Magic 8-Balls's answer: " + answer)
else:
  print("Error")