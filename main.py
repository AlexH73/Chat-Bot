from data import LANGUAGES, CATEGORIES
from ui import choose_language
from order_logic import start_order

if __name__ == '__main__':
    selected_language = choose_language(LANGUAGES)
    start_order(selected_language)