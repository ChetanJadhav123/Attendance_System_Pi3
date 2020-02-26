import thread
import sys
import pyttsx
import Tkinter as tk
#import please_wait
import ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def taxt2speech(threadName, data):

    engine = pyttsx.init()
    engine.setProperty('rate', 125)
    str = data
    if len(sys.argv) > 1:
        str = sys.argv[1]

    engine.say(str)
    engine.runAndWait()
    
class SampleApp(tk.Tk):
   
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #self.overrideredirect(1)        
        image = Image.open("LOGO.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self,image=photo)
        label.image = photo # keep a reference!
        label.place(relx=0.1, rely=0.1, anchor="c")

        image1 = Image.open("BORDER.png")
        photo1 = ImageTk.PhotoImage(image1)
        label = tk.Label(self,image=photo1)
        label.image1 = photo1 # keep a reference!
        label.place(relx=0.5, rely=0.95, anchor="c")

        label1 = tk.Label(font=("default", 8),text="Copyright 2016 V V Technologies | All Rights Reserved")
        label1.config(background="white", foreground="black")
        label1.place(relx=0.56, rely=0.98, anchor="c")
        
        self.geometry("800x479")
        self.config(background="white")
        
        lblInst = tk.Label(self, text="PLEASE CONFIGURE YOUR DEVICE FOR FIRST USE", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 14))
        lblInst.place(relx=0.55, rely=0.2, anchor="c")
        
        lblInst = tk.Label(self, text="CLICK 'START' BUTTON", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 14))
        lblInst.place(relx=0.55, rely=0.3, anchor="c")
        
        self.button = tk.Button(background="black",foreground="white",font=("default", 12),text="START", command=self.start)
        self.button.place(relx=0.52, rely=0.55, anchor="c")
        self.button.config(width="10",height="2",bg="grey")
        
        s = ttk.Style()
        s.theme_use('alt')
        s.configure("pink.Horizontal.TProgressbar", foreground='pink', background='pink')
        self.progress = ttk.Progressbar(self, style="pink.Horizontal.TProgressbar",
                                        orient="horizontal",
                                        length=650, mode="determinate")

        self.progress.place(relx=0.53, rely=0.42, anchor="c")

        self.bytes = 0
        self.maxbytes = 0

    def start(self):
        self.button.config(state='disabled')
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()

        self.initialize1()

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 500
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)

        if self.bytes == self.maxbytes:
            self.initialize()

    def initialize(self):
        self.geometry("800x479")
        self.config(background="white")

        lblInst = tk.Label(self, text="YOUR SYSTEM IS READY TO USE", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 14))
        lblInst.place(relx=0.5, rely=0.7, anchor="c")
 
        lblInst = tk.Label(self, text="CLICK 'OK' to Continue.....!!", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 14))
        lblInst.place(relx=0.52, rely=0.8, anchor="c")
        
        #lblUsername = tk.Label(self, text="Username:", fg="#383a39", bg="#a1dbcd")
        #entUsername = tk.Entry(self)
        #and pack them into the window
        #lblUsername.pack()
        #entUsername.pack()

        #create the widgets for entering a username
        #lblPassword = tk.Label(self, text="Password:", fg="#383a39", bg="#a1dbcd")
        #entPassword = tk.Entry(self)
        #and pack them into to the window
        #lblPassword.pack()
        #entPassword.pack()
        
        self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 12),text="OK", command = self.OnChildClose)
        self.wButton.place(relx=0.9, rely=0.7, anchor="c")
        self.wButton.config(width="10",height="5")
     
    def initialize1(self):
        self.geometry("800x479")
        self.config(background="white")
                
        self.button = tk.Button(background="black",foreground="white",font=("default", 12),text="Please Wait..!!")
        self.button.place(relx=0.52, rely=0.55, anchor="c")
        self.button.config(width="10",height="2",bg="grey")
        self.button.config(state='disabled')
                
    def OnChildClose(self):
        self.destroy()
        
app = SampleApp()
app.mainloop()
