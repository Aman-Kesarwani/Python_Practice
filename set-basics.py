numbers = [101, 102, 101, 102, 103, 104]

unique_elements = set(numbers)
print(unique_elements)
set_1 = {123, 124}
set_1.add(125)
print(len(set_1))
print(set_1)

first = set(numbers)

second = {201, 202, 101, 102}

print(first | second)  # union - all the items which is in first or second

print(first & second)  # intersection

print(first - second)  # difference - all elements of first not in second

# symetric difference - either in first or second not in both
print(first ^ second)

# sets are un-ordered - you can't aspect to get elements in seqeunce of insertion
# so it does not support indexing

if 201 in second:
    print('yes')
