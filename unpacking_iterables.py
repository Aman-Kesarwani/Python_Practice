numbers = [101, 102, 103]
print(numbers)

print(*numbers)  # unpacking would take out individual elements

values = list(range(5))
print(values)

values_1 = [*range(5), *"Hello World"]
print(values_1)

first = [101, 102]
second = [201, 202]

unpack_list = [*first, *second, "Hey"]
print(unpack_list)

first_dict = {"x": 1}
second_dict = {"y": 2}
comb_dict = {**first_dict, **second_dict, "z": 1001}
print(comb_dict)
