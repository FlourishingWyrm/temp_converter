
#description
#input
#output  -#9C0000
#990099  degrees/farenhight #009900
#CC6600  help and history  #004C99

# history and export page last 5 calculations

#return (user_input - 32) * 5 / 9 (celcus)
from tkinter import *
class Converter():
    """conversion tool"""

    def __init__(self):
        """gui"""
        self.temp_frame = Frame(padx=10 , pady=10)
        self.temp_frame.grid(row=0, column=0)

        self.temp_heading = Label(self.temp_frame,
                                  text = "Temperature converter",
                                  font=("arial", 16, "bold"),
                                  )
        self.temp_heading.grid(row=0)
        instructions = ("please enter a temperature below "
                        "then choose the unit to convert to by selecting the corresponding button")
        self.temp_instructions = Label(self.temp_frame,
                                       text = instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)
        self.temp_entry = Entry(self.temp_frame,
                                font=("arial", 14))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a valid temperature"
        self.temp_error = Label(self.temp_frame,text = error,fg="#9C0000")
        self.temp_error.grid(row=3)
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        for item in buttons:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF")

        self.to_celsius_button = Button(self.button_frame,
                                        text="to Celsius",
                                        bg="#990099",
                                        font=("Arial", 12, "bold"), width=12)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="to Celsius",
                                        bg="#990099",
                                        font=("Arial", 12, "bold"), width=12)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame,
                                           text="to Fahrenheit",
                                           bg="#990099",
                                           fg="#ffffff",
                                           font=("Arial", 12, "bold"), width=12)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help/info",
                                     bg="#CC6600",
                                     fg="#ffffff",
                                     font=("Arial", 12, "bold"), width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
                                        text="History/ Export",
                                        bg="#004C99",
                                        fg="#ffffff",
                                        font=("Arial", 12, "bold"), width=12)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)


#main code
if __name__ == '__main__':
    root = Tk()
    root.title("Temprature Converter")
    Converter()
    root.mainloop()