# Выбор основного блюда
def main_course(dish):
    main_course_cash = 0  # Стоимость основного блюда
    main_course_name = "Нет основного блюда"  # Название основного блюда
    extra_name = ""  # Название добавки
    extra_price = 0  # Стоимость добавки

    if dish == "Пицца" or dish == "Пица" or dish == "1":
        main_course_name = "Пицца"
        main_course_cash = 5.00
        main_extra_change = input(
            "Можете выбрать добавку:\n"
            "1. Сыр (+1.50€)\n"
            "2. Бекон (+2.00€)\n"
            "3. Острый соус (+1.00€)\n"
            "4. Отказаться \n"
        )
        extra_pizza, extra_pizza_price  = extra_dish_pizza(main_extra_change)
        extra_name, extra_price = extra_pizza, extra_pizza_price
        print(f"Вы выбрали Пиццу. Цена: {main_course_cash:.2f}€ \n{extra_pizza}. Цена: {extra_pizza_price:.2f}€")
        print(f"Всего: {main_course_cash + extra_pizza_price:.2f}€")
    elif dish == "Паста" or dish == "2":
        main_course_name = "Паста"
        main_course_cash = 6.00
        main_extra_change = input(
            "Хотите добавить экстра:\n"
            "1. Пармезан (+1.20€)\n"
            "2. Грибы (+1.50€)\n"
            "3. Трюфельное масло (+3.00€)\n"
            "4. Отказаться \n"
        )
        extra_pasta_price, extra_pasta = extra_dish_pasta(main_extra_change)
        extra_price, extra_name = extra_pasta_price, extra_pasta
        print(f"Вы выбрали Пасту. Цена: {main_course_cash:.2f}€ \n{extra_pasta}. Цена: {extra_pasta_price:.2f}€")
        print(f"Всего: {main_course_cash + extra_pasta_price:.2f}€")
    elif dish == "Стейк" or dish == "3":
        main_course_name = "Стейк"
        main_course_cash = 7.00
        main_extra_change = input(
            "Хотите добавить экстра:\n"
            "1. Соус барбекю (+1.50€)\n"
            "2. Гарнир (+2.50€)\n"
            "3. Перечный соус (+2.00€)\n"
            "4. Отказаться \n"
        )
        extra_steak, extra_steak_price = extra_dish_steak(main_extra_change)
        extra_price, extra_name = extra_steak_price, extra_steak
        print(f"Вы выбрали Стейк. Цена: {main_course_cash:.2f}€ \n{extra_steak}. Цена: {extra_steak_price:.2f}€")
        print(f"Всего: {main_course_cash + extra_steak_price:.2f}€")
    elif dish == "4":
        print("Вы отказались от основного блюда.")
        return 0, "Нет основного блюда", "Нет добавок", 0
    else:
        print("Некорректный выбор. Попробуйте снова.")
        return start_order()
    return main_course_cash, main_course_name, extra_name, extra_price
# Дополнительные опции для пиццы
def extra_dish_pizza(extra):
    if extra == "1" or extra.lower() == "сыр":  # Сыр
        extra_pizza_price = 1.50
        extra_pizza_name = "С добавкой Сыр"
    elif extra == "2" or extra.lower() == "бекон":  # Бекон
        extra_pizza_price = 2.00
        extra_pizza_name = "С добавкой Бекон"
    elif extra == "3" or extra.lower() == "острый соус" or extra.lower() == "соус":  # Острый соус
        extra_pizza_price = 1.00
        extra_pizza_name = "С добавкой Острый соус"
    elif extra == "4" or extra.lower() == "отказаться":  # Отказ
        extra_pizza_price = 0
        extra_pizza_name = "Вы отказались от добавок"
    else:
        extra_pizza_price = 0
        extra_pizza_name = "Некорректный выбор"
    return extra_pizza_name, extra_pizza_price
