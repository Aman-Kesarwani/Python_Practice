import random
import string

# prints between 0 and 1
print(random.random())

# prints between 1 and 10 (inclusive 1 and 10)
print(random.randint(1, 10))

# picks from the given array
print(random.choice(["hello", 3, 5, 7]))

# picks two items from the given array
print(random.choices(["hello", 3, 5, 7], k=2))

print(random.choices("abcd", k=4))
print("".join((random.choices("abcd", k=4))))
print(",".join((random.choices("abcd", k=4))))

print(string.ascii_letters)
print(string.digits)

# password generator in more better way
print("".join(random.choices(string.ascii_letters + string.digits, k=6)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)

print(numbers)
