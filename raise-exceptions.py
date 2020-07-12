def calculate_pocketMoney(totalMoney, number):
    if number <= 0:
        raise ValueError("number should be greater than zero")
    pocket_money = totalMoney / number


try:
    calculate_pocketMoney(24, -2)
except ValueError as error:
    print(error)
else:
    print("All is well")
