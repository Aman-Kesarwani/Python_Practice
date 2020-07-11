from array import array

numbers = array('i', [101, 102, 103])

numbers.append(104)
print(numbers)

print("After insert at zero place")
numbers[0] = 105
# Every object should be of same type, In this case : integer

print(numbers)

print("After removal of 105:")
numbers.remove(105)
print(numbers)

popped_num = numbers.pop()  # pop the last number 104
print("After popping : ")
print(popped_num)
print(numbers)

# numbers[0] = 4.2 -- you can't insert float in integer array
