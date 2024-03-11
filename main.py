#!/usr/bin/python3
import tkinter as tk

class SimpleCalculator(tk.Tk):
    """
    """
    def __init__(self):
        super().__init__()
        self.title("A simple calculator")

        self.geometry('110x220')

        self.resizable(False, False)

        # Add the top Entry to display calculator results
        self.OPERATIONS = tk.Entry(width=10)
        self.OPERATIONS.grid(row=6, column=0, columnspan=4)
        self.RESULT = tk.Entry(width=10)
        self.RESULT.grid(row=0, column=0, columnspan=4)

        # Add buttons of numbers 9~0, "=", "+" and "C"
        self.number_9 = tk.Button(self, text="9", command=lambda: self.Button_Click("9"))
        self.number_9.grid(row=1, column=0)

        self.number_8 = tk.Button(self, text="8", command=lambda: self.Button_Click("8"))
        self.number_8.grid(row=1, column=1)

        self.number_7 = tk.Button(self, text="7", command=lambda: self.Button_Click("7"))
        self.number_7.grid(row=1, column=2)

        self.number_6 = tk.Button(self, text="6", command=lambda: self.Button_Click("6"))
        self.number_6.grid(row=2, column=0)

        self.number_5 = tk.Button(self, text="5", command=lambda: self.Button_Click("5"))
        self.number_5.grid(row=2, column=1)

        self.number_4 = tk.Button(self, text="4", command=lambda: self.Button_Click("4"))
        self.number_4.grid(row=2, column=2)

        self.number_3 = tk.Button(self, text="3", command=lambda: self.Button_Click("3"))
        self.number_3.grid(row=3, column=0)

        self.number_2 = tk.Button(self, text="2", command=lambda: self.Button_Click("2"))
        self.number_2.grid(row=3, column=1)

        self.number_1 = tk.Button(self, text="1", command=lambda: self.Button_Click("1"))
        self.number_1.grid(row=3, column=2)

        self.number_0 = tk.Button(self, text="0", command=lambda: self.Button_Click("0"))
        self.number_0.grid(row=4, column=0)

        self.ADD = tk.Button(self, text="+", command=self.Add)
        self.ADD.grid(row=4, column=1)

        self.CLEAR = tk.Button(self, text="C", command=self.Button_Clear)
        self.CLEAR.grid(row=4, column=2)

        self.EQUAL = tk.Button(self, text="=", command=lambda: self.Equal(self.OPERATIONS.get()))
        self.EQUAL.grid(row=5, column=0, columnspan=3)

    # button add function
    def Button_Click(self, number):
        self.OPERATIONS.insert(tk.INSERT, number)
        self.RESULT.insert(tk.INSERT, number)


    def Button_Clear(self):
        self.OPERATIONS.delete(0, tk.END)
        self.RESULT.delete(0, tk.END)


    def Add(self):
        self.OPERATIONS.insert(tk.INSERT, "+")



    def Equal(self, args):
        args = args.split('+')
        result = 0
        for arg in args:
            result += int(arg)
        self.OPERATIONS.insert(tk.INSERT, f"={result}")
        self.RESULT.delete(0, tk.END)
        self.RESULT.insert(0, result)

# Run the widget
app = SimpleCalculator()
app.mainloop()
