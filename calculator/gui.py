import tkinter as tk
from tkinter import ttk
from parser import parse_expression #type: ignore
from evaluator import evaluate_expression

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x350")

        self.expression = ""

        # Entry widget to display the expression
        self.expression_entry = ttk.Entry(root, font=('Helvetica', 14), justify="right")
        self.expression_entry.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)

        # Buttons for digits and operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('Clear', 5, 0)  # Removed unnecessary rowspan and columnspan values
        ]

        for (text, row, col) in buttons:
            if text == "Clear":
                btn = ttk.Button(root, text=text, command=self.clear, style="Clear.TButton")
            else:
                btn = ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew")
            root.grid_columnconfigure(col, weight=1)

        # Styling
        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12))
        style.configure("Clear.TButton", font=('Helvetica', 12), background="red")

    def on_button_click(self, value):
        if value == "=":
            self.evaluate()
        else:
            self.expression += value
            self.expression_entry.insert(tk.END, value)

    def evaluate(self):
        try:
            parsed_expression = parse_expression(self.expression)
            result = evaluate_expression(parsed_expression)
            self.expression_entry.delete(0, tk.END)
            self.expression_entry.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception as e:
            self.expression_entry.delete(0, tk.END)
            self.expression_entry.insert(tk.END, "Error")
            self.expression = ""

    def clear(self):
        self.expression_entry.delete(0, tk.END)
        self.expression = ""

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
