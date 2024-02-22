# Learning Project Eight: Physics Class

# You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.


# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Create functions to convert Celsius to Fahrenheit and in reverse
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp / 5/9 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

print(f100_in_celsius)
print(c0_in_fahrenheit)

# Create function to measure energy

def get_force(mass, acceleration):
  return mass*acceleration

train_force = get_force(train_mass, train_acceleration)

print(train_force)

def get_energy(mass, c = 3*10**8):
  return mass * c

bomb_energy = get_energy(bomb_mass)

print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Create function to determine energy output

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance))