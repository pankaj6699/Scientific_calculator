import tkinter as tk
import math
import statistics

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("600x400")  # Increase size to accommodate history

        self.total = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.total, font=("Helvetica", 20))
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)

        self.create_buttons()
        self.history = []

        self.history_label = tk.Label(master, text="History", font=("Helvetica", 12))
        self.history_label.grid(row=0, column=5)
        self.history_listbox = tk.Listbox(master, height=15, width=25)
        self.history_listbox.grid(row=1, column=5, rowspan=6, padx=5, pady=5)
        
        self.reset_button = tk.Button(master, text="Reset History", command=self.reset_history, font=("Helvetica", 12))
        self.reset_button.grid(row=7, column=5, padx=5, pady=5)

    def create_buttons(self):
        button_list = [
            ['sin', 'cos', 'tan', '^2', '10^x'],
            ['7', '8', '9', '/', 'log(x)'],
            ['4', '5', '6', '*', '1/x'],
            ['1', '2', '3', '-', 'x!'],
            ['Mean', 'Median', 'Mode', '+', 'qbrt'],
            ['0', 'C', '=', 'Exp', 'sqrt']
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.master, text=button_text, width=8, height=4, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.master.rowconfigure(i + 1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)
        self.master.columnconfigure(5, weight=1)

    def click(self, button_text):
        if button_text == '=':
            try:
                result = eval(self.entry.get())
                self.total.set(result)
                self.update_history(f"{self.entry.get()} = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"{self.entry.get()} = Error")
        elif button_text == 'C':
            self.total.set("")
        elif button_text in ('sin', 'cos', 'tan'):
            try:
                angle = math.radians(float(self.entry.get()))
                result = getattr(math, button_text)(angle)
                self.total.set(result)
                self.update_history(f"{button_text}({self.entry.get()}) = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"{button_text}({self.entry.get()}) = Error")
        elif button_text == '^2':
            try:
                result = float(self.entry.get()) ** 2
                self.total.set(result)
                self.update_history(f"{self.entry.get()}^2 = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"{self.entry.get()}^2 = Error")
        elif button_text == 'log(x)':
            try:
                result = math.log(float(self.entry.get()))
                self.total.set(result)
                self.update_history(f"log({self.entry.get()}) = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"log({self.entry.get()}) = Error")
        elif button_text == '1/x':
            try:
                result = 1 / float(self.entry.get())
                self.total.set(result)
                self.update_history(f"1/{self.entry.get()} = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"1/{self.entry.get()} = Error")
        elif button_text == 'x!':
            try:
                result = math.factorial(int(self.entry.get()))
                self.total.set(result)
                self.update_history(f"{self.entry.get()}! = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"{self.entry.get()}! = Error")
        elif button_text == '10^x':
            try:
                result = 10 ** float(self.entry.get())
                self.total.set(result)
                self.update_history(f"10^{self.entry.get()} = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"10^{self.entry.get()} = Error")
        elif button_text == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.total.set(result)
                self.update_history(f"sqrt({self.entry.get()}) = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"sqrt({self.entry.get()}) = Error")
        elif button_text == 'qbrt':
            try:
                result = float(self.entry.get()) ** (1/3)
                self.total.set(result)
                self.update_history(f"qbrt({self.entry.get()}) = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"qbrt({self.entry.get()}) = Error")
        elif button_text in ('Mean', 'Median', 'Mode'):
            try:
                numbers = list(map(float, self.entry.get().split(',')))
                if button_text == 'Mean':
                    result = statistics.mean(numbers)
                    self.update_history(f"Mean({self.entry.get()}) = {result}")
                elif button_text == 'Median':
                    result = statistics.median(numbers)
                    self.update_history(f"Median({self.entry.get()}) = {result}")
                elif button_text == 'Mode':
                    result = statistics.mode(numbers)
                    self.update_history(f"Mode({self.entry.get()}) = {result}")
                self.total.set(result)
            except:
                self.total.set("Error")
                self.update_history(f"{button_text}({self.entry.get()}) = Error")
        elif button_text == 'Exp':
            try:
                base, exponent = map(float, self.entry.get().split(','))
                result = base ** exponent
                self.total.set(result)
                self.update_history(f"{base}^{exponent} = {result}")
            except:
                self.total.set("Error")
                self.update_history(f"{self.entry.get()} = Error")
        else:
            self.total.set(self.entry.get() + button_text)

    def update_history(self, calculation):
        if len(self.history) >= 50:
            self.history.pop(0)
        self.history.append(calculation)
        self.history_listbox.insert(tk.END, calculation)
        if len(self.history) > 50:
            self.history_listbox.delete(0)
    
    def reset_history(self):
        self.history = []
        self.history_listbox.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
