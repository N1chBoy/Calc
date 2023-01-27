deistvie = int(input("Введите количество действий: "))
if (deistvie >= 1):
    numberOne = int(input("Введите первое число: "))
    i = 0
    for i in range(deistvie):
        numberTwo = int(input("Введите второе число: "))
        znak = int(input("1 - сложение \n2 - вычитание \n3 - умножение \n4 - деление \n5 - возведение в степень\nВыберите знак: "))
        if (znak == 1, 2, 3, 4, 5):
            if (znak == 1):
                numberOne += numberTwo
                print(numberOne)
            elif (znak == 2):
                numberOne -= numberTwo
                print(numberOne)
            elif (znak == 3):
                numberOne *= numberTwo
                print(numberOne)
            elif (znak == 4):
                if (numberTwo == 0):
                    print("Делить на 0 нельзя")
                else:
                    numberOne /= numberTwo
                    print(numberOne)
            elif (znak == 5):
                numberOne = numberOne ** numberTwo
                print(numberOne)
        else:
            print("Операция введена неправильно")
else:
    print ("Введите корректное число действий")