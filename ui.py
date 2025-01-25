from data import LANGUAGES
import os
from utils import clear_screen

def choose_language(languages):
    """
    Выводит меню выбора языка и возвращает выбранный язык.
    """
    clear_screen()
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
    clear_screen()
    print(f"{lang['choose']} {lang[category_name]}:")
    # Выводим заголовок меню, используя строки из языкового словаря.

    while True:
        # Запускаем бесконечный цикл, пока пользователь не сделает правильный выбор.
        for i, item in enumerate(items, start=1):
            # Выводим пронумерованный список элементов меню с их названиями и ценами.
            print(f"{i}. {item['name'][selected_language]} ({item['price']:.2f}€)")

        if not show_back:
            # Если show_back равно False, выводим опцию "0. Пропустить"
            print(f"0. {lang['exit']}")
        # Выводим опцию для пропуска выбора блюда
        if show_back:
            # Если show_back равно True, выводим опцию "9. Назад".
            print(f"9. {lang['exit']}")

        choice = input(f"\n{lang['choose_dish']} ")
        # Получаем ввод от пользователя.

        if choice == "0" and not show_back:
            # Если пользователь ввел "0" и опция show_back отключена, возвращаем None (пропуск выбора).
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
        print(f"0. {lang['skip_extras']}")
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
            print(lang["choose_extras"])
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
    clear_screen()
    print("\n" + lang["order_summary"])
    # Выводим заголовок заказа, используя строки из языкового словаря.
    clear_screen()
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
    print(f"{lang['total_price']}: {total_price:.2f}€\n")
    # Выводим общую стоимость заказа.

def change_order(order, lang, selected_language):
    """
      Позволяет пользователю изменить заказ - удалить блюдо.

      Args:
          order (list): Список словарей, представляющий заказ.
          lang (dict): Словарь с текстовыми строками для выбранного языка.
          selected_language (str): Выбранный язык.
    """
    clear_screen()
    while True:
        # Запускаем бесконечный цикл, пока пользователь не завершит изменение заказа.
        print("\n" + lang["change_order"])
        # Выводим заголовок, используя строки из языкового словаря.
        for i, item in enumerate(order, start=1):
            # Выводим пронумерованный список элементов текущего заказа.
            print(f"{i}. {item['name']}")
        print(f"9. {lang['exit']}")
        # Выводим опцию для пропуска изменения заказа.
        print(f"0. {lang['add_item']}")
        # Выводим опцию для добавления блюда.
        choice = input(f"{lang['remove_item']}")
        # Получаем ввод от пользователя.
        if choice == "9":
            # Если пользователь ввел "9", выходим из цикла.
            return "back"
        elif choice.isdigit() and 1 <= int(choice) <= len(order):
            # Если ввод является цифрой и находится в пределах доступных вариантов,
            del order[int(choice) - 1]
            # Удаляем выбранный элемент из заказа.
        elif choice == "0":
            # Если пользователь ввел "0", возвращаем "add_item" для добавления блюда
           return "add_item"

        else:
            # Если ввод не соответствует ни одному из условий, выводим сообщение об ошибке.
            print(lang["error"])
    return order
    # Возвращаем измененный заказ.