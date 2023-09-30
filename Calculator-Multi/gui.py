import tkinter as tk
from tkinter import messagebox
from factories import FeatureFactory
import re

class CalculatorApplication:
    def __init__(self, root):
        """Constructs all the necessary attributes for the CalculatorApplication object."""
        self.root = root
        self.root.title("Calculator")
        self.history_manager = FeatureFactory.create_factory("history").create_feature()
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set('0')
        
        # Display
        display = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 24), justify='right')
        display.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('History', 5, 0), ('Exit', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
        
    def on_button_click(self, button_text):
        current_text = self.result_var.get()
        if button_text.isdigit() or button_text in ['+', '-', '*', '/']:
            new_text = current_text + button_text if current_text != '0' else button_text
            self.result_var.set(new_text)
        elif button_text == '=':
            try:
                operation = self.result_var.get()
                # Assuming that the user enters in the format: a operation b
                print(operation)
                a, op, b = re.split(r'([^\d.])', operation)
                factory = FeatureFactory.create_factory(op)
                calculator = factory.create_feature()
                result = calculator.calculate(float(a), float(b))
                self.history_manager.append_history(f"{a} {op} {b} = {result}")
                self.result_var.set(str(result))
            except Exception as e:
                messagebox.showerror('Error', str(e))
        elif button_text == 'C':
            self.result_var.set('0')
        elif button_text == 'History':
            messagebox.showinfo('History', str(self.history_manager))
        elif button_text == 'Exit':
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApplication(root, 'normal')
    root.mainloop()