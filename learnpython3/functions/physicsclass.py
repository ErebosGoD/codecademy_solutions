train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1



def fahrenheit_to_celcius(fahrenheit_temperature):
    celcius_temperature = (fahrenheit_temperature-32)*5/9
    return celcius_temperature

fahrenheit100_in_celsius = fahrenheit_to_celcius(100)
print(fahrenheit100_in_celsius)



def celcius_to_fahrenheit(celcius_temperature):
    fahrenheit_temperature = celcius_temperature *(9/5)+32
    return fahrenheit_temperature

celcius0_in_fahrenheit = celcius_to_fahrenheit(0)
print(celcius0_in_fahrenheit)



def get_force(mass,acceleration):
    return mass*acceleration

train_force = get_force(train_mass,train_acceleration)
print(train_force)

print(f"The GE train supplies {train_force} Newtons of force.")



def get_energy(mass,c=3*10**8):
    return mass * c**2

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

print(f"A 1kg bomb supplies {bomb_energy} Joules.")



def get_work(mass,acceleration,distance):
    return get_force(mass,acceleration) * distance

train_work = get_work(train_mass,train_acceleration,train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")