# MOU GUI Toolkit

**MOU (Modern UI)** is a lightweight, cross-platform Python GUI toolkit built on `tkinter`.
It provides easy-to-use widgets like labels, buttons, sliders, trees, lists, tabs, and more — perfect for building modern-looking Python applications quickly.

---

## ✨ Features

* Labels, Buttons, Checkboxes, Radio Buttons
* Sliders, Entry, Combobox
* Progress Bars, Lists, Trees
* Tabs / Notebook support
* Simple and consistent API for all widgets
* Works on **Windows, macOS, Linux**

---

## 🚀 Installation

Install directly from source:

```bash
git clone https://github.com/LightingDev/mou-gui.git
cd mou-gui
pip install .
```

For development (editable install):

```bash
pip install -e .
```

> Now you can `import mou` in your Python scripts!

---

## 📝 Quick Tutorial

```python
from mou import MOUApp, MLabel, MButton, MSlider

app = MOUApp(title="Hello MOU!")

label = MLabel(app.root, "Welcome to MOU!")
button = MButton(app.root, "Click Me", lambda: label.set_text("You clicked!"))
slider = MSlider(app.root)

app.run()
```

* Create an `MOUApp` instance
* Add widgets like `MLabel`, `MButton`, `MSlider`
* Call `app.run()` to start the GUI

---

## 🛠️ Templates

You can quickly create apps using these templates:

```python
# templates/simple_app.py
from mou import MOUApp, MLabel, MButton

app = MOUApp(title="Simple Template")
MLabel(app.root, "Hello Template!")
MButton(app.root, "Click Me", lambda: print("Clicked!"))
app.run()
```

---

## 🤝 Contributing

1. Fork the repository
2. Install MOU from source (`pip install -e .`)
3. Add your widgets, templates, or improvements
4. Open a Pull Request

---

## 📜 License

apache-2.0 License — free to use, modify, and distribute.

---
