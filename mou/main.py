import tkinter as tk
from tkinter import ttk

# ------------------------
# Base Widget
# ------------------------
class Widget:
    def __init__(self, master):
        self.master = master

# ------------------------
# Labels
# ------------------------
class MLabel(Widget):
    def __init__(self, master, text):
        super().__init__(master)
        self.label = ttk.Label(master, text=text)
        self.label.pack(pady=5)

    def set_text(self, text):
        self.label.config(text=text)

# ------------------------
# Buttons
# ------------------------
class MButton(Widget):
    def __init__(self, master, text, command):
        super().__init__(master)
        self.button = ttk.Button(master, text=text, command=command)
        self.button.pack(pady=5)

# ------------------------
# Checkboxes
# ------------------------
class MCheckbox(Widget):
    def __init__(self, master, text):
        super().__init__(master)
        self.var = tk.IntVar()
        self.checkbox = ttk.Checkbutton(master, text=text, variable=self.var)
        self.checkbox.pack(pady=5)

    def is_checked(self):
        return self.var.get() == 1

# ------------------------
# Radio Buttons
# ------------------------
class MRadioGroup(Widget):
    def __init__(self, master, options):
        super().__init__(master)
        self.var = tk.StringVar()
        self.buttons = []
        for opt in options:
            rb = ttk.Radiobutton(master, text=opt, value=opt, variable=self.var)
            rb.pack(anchor="w")
            self.buttons.append(rb)

    def get_value(self):
        return self.var.get()

# ------------------------
# Slider
# ------------------------
class MSlider(Widget):
    def __init__(self, master, from_=0, to=100, orient='horizontal', command=None):
        super().__init__(master)
        self.scale = ttk.Scale(master, from_=from_, to=to, orient=orient, command=command)
        self.scale.pack(pady=5)

    def get_value(self):
        return self.scale.get()

# ------------------------
# Entry
# ------------------------
class MEntry(Widget):
    def __init__(self, master):
        super().__init__(master)
        self.entry = ttk.Entry(master)
        self.entry.pack(pady=5)

    def get_text(self):
        return self.entry.get()

# ------------------------
# Combobox
# ------------------------
class MCombobox(Widget):
    def __init__(self, master, values):
        super().__init__(master)
        self.combobox = ttk.Combobox(master, values=values)
        self.combobox.pack(pady=5)

    def get_value(self):
        return self.combobox.get()

# ------------------------
# Progress Bar
# ------------------------
class MProgressBar(Widget):
    def __init__(self, master, length=200, mode='determinate'):
        super().__init__(master)
        self.progress = ttk.Progressbar(master, length=length, mode=mode)
        self.progress.pack(pady=5)

    def set_value(self, value):
        self.progress['value'] = value

# ------------------------
# Listbox
# ------------------------
class MList(Widget):
    def __init__(self, master, items):
        super().__init__(master)
        self.listbox = tk.Listbox(master)
        for item in items:
            self.listbox.insert(tk.END, item)
        self.listbox.pack(pady=5)

    def get_selected(self):
        return [self.listbox.get(i) for i in self.listbox.curselection()]

# ------------------------
# Tree
# ------------------------
class MTree(Widget):
    def __init__(self, master, columns, data):
        super().__init__(master)
        self.tree = ttk.Treeview(master, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
        for row in data:
            self.tree.insert("", tk.END, values=row)
        self.tree.pack(pady=5)

    def get_selected(self):
        return self.tree.selection()

# ------------------------
# Tabs
# ------------------------
class MTabs(Widget):
    def __init__(self, master):
        super().__init__(master)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill='both')
        self.tabs = {}

    def add_tab(self, name):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=name)
        self.tabs[name] = frame
        return frame

# ------------------------
# App Class
# ------------------------
class MOUApp:
    def __init__(self, width=600, height=400, title="MOU App"):
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)

    def run(self):
        self.root.mainloop()
