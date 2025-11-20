import json
with open("dump.json", "r", encoding="utf - 8") as izi_pizy_lemon_squizue:
    a = json.load(izi_pizy_lemon_squizue)
    qualiti = input("введите номер квалификации: ").strip()
    for word in a:
        if word.get("model") == "data.skill":
            if word.get("fields", {}).get("code") == qualiti:
                print(f"======================== Найдено ==========================")
                print(f"{word["fields"]["title"]}")
                break
            else:
                print("===========================Не найдено ============================")
                break
