from Tkinter import *
import sys

class Application(Frame):
    


    def browse(self):
        from tkFileDialog import askopenfilename

        Tk().withdraw() 
        self.filename = askopenfilename()

        
        self.text = Text(root)
        self.text.insert(INSERT, self.filename)
        self.text.pack()


    def pars_name(self):

        x=0
        for i in range(len(self.filename)):
            if self.filename[i] == "/":
                x = i

        return self.filename[x+1:]

        
    def begining(self):

        
        self.text = Text(root)
        self.text.insert(INSERT, self.pars_name())
        self.text.grid(row=12, column=100)


    def open_file(self):
        
        fo = open("myfile1.txt", "wb")

        fo.write('blah')

        fo.close()


    def createWidgets(self):
        self.QUIT = Button(root)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.grid(row=3, column=0)

        
        self.browser = Button(root)
        self.browser["text"] = "Browse"
        self.browser["fg"]   = "red"
        self.browser["command"] =  self.browse
        self.browser.grid(row=0, column=0)

        self.begin = Button(root)
        self.begin["text"] = "Begin"
        self.begin["fg"]   = "red"
        self.begin["command"] = self.begining
        self.begin.grid(row=1, column=0)
        
        self.array = Button(root)
        self.array["text"] = "Open File"
        self.array["fg"]   = "red"
        self.array["command"] = self.open_file
        self.array.grid(row=2, column=0)

        



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()
        self.filename=""
        
    
root = Tk()
app = Application(master=root)
RTitle=root.title("Simsurve")
root.geometry("750x150")
app.mainloop()
root.destroy()