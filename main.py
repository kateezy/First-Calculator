# value_1 = int(input("Введите первое число: "))
# value_2 = int(input("Введите второе число: "))
# operation = input("Выберите метод вычисления: + - / * % ** //: ")
# if operation == "+":
#     print(value_1 + value_2)
# if operation == "-":
#     print(value_1 - value_2)
# if operation == "/":
#     if value_2 == 0:
#         print("Нельзя")
#         quit()
#     print(value_1 / value_2)
# elif operation == "*":
#     print(value_1 * value_2)
# elif operation == "%":
#     print(value_1 % value_2)
# elif operation == "**":
#     print(value_1 ** value_2)
# elif operation == "//":
#     print(value_1 // value_2)
# else:
#     print("Нет решения")
# from nis import match

# proceed = 'z'
# while proceed == 'z':
#     value_1 = float(input("Введите первое число: "))
#     operation = input("Введите опрерацию: ")
#     value_2 = float(input("Введите второе число: "))
#     if operation == "+":
#         print(value_1 + value_2)
#     elif operation == "-":
#         print(value_1 - value_2)
#     elif operation == "*":
#         print(value_1 - value_2)
#     elif operation == "/":
#         print(value_1 - value_2)
#     elif operation == "%":
#         print(value_1 % value_2)
#     elif operation == "**":
#         print(value_1 ** value_2)
#     elif operation == "//":
#         print(value_1 // value_2)
#     else:
#         print("Ошибка")
#     proceed = input("Введите 'z' чтобы продолжить, или 'x', чтобы завершить: ")

value_1 = None
bool_value = True
while bool_value:
    if value_1 is None: value_1 = float(input("Введите первое число: "))
    operation = input("Введите опрерацию: ")
    value_2 = float(input("Введите второе число: "))
    match operation:
        case "+":
                print(value_1 + value_2)
                value_1 += value_2
        case "-":
            print(value_1 - value_2)
            value_1 -= value_2
        case "*":
            print(f"{value_1 * value_2}")
            value_1 *= value_2
        case "/":
          try:
              print(value_1 / value_2)
              value_1 /= value_2
          except:
              print("Ошибка")
        case "%":
            print(value_1 % value_2)
            value_1 %= value_2
        case "**":
            print(value_1 ** value_2)
            value_1 **= value_2
        case "//":
            print(value_1 // value_2)
            value_1 //= value_2
        case "!":
            bool_value = False
        case _:
             print("неизвестный опер")

























# import array
# nums = array.array('d', [1, 90.1, 101.2, 78])
# print(nums)
# for i in nums:
#     print(i)
# for i in range(len(nums)):
#     print(nums[i])

# spisok = ["a", "b", "c"]
# print(",".join(spisok))
# text = "   love you Ilya   "
# print(text.lstrip())
# text = "lololololololololololololo"
# print(text.replace("l", "k"))
# list_one = [list_one * 3 for list_one in "list.one"]
# # list generator
# variable = [variable for variable in range (101)]
# for i in variable:
#     print(f"{i}")
# list_one = [2, 5, 8, 9, 10, 152, 89]
# list_one2 = [2, 4, 5, 9, 99]
# list_one2[0] =12
# print(list_one2)
# list_one2.insert(1, 58)
# print(list_one2)
# list_one.append(2)
# print(list_one)
# list_one2.extend(list_one)
# print(list_one2)























