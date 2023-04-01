# Putting what I've learned from function section into practice
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:
# This function converts farhenheit to celsius 
# f_temp = Fahrenheit Temperature
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Testing our function
f100_in_celsius = round(f_to_c(100), 1)
print(f100_in_celsius)

# Creating a function that converts celsius to fahrenheint.
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# testing our c_to_f function
c0_in_fahrenheit = round(c_to_f(0), 1)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")