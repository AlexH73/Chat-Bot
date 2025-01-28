import json
import os
from pathlib import Path


def load_data():
    """Загружает данные из JSON-файлов."""

    # Если скрипт запущен не из tests
    if os.path.basename(os.getcwd()) != 'tests':
        languages_path = Path(__file__).parent / 'data' / 'languages.json'
        menu_path = Path(__file__).parent / 'data' / 'menu.json'
    # Если скрипт запущен из tests
    else:
        languages_path = Path(__file__).parent.parent / 'data' / 'languages.json'
        menu_path = Path(__file__).parent.parent / 'data' / 'menu.json'

    with open(languages_path, 'r', encoding='utf-8') as f:
        LANGUAGES = json.load(f)

    with open(menu_path, 'r', encoding='utf-8') as f:
        CATEGORIES = json.load(f)

    return LANGUAGES, CATEGORIES


LANGUAGES, CATEGORIES = load_data()