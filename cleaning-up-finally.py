try:
    file = open("array-basics.py")
    number_of_people = int(input("Enter people: "))
    pocket_money = 8000 / number_of_people

    # file.close() -- file won't close if exception occurs before this call

except (ValueError, ZeroDivisionError):
    print("You did not enter a non zero")
    # file.close() -- file would close only if execption occurs
else:
    print("No exception")
    # file.close() -- Its duplicate code, not recommended

finally:
    file.close()
