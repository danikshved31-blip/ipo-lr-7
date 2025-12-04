 import json

FILE_NAME = "cities_data.json"

operations_count = 0

try:
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):

    data = [
        {
            "id": 1,
            "name": "Москва",
            "country": "Россия",
            "is_big": True,
            "people_count": 13000000
        },
        {
            "id": 2,
            "name": "Санкт-Петербург",
            "country": "Россия",
            "is_big": True,
            "people_count": 5600000
        },
        {
            "id": 3,
            "name": "Новосибирск",
            "country": "Россия",
            "is_big": True,
            "people_count": 1600000
        },
        {
            "id": 4,
            "name": "Берлин",
            "country": "Германия",
            "is_big": True,
            "people_count": 3800000
        },
        {
            "id": 5,
            "name": "Суздаль",
            "country": "Россия",
            "is_big": False,
            "people_count": 9500
        }
    ]

    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print("Создан файл с 5 начальными записями о городах.")
while True:
    print("\n")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю id")
    print("3. Добавить запись")
    print("4. Удалить запись по полю id")
    print("5. Выйти из программы")

    try:
        choise = int(input("выберите пункт "))
    except ValueError:
        print("Введите число от 1 до 5")
        continue
    
    if choise == 1:
        for i, city in enumerate(data, 1):
                print(f"\nЗапись #{i}:")
                print(f"  ID: {city['id']}")
                print(f"  Город: {city['name']}")
                print(f"  Страна: {city['country']}")
                print(f"  Крупный город (>100 тыс. чел.): {'Да' if city['is_big'] else 'Нет'}")
                print(f"  Население: {city['people_count']:,} чел.")
        
        operations_count += 1
    elif choise == 2:
        try:
            num = int(input("введите id города: "))
        except ValueError:
            print("введите число от 1 до 5")
            continue
        for i, city in enumerate(data):
            if city['id'] == num:
                print("\n")
                print(f"  ID: {city['id']}")
                print(f"  Город: {city['name']}")
                print(f"  Страна: {city['country']}")
                print(f"  Крупный город (>100 тыс. чел.): {'Да' if city['is_big'] else 'Нет'}")
                print(f"  Население: {city['people_count']:,} чел.")
                operations_count += 1
                break

    elif choise == 3:
            print("введите новые записи о городе")
            
            try:
                new_id = int(input("введите новое Id для города: "))
                 
                for city in data:
                    if city['id'] == new_id:
                        print("город с таким айди уже сущесвует: ")
                        break
                    else:
                        name = input("введите новое название города: ")
                        country = input("введите страну в которой находится город: ")

                        print("\nЯвляется ли город крупным (население > 100 000 чел.)?")
                        print("1. Да")
                        print("2. Нет")
                        is_big_choice = int(input("Введите номер: "))
                        if is_big_choice == 1:
                            is_big = True
                        elif is_big_choice == 2:
                            is_big = False
                        else:
                            print("чето вы не то ввели")
                        people_count = int(input("введите чему равно население города: "))
                        break
                
                new_city = {
                    "id": new_id,
                    "name": name,
                    "country": country,
                    "is_big": is_big,
                    "people_count": people_count
                }
                data.append(new_city)

                with open(FILE_NAME, 'w', encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=2)
                    print("город успешно записан в файл")
                    operations_count += 1

            except ValueError:
                print("id должно быть числом")

    elif choise == 4:
        try:
            delete_id = int(input("\nВведите ID города для удаления: "))
        except ValueError:
            print("Ошибка! ID должен быть числом.")
            continue
        
        found = False
        for i, city in enumerate(data):
            if city['id'] == delete_id:
                print(f"\nВы уверены, что хотите удалить город '{city['name']}' (ID: {city['id']})?")
                confirm = input("Введите 'да' для подтверждения или любую другую клавишу для отмены: ")
                
                if confirm.lower() == 'да' or 'Да' or 'ДА':
                    deleted_city = data.pop(i)
                    
                    with open(FILE_NAME, 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False, indent=2)
                    
                    print(f"\nГород '{deleted_city['name']}' успешно удален!")
                    operations_count += 1
                else:
                    print("Удаление отменено.")
                
                found = True
                break
        
        if not found:
            print(f"\nВнимание: Город с ID {delete_id} не найден!")

    elif choise == 5:
        print("\n")
        print("ВЫХОД ИЗ ПРОГРАММЫ")
        print(f"Количество выполненных операций с записями: {operations_count}")
        break
    
    else:
        print("Ошибка! Введите число от 1 до 5.")                                    
