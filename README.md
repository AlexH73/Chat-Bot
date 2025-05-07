# Chat-Bot
## 🇩🇪 Beschreibung
Dieses Projekt ist eine textbasierte Benutzeroberfläche für die Bestellung in einem Gastronomiebetrieb. Der Chatbot unterstützt mehrere Sprachen und bietet eine benutzerfreundliche Oberfläche.

## 🇷🇺 Описание
Этот проект представляет собой текстовый интерфейс для оформления заказов в заведении общепита. Чат-бот поддерживает несколько языков и предоставляет интуитивно понятный интерфейс для пользователей.

## 🇬🇧 Description
This project is a text-based interface for placing orders in a catering establishment. The chatbot supports multiple languages and provides an intuitive interface for users.




## 🇩🇪 Funktionen
- Mehrsprachige Unterstützung (Russisch, Englisch, Deutsch).
- Auswahl von Gerichten aus verschiedenen Kategorien.
- Zusätzliche Toppings für Gerichte.
- Anzeige der endgültigen Bestellung mit Preisen.
- Bearbeiten oder Entfernen von Gerichten vor der Bestätigung der Bestellung.
- Benutzerfreundliche Oberfläche.

## 🇷🇺 Возможности
- Поддержка нескольких языков (русский, английский, немецкий).
- Выбор блюд из различных категорий.
- Добавки к блюдам.
- Просмотр итогового заказа с ценами.
- Изменение или удаление блюд перед подтверждением заказа.
- Интуитивно понятный интерфейс.

## 🇬🇧 Features
- Multilingual support (Russian, English, German).
- Selection of dishes from different categories.
- Additional toppings for dishes.
- View final order with prices.
- Edit or remove dishes before confirming the order.
- User-friendly interface.
  
---

## 🇩🇪 Besonderheit
Das Hauptmerkmal des Skripts ist seine Mehrsprachigkeit und das strukturierte Datenspeicherungssystem für Gerichte und Beilagen. Dieses Design ermöglicht die einfache Hinzufügung neuer Menüelemente und die Unterstützung mehrerer Sprachversionen der Anwendung ohne wesentliche Codeänderungen. Sprach- und Gerichtsdaten werden in separaten JSON-Dateien gespeichert, was die Bearbeitung und Verwaltung vereinfacht.

## 🇷🇺 Особенность
Главной особенностью скрипта является его мультиязычность и структурированная система хранения данных о блюдах и добавках, что позволяет легко добавлять новые позиции в меню и поддерживать несколько языковых версий приложения без значительных изменений кода. Данные о языках и блюдах хранятся в отдельных JSON файлах, что упрощает редактирование и управление ими.

## 🇬🇧 Distinctive Feature
The main feature of the script is its multilingual support and structured data storage system for dishes and toppings. This design allows for easy addition of new menu items and support for multiple language versions of the application without significant code changes. Language and dish data are stored in separate JSON files, simplifying editing and management.

---

## 🇩🇪 Potenzial
- Integration mit Zahlungssystemen.
- Erweiterung der Funktionen (neue Kategorien, Schärfegrade, Portionen).
- Entwicklung einer grafischen Benutzeroberfläche.
- Integration mit einer Datenbank zur Speicherung von Menüs und Bestellungen.
- Einsatz in realen Bedingungen.

## 🇷🇺 Потенциал
- Интеграция с платежными системами.
- Расширение функционала (новые категории блюд, уровни остроты, порции).
- Разработка графического интерфейса.
- Интеграция с базой данных для хранения меню и заказов.
- Использование в реальных условиях.

## 🇬🇧 Potential
- Integration with payment systems.
- Expanding functionality (new dish categories, spice levels, portions).
- Development of a graphical interface.
- Integration with a database for storing menu and orders.
- Real-world deployment.

---

## 🇩🇪 Fazit
Dieses Projekt dient als Grundlage für die Entwicklung eines komplexeren Bestellmanagementsystems. Es kann an verschiedene Anwendungsszenarien angepasst werden.

## 🇷🇺 Заключение
Данный проект представляет собой основу для разработки более сложной системы управления заказами. Он может быть адаптирован под различные сценарии использования.

## 🇬🇧 Conclusion
This project serves as a foundation for developing a more complex order management system. It can be adapted for various use cases.


## 🇩🇪 Dateistruktur /  🇷🇺  Файловая структура /  🇬🇧 File Structure
    Chat-Bot/ 
        ├── data/  
        │   ├── languages.json 
        │   └── menu.json 
        ├── docs/ 
        │   └── README.md 
        │   └── TODO.md  
        ├── tests/ 
        ├── main.py  
        ├── ui.py 
        ├── order_logic.py   
        ├── utils.py
        └── data.py

🇩🇪
*   **`data/`:** Enthält Datendateien (Sprachstrings und Menü) im JSON-Format.
*   **`docs/`:** Enthält die Projektdokumentation.
*   **`tests/`:** Ordner für Unit-Tests.
*   **`main.py`:** Hauptdatei zum Starten der Anwendung.
*   **`ui.py`:** Funktionen für die Benutzeroberfläche.
*   **`order_logic.py`:** Verwalten der Bestelllogik mit der Funktion `start_order`.
*   **`utils.py`:** Enthält Hilfsfunktionen.
*   **`data.py`:** Definiert die globalen Variablen `LANGUAGES` und `CATEGORIES`.

🇷🇺
*   **`data/`:** Содержит файлы с данными (языковые строки и меню) в формате JSON.
*   **`docs/`:** Содержит документацию проекта.
*   **`tests/`:** Папка для хранения юнит-тестов.
*   **`main.py`:** Основной файл запуска приложения.
*   **`ui.py`:** Файл с функциями для работы с пользовательским интерфейсом.
*   **`order_logic.py`:** Файл с функцией `start_order`, управляющей логикой заказа.
*   **`utils.py`:** Файл с вспомогательными функциями.
*   **`data.py`:** Файл, содержащий общие переменные `LANGUAGES` и `CATEGORIES`.

🇬🇧
*   **`data/`:** Contains data files (language strings and menu) in JSON format.
*   **`docs/`:** Contains project documentation.
*   **`tests/`:** Folder for unit tests.
*   **`main.py`:** Main application entry point.
*   **`ui.py`:** Functions for user interface.
*   **`order_logic.py`:** Manages order logic with the `start_order` function.
*   **`utils.py`:** Contains utility functions.
*   **`data.py`:** Defines global variables `LANGUAGES` and `CATEGORIES`.
