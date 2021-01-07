from pypresence import Presence
import time
sny = time.time()
client_id = '791911792019898388'
RPC = Presence(client_id,pipe=0)
RPC.connect()
RPC.update(details="Ayarlanmamış")
#######################################
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.save = tk.Button(self)
        self.save["text"] = "Güncelle"
        self.save["command"] = self.tst
        self.save.pack(side="bottom")
        self.ust = tk.Entry()
        self.alt = tk.Entry()
        self.ust.pack(side="left")
        self.alt.pack(side="right")
        self.ustcontent = tk.StringVar()
        self.altcontent = tk.StringVar()
        self.ust["textvariable"] = self.ustcontent
        self.alt["textvariable"] = self.altcontent
    def tst(self):
        ust=self.ustcontent.get()
        alt=self.altcontent.get()
        print(alt)
        print(ust)
        if alt:
            print(RPC.update(details=ust, state=alt, start=sny))
        else:
            print(RPC.update(details=ust, start=sny))



root = tk.Tk()
app = Application(master=root)
app.master.title("Discord Rich Presence")
app.master.maxsize(300, 300)
app.mainloop()