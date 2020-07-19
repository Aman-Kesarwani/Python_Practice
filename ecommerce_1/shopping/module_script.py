def calc_tax():
    print("tax")


def calc_shopping():
    print("shopping")


# Below code would be called if we run script here
# Below code wont call if we import this file
if __name__ == "__main__":
    print("Sales Just started")
    calc_tax()
