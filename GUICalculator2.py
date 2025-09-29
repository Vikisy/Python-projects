import tkinter as tk
from tkinter import ttk
from math import sin, cos, tan, asin, acos, atan, sqrt, log10, pi, e, radians, degrees

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("𝑽𝒊𝒄𝒕𝒐𝒓 𝑬.𝑶.꧂")
        self.expression = ""
        self.memory = 0
        self.is_dark_mode = False
        self.input_text = tk.StringVar()

        self.buttons = []  # Track buttons for dynamic theme update
        self.build_ui()
        self.apply_theme()

    def build_ui(self):
        # Top frame
        top_frame = ttk.Frame(self.root)
        top_frame.pack(pady=5)

        self.theme_button = ttk.Button(top_frame, text="𝓣", width=1, command=self.toggle_theme)
        self.theme_button.pack(side=tk.LEFT, padx=0, pady=0)

        self.input_field = tk.Entry(top_frame, textvariable=self.input_text, font=('Arial', 16),
                                    bd=5, relief=tk.RIDGE, justify='right', width=20)
        self.input_field.pack(side=tk.LEFT, padx=5)

        # Buttons layout
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ['sin', 'cos', 'tan', 'C'],
            ['asin', 'acos', 'atan', 'log'],
            ['^', '√', 'π', 'e'],
            ['MR', 'M+', 'M-', 'MC'],
            ['7', '8', '9', '÷'],       
            ['4', '5', '6', '×'], 
            ['1', '2', '3', '-'],
            ['=', '0', '.', '+']
        ]

        for r, row in enumerate(buttons):
            for c, btn in enumerate(row):
                button = tk.Button(button_frame, text=btn, width=5, height=2,
                                   font=('Arial', 12), command=lambda b=btn: self.on_button_click(b))
                button.grid(row=r, column=c, padx=2, pady=2)
                self.buttons.append(button)

    def get_button_color(self):
        return "black" if self.is_dark_mode else "lightblue"  # dark gray vs light blue

    def apply_theme(self):
        bg = "gray" if self.is_dark_mode else "blue"
        fg = "white" if self.is_dark_mode else "black"
        entry_bg = "black" if self.is_dark_mode else "white"

        self.root.configure(bg=bg)
        self.input_field.configure(bg=entry_bg, fg=fg, insertbackground=fg)

        for button in self.buttons:
            button.configure(bg=self.get_button_color(), fg=fg, activebackground="#777" if self.is_dark_mode else "#ccc")

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()

    def on_button_click(self, button):
        try:
            if button == 'C':
                self.expression = ""
                self.input_text.set("")
            elif button == '=':
                result = eval(self.expression)
                self.input_text.set(result)
                self.expression = str(result)
            elif button == '√':
                result = sqrt(eval(self.expression))
                self.input_text.set(result)
                self.expression = str(result)
            elif button == 'log':
                result = log10(eval(self.expression))
                self.input_text.set(result)
                self.expression = str(result)
            elif button == '^':
                self.expression += '**'
                self.input_text.set(self.expression)
            elif button == 'π':
                self.expression += str(pi)
                self.input_text.set(self.expression)
            elif button == 'e':
                self.expression += str(e)
                self.input_text.set(self.expression)
            elif button in ['sin', 'cos', 'tan']:
                angle = radians(eval(self.expression))
                result = {'sin': sin(angle), 'cos': cos(angle), 'tan': tan(angle)}[button]
                self.input_text.set(result)
                self.expression = str(result)
            elif button in ['asin', 'acos', 'atan']:
                value = eval(self.expression)
                angle = {'asin': asin(value), 'acos': acos(value), 'atan': atan(value)}[button]
                result = degrees(angle)
                self.input_text.set(result)
                self.expression = str(result)
            elif button == 'M+':
                self.memory += eval(self.expression)
                self.input_text.set(f"Memory: {self.memory}")
                self.expression = ""
            elif button == 'M-':
                self.memory -= eval(self.expression)
                self.input_text.set(f"Memory: {self.memory}")
                self.expression = ""
            elif button == 'MR':
                self.input_text.set(str(self.memory))
                self.expression = str(self.memory)
            elif button == 'MC':
                self.memory = 0
                self.input_text.set("Memory cleared")
                self.expression = ""
            elif button == '×':
                self.expression += '*'
                self.input_text.set(self.expression)
            elif button == '÷':
                self.expression += '/'
                self.input_text.set(self.expression)
            else:
                self.expression += str(button)
                self.input_text.set(self.expression)
        except Exception as err:
            self.input_text.set(f"Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = ScientificCalculator(root)
    root.mainloop()