# Дополнительные опции для пасты
def extra_dish_pasta(extra):
    if extra == "1" or extra.lower() == "пармезан":  # Пармезан
        extra_pasta_price = 1.20
        extra_pasta = "С добавкой Пармезан"
    elif extra == "2" or extra.lower() == "грибы":  # Грибы
        extra_pasta_price = 1.50
        extra_pasta = "С добавкой Грибы"
    elif extra == "3" or extra.lower() == "трюфельное масло" or extra.lower() == "масло":  # Трюфельное масло
        extra_pasta_price = 3.00
        extra_pasta = "С добавкой Трюфельное масло"
    elif extra == "4" or extra.lower() == "отказаться":  # Отказ
        extra_pasta_price = 0
        extra_pasta = "Вы отказались от добавок."
    else:
        extra_pasta_price = 0
        extra_pasta = "Некорректный выбор."
    return extra_pasta_price, extra_pasta
# Дополнительные опции для стейка
def extra_dish_steak(extra):
    if extra == "1" or extra.lower() == "соус барбекю": # Соус барбекю
        extra_steak_price = 1.50
        extra_steak = "С добавкой Соус барбекю"
    elif extra == "2" or extra.lower() == "гарнир":  # Гарнир
        extra_steak_price = 2.50
        extra_steak = "С добавкой Гарнир"
    elif extra == "3" or extra.lower() == "перечный соус":  # Перечный соус
        extra_steak_price = 2.00
        extra_steak = "С добавкой Перечный соус"
    elif extra == "4" or extra.lower() == "отказаться":  # Отказ
        extra_steak_price = 0
        extra_steak = "Вы отказались от добавок."
    else:
        extra_steak_price = 0
        extra_steak = "Некорректный выбор."
    return extra_steak, extra_steak_price
# Выбор салата
def salad_selection(salad):
    salad_cash = 0
    salad_extra_price = 0
    salad_name = "Без салата"
    salad_extra_name = ""

    if salad == "Цезарь" or salad == "1":
        salad_cash = 8
        salad_name = "Цезарь"
        salad_extra_change = input(
            "Хотите добавить экстра:\n"
            "1. Курица (+2.00€)\n"
            "2. Креветки (+4.00€)\n"
            "3. Дополнительный сыр (+1.00€)? \n"
            "4. Отказаться \n"
        )
        salad_extra_cesar, salad_extra_cesar_price = extra_dish_cesar(salad_extra_change)
        salad_extra_name, salad_extra_price = salad_extra_cesar, salad_extra_cesar_price
        print(f"Вы выбрали Цезарь. Цена: {salad_cash:.2f}€ \n{salad_extra_name}. Цена: {salad_extra_price:.2f}€")
        print(f"Всего: {salad_cash + salad_extra_price:.2f}€")
    elif salad == "Греческий" or salad == "2":
        salad_cash = 9
        salad_name = "Греческий"
        salad_extra_change = input(
            "Хотите добавить экстра:\n"
            "1. Маслины (+0.50€)\n"
            "2. Дополнительный сыр Фета (+1.50€)\n"
            "3. Хрустящие гренки (+1.00€)? \n"
            "4. Отказаться \n"
        )
        salad_extra_greek, salad_extra_greek_price = extra_dish_greek(salad_extra_change)
        salad_extra_name, salad_extra_price = salad_extra_greek, salad_extra_greek_price
        print(f"Вы выбрали Греческий. Цена: {salad_cash:.2f}€ \n{salad_extra_name}. Цена: {salad_extra_price:.2f}€")
        print(f"Всего: {salad_cash + salad_extra_price:.2f}€")
    elif salad == "Тунец" or salad == "3":
        salad_cash = 10
        salad_name = "Тунец"
        salad_extra_change = input(
            "Хотите добавить экстра:\n"
            "1. Креветки (+4.00€)\n"
            "2. Авокадо (+2.50€)\n"
            "3. Яйцо (+0.50€)? \n"
            "4. Отказаться \n"
        )
        salad_extra_tuna, salad_extra_tuna_price = extra_dish_tuna(salad_extra_change)
        salad_extra_name, salad_extra_price = salad_extra_tuna, salad_extra_tuna_price
        print(f"Вы выбрали Греческий. Цена: {salad_cash:.2f}€ \n{salad_extra_name}. Цена: {salad_extra_price:.2f}€")
        print(f"Всего: {salad_cash + salad_extra_price:.2f}€")
        print(f"Вы выбрали Салат с тунцом. Цена: {salad_cash}€")
    elif  salad == "4":
        print("Вы отказались от салата.")
        salad_cash = 0
        salad_name = ""
        return "Нет салата", 0, "Нет добавок", 0
    else:
        print("Некорректный выбор. Попробуйте снова.")
        salad_cash = 0
        salad_name = ""
    return salad_name, salad_cash, salad_extra_name, salad_extra_price
# Дополнительные блюда для салата Цезарь
def extra_dish_cesar(extra):
    if extra == "1":
        salad_extra_cesar = "С Курицей"
        salad_extra_cesar_price = 2.00
    elif extra == "2":
        salad_extra_cesar = "С Креветками"
        salad_extra_cesar_price = 4.00
    elif extra == "3":
        salad_extra_cesar = "С Дополнительным сыром"
        salad_extra_cesar_price = 1.00
    elif extra == "4":
        salad_extra_cesar = "Вы отказались от добавки."
        salad_extra_cesar_price = 0
    else:
        salad_extra_cesar = "Некорректный выбор."
        salad_extra_cesar_price = 0
    return salad_extra_cesar, salad_extra_cesar_price
# Дополнительные блюда для Греческого салата
def extra_dish_greek(extra):
    if extra == "1":
        salad_extra_greek = "С Маслинами"
        salad_extra_greek_price = 0.50
    elif extra == "2":
        salad_extra_greek = "С Дополнительным сыром Фета"
        salad_extra_greek_price = 1.50
    elif extra == "3":
        salad_extra_greek = "С Хрустящими гренками"
        salad_extra_greek_price = 1.00
    elif extra == "4":
        salad_extra_greek = ""
        salad_extra_greek_price = 0
        print("Вы отказались от добавки.")
    else:
        salad_extra_greek = ""
        salad_extra_greek_price = 0
        print("Некорректный выбор. Попробуйте снова.")
    return salad_extra_greek, salad_extra_greek_price
# Дополнительные блюда для салата с тунцом
def extra_dish_tuna(extra):
    if extra == "1":
        salad_extra_tuna = "С Креветками"
        salad_extra_tuna_price = 4.00
    elif extra == "2":
        salad_extra_tuna = "С Авокадо"
        salad_extra_tuna_price = 2.50
    elif extra == "3":
        salad_extra_tuna = "С Яйцом"
        salad_extra_tuna_price = 0.50
    elif extra == "4":
        salad_extra_tuna = ""
        salad_extra_tuna_price = 0
        print("Вы отказались от добавки.")
    else:
        salad_extra_tuna = ""
        salad_extra_tuna_price = 0
        print("Некорректный выбор. Попробуйте снова.")
    return salad_extra_tuna, salad_extra_tuna_price
# Выбор десерта
def dessert_selection(dessert):
    dessert_name = ""
    dessert_price = 0
    dessert_extra_name = ""
    dessert_extra_price = 0

    if dessert == "Чизкейк" or dessert == "1":
        dessert_name = "Чизкейк"
        dessert_price = 4
        dessert_extra_change = input(
            "Хотите добавить экстра:\n"
            "Топпинг:\n"
                "\t1. шоколадный (+1.00€)\n"
                "\t2. карамельный (+1.00€)\n"
            "3. Орехи (+1.00€)\n"
            "4. Взбитые сливки (+1.50€)? \n"
        )
        dessert_extra_name, dessert_extra_price = extra_dish_dessert(dessert_extra_change)
        print(f"Вы выбрали {dessert_name}. Цена: {dessert_price:.2f}€ \n{dessert_extra_name}. Цена: {dessert_extra_price:.2f}€")
        print(f"Всего: {dessert_price + dessert_extra_price:.2f}€")

    elif dessert == "Маффин" or dessert == "2":
        dessert_name = "Маффин"
        dessert_price = 3
        dessert_extra_change = input(
            "Хотите добавить экстра:\n"
            "Топпинг:\n"
                "\t1. шоколадный (+1.00€)\n"
                "\t2. карамельный (+1.00€)\n"
            "3. Орехи (+1.00€)\n"
            "4. Взбитые сливки (+1.50€)? \n"
        )
        dessert_extra_name, dessert_extra_price = extra_dish_dessert(dessert_extra_change)
        print(f"Вы выбрали {dessert_name}. Цена: {dessert_price:.2f}€ \n{dessert_extra_name}. Цена: {dessert_extra_price:.2f}€")
        print(f"Всего: {dessert_price + dessert_extra_price:.2f}€")
    elif dessert == "Тирамису" or dessert == "3":
        dessert_name = "Тирамису"
        dessert_price = 4.5
        dessert_extra_change = input(
            "Хотите добавить экстра:\n"
            "Топпинг:\n"
                "\t1. шоколадный (+1.00€)\n"
                "\t2. карамельный (+1.00€)\n"
            "3. Орехи (+1.00€)\n"
            "4. Взбитые сливки (+1.50€)? \n"
        )
        dessert_extra_name, dessert_extra_price = extra_dish_dessert(dessert_extra_change)
        print(f"Вы выбрали {dessert_name}. Цена: {dessert_price:.2f}€ \n{dessert_extra_name}. Цена: {dessert_extra_price:.2f}€")
        print(f"Всего: {dessert_price + dessert_extra_price:.2f}€")
    return dessert_name, dessert_price, dessert_extra_name, dessert_extra_price
# Дополнительные блюда для десертов
def extra_dish_dessert(extra):
    if extra == "1":
        dessert_extra_name = "С шоколадным топпингом"
        dessert_extra_price = 1.00
    elif extra == "2":
        dessert_extra_name = "С карамельным топпингом"
        dessert_extra_price = 1.00
    elif extra == "3":
        dessert_extra_name = "С орехами"
        dessert_extra_price = 1.00
    elif extra == "4":
        dessert_extra_name = "С взбитыми сливками"
        dessert_extra_price = 1.50
    else:
        dessert_extra_name = "Без добавок"
        dessert_extra_price = 0
        print("Вы отказались от добавки.")
    return dessert_extra_name, dessert_extra_price
# Выбор напитка
def drink_selection(drink):
    drink_price = 0  # Стоимость напитка
    drink_name = "Нет напитка"  # Название напитка
    drink_extra_name = "Без добавок"  # Название добавки
    drink_extra_price = 0  # Стоимость добавки

    if drink == "1" or drink.lower() == "кофе":
        drink_name = "Кофе"
        drink_price = 2.50
        drink_extra_change = input(
            "Хотите добавить экстра к кофе:\n"
            "1. Сливки (+0.50€)\n"
            "2. Взбитые сливки (+1.00€)\n"
            "3. Мята (+0.80€)\n"
            "4. Корица (+0.30€)\n"
            "5. Без добавки\n"
        )
        drink_extra_name, drink_extra_price = extra_dish_drink("кофе", drink_extra_change)
    elif drink == "2" or drink.lower() == "чай":
        drink_name = "Чай"
        drink_price = 2.00
        drink_extra_change = input(
            "Хотите добавить экстра к чаю:\n"
            "1. Лимон (+0.30€)\n"
            "2. Мята (+0.50€)\n"
            "3. Имбирь (+0.70€)\n"
            "4. Без добавки\n"
        )
        drink_extra_name, drink_extra_price = extra_dish_drink("чай", drink_extra_change)
    elif drink == "3" or drink.lower() == "лимонад":
        drink_name = "Лимонад"
        drink_price = 3.00
        drink_extra_change = input(
            "Хотите добавить экстра к лимонаду:\n"
            "1. Лед (бесплатно)\n"
            "2. Фрукты (+2.00€)\n"
            "3. Мята (+0.80€)\n"
            "4. Без добавки\n"
        )
        drink_extra_name, drink_extra_price = extra_dish_drink("лимонад", drink_extra_change)
    elif drink == "4" or drink.lower() == "отказаться":
        print("Вы отказались от напитка.")
        return 0, "Нет напитка", "Без добавок", 0
    else:
        print("Некорректный выбор. Попробуйте снова.")
        return drink_selection(input("\nВыберите напиток:\n1. Кофе\n2. Чай\n3. Лимонад\n4. Отказаться\n"))

    return drink_price, drink_name, drink_extra_name, drink_extra_price

