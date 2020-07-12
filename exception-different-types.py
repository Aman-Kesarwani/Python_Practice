try:
    age = int(input("AGE: "))
    ageFactor = 15 / age  # division by zero

except ValueError:
    print("Please enter the valid age")

except ZeroDivisionError:
    print("Please enter the valid age")

else:
    print("Every thing working fine")

################--Handling Exception --##################################
try:
    age_1 = int(input("AGE: "))
    ageFactor_1 = 15 / age_1  # division by zero

except (ValueError, ZeroDivisionError):
    print("Please enter the valid age")

except ZeroDivisionError:  # this will not execute
    print("Zero not acceptable")

else:
    print("Every thing working fine")
