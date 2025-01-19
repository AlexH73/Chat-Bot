# --- Мультиязычность ---
LANGUAGES = {
    "ru": {
        "welcome": "Привет! Я помогу вам оформить заказ. Давайте начнем с выбора блюда.",
        "main_menu": "Какое блюдо вы хотите?\n0. Завершить заказ\n1. Основное блюдо\n2. Салат\n3. Десерт\n4. Напиток\n9. Назад",
        "choose_dish": "Выберите блюдо:",
        "choose_extras": "Выберите добавки (введите номер или 0 для пропуска):",
        "dish_added": "Добавлено:",
        "order_summary": "Ваш заказ:",
        "total_price": "Общая стоимость",
        "thank_you": "Спасибо за заказ!",
        "exit": "Вернуться назад",
        "error": "Некорректный выбор. Попробуйте снова.",
        "main_course": "основное блюдо",
        "salad": "салат",
        "dessert": "десерт",
        "drink": "напиток",
        "your_choice": "Ваш выбор: ",
        "invalid_language": "Неверный язык. Попробуйте снова.",
        "change_order": "Изменить заказ",
        "remove_item": "Удалить блюдо:",
        "add_item": "Добавить блюдо:",
        "change_question": "Хотите что-то изменить?\n0. Завершить заказ\n5. Изменить/удалить блюдо"
    },
    "en": {
        "welcome": "Hello! I will help you place an order. Let's start by choosing a dish.",
        "main_menu": "What dish do you want?\n0. Finish order\n1. Main course\n2. Salad\n3. Dessert\n4. Drink\n9. Back",
        "choose_dish": "Choose a dish:",
        "choose_extras": "Choose extras (enter the number or 0 to skip):",
        "dish_added": "Added:",
        "order_summary": "Your order:",
        "total_price": "Total price",
        "thank_you": "Thank you for your order!",
        "exit": "Go back",
        "error": "Invalid choice. Please try again.",
        "main_course": "main course",
        "salad": "salad",
        "dessert": "dessert",
        "drink": "drink",
        "your_choice": "Your choice: ",
        "invalid_language": "Invalid language. Please try again.",
        "change_order": "Change order",
        "remove_item": "Remove item:",
        "add_item": "Add item:",
        "change_question": "Do you want to change anything?\n0. Finish order\n5. Change/remove dish"
    },
    "de": {
        "welcome": "Hallo! Ich helfe Ihnen bei der Bestellung. Lassen Sie uns mit der Auswahl eines Gerichts beginnen.",
        "main_menu": "Welches Gericht möchten Sie?\n0. Bestellung abschließen\n1. Hauptgericht\n2. Salat\n3. Dessert\n4. Getränk\n9. Zurück",
        "choose_dish": "Wählen Sie ein Gericht:",
        "choose_extras": "Wählen Sie Extras (Nummer eingeben oder 0 zum Überspringen):",
        "dish_added": "Hinzugefügt:",
        "order_summary": "Ihre Bestellung:",
        "total_price": "Gesamtpreis",
        "thank_you": "Vielen Dank für Ihre Bestellung!",
        "exit": "Zurück",
        "error": "Ungültige Wahl. Bitte versuchen Sie es erneut.",
        "main_course": "Hauptgericht",
        "salad": "Salat",
        "dessert": "Dessert",
        "drink": "Getränk",
        "your_choice": "Ihre Wahl: ",
        "invalid_language": "Ungültige Sprache. Bitte versuchen Sie es erneut.",
        "change_order": "Bestellung ändern",
        "remove_item": "Element entfernen:",
        "add_item": "Element hinzufügen:",
        "change_question": "Möchten Sie etwas ändern?\n0. Bestellung abschließen\n5. Gericht ändern/entfernen"
    },
}

