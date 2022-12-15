first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name,last_name):
  return first_name[:3]+last_name[:3]

new_account = account_generator(first_name,last_name)

first_name1 = "Reiko"
last_name1 = "Matsuki"

def password_generator(first_name,last_name):
  print(last_name[2:])
  return str(first_name[len(first_name)-3:]+last_name[len(last_name)-3:])