#import userpwd
#import Progress
#import delete,download,enroll,search
import socket
import os
import serial
import threading
import MySQLdb as mdb
import RPi.GPIO as GPIO
import time
import ttk
from PIL import ImageTk, Image
import sys
import Tkinter as tk
import subprocess

import MySQLdb as mdb

global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
global ok,download,enroll,delete,attendance,x,er,reset,process,finish
global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
global image,photo,label,image1,photo1,label1,mainlabel,run,setting
global d_f,e_f,l_f,mainlabe3,mainlabe4
global msg,s_loc,l_loc,faculty,student
global label5,label6,label7
global att_s,yr_f,yr_label

att_s=0

faculty=student=0
d_f=e_f=l_f=0
download=enroll=delete=attendance=0

class MyOptionMenu(tk.OptionMenu):
    def __init__(self, master, status, *options):
        self.var = tk.StringVar(master)
        self.var.set(status)
        tk.OptionMenu.__init__(self, master, self.var, *options)
        self.config(
            font=('calibri', (10)), bg='white', width=12, fg='dark red')
        self['menu'].config(font=('calibri', (10)), bg='white', fg='dark blue')


    def callback1(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
        global ok,download,enroll,delete,attendance,x,er,reset,process,finish
        global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
        
        val1 = '{}.py'.format(self.var.get())
        #print(val1)

        if 'Select-Option.py' in val1:
            print(val1)
            download=0
            b1_1.config(state='active')
            mymenu1.config(state='active')
            #mymenu8.destroy()
            #mainlabe2.remove()
            mainlabe2 = tk.Label(background="white",text='PLEASE SELECT OPTION', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        if 'ENROLL-LECTURER.py' in val1:
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            mainlabe2 = tk.Label(background="white",text='Your Selected ENROLL-LECTURER | click OK to Process', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            download=1
            print(val1)
            b1_1.config(state='disabled')
            mymenu1.config(state='disabled')
            ok.config(state='active')

    def callback2(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
        global ok,download,enroll,delete,attendance,x,er,reset,process,finish
        global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
        
        val1 = '{}.py'.format(self.var.get())
        
        if 'Select-Option.py' in val1:
            print(val1)
            enroll=0
            b2_2.config(state='active')
            mymenu1.config(state='active')
            mainlabe2 = tk.Label(background="white",text='PLEASE SELECT OPTION', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        if 'ENROLL-STUDENT.py' in val1:
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            mainlabe2 = tk.Label(background="white",text='Your Selected ENROLL-STUDENT | click OK to Process', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            print(val1)
            enroll=1
            b2_2.config(state='disabled')
            mymenu1.config(state='disabled')
            ok.config(state='active')

    def callback3(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
        global ok,download,enroll,delete,attendance,x,er,reset,process,finish
        global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
        
        val1 = '{}.py'.format(self.var.get())
        #print(val1)

        if 'Select-Option.py' in val1:
            print(val1)
            delete=0
            b3_3.config(state='active')
            mymenu1.config(state='active')
            mainlabe2 = tk.Label(background="white",text='PLEASE SELECT OPTION', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        if 'DELETE-DB.py' in val1:
            mainlabe2 = tk.Label(background="white",text='               '+'                                                                                                                                                                   ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            mainlabe2 = tk.Label(background="white",text='Your Selected DELETE DB-STUDENT/LECTURER | click OK to Process', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            print(val1)
            delete=1
            b3_3.config(state='disabled')
            mymenu1.config(state='disabled')
            ok.config(state='active')

    def callback4(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
        global ok,download,enroll,delete,attendance,x,er,reset,process,finish
        global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
        
        val1 = '{}.py'.format(self.var.get())
        #print(val1)

        if 'Select-Option.py' in val1:
            print(val1)
            attendance=0
            b4_4.config(state='active')
            mymenu1.config(state='active')
            mainlabe2 = tk.Label(background="white",text='PLEASE SELECT OPTION', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        if 'STUDENT-ATTENDANCE.py' in val1:
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            mainlabe2 = tk.Label(background="white",text='Your Selected STUDENT-ATTENDANCE/LECTURER | click OK to Process', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            print(val1)
            attendance=1
            b4_4.config(state='disabled')
            mymenu1.config(state='disabled')
            ok.config(state='active')
            
    def settings(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
        global ok,download,enroll,delete,attendance,x,er,reset,process,finish
        global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
       
        funtion_run()
        download=enroll=delete=attendance=0
        d_f=0
        #b1_1.config(state='active')
        #b2_2.config(state='active')
        #b3_3.config(state='active')
        #b4_4.config(state='active')
        #mymenu1.config(state='active')
        
    def System_run(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
        global ok,download,enroll,delete,attendance,x,er,reset,process,finish
        global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label

        val_s = '{}.py'.format(self.var.get())

        mymenu1.config(state='disabled')
        ok.config(state='disabled')

        if 'GENERATE-REPORT.py' in val_s:
            import report_generate
            report_generate.run_admin_page()
            
        elif download==1:
            self.enroll_lecturer_finger()
                    
        elif enroll==1:
            self.enroll_student_finger()
            
        elif delete==1:
            self.delete_reg_finger()
            
        elif attendance==1:
            self.student_attendace_system()

        elif d_f==1:
            import delete
            import data_base_update
            
            x = field1.get()
            print x
            d_f=0
            c=delete.delete_template_finger_image(x)
            mainlabe2 = tk.Label(background="white",text=c+'Click BACK to Continue', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

            data_base_update.delete_faculty_db(x)
            data_base_update.delete_firstyear_db(x)
            data_base_update.delete_secondyear_db(x)
            data_base_update.delete_thirdyear_db(x)
            data_base_update.delete_fourthyear_db(x)

        elif faculty==1:
            import data_base_update
            
            reset.config(state='active')
            namef=field1.get()
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

            mainlabe2 = tk.Label(background="white",text='Database Updated!'+'Your Finger Id:'+str(l_loc)+' | '+'Your Name:'+namef, font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

            data_base_update.update_faculty_db(l_loc,namef)
            
            
        elif student==1:
            import data_base_update
            
            reset.config(state='active')
            names=field1.get()
            yr = field2.get()
            usn = field3.get()

            if '1' in yr:
                data_base_update.update_firstyear_db(s_loc,names,yr,usn)

            elif '2' in yr:
                data_base_update.update_secondyear_db(s_loc,names,yr,usn)

            elif '3' in yr:
                data_base_update.update_thirdyear_db(s_loc,names,yr,usn)

            elif '4' in yr:
                data_base_update.update_fourthyear_db(s_loc,names,yr,usn)

            mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                                 fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

            mainlabe2 = tk.Label(background="white",text='DB Updated!!'+'Finger Id:'+str(s_loc)+'|'+'Name:'+names+'|'+'Year:'+str(yr)+'|'+'USN:'+usn, font=('calibri', (14)),
                                 fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
                              
        else:
            download=enroll=delete=attendance=0
            d_f=e_f=l_f=0

    def delete_reg_finger(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,process,finish
        global ok,download,enroll,delete,attendance,x,er,reset
        global mymenu1,mymenu9,mainlabe2,nextb,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
        download=enroll=delete=attendance=0
        d_f=e_f=0

        nextb.config(state='active')
        self.destroy_label_buttons()
        mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        label5 =tk.Label(text="Enter Student finger ID to DELETE:")
        label5.place(relx=0.15, rely=0.68, anchor="c")
        label5.config(background="white", foreground="black")

        field1 = tk.Entry(Dragonfly,width=8)
        field1.place(relx=0.35, rely=0.68, anchor="c")

        #if d_f==1:
        nextb.config(state='disabled')
        ok.config(state='active')
        d_f=1
        mainlabe2 = tk.Label(background="white",text='Enter Student finger ID to DELETE and click OK', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

    def enroll_lecturer_finger(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,process,finish
        global ok,download,enroll,delete,attendance,x,er,reset
        global mymenu1,mymenu9,mainlabe2,nextb,label5,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
        d_f=e_f=l_f=0

        #import enroll

        nextb.config(state='disabled')
        ok.config(state='disabled')
        reset.config(state='active')

        self.destroy_label_buttons()
        label5 =tk.Label(text="Full Name:")
        label5.place(relx=0.05, rely=0.68, anchor="c")
        label5.config(background="white", foreground="black")
        field1 = tk.Entry(Dragonfly,width=12)
        field1.place(relx=0.16, rely=0.68, anchor="c")
        
        download=enroll=delete=attendance=0

        mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        mainlabe2 = tk.Label(background="white",text='Keep finger on reader, fill blank field, click NEXT to process, click OK to finish', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        nextb.config(state='active')
        l_f=1


    def enroll_student_finger(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,process,finish
        global ok,download,enroll,delete,attendance,x,er,reset
        global mymenu1,mymenu9,mainlabe2,nextb,label5,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,s_loc,l_loc,faculty,student
        global label5,label6,label7,mainlabe3,mainlabe4
        global att_s,yr_f,yr_label
        d_f=e_f=0

        #import enroll

        nextb.config(state='disabled')
        ok.config(state='disabled')
        reset.config(state='active')

        self.destroy_label_buttons()
        label5 =tk.Label(text="Full Name:")
        label5.place(relx=0.05, rely=0.68, anchor="c")
        label5.config(background="white", foreground="black")
        field1 = tk.Entry(Dragonfly,width=12)
        field1.place(relx=0.16, rely=0.68, anchor="c")

        label6 =tk.Label(text="Year:")
        label6.place(relx=0.3, rely=0.68, anchor="c")
        label6.config(background="white", foreground="black")
        field2 = tk.Entry(Dragonfly,width=6)
        field2.place(relx=0.375, rely=0.68, anchor="c")

        label7 =tk.Label(text="USN:")
        label7.place(relx=0.48, rely=0.68, anchor="c")
        label7.config(background="white", foreground="black")
        field3 = tk.Entry(Dragonfly,width=12)
        field3.place(relx=0.6, rely=0.68, anchor="c")
        
        download=enroll=delete=attendance=0
        d_f=0

        mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        mainlabe2 = tk.Label(background="white",text='Keep finger on reader, fill blank field, click NEXT to process, click OK to finish', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

        nextb.config(state='active')
        e_f=1

    def Next_Process(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,process,finish
        global ok,download,enroll,delete,attendance,x,er,reset
        global mymenu1,mymenu9,mainlabe2,nextb,label5,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,mainlabe3,mainlabe4
        global msg,s_loc,l_loc,faculty,student
        global label5,label6,label7
        global att_s,yr_f,yr_label

        faculty=student=0

        import enroll

        if e_f==1:            
            nextb.config(state='disabled')
            ok.config(state='active')
            msg=enroll.Enroll_New_Finger()
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            mainlabe2 = tk.Label(background="white",text=msg, font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

            if 'Template already exists' in msg:
                nextb.config(state='disabled')
                ok.config(state='disabled')
                reset.config(state='active')

            s_loc = msg[44:47]

            print s_loc
                
            #s_loc=int(dat)
            student=1
            #print s_loc
            

        elif l_f==1:            
            nextb.config(state='disabled')
            ok.config(state='active')
            msg=enroll.Enroll_New_Finger()
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
            mainlabe2 = tk.Label(background="white",text=msg, font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

            if 'Template already exists' in msg:
                nextb.config(state='disabled')
                ok.config(state='disabled')
                reset.config(state='active')

            #l_loc = '%03d'%int(msg[44])
            l_loc = msg[44:47]

            print l_loc
            
            #l_loc= int(dat)
            faculty=1
            #print l_loc

        else:
            d_f=e_f=l_f=0
            faculty=student=0


    def destroy_label_buttons(self):
        mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")
        
        label5 =tk.Label(text="                                                          ")
        label5.place(relx=0.15, rely=0.68, anchor="c")
        label5.config(background="white", foreground="black")

        label6 =tk.Label(text="                    ")
        label6.place(relx=0.3, rely=0.68, anchor="c")
        label6.config(background="white", foreground="black")

        label7 =tk.Label(text="                     ")
        label7.place(relx=0.48, rely=0.68, anchor="c")
        label7.config(background="white", foreground="black")

        field1.destroy()
        field2.destroy()
        field3.destroy()


    def student_attendace_system(self):
        global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,process,finish
        global ok,download,enroll,delete,attendance,x,er,reset
        global mymenu1,mymenu9,mainlabe2,nextb,label5,field1,field2,field3
        global image,photo,label,image1,photo1,label1,mainlabel,run,setting
        global d_f,e_f,l_f,mainlabe3,mainlabe4
        global msg,s_loc,l_loc,faculty,student
        global label5,label6,label7
        global att_s,yr_f,yr_label
        
        self.destroy_label_buttons()
        b1_1.destroy()
        b2_2.destroy()
        b3_3.destroy()
        b4_4.destroy()

        mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

        mainlabe2 = tk.Label(background="white",text='Before click "PROCESS" button please keep your registered finger on reader to mark attendance......', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

        mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

        mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

        nextb.config(state='disabled')
        ok.config(state='disabled')
        reset.config(state='disabled')

        process = tk.Button(Dragonfly, text="Process", fg='blue',command=self.process_attendance)
        process.config(bg="light grey",width="15",height="2")
        process.place(relx=0.2, rely=0.4, anchor="c")

        yr_f = tk.Entry(Dragonfly,width=12)
        yr_f.place(relx=0.3, rely=0.55, anchor="c")

        yr_label = tk.Label(background="white",text='YEAR:', font=('calibri', (10)),
                            fg='dark blue').place(relx=0.2, rely=0.55, anchor="c")

        finish = tk.Button(Dragonfly, text="FINISH", fg='blue',command=self.finish_attendance)
        finish.config(bg="light grey",width="15",height="2")
        finish.place(relx=0.5, rely=0.4, anchor="c")

        finish.config(state='disabled')

    def process_attendance(self):
        global att_s,yr_f,yr_label
        import process_att
        import search
        import data_base_update

        y_d = yr_f.get()

        msg=search.Attendance_Mark()
        print msg

        dat = str(msg[28:31])

        print dat

        if 'Found template at position' in msg:
            if att_s==0:
                att_s=1
                msg1,msg2,msg3,msg4,msg5=data_base_update.get_attendance(0,y_d,str(msg[28:31]))

                mainlabe2 = tk.Label(background="white",text='                                                                                                                                                                      ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                mainlabe2 = tk.Label(background="white",text='Attendance Marked by-'+msg1+'  '+msg2+'  '+msg3+'  '+msg4+'  '+msg5, font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

                mainlabe4 = tk.Label(background="white",text='Keep next person registered finger to mark attendance then click "PROCESS" button', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

                mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                finish.config(state='active')

                if 'no_db' in msg1:
                    reset.config(state='disabled')
                    mainlabe2 = tk.Label(background="white",text='                                                                                                                                                             ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                    mainlabe2 = tk.Label(background="white",text='Please keep faculty finger to start attendacne system, click PROCESS', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                    mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

                    mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                    mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                    att_s=0

            elif att_s==1:
                att_s=1
                msg1,msg2,msg3,msg4,msg5=data_base_update.get_attendance(1,y_d,str(msg[28:31]))

                mainlabe2 = tk.Label(background="white",text='                                                                                                                                                                     ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                mainlabe2 = tk.Label(background="white",text='Attendance Marked by-'+msg1+'  '+msg2+'  '+msg3+'  '+msg4+'  '+msg5, font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

                mainlabe4 = tk.Label(background="white",text='Keep next person registered finger to mark attendance then click "PROCESS" button', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

                mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                if 'no_db' in msg1:
                    reset.config(state='disabled')
                    mainlabe2 = tk.Label(background="white",text='                                                                                                                                                                ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                    mainlabe2 = tk.Label(background="white",text='Please keep student finger to mark attendacne and click PROCESS', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                    mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

                    mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                    mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                finish.config(state='active')

        elif 'No match found' in msg:
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                                                    ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

            mainlabe2 = tk.Label(background="white",text=msg+'Try again', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

            mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

            mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

            mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

    def finish_attendance(self):
        global att_s,yr_f,yr_label
        import process_att
        import search
        import data_base_update

        process.config(state='disabled')

        y_d = yr_f.get()

        msg=search.Attendance_Mark()

        dat = msg[28:31]

        print dat

        if 'Found template at position' in msg:
            msg1=data_base_update.get_attendance(0,y_d,msg[28:31])

            mainlabe2 = tk.Label(background="white",text='                                                                                                                                                              ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

            mainlabe2 = tk.Label(background="white",text='Updating Attendance Sheet please wait...!', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

            mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

            mainlabe4 = tk.Label(background="white",text='Attendance DB updated Sucessfully,... Thank you', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

            mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

            mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking FINISH please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

            if 'no_db' in msg1:
                process.config(state='active')
                reset.config(state='disabled')
                mainlabe2 = tk.Label(background="white",text='                                                                                                                                                           ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                mainlabe2 = tk.Label(background="white",text='Please keep faculty registered finger to finish todays attendacne system', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

                mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

                mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

                mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

            else:
                reset.config(state='active')

        elif 'No match found' in msg:
            mainlabe2 = tk.Label(background="white",text='                                                                                                                                                           ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

            mainlabe2 = tk.Label(background="white",text=msg+'Try again', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

            mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

            mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")

            mainlabe3 = tk.Label(background="white",text='"FINISH" button should click by faculty to complete todays attendance process, before clicking finish please keep registered finger on reader', font=('calibri', (7)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")
       

def funtion_run():
    global b1_1,b2_2,b3_3,b4_4,b5_5,b6_6,b7_7,b8_8,Dragonfly
    global ok,download,enroll,delete,attendance,x,er,reset,process,finish
    global mymenu1,mymenu9,mainlabe2,nextb,label5,field1,field2,field3
    global image,photo,label,image1,photo1,label1,mainlabel,run,setting
    global d_f,e_f,l_f,s_loc,l_loc,faculty,student
    global label5,label6,label7,mainlabe3,mainlabe4
    global att_s,yr_f,yr_label
    att_s=0

    p1=p2=p3=p4=p5=p6=p7=p8=0

    mymenu1 = MyOptionMenu(Dragonfly, 'Select-Option','ENROLL-LECTURER','ENROLL-STUDENT','DELETE-DB','STUDENT-ATTENDANCE','GENERATE-REPORT')
    mymenu1.config(background="white",bg="white",width="20",height="1")
    mymenu1.place(relx=0.5, rely=0.25, anchor="c")

    mainlabe2 = tk.Label(background="white",text='                                                                                                                                                                      ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.7, anchor="c")

    mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.77, anchor="c")

    mainlabe3 = tk.Label(background="white",text='                                                                                                                                                                                                               ', font=('calibri', (8)),
                         fg='dark blue').place(relx=0.5, rely=0.85, anchor="c")
    
    mainlabe3 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

    mainlabe4 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

    mainlabe2 = tk.Label(background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

    mainlabe2 = tk.Label(background="white",text='your status is here', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.8, anchor="c")

    
    mymenu9 = MyOptionMenu(Dragonfly, 'Select Option', '')
    
    b1_1 = tk.Button(Dragonfly, text="ENROLL LECTURER", fg='blue',command=mymenu1.callback1)
    b1_1.config(bg="light grey",width="15",height="2")
    b1_1.place(relx=0.2, rely=0.4, anchor="c")

    b2_2 = tk.Button(Dragonfly, text="ENROLL STUDENT", fg='blue',command=mymenu1.callback2)
    b2_2.config(bg="light grey",width="15",height="2")
    b2_2.place(relx=0.5, rely=0.4, anchor="c")

    b3_3 = tk.Button(Dragonfly, text="DELETE LECTURER/STUDENT", fg='blue',command=mymenu1.callback3)
    b3_3.config(bg="light grey",width="20",height="2")
    b3_3.place(relx=0.5, rely=0.55, anchor="c")

    b4_4 = tk.Button(Dragonfly, text="STUDENT ATTENDANCE", fg='blue',command=mymenu1.callback4)
    b4_4.config(bg="light grey",width="20",height="2")
    b4_4.place(relx=0.2, rely=0.55, anchor="c")

    reset=tk.Button(Dragonfly,text="BACK",command=mymenu9.settings)
    reset.place(relx=0.9, rely=0.4, anchor="c")
    reset.config(width="10",height="5")

    ok=tk.Button(Dragonfly,text="OK",command=mymenu1.System_run)
    ok.place(relx=0.73, rely=0.4, anchor="c")
    ok.config(state='active',width="10",height="5")

    nextb=tk.Button(Dragonfly,text="NEXT",command=mymenu9.Next_Process)
    nextb.place(relx=0.83, rely=0.6, anchor="c")
    nextb.config(state='disabled',width="10",height="2")

    label5 =tk.Label(text="                                                          ")
    label5.place(relx=0.15, rely=0.68, anchor="c")
    label5.config(background="white", foreground="black")

    label6 =tk.Label(text="                    ")
    label6.place(relx=0.3, rely=0.68, anchor="c")
    label6.config(background="white", foreground="black")

    label7 =tk.Label(text="                     ")
    label7.place(relx=0.48, rely=0.68, anchor="c")
    label7.config(background="white", foreground="black")

    yr_label =tk.Label(text="ccc")
    yr_label.place(relx=0.48, rely=0.68, anchor="c")
    yr_label.config(background="white", foreground="black")

    process = tk.Button(Dragonfly, text="Process", fg='blue',command=mymenu1.callback1)
    process.config(bg="light grey",width="15",height="2")
    process.place(relx=0.2, rely=0.4, anchor="c")

    finish = tk.Button(Dragonfly, text="FINISH", fg='blue',command=mymenu1.callback2)
    finish.config(bg="light grey",width="15",height="2")
    finish.place(relx=0.5, rely=0.4, anchor="c")
    
    yr_label.destroy()

    field1.destroy()
    field2.destroy()
    field3.destroy()
    process.destroy()
    finish.destroy()
    yr_f.destroy()
    
Dragonfly = tk.Tk()
Dragonfly.geometry('800x479')
Dragonfly.config(background="white")
Dragonfly.title('V V Technologies, Tumkur')
Dragonfly.columnconfigure(0, weight=1)
Dragonfly.columnconfigure(1, weight=1)

#Dragonfly.overrideredirect(1)
label5 =tk.Label(text="Full Name:")
label5.place(relx=0.05, rely=0.68, anchor="c")
label5.config(background="white", foreground="black")
        
field1 = tk.Entry(Dragonfly,width=12)
field1.place(relx=0.16, rely=0.68, anchor="c")

label6 =tk.Label(text="Semester:")
label6.place(relx=0.3, rely=0.68, anchor="c")
label6.config(background="white", foreground="black")
        
field2 = tk.Entry(Dragonfly,width=6)
field2.place(relx=0.375, rely=0.68, anchor="c")

label7 =tk.Label(text="Subject Name:")
label7.place(relx=0.48, rely=0.68, anchor="c")
label7.config(background="white", foreground="black")
        
field3 = tk.Entry(Dragonfly,width=12)
field3.place(relx=0.6, rely=0.68, anchor="c")

yr_f = tk.Entry(Dragonfly,width=12)
yr_f.place(relx=0.6, rely=0.68, anchor="c")

image = Image.open("LOGO.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(Dragonfly,image=photo)
label.image = photo # keep a reference!
label.place(relx=0.1, rely=0.08, anchor="c")

image1 = Image.open("BORDER.png")
photo1 = ImageTk.PhotoImage(image1)
label = tk.Label(Dragonfly,image=photo1)
label.image1 = photo1 # keep a reference!
label.place(relx=0.5, rely=0.95, anchor="c")

label1 = tk.Label(font=("default", 8),text="Copyright 2016 V V Technologies | All Rights Reserved")
label1.config(background="white", foreground="black")
label1.place(relx=0.56, rely=0.98, anchor="c")

mainlabel = tk.Label(background="white",text='SMART ATTENDANCE SYSTEM', font=('calibri', (14)),
                  fg='dark blue').place(relx=0.5, rely=0.1, anchor="c")
funtion_run()

#main()

Dragonfly.mainloop()


