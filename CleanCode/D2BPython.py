def D2B(num):

    if num > 1:
        D2B(num // 2)
    print (num % 2, end='')

    number = int(input("Enter any decimal number: "))

    D2B (number)