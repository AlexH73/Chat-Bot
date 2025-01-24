import json
from ui import choose_language, choose_item, confirm_order, change_order
from utils import clear_screen

with open('languages.json', 'r', encoding='utf-8') as f:
    LANGUAGES = json.load(f)

with open('menu.json', 'r', encoding='utf-8') as f:
    CATEGORIES = json.load(f)

def start_order(selected_language, order=None):
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
        elif choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            # Если ввод является цифрой и находится в пределах доступных категорий,
            history.append(order)
            # Добавляем текущий заказ в историю.
            category_index = int(choice) - 1
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
                    order = []
                    break
            elif dish:
                # Если пользователь выбрал элемент, добавляем его в заказ.
                order.append(dish)
        elif choice == "9":
            # Если пользователь ввел "9" очищаем заказ и выходим из цикла
            order = []
            break
        else:
            # Если ввод не соответствует ни одному из условий, выводим сообщение об ошибке.
            print(lang["error"])