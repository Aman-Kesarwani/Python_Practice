def fizz_buzz(input):

    if input % 5 == 0 and input % 3 == 0:
        return "fizzbuzz"

    elif input % 3 == 0:
        return "fizz"

    elif input % 5 == 0:
        return "buzz"

    else:
        return input


number = 0
while number != 1:
    number = int(input('Enter the number\n'))
    print(fizz_buzz(number))
