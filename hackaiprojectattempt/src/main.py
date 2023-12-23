from interface import root, Update
import threading
from agents import AllAgents

if __name__=='__main__':
    t1 =threading.Thread(target=Update, daemon=True)
    t1.start()
    t2 = threading.Thread(target=AllAgents.run, daemon=True)
    t2.start()

    root.mainloop()