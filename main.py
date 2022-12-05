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
