
#description
#input
#output  -#9C0000
#990099  degrees/farenhight #009900
#CC6600  help and history  #004C99

# history and export page last 5 calculations

#return (user_input - 32) * 5 / 9 (celcus)

# ///////////////////////////////////////          IMPORTANT : make a percent file to store the memory cause i can ///////////////////////////////////////////////////////
from tkinter import *
import all_constants as c
import os
import time
history_storage = []
history_temp = []
incorrect_input = 0
if not os.path.exists("{}.txt".format("data")):
    text_file = open("{}.txt".format("data"), "w+")
    history_storage = [""] * 5
    history_temp = [""] * 5
    text = str(history_storage)
    text = text.strip("[]")
    text = "," + text + "="
    open("data.txt", "w+").write(text)
else:
    text_file = open("{}.txt".format("data"), "r")
    data = text_file.read()
    data = data.translate("")
    data = data.replace(" ","")
    ticker = 0
    tempword = ""
    current_item_index = 0
    # runs until the intended end of the file
    while not data[ticker] == "=":
        # breaks up each item
        if data[ticker] == "," and not data[ticker] == "=":
            ticker += 1
            # runs untill the next break
            while not data[ticker] == "," and not data[ticker] == "=":
                # ignores the quotes
                if not data[ticker] == "'":
                    # adds the char to the temp word
                    tempword = tempword + data[ticker]
                ticker += 1
            history_storage.append(tempword)
            history_temp.append(tempword)
            tempword = ""

class Converter():
    """conversion tool"""
    global history_storage, incorrect_input

    def __init__(self):
        """gui"""

        self.temp_frame = Frame(padx=10 , pady=10)
        self.temp_frame.grid(row=0, column=0)

        self.temp_heading = Label(self.temp_frame,
                                  text = "Temperature converter",
                                  font=("arial", 16, "bold"),
                                  )

        self.temp_heading.grid(row=0)
        # headddding
        instructions = ("please enter a temperature below "
                        "then choose the unit to convert to by selecting the corresponding button")
        self.temp_instructions = Label(self.temp_frame,
                                       text = instructions,
                                       wraplength=250, width=40,
                                       justify="left")

        self.temp_instructions.grid(row=1)
        self.temp_entry = Entry(self.temp_frame,
                                font=("arial", 14))
        # instructions
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a valid temperature"
        self.answer_error = Label(self.temp_frame, text = error, fg="#004C99",
                                  font=("Arial", 14, "bold"))
        self.answer_error.grid(row=3)
        # error messages
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
        # button set up
        buttons = [
            ["To celcus", "#990099",lambda: self.check_temp(c.ABS_ZERO_CELSIUS),0,0],
            ["to Farenheight","#009900",lambda: self.check_temp(c.ABS_ZER0_FAHRENHEIT),0,1],
            ["Help/info","#CC6600",lambda: self.help_goto(),1,0],
            ["History/Export","#004C99",lambda: self.history_goto(),1,1]
        ]
        # button attributes
        self.button_ref_list = []
        for item in buttons:
        # creates the buttons
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF",font=("Arial", 12, "bold"),
                                      width=12,command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)
        self.to_history_button = self.button_ref_list[3]
    def check_temp(self, min_temp,valid=False):
        """checks if the temperature is valid and converts it to the selected unit"""
        global incorrect_input
        unit = ["°F","°C"][[-459,-273].index(min_temp)]
        try:
            to_convert = round(float(self.temp_entry.get().strip(unit)))
            # makes the input a float and strips the unit
            if (to_convert >= min_temp):
                error = ""
                valid = True
            else:
                error = f"temperature must be greater than or equal to {min_temp}"
                incorrect_input +=1
        except ValueError:
            error="Please enter a valid temperature"
            incorrect_input +=1

        if error !="":
            self.answer_error.config(text=error,fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            # self.temp_entry.focus_set()
        if valid == True:
            self.answer_error.config(fg="#004C99")
            self.temp_entry.config(bg="#FFFFFF")
            self.temp_entry.delete(0, END)
            output = str(to_convert)+unit+" → "+str(round([(to_convert* 9/5) + 32,(to_convert - 32) * 5/9][[-273,-459].index(min_temp)]+0.1))+["°F","°C"][[-273,-459].index(min_temp)]
            self.answer_error.config(text=output,font=("Arial", 18, "bold"))
            history_temp.pop(-1)
            history_temp.insert(0,output.replace(" ","!"))
            history_storage.insert(0,output.replace(" ","!"))
            text = str(history_temp)
            text = text.strip("[]")
            text = "," + text + "="
            open("data.txt", "w+").write(text)
        if incorrect_input > 2:
            self.help_goto()



            # if else statement in one line (to be cleaned up before final submission dues to inneficency)
            # rounding is fixed through the +0.1
    def history_goto(self):
        self.temp_frame.destroy()
        history()
    def help_goto(self):
        incorrect_input = 0
        self.temp_frame.destroy()
        help()
class history():
    """calculation history"""
    global history_storage, history_temp
    def __init__(self):
        history_text = ""
        ticker = 0
        for item in history_temp:
            history_text += item.replace("!"," ") + f"\n"
            if ticker <= 5:
                history_print = history_text
            ticker += 1
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid(row=0, column=0)

        self.temp_heading = Label(self.temp_frame,
                                  text="Converter history",
                                  font=("arial", 16, "bold"),
                                  )

        self.temp_heading.grid(row=0)
        # headddding
        instructions = ("displays the history of the calculator"
                        f"you are currently displaying {len(history_temp)}/{len(history_storage)} of your past calculations")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")

        self.temp_instructions.grid(row=1)
        self.history_entry = Label(self.temp_frame,
                                   text=history_text,
                                   font=("arial", 10))
        self.history_entry.grid(row=2, padx=10, pady=10)
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
        buttons = [
            ["To calculator", "#990099", lambda: self.back(), 0, 0],
            ["Export to file", "#009900", lambda: self.export(history_print), 0, 1],
        ]
        self.button_ref_list = []
        for item in buttons:
            # creates the buttons
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", 12, "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)
    def export(self,history_text):
        exported = open(os.path.join(os.path.expanduser("~"), "Desktop", f"{time.time()}.txt"),'w')
        exported.write(f"Converter history\n{history_text}")
    def back(self):
        self.temp_frame.destroy()
        Converter()

class help():
    """help help"""
    def __init__(self):
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid(row=0, column=0)

        self.temp_heading = Label(self.temp_frame,
                                  text="Help page",
                                  font=("arial", 16, "bold"),
                                  )

        self.temp_heading.grid(row=0)
        # headddding
        instructions = ("this app lets you easily convert celcus to faringheit and export the history of your "
                        "conversions seamlessly each section details how to preform the actions or what they are but press the corresponding "
                        "button that maches the action you want to take\n\n\n")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)
        self.temp_instructions.grid(row=1)
        buttons = [
            ["To calculator", "#990099", lambda: Converter(), 0, 0],
            ["History/Export", "#009900", lambda: self.history_goto(), 0, 1]
        ]
        # button attributes
        self.button_ref_list = []
        for item in buttons:
            # creates the buttons
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", 12, "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

    def history_goto(self):
        self.temp_frame.destroy()
        history()



# [(to_convert× 9/5) + 32,(to_convert − 32) × 5/9]
#main code
if __name__ == '__main__':
    root = Tk()
    root.title("Temprature Converter")
    Converter()
    root.mainloop()