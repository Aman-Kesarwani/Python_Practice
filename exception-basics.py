try:
    age = int(input("Age: "))  # if non-intger entered exception thrown

except ValueError as ex:
    print("You did not enter a valid age")
    print("EX: ", ex)
    print("type: ", type(ex))

else:
    print("Everything is working fine")

print("Execution Continues without any issues")