# Функция обработки добавок для напитков
def extra_dish_drink(drink_type, extra):
    if drink_type == "кофе":
        if extra == "1":
            return "Сливки", 0.50
        elif extra == "2":
            return "Взбитые сливки", 1.00
        elif extra == "3":
            return "Мята", 0.80
        elif extra == "4":
            return "Корица", 0.30
        elif extra == "5":
            return "Без добавок", 0.0
    elif drink_type == "чай":
        if extra == "1":
            return "Лимон", 0.30
        elif extra == "2":
            return "Мята", 0.50
        elif extra == "3":
            return "Имбирь", 0.70
        elif extra == "4":
            return "Без добавок", 0.0
    elif drink_type == "лимонад":
        if extra == "1":
            return "Лед", 0.0
        elif extra == "2":
            return "Фрукты", 2.00
        elif extra == "3":
            return "Мята", 0.80
        elif extra == "4":
            return "Без добавок", 0.0
    print("Некорректный выбор добавки. Попробуйте снова.")
    return extra_dish_drink(
        drink_type,
        input("Выберите добавку снова:\n")
    )

# Подтверждение заказа
def confirm_order(main_course_cash, main_course_name, extra_name, extra_price, salad_name, salad_cash, salad_extra_name, salad_extra_price, dessert_name, dessert_price, dessert_extra_name, dessert_extra_price, drink_price,drink_name, drink_extra_name, drink_extra_price):

    total =(main_course_cash + extra_price +
            salad_cash + salad_extra_price +
            dessert_price + dessert_extra_price +
            drink_price + drink_extra_price
    )
    print(f"\nВаш заказ:")
    print(f"Основное блюдо:\n"
          f"{main_course_name} ({main_course_cash:.2f}€)\n"
          f"{extra_name} ({extra_price:.2f}€)\n"
    )
    print(f"Салат:\n"
          f"{salad_name} ({salad_cash:.2f}€)\n"
          f"{salad_extra_name} ({salad_extra_price:.2f}€)\n"
    )
    print(f"Десерт:\n"
          f"{dessert_name} ({dessert_price:.2f}€)\n"
          f"{dessert_extra_name} ({dessert_extra_price:.2f}€)\n"
    )
    print(f"Напиток:\n"
          f"{drink_name} ({drink_price:.2f}€)\n"
          f"{drink_extra_name} ({drink_extra_price:.2f}€)\n")
    print(f"Общая сумма: {total:.2f}€")
    confirmation = input("\nВсё верно? (1.Да/2.Нет): ").lower()
    if confirmation == "да" or confirmation == "1":
        print("Спасибо за заказ! Ожидайте доставку через 30 минут.")
    else:
        print("Хорошо, давайте что-то изменим!")
        return start_order()


# Основной блок программы
def start_order():
    print("Привет! Я помогу вам оформить заказ. Давайте начнем с выбора основного блюда.")

    # Выбор основного блюда
    main_course_choice = input("Выберите основное блюдо:\n1. Пицца\n2. Паста\n3. Стейк\n4. Отказаться\n")
    main_course_cash, main_course_name, extra_name, extra_price = main_course(main_course_choice)

    # Выбор салата
    salad_choice = input("\nВыберите салат:\n1. Цезарь\n2. Греческий\n3. Салат с тунцом\n4. Отказаться\n")
    salad_name, salad_cash, salad_extra_name, salad_extra_price = salad_selection(salad_choice)

    # Выбор десерта
    dessert_choice = input("\nВыберите десерт:\n1. Чизкейк\n2. Маффин\n3. Тирамису\n4. Отказаться\n")
    dessert_name, dessert_price, dessert_extra_name, dessert_extra_price = dessert_selection(dessert_choice)

    # Выбор напитка
    drink_choice = input("\nВыберите напиток:\n1. Кофе\n2. Чай\n3. Лимонад\n4. Отказаться\n")
    drink_price, drink_name, drink_extra_name, drink_extra_price = drink_selection(drink_choice)

    # Подтверждение заказа
    confirm_order(
        main_course_cash, main_course_name, extra_name, extra_price,
        salad_name, salad_cash, salad_extra_name, salad_extra_price,
        dessert_name, dessert_price, dessert_extra_name, dessert_extra_price,
        drink_price, drink_name, drink_extra_name, drink_extra_price)


# Запуск программы
start_order()
