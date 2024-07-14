# Assuming a is a 1D list representing a 2D array with 64 columns per row
a = [k * k for k in range(128)]  # Filling the array with some values for example

i = 1
j = 5
z = a[i*64 + j]

print(f"The value of z is: {z}")  # This will print the value of a[69]
