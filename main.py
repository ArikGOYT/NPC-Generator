from logic import show_npc, load_data

print("Это генератор НПС. Развлекайтесь!")
data = load_data()
while True:
    try:
        userInput=int(input(f"1. Создать пачку НПС\n2. Выход  \n"))
        if userInput == 1:
            show_npc(data)
        elif userInput == 2:
            break
        else:
            print(f"Введите цифру из предложенного списка...\n")
    except (IndexError, ValueError, TypeError) as e:
        print(f"Что-то пошло не так...{e}\n")

