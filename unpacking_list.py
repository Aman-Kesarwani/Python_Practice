
numbers = [1, 2, 3, 4, 5, 6]
first, second, *other = numbers

print(first)  # print 1
print(second)  # print 2
print(other)  # print remaing list [3, 4, 5, 6]

first, *other, last = numbers

print(last)  # print last element
print(first)
print(other)
