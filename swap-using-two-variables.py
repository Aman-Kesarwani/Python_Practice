x = 10
y = 20

print("The current variables are: ")
print("X: ", x)
print("y: ", y)

z = x
x = y
y = z

print("Swap using 3 variables ")
print("X: ", x)
print("y: ", y)

x, y = y, x  # the tuple way its same as (x, y)
print("Swap again using 2 variables")
print("X: ", x)
print("y: ", y)
