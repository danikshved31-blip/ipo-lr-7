import json

# Имя файла для хранения данных
FILE_NAME = "cities_data.json"

# Переменная для подсчета операций
operations_count = 0

# Инициализация файла, если он не существует или пустой
try:
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    # 5 записей о городах
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
                break

