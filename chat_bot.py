# --- Мультиязычность ---
LANGUAGES = {
    "ru": {
        "welcome": "Привет! Я помогу вам оформить заказ. Давайте начнем с выбора блюда.",
        "main_menu": "Какое блюдо вы хотите?\n0. Завершить заказ\n1. Основное блюдо\n2. Салат\n3. Десерт\n4. Напиток\n9. Назад",
        "choose_dish": "Введите свой выбор:",
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
        "add_item": "Добавить блюдо",
        "change_question": "Хотите что-то изменить?\n0. Завершить заказ\n5. Изменить/удалить блюдо"
    },
    "en": {
        "welcome": "Hello! I will help you place an order. Let's start by choosing a dish.",
        "main_menu": "What dish do you want?\n0. Finish order\n1. Main course\n2. Salad\n3. Dessert\n4. Drink\n9. Back",
        "choose_dish": "Enter your choice:",
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
        "add_item": "Add item",
        "change_question": "Do you want to change anything?\n0. Finish order\n5. Change/remove dish"
    },
    "de": {
        "welcome": "Hallo! Ich helfe Ihnen bei der Bestellung. Lassen Sie uns mit der Auswahl eines Gerichts beginnen.",
        "main_menu": "Welches Gericht möchten Sie?\n0. Bestellung abschließen\n1. Hauptgericht\n2. Salat\n3. Dessert\n4. Getränk\n9. Zurück",
        "choose_dish": "Geben Sie Ihre Wahl ein:",
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
        "add_item": "Element hinzufügen",
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
    """
    Выводит меню выбора языка и возвращает выбранный язык.
    """
    print("Choose a language / Выберите язык / Wählen Sie eine Sprache:")
    # Выводим сообщение о выборе языка на трех языках.
    print("1. English\n2. Русский\n3. Deutsch")
    # Выводим пронумерованный список доступных языков.
    while True:
        # Запускаем бесконечный цикл, пока пользователь не сделает правильный выбор.
        choice = input("Enter your choice: ")
        # Получаем ввод от пользователя.
        if choice == "1":
            # Если пользователь ввел "1", возвращаем английский язык.
            return "en"
        elif choice == "2":
            # Если пользователь ввел "2", возвращаем русский язык.
            return "ru"
        elif choice == "3":
            # Если пользователь ввел "3", возвращаем немецкий язык.
            return "de"
        else:
            # Если пользователь ввел некорректное значение, выводим сообщение об ошибке (на английском).
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
        dict or None or "back": Словарь выбранного элемента, None если "Пропустить", или "back" если "Назад".
    """
    print(f"{lang['choose_dish']} {lang[category_name]}:")
    # Выводим заголовок меню, используя строки из языкового словаря

    while True:
        # Запускаем бесконечный цикл, пока пользователь не сделает правильный выбор.
        for i, item in enumerate(items, start=1):
            # Выводим пронумерованный список элементов меню с их названиями и ценами.
            print(f"{i}. {item['name'][selected_language]} ({item['price']:.2f}€)")

        if not show_back:  # Изменено
            print(f"0. {lang['exit']}")  # Изменено
        # Выводим опцию для пропуска выбора блюда
        if show_back:
            # Если show_back == True, выводим опцию "9. Назад".
            print(f"9. {lang['exit']}")

        choice = input(f"{lang['choose_dish']} ")
        # Получаем ввод от пользователя.

        if choice == "0" and not show_back:  # Изменено
            # Если пользователь ввел "0", возвращаем None (пропуск выбора).
            return None
        if show_back and choice == "9":
            # Если пользователь ввел "9" и опция show_back включена, возвращаем "back" (возврат назад).
            return "back"

        if choice.isdigit() and 1 <= int(choice) <= len(items):
            # Если ввод является цифрой и находится в пределах доступных вариантов,
            selected_item = items[int(choice) - 1]
            # Получаем словарь выбранного элемента.
            extras = choose_extras(selected_item.get("extras", []), lang, selected_language,
                                   selected_item.get("max_extras", 0))
            # Вызываем функцию выбора добавок и сохраняем выбранные добавки
            return {"name": selected_item["name"][selected_language], "price": selected_item["price"], "extras": extras}
            # Возвращаем словарь с информацией о выбранном элементе.
        else:
            # Если ввод не соответствует ни одному из условий, выводим сообщение об ошибке.
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
    # Инициализируем пустой список для хранения выбранных добавок.
    if not extras:
        # Если список добавок пуст, возвращаем пустой список.
        return selected_extras

    print(lang["choose_extras"])
    # Выводим приглашение для выбора добавок, используя строки из языкового словаря
    while True:
        # Запускаем бесконечный цикл, пока пользователь не сделает правильный выбор
        for i, extra in enumerate(extras, start=1):
            # Выводим пронумерованный список добавок с их названиями и ценами.
            print(f"{i}. {extra['name'][selected_language]} (+{extra['price']:.2f}€)")
        print(f"0. {lang['exit']}")
        # Выводим опцию для пропуска выбора добавок.

        choice = input(f"{lang['your_choice']}")
        # Получаем ввод от пользователя

        if choice == "0":
            # Если пользователь ввел "0", выходим из цикла выбора добавок.
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(extras):
            # Если ввод является цифрой и находится в пределах доступных вариантов,
            selected_extras.append(extras[int(choice) - 1])
            # Добавляем выбранную добавку в список.
            print(f"{lang['dish_added']} {extras[int(choice) - 1]['name'][selected_language]}")
            # Выводим сообщение о добавлении.
            if max_extras != 0 and len(selected_extras) == max_extras:
                # Если достигнут лимит максимального количества добавок, выходим из цикла.
                break
        else:
            # Если ввод не соответствует ни одному из условий, выводим сообщение об ошибке.
            print(lang["error"])
    return selected_extras
    # Возвращаем список выбранных добавок.


def confirm_order(order, lang, selected_language):
    """
    Выводит сводку заказа и общую стоимость.

    Args:
        order (list): Список словарей, представляющий заказ.
        lang (dict): Словарь с текстовыми строками для выбранного языка.
        selected_language (str): Выбранный язык.
    """
    print("\n" + lang["order_summary"])
    # Выводим заголовок заказа, используя строки из языкового словаря.
    total_price = 0
    # Инициализируем переменную для хранения общей стоимости заказа.
    for i, item in enumerate(order, start=1):
        # Перебираем все элементы в заказе и выводим их номер, название и цену.
        print(f"{i}. {item['name']} ({item['price']:.2f}€)")
        total_price += item["price"]
        # Добавляем цену текущего элемента к общей стоимости заказа.
        if "extras" in item and item["extras"]:
            # Если у элемента есть добавки, перебираем их и выводим информацию о них.
            for extra in item["extras"]:
                # Выводим информацию о добавке с ее названием и ценой.
                print(f"   └─ {extra['name'][selected_language]} (+{extra['price']:.2f}€)")
                total_price += extra["price"]
                # Добавляем цену текущей добавки к общей стоимости заказа.
    print(f"\n{lang['total_price']}: {total_price:.2f}€")
    # Выводим общую стоимость заказа.
    print(lang["thank_you"])
    # Выводим сообщение благодарности.


def change_order(order, lang, selected_language):
    """
      Позволяет пользователю изменить заказ - удалить блюдо.

      Args:
          order (list): Список словарей, представляющий заказ.
          lang (dict): Словарь с текстовыми строками для выбранного языка.
          selected_language (str): Выбранный язык.
    """
    while True:
        # Запускаем бесконечный цикл, пока пользователь не завершит изменение заказа.
        print("\n" + lang["change_order"])
        # Выводим заголовок, используя строки из языкового словаря.
        for i, item in enumerate(order, start=1):
            # Выводим пронумерованный список элементов текущего заказа.
            print(f"{i}. {item['name']}")
        print(f"0. {lang['exit']}")
        # Выводим опцию для пропуска изменения заказа.
        print(f"5. {lang['add_item']}")
        # Выводим опцию для добавления блюда.
        choice = input(f"{lang['remove_item']}")
        # Получаем ввод от пользователя.
        if choice == "0":
            # Если пользователь ввел "0", выходим из цикла.
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(order):
            # Если ввод является цифрой и находится в пределах доступных вариантов,
            del order[int(choice) - 1]
            # Удаляем выбранный элемент из заказа.
        elif choice == "5":
            # Если пользователь ввел "2" вызываем функцию `start_order` для добавления блюда
            start_order(selected_language, order)
        else:
            # Если ввод не соответствует ни одному из условий, выводим сообщение об ошибке.
            print(lang["error"])
    return order
    # Возвращаем измененный заказ.


def start_order(selected_language, order = None):
    """
    Управляет основным циклом заказа.

    Args:
        selected_language (str): Выбранный язык.
         order (list): Список словарей, представляющий заказ.
    """
    lang = LANGUAGES[selected_language]
    # Получаем языковой словарь для выбранного языка.
    print(lang["welcome"])
    # Выводим приветствие, используя строки из языкового словаря.
    if order is None:
        # Если заказ не передан, инициализируем пустой список для хранения заказа.
        order = []
    history = []
    # Инициализируем список для истории заказов
    while True:
        # Запускаем бесконечный цикл, пока пользователь не завершит заказ или не захочет вернуться к выбору языка.
        print(lang["main_menu"])
        # Выводим главное меню, используя строки из языкового словаря.
        choice = input("\n" + lang["choose_dish"] + " ")
        # Получаем ввод от пользователя.

        if choice == "0":
            # Если пользователь ввел "0", это означает, что он хочет завершить заказ
            if order:
                # Если заказ не пустой, вызываем функцию подтверждения заказа.
                 confirm_order(order, lang, selected_language)
                 # Выводим сводку заказа
                 print(lang["change_question"])
                 # Задаем вопрос, хочет ли пользователь что-то изменить
                 choice = input(f"{lang['your_choice']}")
                 # Получаем ответ от пользователя
                 if choice == "5":
                    # Если пользователь ответил "5" вызываем функцию изменения заказа
                    order = change_order(order, lang, selected_language)
                 else:
                    # Если пользователь ответил не "5"  завершаем заказ и выходим из цикла
                      break
            else:
                # Если заказ пустой, выходим из цикла.
                break
        elif choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES) :
            # Если ввод является цифрой и находится в пределах доступных категорий,
          history.append(order)
          # Добавляем текущий заказ в историю.
          category_index = int(choice) -1
          # Получаем индекс выбранной категории
          category_name = list(CATEGORIES.keys())[category_index]
          # Получаем название категории из словаря.
          category = CATEGORIES[category_name]
          # Получаем словарь категории.
          dish = choose_item(category["items"], category_name, lang, selected_language, True)
          # Вызываем функцию выбора элемента для текущей категории.
          if dish == "back":
             # Если пользователь выбрал "Назад",
            if history:
                # Если история не пуста, возвращаемся к предыдущему заказу
                order = history.pop()
            else:
               # Если история пуста,  очищаем заказ и выходим из цикла
               order = [] # Изменено
               break # Изменено
          elif dish:
            # Если пользователь выбрал элемент, добавляем его в заказ.
            order.append(dish)
        elif choice == "9":
           # Если пользователь ввел "9" очищаем заказ и выходим из цикла
            order = [] # Изменено
            break # Изменено
        else:
            # Если ввод не соответствует ни одному из условий, выводим сообщение об ошибке.
            print(lang["error"])

# --- Основной вход в программу ---
if __name__ == "__main__":
    # Проверяем, что скрипт запущен как основная программа.
    while True:
      # Запускаем бесконечный цикл выбора языка и заказа.
      selected_language = choose_language()
      # Вызываем функцию для выбора языка.
      if selected_language in LANGUAGES:
        # Если выбранный язык есть в словаре языков
        start_order(selected_language)
        # Запускаем основной цикл заказа, передавая выбранный язык.
      else:
        # Если выбранный язык не найден в словаре, выводим сообщение об ошибке (на английском).
        print(LANGUAGES["en"]["invalid_language"])