# Chat-Bot: A Multilingual Restaurant Ordering Assistant

Welcome to the **Chat-Bot** repository! This project is a text-based chatbot designed to streamline the ordering process in restaurants. With multilingual support and a user-friendly interface, it provides an efficient and accessible solution for both customers and restaurant operators.

---

## 🌍 Key Features

- **Multilingual Support**: Available in Russian 🇷🇺, English 🇬🇧, and German 🇩🇪.
- **Menu Customization**: Choose dishes and additional toppings from structured categories.
- **Order Management**: Modify or remove items before confirming your order.
- **Intuitive Design**: Clear and user-focused interaction flow.
- **Expandable Architecture**: Menu and language data are stored in JSON files, making it easy to update and scale.

---

## ⚠️ Development Status

**This project is currently under development.**  
Please note that the structure and logic of the application are subject to change as the project evolves.

---

## 🚀 What Makes This Unique?

The chatbot's **structured data storage system** allows for:
- Easy integration of new menu items and categories.
- Seamless support for additional languages.
- Minimal code changes when scaling or updating the system.

---

## 🔮 Potential Enhancements

This project is a foundation for more advanced features:
1. **Payment Integration**: Add online payment functionality.
2. **Graphical Interface**: Develop a GUI for better user experience.
3. **Database Connection**: Use databases for storing menu and order data.
4. **Real-World Deployment**: Deploy the chatbot on servers for live use.

---

## 🛠️ File Structure

```
Chat-Bot/
├── data/
│   ├── languages.json   # Stores multilingual strings
│   └── menu.json        # Stores menu items and categories
├── docs/
│   ├── README.md        # Documentation
│   └── TODO.md          # Development notes
├── tests/               # Unit tests folder
├── main.py              # Main application entry point
├── ui.py                # User interface functions
├── order_logic.py       # Core order management logic
├── utils.py             # Utility functions
└── data.py              # Global variables for LANGUAGES and CATEGORIES
```

---

## 🖥️ How It Works

1. **Choose a Language**: Start by selecting your preferred language.
2. **Browse the Menu**: Navigate through categories and select dishes or toppings.
3. **Review Your Order**: See a summary with prices and make adjustments if needed.
4. **Confirm**: Finalize your order.

---

## 💬 Supported Languages

🇷🇺 **Russian**  
🇬🇧 **English**  
🇩🇪 **German**

Adding more languages is simple by editing the `languages.json` file.

---

## 📚 Documentation

Detailed documentation is available in the `docs/` folder, including:
- Code structure and logic
- How to add new features
- Testing guidelines

---

## 📈 Future Roadmap

We envision the following developments:
- **AI Integration**: Enhance interactions with natural language processing.
- **Cloud Deployment**: Host the chatbot on cloud platforms for scalability.
- **Mobile App**: Extend functionality to mobile platforms.

---

## 🧪 Testing

Unit tests are included in the `tests/` directory. Run the tests using:
```bash
python -m unittest discover tests
```

---

## 👤 Author

**AlexH73**  
- [GitHub Profile](https://github.com/AlexH73)  
- [Slack Profile](https://ait-tr.slack.com/team/U07V574LHN0)

---

## 💡 Contributions

We welcome suggestions and contributions!  
Feel free to open an [Issue](https://github.com/AlexH73/Chat-Bot/issues) or submit a [Pull Request](https://github.com/AlexH73/Chat-Bot/pulls).

---

## 📜 License

This project is licensed under the [MIT License](https://github.com/AlexH73/Chat-Bot/tree/main?tab=MIT-1-ov-file). Feel free to contribute, modify, and share!

---

Thank you for exploring the repository! For any questions or feedback, please don't hesitate to reach out. 🎉