# --- Данные о блюдах ---
CATEGORIES = {
    "main_course": {
        "name": {
            "ru": "Основное блюдо",
            "en": "Main course",
            "de": "Hauptgericht"
        },
        "items": [
            {"name": {"ru": "Пицца", "en": "Pizza", "de": "Pizza"}, "price": 10.00, "extras": [
                {"name": {"ru": "Сыр", "en": "Cheese", "de": "Käse"}, "price": 1.50},
                {"name": {"ru": "Бекон", "en": "Bacon", "de": "Speck"}, "price": 2.00},
                {"name": {"ru": "Острый соус", "en": "Spicy sauce", "de": "Scharfe Soße"}, "price": 1.00},
            ],
             "max_extras": 2
             },
            {"name": {"ru": "Паста", "en": "Pasta", "de": "Pasta"}, "price": 8.00, "extras": [
                {"name": {"ru": "Сыр", "en": "Cheese", "de": "Käse"}, "price": 1.00},
                {"name": {"ru": "Грибы", "en": "Mushrooms", "de": "Pilze"}, "price": 1.50},
                {"name": {"ru": "Бекон", "en": "Bacon", "de": "Speck"}, "price": 1.50},
            ],
             "max_extras": 2
             },
            {"name": {"ru": "Стейк", "en": "Steak", "de": "Steak"}, "price": 15.00, "extras": [
                {"name": {"ru": "Соус", "en": "Sauce", "de": "Soße"}, "price": 2.00},
                {"name": {"ru": "Картофель", "en": "Potatoes", "de": "Kartoffeln"}, "price": 1.50},
            ],
             "max_extras": 1
             },
        ]
    },
    "salad": {
        "name": {
            "ru": "Салат",
            "en": "Salad",
            "de": "Salat"
        },
        "items": [
            {"name": {"ru": "Цезарь", "en": "Caesar", "de": "Caesar"}, "price": 5.00, "extras": [
                {"name": {"ru": "Гренки", "en": "Croutons", "de": "Croutons"}, "price": 0.50},
                {"name": {"ru": "Курица", "en": "Chicken", "de": "Hähnchen"}, "price": 1.00},
            ],
             "max_extras": 2},
            {"name": {"ru": "Греческий", "en": "Greek", "de": "Griechisch"}, "price": 4.50, "extras": [
                {"name": {"ru": "Маслины", "en": "Olives", "de": "Oliven"}, "price": 0.50},
                {"name": {"ru": "Сыр фета", "en": "Feta cheese", "de": "Feta-Käse"}, "price": 1.00},
            ],
             "max_extras": 2},
            {"name": {"ru": "Оливье", "en": "Olivier", "de": "Olivier"}, "price": 6.00, "extras": [
                {"name": {"ru": "Зеленый горошек", "en": "Green peas", "de": "Grüne Erbsen"}, "price": 0.50},
                {"name": {"ru": "Морковь", "en": "Carrot", "de": "Karotte"}, "price": 0.50},
            ],
             "max_extras": 2},
        ]
    },
    "dessert": {
        "name": {
            "ru": "Десерт",
            "en": "Dessert",
            "de": "Dessert"
        },
        "items": [
            {"name": {"ru": "Чизкейк", "en": "Cheesecake", "de": "Käsekuchen"}, "price": 4.00, "extras": [
                {"name": {"ru": "Шоколадный сироп", "en": "Chocolate syrup", "de": "Schokoladensirup"}, "price": 0.50},
            ],
             "max_extras": 1},
            {"name": {"ru": "Тирамису", "en": "Tiramisu", "de": "Tiramisu"}, "price": 4.50, "extras": [
                {"name": {"ru": "Какао", "en": "Cocoa", "de": "Kakao"}, "price": 0.50},
            ],
             "max_extras": 1},
            {"name": {"ru": "Мороженое", "en": "Ice cream", "de": "Eis"}, "price": 3.00, "extras": [
                {"name": {"ru": "Фрукты", "en": "Fruits", "de": "Früchte"}, "price": 1.00},
            ],
             "max_extras": 1},
        ]
    },
    "drink": {
        "name": {
            "ru": "Напиток",
            "en": "Drink",
            "de": "Getränk"
        },
        "items": [
            {"name": {"ru": "Кофе", "en": "Coffee", "de": "Kaffee"}, "price": 2.50, "extras": [
                {"name": {"ru": "Молоко", "en": "Milk", "de": "Milch"}, "price": 0.50},
                {"name": {"ru": "Сахар", "en": "Sugar", "de": "Zucker"}, "price": 0.50},
            ],
             "max_extras": 2},
            {"name": {"ru": "Чай", "en": "Tea", "de": "Tee"}, "price": 2.00, "extras": [
                {"name": {"ru": "Лимон", "en": "Lemon", "de": "Zitrone"}, "price": 0.50},
                {"name": {"ru": "Мед", "en": "Honey", "de": "Honig"}, "price": 0.50},
            ],
             "max_extras": 2},
            {"name": {"ru": "Сок", "en": "Juice", "de": "Saft"}, "price": 3.00, "extras": [
                {"name": {"ru": "Лед", "en": "Ice", "de": "Eis"}, "price": 0.50},
            ],
             "max_extras": 1},
        ]
    },
}


def choose_language():
    print("Choose a language / Выберите язык / Wählen Sie eine Sprache:")
    print("1. English\n2. Русский\n3. Deutsch")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            return "en"
        elif choice == "2":
            return "ru"
        elif choice == "3":
            return "de"
        else:
            print(LANGUAGES["en"]["invalid_language"])


