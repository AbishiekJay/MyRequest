from tkinter import *
"""root = Tk()
# Code to add widgets will go here...
root.title(" MyGUI " )
root.geometry("1080x720")
root._displayof("Test")
root.mainloop()"""

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_window()
    def init_window(self):
        self.master.title("TEST")
        self.pack(fill=BOTH,expand=1)
        quitButton=Button(self,text="quit",command=quit)
        quitButton.place(x=100,y=100)
        var1=IntVar()
        Checkbutton(self,text=" test" ,variable= var1).grid(row=2,sticky=W)
        
root=Tk()
root.geometry("1080x720")
app =Window(root)
root.mainloop()