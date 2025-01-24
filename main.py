import json
from ui import choose_language
from order_logic import start_order

# Загружаем языковые строки
with open('data/languages.json', 'r', encoding='utf-8') as f:
    LANGUAGES = json.load(f)

# Загружаем меню
with open('data/menu.json', 'r', encoding='utf-8') as f:
    CATEGORIES = json.load(f)

if __name__ == '__main__':
    selected_language = choose_language(LANGUAGES)
    start_order(selected_language)