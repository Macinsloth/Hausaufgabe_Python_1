number_1 = int(input("Your first number: "))
sign = input("Put in one of the following signs: +(plus) - (minus) * (multiply) / (divide): ")
number_2 = int(input("Your second number: "))


if sign == "+":
    print(number_1 + number_2)
if sign == "-":
    print(number_1 - number_2)
if sign == "*":
    print(number_1 * number_2)
if sign == "/":
    print(number_1 / number_2)
