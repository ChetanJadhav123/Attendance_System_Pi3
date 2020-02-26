import os
import MySQLdb as mdb
import time
import ttk
from PIL import ImageTk, Image
import sys
import Tkinter as tk
import subprocess

import MySQLdb as mdb
import xlsxwriter

global admin_menu,admin_menu_dummy,admin_window,admin_label
global result_btn,run_voting,yr1,yr2,yr3,yr4,back,ok
global result,voting
result=0

global con
con = mdb.connect('localhost', 'chetankj', 'chetankj123', 'AttendanceSystem');

class adminMyOptionMenu(tk.OptionMenu):
        def __init__(self, master, status, *options):
                self.var = tk.StringVar(master)
                self.var.set(status)
                tk.OptionMenu.__init__(self, master, self.var, *options)
                self.config(font=('calibri', (10)), bg='white', width=12, fg='dark red')
                self['menu'].config(font=('calibri', (10)), bg='white', fg='dark blue')

        def settings(self):
                global result
                global admin_menu,admin_menu_dummy,admin_window,admin_label
                global result_btn,run_voting,yr1,yr2,yr3,yr4,back,ok

                if result == 0:
                        import a
                        a.run_cloud_sys()
                        result = 1

                elif result == 1:
                        result = 0
                        self.master.destroy()

        def System_run(self):
                global result,voting
                global admin_menu,admin_menu_dummy,admin_window,admin_label
                global result_btn,run_voting,yr1,yr2,yr3,yr4,back,ok

                result_btn.config(state='disabled')
                
                admin_label = tk.Label(admin_window,background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                                       fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

                admin_label = tk.Label(admin_window,background="white",text='Click/Choose YEAR button', font=('calibri', (14)),
                                       fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")


                yr1.config(state='active')
                yr2.config(state='active')
                yr3.config(state='active')
                yr4.config(state='active')

        def first_year(self):
                global con
                with con:
                        cur = con.cursor()
                        cur.execute("SELECT * FROM first_year_db")
                        workbook = xlsxwriter.Workbook('First_Year.xlsx')
                        sheet = workbook.add_worksheet()
                        for r, row in enumerate(cur.fetchall()):
                                for c, col in enumerate(row):
                                        sheet.write(r, c, col)

                        workbook.close()
                        print 'First Year Report Generated'
                
                
        def second_year(self):
                global con
                with con:
                        cur = con.cursor()
                        cur.execute("SELECT * FROM second_year_db")
                        workbook = xlsxwriter.Workbook('Second_Year.xlsx')
                        sheet = workbook.add_worksheet()
                        for r, row in enumerate(cur.fetchall()):
                                for c, col in enumerate(row):
                                        sheet.write(r, c, col)

                        workbook.close()
                        print 'Second Year Report Generated'
                
                
        def third_year(self):
                global con
                with con:
                        cur = con.cursor()
                        cur.execute("SELECT * FROM third_year_db")
                        workbook = xlsxwriter.Workbook('Third_Year.xlsx')
                        sheet = workbook.add_worksheet()
                        for r, row in enumerate(cur.fetchall()):
                                for c, col in enumerate(row):
                                        sheet.write(r, c, col)

                        workbook.close()
                        print 'Third Year Report Generated'
                
                
        def fourth_year(self):
                global con
                with con:
                        cur = con.cursor()
                        cur.execute("SELECT * FROM fourth_year_db")
                        workbook = xlsxwriter.Workbook('Fourth_Year.xlsx')
                        sheet = workbook.add_worksheet()
                        for r, row in enumerate(cur.fetchall()):
                                for c, col in enumerate(row):
                                        sheet.write(r, c, col)

                        workbook.close()
                        print 'Fourth Year Report Generated'


def run_admin_page():
        global result,voting
        global admin_menu,admin_menu_dummy,admin_window,admin_label
        global result_btn,run_voting,yr1,yr2,yr3,yr4,back,ok
        result=voting=0

        admin_window = tk.Toplevel()
        admin_window.geometry('800x479')
        admin_window.config(background="white")
        admin_window.wm_title("Admin System")
        admin_window.columnconfigure(0, weight=1)
        admin_window.columnconfigure(1, weight=1)

        admin_logo_image = Image.open("LOGO.png")
        admin_logo_photo = ImageTk.PhotoImage(admin_logo_image)
        admin_label = tk.Label(admin_window,image=admin_logo_photo)
        admin_label.admin_logo_image = admin_logo_photo
        admin_label.place(relx=0.1, rely=0.08, anchor="c")

        admin_border_image1 = Image.open("BORDER.png")
        admin_border_photo1 = ImageTk.PhotoImage(admin_border_image1)
        admin_label = tk.Label(admin_window,image=admin_border_photo1)
        admin_label.admin_border_image1 = admin_border_photo1 # keep a reference!
        admin_label.place(relx=0.5, rely=0.95, anchor="c")

        mainlabel = tk.Label(admin_window,background="white",text='SMART VOTING SYSTEM-Admin System', font=('calibri', (14)),
                             fg='dark blue').place(relx=0.5, rely=0.1, anchor="c")


        admin_label = tk.Label(admin_window,background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        admin_label = tk.Label(admin_window,background="white",text='your status is here', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        admin_menu = adminMyOptionMenu(admin_window, 'Select Option', '')

        result_btn = tk.Button(admin_window, text="GENERATE REPORT", fg='blue',
                               command=admin_menu.System_run)
        result_btn.config(bg="light grey",width="15",height="2")
        result_btn.place(relx=0.4, rely=0.4, anchor="c")

        yr1 = tk.Button(admin_window, text="FIRST YEAR", fg='blue',command=admin_menu.first_year)
        yr1.config(bg="light grey",width="10",height="1")
        yr1.place(relx=0.2, rely=0.615, anchor="c")
        yr1.config(state='disabled')

        yr2 = tk.Button(admin_window, text="SECOND YEAR", fg='blue',command=admin_menu.second_year)
        yr2.config(bg="light grey",width="10",height="1")
        yr2.place(relx=0.4, rely=0.615, anchor="c")
        yr2.config(state='disabled')

        yr3 = tk.Button(admin_window, text="THIRD YEAR", fg='blue',command=admin_menu.third_year)
        yr3.config(bg="light grey",width="10",height="1")
        yr3.place(relx=0.6, rely=0.615, anchor="c")
        yr3.config(state='disabled')

        yr4 = tk.Button(admin_window, text="FOURTH YEAR", fg='blue',command=admin_menu.fourth_year)
        yr4.config(bg="light grey",width="10",height="1")
        yr4.place(relx=0.8, rely=0.615, anchor="c")
        yr4.config(state='disabled')

        back=tk.Button(admin_window,text="BACK",command=admin_menu.settings)
        back.place(relx=0.9, rely=0.4, anchor="c")
        back.config(width="10",height="5")


        


