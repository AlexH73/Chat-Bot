first_dish_name = ""  # pizza, pasta or steak
first_dish_price = 0  # price for pizza/pasta/steak
first_dish_extra_name = ""  # additionals for first dish
first_dish_extra_price = 0  # price for extras

tsalad_name = ""
salad_extra_name = ""
salad_extra_price = 0
salad_price = 0
drik_name = ""
drink_price = 0
drink_extra_name = ""
drink_extra_price = 0


# sweets...

def count_total_price():
    total_price = first_dish_price + first_dish_extra_price + salad_price + salad_extra_price + drink_price + drink_extra_price
    return total_price


def start_order():
    print("Привет! Я помогу вам оформить заказ. Давайте начнем с выбора основного блюда.")
    # Начинаем бесконечный цикл для обработки выбора добавки к греческому салату

    while True:
        print(
            "1. Выбор основного блюда\n"
            "2. Выбор салат\n"
            "3. Выбор десерта\n"
            "4. Выбор напитка\n"
            "0. Выход\n"
        )

        main_course_choice = input() # не работает в онлайн IDE
        #main_course_choice = "1"

        if main_course_choice == "1":
            # вызов метода, в котором будет происходить выбор основного блюда
            # написать новый метод и вызвать его отсюда
            first_dish_chooser()

            #  ...
        elif main_course_choice == "2":
        # ...
            continue
        elif main_course_choice == "3":
        # ...
            continue
        elif main_course_choice == "4":
        # ...
            continue
        elif main_course_choice == "0":
            print("Вы хотите что-то изменить? 1. Да  / 2.Нет")
            final_order = "2"
            if final_order == 1:
                continue
            else:
                break
        else:
            print("Не корректное значение")
            continue

    # после выбора "0" в цикле мы окажемся тут. Какой дальнейший шаг?
    print("что было заказано и сколько стоит -> оплата? да/нет -> ")
    # complete_order = input() # не работает в онлайн IDE
    complete_order = "1"
    if complete_order == "1":
        print("спасибо, ожидайте заказ")
    else:
        print("до свидания!")


# метод который нужен для оформления заказа основного блюда:
def first_dish_chooser():
    print("Sie haben nummer 1 gewählt , sie haben noch folgende optionen\n : "
          "1. Пицца\n"
          "2. Паста\n"
          "3. Стейк\n"
          "0. Выход\n"
          )
    first_dish_choise = input() # не работает в онлайн IDE
    #first_dish_choise = "1"

    if first_dish_choise == "1":
        first_dish_name = "Пицца"
        first_dish_price = 8.00
        pizza_extras_chooser()

    elif first_dish_choise == "2":
        first_dish_name = "Паста"
        first_dish_price = 7.50
        # ...
    elif first_dish_choise == "3":
        first_dish_name = "Стейк"
        first_dish_price = 15.00
        # ...
    elif first_dish_choise == "0":
        start_order()
    else:
        print("Не корректное значение")


def pizza_extras_chooser():
    print("Sie haben nummer 1 gewählt , sie haben noch folgende optionen\n : "
          "1. Kaese\n"
          "2. Bekon\n"
          "3. Spicy sauce\n"
          "0. Выход\n"
          )
    pizza_extras_chooser = input() # не работает в онлайн IDE
    #pizza_extras_chooser = ""

    if pizza_extras_chooser == "1":
        first_dish_extra_name = "Kaese"
        first_dish_extra_price = 1.50

    elif pizza_extras_chooser == "2":
        first_dish_extra_name = "Bekon"
        first_dish_extra_price = 2.00

    elif pizza_extras_chooser == "3":
        first_dish_extra_name = "Spicy sauce"
        first_dish_extra_price = 1.00

    elif pizza_extras_chooser == "0":
        return
    else:
        print("Не корректное значение")