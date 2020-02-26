from Tkinter import *
import MySQLdb as mdb
import thread
import sys
import pyttsx
import Tkinter as tk
import ttk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from functools import partial

global entUsername,entPassword,lblUsername,lblPassword,stat


con = mdb.connect('localhost', 'chetan1', 'chetankj123', 'useridpassword');

class _PopupKeyboard(Toplevel):
    
    def __init__(self, parent, attach, x, y, keycolor, keysize=5):
        Toplevel.__init__(self, takefocus=0)
        
        self.attributes('-alpha',0.85)

        self.parent = parent
        self.attach = attach
        self.keysize = keysize
        self.keycolor = keycolor
        self.x = 0
        self.y = 270

        self.row1 = Frame(self)
        self.row2 = Frame(self)
        self.row3 = Frame(self)
        self.row4 = Frame(self)

        self.row1.grid(row=1)
        self.row2.grid(row=2)
        self.row3.grid(row=3)
        self.row4.grid(row=4)
        
        self._init_keys()

        # destroy _PopupKeyboard on keyboard interrupt
        self.bind('<Key>', lambda e: self._destroy_popup())

        # resize to fit keys
        self.update_idletasks()
        self.geometry('{}x{}+{}+{}'.format(self.winfo_width(),
                                           self.winfo_height(),
                                           self.x,self.y))
        
    def _init_keys(self):
        self.alpha = {
            'row1' : ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            'row2' : ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l'],
            'row3' : ['m','n', 'o', 'p', 'q', 'r', 's', 't','u','v','w','x'],
            'row4' : ['y','[ space ]','z']
            }
        
        for row in self.alpha.iterkeys(): # iterate over dictionary of rows
            if row == 'row1':             # TO-DO: re-write this method
                i = 1                     # for readability and functionality
                for k in self.alpha[row]:
                    Button(self.row1,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            elif row == 'row2':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row2,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            elif row == 'row3':
                i = 2
                for k in self.alpha[row]:
                    Button(self.row3,
                           text=k,
                           width=self.keysize,
                           bg=self.keycolor,
                           command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1
            else:
                i = 3
                for k in self.alpha[row]:
                    if k == '[ space ]':
                        Button(self.row4,
                               text=k,
                               width=self.keysize * 3,
                               bg=self.keycolor,
                               command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    else:
                        Button(self.row4,
                               text=k,
                               width=self.keysize,
                               bg=self.keycolor,
                               command=lambda k=k: self._attach_key_press(k)).grid(row=0,column=i)
                    i += 1

    def _destroy_popup(self):
        self.destroy()

    def _attach_key_press(self, k):
        if k == '>>>':
            self.attach.tk_focusNext().focus_set()
            self.destroy()
        elif k == '<<<':
            self.attach.tk_focusPrev().focus_set()
            self.destroy()
        elif k == '[1,2,3]':
            pass
        elif k == '[ space ]':
            self.attach.insert(END, ' ')
        else:
            self.attach.insert(END, k)


class SampleApp(tk.Tk):
   
    def __init__(self, keysize=5, keycolor='gray', *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        global entUsername,entPassword,lblUsername,lblPassword,stat

        self.state = 'idle'

        self.keysize = keysize
        self.keycolor = keycolor

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
        
        lblInst = tk.Label(self, text="PLEASE LOGIN FOR FIRST USE", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 14))
        lblInst.place(relx=0.52, rely=0.12, anchor="c")
        
        lblUsername = tk.Label(self, text="   Username :", fg="#383a39", bg="#a1dbcd")
        lblUsername.place(relx=0.08, rely=0.35, anchor="c")
        
        lblPassword = tk.Label(self, text="    Password  :", fg="#383a39", bg="#a1dbcd")
        lblPassword.place(relx=0.08, rely=0.45, anchor="c")

        entUsername = tk.Entry(self)
        entUsername.place(relx=0.25, rely=0.35, anchor="c")
        
        entPassword = tk.Entry(self)
        entPassword.place(relx=0.25, rely=0.45, anchor="c")

        self.binding_user()
        self.binding_pwd()

        self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 12),text="OK", command = self.OnChildEnter)
        self.wButton.place(relx=0.5, rely=0.4, anchor="c")
        self.wButton.config(width="3",height="2")

        self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 10),text="Password Change", command = self.OnChildClose)
        self.wButton.place(relx=0.9, rely=0.25, anchor="c")
        self.wButton.config(width="13",height="2")

        self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 10),text="BACK", command = self.OnChildBack)
        self.wButton.place(relx=0.9, rely=0.4, anchor="c")
        self.wButton.config(width="13",height="2")

        stat = tk.Label(self, text="", font=("Helvetica", 1))
        stat.place(relx=0.52, rely=0.25, anchor="c")


    def binding_user(self):
        global entUsername,entPassword,lblUsername,lblPassword,stat
        
        entUsername.bind('<FocusIn>', lambda e: self._check_state1('focusin'))
        entUsername.bind('<FocusOut>', lambda e: self._check_state1('focusout'))
        entUsername.bind('<Key>', lambda e: self._check_state1('keypress'))


    def binding_pwd(self):
        global entUsername,entPassword,lblUsername,lblPassword,stat
        
        entPassword.bind('<FocusIn>', lambda e: self._check_state2('focusin'))
        entPassword.bind('<FocusOut>', lambda e: self._check_state2('focusout'))
        entPassword.bind('<Key>', lambda e: self._check_state2('keypress'))


    def _check_state1(self, event):
        '''finite state machine'''
        if self.state == 'idle':
            if event == 'focusin':
                self._call_popup1()
                self.state = 'virtualkeyboard'
        elif self.state == 'virtualkeyboard':
            if event == 'focusin':
                self._destroy_popup()
                self.state = 'typing'
            elif event == 'keypress':
                self._destroy_popup()
                self.state = 'typing'
        elif self.state == 'typing':
            if event == 'focusout':
                self.state = 'idle'
        
    def _call_popup1(self):
        self.kb = _PopupKeyboard(attach=entUsername,
                                 parent=self.tk,
                                 x=entUsername.winfo_rootx(),
                                 y=entUsername.winfo_rooty() + entUsername.winfo_reqheight(),
                                 keysize=self.keysize,
                                 keycolor=self.keycolor)

    def _check_state2(self, event):
        '''finite state machine'''
        if self.state == 'idle':
            if event == 'focusin':
                self._call_popup2()
                self.state = 'virtualkeyboard'
        elif self.state == 'virtualkeyboard':
            if event == 'focusin':
                self._destroy_popup()
                self.state = 'typing'
            elif event == 'keypress':
                self._destroy_popup()
                self.state = 'typing'
        elif self.state == 'typing':
            if event == 'focusout':
                self.state = 'idle'
        
    def _call_popup2(self):
        self.kb = _PopupKeyboard(attach=entPassword,
                                 parent=self.tk,
                                 x=entPassword.winfo_rootx(),
                                 y=entPassword.winfo_rooty() + entPassword.winfo_reqheight(),
                                 keysize=self.keysize,
                                 keycolor=self.keycolor)

    def _destroy_popup(self):
        self.kb._destroy_popup()

    def OnChildClose(self):
        global entUsername,entPassword,lblUsername,lblPassword,stat
        stat.destroy()
        lblPassword.destroy()
        entPassword.destroy()

        lblUsername = tk.Label(self, text="Old Password:", fg="#383a39", bg="#a1dbcd")
        lblUsername.place(relx=0.08, rely=0.35, anchor="c")

        entUsername = tk.Entry(self)
        entUsername.place(relx=0.25, rely=0.35, anchor="c")

        self.binding_user()
        
        self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 12),text="OK", command = self.OnChildChange1)
        self.wButton.place(relx=0.5, rely=0.4, anchor="c")
        self.wButton.config(width="3",height="2")          

    def OnChildChange1(self):
        global entUsername,entPassword,lblUsername,lblPassword,stat
        stat.destroy()
        entPassword.destroy()
        entPassword.destroy()
        oldpassword = entUsername.get()
        
        if len(oldpassword) > 0:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM UserPwd")

                for i in range(cur.rowcount):
                    row = cur.fetchone()

                if oldpassword in row[2]:
                    print oldpassword

                    lblPassword = tk.Label(self, text="New Password:", fg="#383a39", bg="#a1dbcd")
                    lblPassword.place(relx=0.08, rely=0.45, anchor="c")

                    entPassword = tk.Entry(self)
                    entPassword.place(relx=0.25, rely=0.45, anchor="c")
                    self.binding_pwd()

                    self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 12),text="OK", command = self.OnChildChange2)
                    self.wButton.place(relx=0.5, rely=0.4, anchor="c")
                    self.wButton.config(width="3",height="2")

                else:
                    stat = tk.Label(self, text="Please Enter Valid Password", font=("Helvetica", 12))
                    stat.place(relx=0.52, rely=0.25, anchor="c")

        else:
            stat = tk.Label(self, text="Please Enter Valid Password", font=("Helvetica", 12))
            stat.place(relx=0.52, rely=0.25, anchor="c")
                        

    def OnChildChange2(self):
        global entUsername,entPassword,lblUsername,lblPassword,stat
        stat.destroy()
        newpassword = entPassword.get()

        if len(newpassword) > 0:
            lblPassword.destroy()
            entPassword.destroy()
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM UserPwd")

                cur.execute("UPDATE UserPwd SET user_pwd=%s WHERE Id=1", (newpassword))
                con.commit()

                cur.execute("SELECT * FROM UserPwd")

                for i in range(cur.rowcount):
                    row = cur.fetchone()
                    print row

                stat = tk.Label(self, text="   New Password Updated   ", font=("Helvetica", 12))
                stat.place(relx=0.52, rely=0.25, anchor="c")

                lblUsername = tk.Label(self, text="   Username :", fg="#383a39", bg="#a1dbcd")
                lblUsername.place(relx=0.08, rely=0.35, anchor="c")

                entUsername = tk.Entry(self)
                entUsername.place(relx=0.25, rely=0.35, anchor="c")

                lblPassword = tk.Label(self, text="    Password  :", fg="#383a39", bg="#a1dbcd")
                lblPassword.place(relx=0.08, rely=0.45, anchor="c")

                entPassword = tk.Entry(self)
                entPassword.place(relx=0.25, rely=0.45, anchor="c")

                self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 12),text="OK", command = self.OnChildEnter)
                self.wButton.place(relx=0.5, rely=0.4, anchor="c")
                self.wButton.config(width="3",height="2")

                self.binding_user()
                self.binding_pwd()

        else:
            stat = tk.Label(self, text="Please Enter Valid Charcter", font=("Helvetica", 12))
            stat.place(relx=0.52, rely=0.25, anchor="c")

    def OnChildBack(self):
        global entUsername,entPassword,lblUsername,lblPassword,stat

        stat.destroy()
        #self._destroy_popup()

        lblUsername = tk.Label(self, text="   Username :", fg="#383a39", bg="#a1dbcd")
        lblUsername.place(relx=0.08, rely=0.35, anchor="c")

        entUsername = tk.Entry(self)
        entUsername.place(relx=0.25, rely=0.35, anchor="c")

        lblPassword = tk.Label(self, text="    Password  :", fg="#383a39", bg="#a1dbcd")
        lblPassword.place(relx=0.08, rely=0.45, anchor="c")

        entPassword = tk.Entry(self)
        entPassword.place(relx=0.25, rely=0.45, anchor="c")

        self.binding_user()
        self.binding_pwd()

        self.wButton = tk.Button(self, background="Grey",foreground="white",font=("default", 12),text="OK", command = self.OnChildEnter)
        self.wButton.place(relx=0.5, rely=0.4, anchor="c")
        self.wButton.config(width="3",height="2")
           

    def OnChildEnter(self):
        global entUsername,entPassword,lblUsername,lblPassword,stat
        stat.destroy()
        username = entUsername.get()
        password = entPassword.get()

        if len(username)>0:
            if len(password)>0:
                with con:
                    cur = con.cursor()
                    cur.execute("SELECT * FROM UserPwd")

                    for i in range(cur.rowcount):
                        row = cur.fetchone()
                        print row

                    if username in row[1]:
                        if password in row[2]:
                            print username,password
                            self.destroy()

                        else:
                            stat = tk.Label(self, text="Not valid 'UserName' or 'Password'", font=("Helvetica", 12))
                            stat.place(relx=0.52, rely=0.25, anchor="c")

                    else:
                        stat = tk.Label(self, text="Not valid 'UserName' or 'Password'", font=("Helvetica", 12))
                        stat.place(relx=0.52, rely=0.25, anchor="c")

            else:
                stat = tk.Label(self, text="Not valid 'UserName' or 'Password'", font=("Helvetica", 12))
                stat.place(relx=0.52, rely=0.25, anchor="c")
        else:
            stat = tk.Label(self, text="Not valid 'UserName' or 'Password'", font=("Helvetica", 12))
            stat.place(relx=0.52, rely=0.25, anchor="c")    
        
app = SampleApp()
app.mainloop()
