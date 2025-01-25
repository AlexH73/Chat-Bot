import json

with open('data/languages.json', 'r', encoding='utf-8') as f:
    LANGUAGES = json.load(f)

with open('data/menu.json', 'r', encoding='utf-8') as f:
    CATEGORIES = json.load(f)