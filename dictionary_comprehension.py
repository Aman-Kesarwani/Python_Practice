values = []

for item in range(10):
    values.append(item*2)

print(values)
values_1 = [x*2 for x in range(10)]  # list comprehension
print(values_1)

set_values = {x*2 for x in range(10)}  # set compreshension
print(set_values)

dict_values = {}
for x in range(10):
    dict_values[x] = x*2
print(dict_values)

dict_values_1 = {x: x*2 for x in range(10)}  # dictionary compreshension
print(dict_values_1)

# value_2 would be generator object not tuple in this case
values_2 = (x*2 for x in range(10))
print(values_2)