def choose_item(items, category_name, lang, selected_language, show_back=True):
    """
    Выводит меню элементов и обрабатывает выбор пользователя.

    Args:
        items (list): Список словарей, содержащий элементы меню.
        category_name (str): Название категории (используется для отображения заголовка).
        lang (dict): Словарь с текстовыми строками для выбранного языка.
        selected_language (str): Выбранный язык.
        show_back (bool): Показывать ли опцию "9. Назад".

    Returns:
        dict or None: Словарь выбранного элемента или None, если выбран пункт "пропустить".
    """
    # Выводим заголовок меню, используя строки из языкового словаря
    print(f"{lang['choose_dish']} {lang[category_name]}:")

    while True:  # Бесконечный цикл, пока пользователь не сделает корректный выбор или не выйдет
        # Выводим список элементов
        for i, item in enumerate(items, start=1):
            # Выводим номер элемента, его название (на выбранном языке) и цену
            print(f"{i}. {item['name'][selected_language]} ({item['price']:.2f}€)")

        # Выводим опцию для пропуска
        print(f"0. {lang['exit']}")
        if show_back:
            print(f"9. {lang['exit']}")

        # Получаем ввод от пользователя
        choice = input(f"{lang['choose_dish']} ")

        # Проверяем ввод пользователя
        if choice == "0":
            # Если пользователь ввел 0, возвращаем None, что означает, что он не выбрал элемент
            return None
        if show_back and choice == "9":
            return "back"

        if choice.isdigit() and 1 <= int(choice) <= len(items):
            # Если ввод - цифра и находится в диапазоне доступных элементов
            selected_item = items[int(choice) - 1]  # Получаем выбранный элемент из списка
            # Вызываем функцию choose_extras для выбора добавок к элементу
            # (передаем список добавок элемента, языковой словарь и выбранный язык)
            extras = choose_extras(selected_item.get("extras", []), lang, selected_language,
                                   selected_item.get("max_extras", 0))
            # Возвращаем словарь с информацией о выбранном элементе (название, цена, выбранные добавки)
            return {"name": selected_item["name"][selected_language], "price": selected_item["price"], "extras": extras}
        else:
            # Если ввод некорректен, выводим сообщение об ошибке
            print(lang["error"])


def choose_extras(extras, lang, selected_language, max_extras=0):
    """
    Выводит меню добавок и обрабатывает выбор пользователя.

    Args:
        extras (list): Список словарей, содержащий добавки.
        lang (dict): Словарь с текстовыми строками для выбранного языка.
        selected_language (str): Выбранный язык.
         max_extras (int): Максимальное количество добавок.

    Returns:
       list: Список словарей выбранных добавок.
    """
    selected_extras = []
    if not extras:
        return selected_extras

    print(lang["choose_extras"])
    while True:
        for i, extra in enumerate(extras, start=1):
            print(f"{i}. {extra['name'][selected_language]} (+{extra['price']:.2f}€)")
        print(f"0. {lang['exit']}")

        choice = input(f"{lang['your_choice']}")

        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(extras):
            selected_extras.append(extras[int(choice) - 1])
            print(f"{lang['dish_added']} {extras[int(choice) - 1]['name'][selected_language]}")
            if max_extras != 0 and len(selected_extras) == max_extras:
                break
        else:
            print(lang["error"])
    return selected_extras


def confirm_order(order, lang, selected_language):
    """
    Выводит сводку заказа и общую стоимость.

    Args:
        order (list): Список словарей, представляющий заказ.
        lang (dict): Словарь с текстовыми строками для выбранного языка.
        selected_language (str): Выбранный язык.
    """
    print("\n" + lang["order_summary"])
    total_price = 0
    for i, item in enumerate(order, start=1):
        print(f"{i}. {item['name']} ({item['price']:.2f}€)")
        total_price += item["price"]
        if "extras" in item and item["extras"]:
            for extra in item["extras"]:
                print(f"   └─ {extra['name'][selected_language]} (+{extra['price']:.2f}€)")
                total_price += extra["price"]
    print(f"\n{lang['total_price']}: {total_price:.2f}€")
    print(lang["thank_you"])


def change_order(order, lang, selected_language):
    while True:
        print("\n" + lang["change_order"])
        for i, item in enumerate(order, start=1):
            print(f"{i}. {item['name']}")
        print(f"0. {lang['exit']}")
        print(f"a. {lang['add_item']}")
        choice = input(f"{lang['remove_item']}")
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(order):
            del order[int(choice) - 1]
        elif choice == "a":
            start_order(selected_language, order)
        else:
            print(lang["error"])
    return order


def start_order(selected_language, order=None):
    """
    Управляет основным циклом заказа.

    Args:
        selected_language (str): Выбранный язык.
         order (list): Список словарей, представляющий заказ.
    """
    lang = LANGUAGES[selected_language]
    print(lang["welcome"])
    if order is None:
        order = []
    history = []
    while True:
        print(lang["main_menu"])
        choice = input("\n" + lang["choose_dish"] + " ")

        if choice == "0":
            if order:
                confirm_order(order, lang, selected_language)
                print(lang["change_question"])
                choice = input(f"{lang['your_choice']}")
                if choice == "5":
                    order = change_order(order, lang, selected_language)
                else:
                    break
            else:
                break
        elif choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            history.append(order)
            category_index = int(choice) - 1
            category_name = list(CATEGORIES.keys())[category_index]
            category = CATEGORIES[category_name]
            dish = choose_item(category["items"], category_name, lang, selected_language, True)
            if dish == "back":
                if history:
                    order = history.pop()
                else:
                    continue
            elif dish:
                order.append(dish)
        elif choice == "9":
            if history:
                order = history.pop()
            else:
                continue
        else:
            print(lang["error"])


# --- Основной вход в программу ---
if __name__ == "__main__":
    while True:
        selected_language = choose_language()
        if selected_language in LANGUAGES:
            start_order(selected_language)
            break
        else:
            print(LANGUAGES["en"]["invalid_language"])

