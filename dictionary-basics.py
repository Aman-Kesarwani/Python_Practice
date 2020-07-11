training_data = {"x_train": 1, "y_train": 2}

print(training_data)

training_data_1 = dict(x=1, y=2, abc=10)  # another way

print(training_data["x_train"])

training_data["z_train"] = 4
print(training_data)

# print(training_data["10"]) -- key error

if "x_train" in training_data:
    print("key Found and value is: ", training_data['x_train'])

a = training_data.get("10")  # get() would return none if key does not exist
print(a)

b = training_data.get("20", "key not found")
print(b)

c = training_data.get("x_train", "key not present")
print(c)

del training_data["x_train"]
print(training_data)

for key in training_data:  # iterate throuh ky
    print(training_data[key])

for x in training_data.items():  # each iteration give you tuple (key, value)
    print(x)

for key, value in training_data.items():  # each iteration give you tuple (key, value)
    print(key, ":", value)
