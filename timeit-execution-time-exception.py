from timeit import timeit

code_1 = """
def calculate_income(age):
    if age <= 0:
        raise ValueError("Age should be non zero")
    return 100000/age


try:
    calculate_income(0)
except ValueError as error:
    pass
"""


code_2 = """
def calculate_income(age):
    if age <= 0:
        return None
    return 100000/age

income_factor = calculate_income(0)

if income_factor == None:
    pass

"""
print(timeit(code_1, number=10000))
print(timeit(code_2, number=10000))
