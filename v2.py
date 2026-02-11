
#description
#input
#output  -#9C0000
#990099  degrees/farenhight #009900
#CC6600  help and history  #004C99

# history and export page last 5 calculations

#return (user_input - 32) * 5 / 9 (celcus)
from tkinter import *
import all_constants as c
import time
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
        self.answer_error = Label(self.temp_frame, text = error, fg="#004C99",
                                  font=("Arial", 14, "bold"))
        self.answer_error.grid(row=3)
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
        buttons = [
            ["To celcus", "#990099",lambda: self.check_temp(c.ABS_ZERO_CELSIUS),0,0],
            ["to Farenheight","#009900",lambda: self.check_temp(c.ABS_ZER0_FAHRENHEIT),0,1],
            ["Help/info","#CC6600","",1,0],
            ["History/Export","#004C99","",1,1]
        ]
        self.button_ref_list = []
        for item in buttons:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF",font=("Arial", 12, "bold"),
                                      width=12,command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)
    def check_temp(self, min_temp,valid=False):
        """checks if the temperature is valid and converts it to the selected unit"""
        try:
            to_convert = float(self.temp_entry.get().strip(["°F","°C"][[-459,-273].index(min_temp)]))
            if (to_convert >= min_temp):
                error = ""
                valid = True
            else:
                error = f"temperature must be greater than or equal to {min_temp}"
        except ValueError:
            error="Please enter a valid temperature"
        if error !="":
            self.answer_error.config(text=error,fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            # self.temp_entry.focus_set()
        if valid == True:
            self.temp_entry.delete(0, END)
            self.answer_error.config(text=str(round([(to_convert* 9/5) + 32,(to_convert - 32) * 5/9][[-273,-459].index(min_temp)]+0.1)),font=("Arial", 18, "bold"))

# [(to_convert× 9/5) + 32,(to_convert − 32) × 5/9]
#main code
if __name__ == '__main__':
    root = Tk()
    root.title("Temprature Converter")
    Converter()
    root.mainloop()