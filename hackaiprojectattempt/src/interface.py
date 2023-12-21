import customtkinter as ctk
from agents import Val2, Val1, infoVal, tick, AllAgents
from apiCall import readVals
import threading
import time
#window
root = ctk.CTk()
root.geometry("800x800")
root.resizable(False, False)
root.title("Currency Converter")

#variables



cur_keys= readVals().keys()

#functions
# def leftChoose(choice):
#     print(f"Choice1 is {choice}")
#     global Val1
#     Val1 == str(choice)

# def rightChoose(choice):
#     print(f"Choice2 is {choice}")
#     global Val2
#     Val2 == str(choice)
def rightChoose(_):
    pass
def leftChoose(_):
    pass
def setVals():
    global Val1, Val2, cur_keys
    if Val1=="":
        Val1=None
    if Val2=="":
        Val2=None
    Val1= str(comboBox1.get())
    Val2= str(comboBox2.get())
    if Val1!=None and Val1 not in cur_keys:
        print("Val1 is invalid, ignoring")
        Val1=None
    if Val2!=None and Val2 not in cur_keys:
        print("Val2 is invalid, ignoring.")
        Val2=None
    print(f"Val1: {Val1}, Val2: {Val2}")

def Update():
    global tick, infoVal
    if tick==3:
        textbox.configure(state='enabled')
        textbox.delete("0.0", "end")
        if type(infoVal) == int:
            textbox.insert("0.0", f"1 {Val1} = {infoVal:.6g} {Val2}")
        elif type(infoVal)==dict:
            if(len(infoVal)==0):
                pass  #Empty vals
            else:
                for i in infoVal.keys():
                    textbox.insert("end", f"1 {Val1} = {infoVal[i]:.6g} {i}\n")
        textbox.configure(state='disabled')
        tick=0



        pass
    else:
        time.sleep(0.5)
#widgets
    
comboBox1 = ctk.CTkComboBox(master=root, width=150, height=50, values=[str(f) for f in range(1, 50)], command=leftChoose,corner_radius=15)
comboBox1.place(x=220, y=50)
comboBox2 = ctk.CTkComboBox(master=root, width=150, height=50, values=[str(f) for f in range(1, 50)], command=rightChoose, corner_radius=15)
comboBox2.place(x=430, y=50)
enterValBut = ctk.CTkButton(master=root, width = 60, height=50, corner_radius=10, text="Submit", command= setVals)
enterValBut.place(x=600, y=50)
frame = ctk.CTkFrame(master=root, width = 500, height= 500, corner_radius=10)
frame.place(x=150, y=150)
textbox = ctk.CTkTextbox(master=frame, height=500, width=500, border_spacing=100, state='disabled')
textbox.pack()


# textbox.insert("0.0", "new txsxnnqkxsmx njkelms.,xm csndewjlsext to insertell\n\n\n\n\n\n\n\n\n H")  # insert at line 0 character 0
# text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the en
# textbox.delete("0.0", "end")  # delete all text
# textbox.configure(text_color="#999999")  # configure textbox to be read-only\
# textbox.pack()



#run
if __name__=='__main__':
    t1 =threading.Thread(target=Update, daemon=True)
    t1.start()
    
    root.mainloop()