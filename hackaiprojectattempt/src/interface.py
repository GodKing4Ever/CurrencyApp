import customtkinter as ctk
#window
root = ctk.CTk()
root.geometry("800x800")
root.resizable(False, False)
root.title("Currency Converter")

#variables
Val1 = ""
Val2 = ""


#functions
def leftChoose(choice):
    print(f"Choice1 is {choice}")

def rightChoose(choice):
    print(f"Choice2 is {choice}")


#widgets
    
comboBox1 = ctk.CTkComboBox(master=root, width=150, height=50, values=[str(f) for f in range(5)], command=leftChoose)
comboBox1.place(x=220, y=50)
comboBox2 = ctk.CTkComboBox(master=root, width=150, height=50, values=[str(f) for f in range(5)], command=rightChoose)
comboBox2.place(x=430, y =50)


#run
root.mainloop()