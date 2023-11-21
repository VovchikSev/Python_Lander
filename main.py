# решение задачек по ссылке https://smartiqa.ru/python-workbook
# а так же из прилагаемого в каталоге книги


def test_input()-> float:
        min_value = 1.5
        max_value = min_value * 10
        message = "Введите скорость сжигания топлива (или quit) "        
        inputStr = input(message)

        while True:
            if ((inputStr.lower() == "quit") or (inputStr.lower() == "q")):
                print("Прервано по команде пользователя")
                return            
            try:
                faccel = float(inputStr)

                if faccel >= 0.0 :
                    if faccel <=max_value:                    
                        if faccel >= min_value:                            
                            return faccel
                        else:
                            if faccel > 0.0: #nonzero but invalid thrust : print a message
                                print('это ниже минимального значения,  вернем 0')                            
                            return 0.0
                    else:                        
                        print (f"Нельзя подать топливо больше {max_value} его и подали")
                        return max_value
                else:
                    print ("Вводить только положительное число" )
            except:
                print ("введите число или quit!")

            inputStr = input(message)    

def my_enter():
    print(f'Функция вернула <{test_input()}>')


if __name__ == "__main__":
    my_enter()