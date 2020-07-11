from sys import getsizeof

values = [x * 2 for x in range(100000)]
print("values length: ", len(values))
print("size Of values - list: ", getsizeof(values))

# for billion object you won't do the above way since the above way
# would consume very much memory
# Best way is to use generator

values = (x*2 for x in range(100000))
# print("values length: ", len(values)) -- returns error as generator object would comes into existence
# when iterating
print("size Of values - generator: ", getsizeof(values))
print(values)
