import customtkinter as ctk
from agents import AllAgents, changeVar, getClock, getInfoVal
from apiCall import readVals
import threading
import time
#window
root = ctk.CTk()
root.geometry("800x800")
root.resizable(False, False)
root.title("Currency Converter")

#variables
V1 = None
V2 = None
clock = 0


cur_keys= list(readVals().keys())

#functions
def changeClock(a):
    global clock
    clock = a
# def leftChoose(choice):
#     print(f"Choice1 is {choice}")
#     global V1
#     V1 == str(choice)

# def rightChoose(choice):
#     print(f"Choice2 is {choice}")
#     global V2
#     V2 == str(choice)
def rightChoose(_):
    pass
def leftChoose(_):
    pass
def setVals():
    global V1, V2, cur_keys
    if V1=="":
        V1=None
    if V2=="":
        V2=None
    V1= str(comboBox1.get())
    V2= str(comboBox2.get())
    if V1!=None and V1 not in cur_keys:
        print("V1 is invalid, ignoring")
        V1=None
    if V2!=None and V2 not in cur_keys:
        print("V2 is invalid, ignoring.")
        V2=None
    # print(f"V1: {V1}, V2: {V2}")

def Update():
    global clock, infoVal
    while(True):
        clock = getClock()
        # print(clock)
        if clock==1:
            infoVal = getInfoVal()
            print(infoVal, type(infoVal))
            textbox.configure(state='normal')
            textbox.delete("0.0", "end")
            if type(infoVal) != dict:
                textbox.insert("end", f"   1 {V1} = {str(infoVal)} {V2}")
            elif type(infoVal)==dict:
                if(len(infoVal)==0):
                    pass  #Empty vals
                else:
                    for i in infoVal.keys():
                        textbox.insert("end", f"   1 {V1 or V2} = {infoVal[i]:.6g} {i}\n")
            textbox.configure(state='disabled')
            clock=0



            pass
        else:
            changeVar(V1, V2)
            time.sleep(0.5)
#widgets
    
comboBox1 = ctk.CTkComboBox(master=root, width=150, height=50, values=cur_keys, command=leftChoose,corner_radius=15)
comboBox1.place(x=220, y=50)
comboBox2 = ctk.CTkComboBox(master=root, width=150, height=50, values=cur_keys, command=rightChoose, corner_radius=15)
comboBox2.place(x=430, y=50)
enterValBut = ctk.CTkButton(master=root, width = 60, height=50, corner_radius=10, text="Submit", command= setVals)
enterValBut.place(x=600, y=50)
frame = ctk.CTkFrame(master=root, width = 500, height= 500, corner_radius=10)
frame.place(x=150, y=150)
textbox = ctk.CTkTextbox(master=frame, height=500, width=200, border_spacing=10, state='disabled')
textbox.place(x= 150, y=50)


# textbox.insert("0.0", "new txsxnnqkxsmx njkelms.,xm csndewjlsext to insertell\n\n\n\n\n\n\n\n\n H")  # insert at line 0 character 0
# text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the en
# textbox.delete("0.0", "end")  # delete all text
# textbox.configure(text_color="#999999")  # configure textbox to be read-only\
# textbox.pack()



#run
if __name__=='__main__':
    t1 =threading.Thread(target=Update, daemon=True)
    t1.start()
    t2 = threading.Thread(target=AllAgents.run, daemon=True)
    t2.start()

    root.mainloop()