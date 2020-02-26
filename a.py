from dropbox.client import DropboxOAuth2FlowNoRedirect
from dropbox.client import DropboxClient
import time
import threading
import warnings
import datetime
import imutils
import os.path,subprocess
import Tkinter as tk
from tkFileDialog import *
import tkMessageBox
import json
import ttk
from PIL import ImageTk, Image

global client,auth,ok,submit
global ph,te,flow,form_label,cloud_window

def get_otp():
        global client,auth,ok,submit
        global ph,te,flow,form_label,cloud_window
        conf = json.load(open('conf.json'))
        client = None
        secret_code = te.get().strip()

        try:
                (accessToken, userID) = flow.finish(secret_code)
                client = DropboxClient(accessToken)

                form_label = tk.Label(cloud_window,background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                                      fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")
                submit.config(state='active')
                ph.config(state='disabled')
                te.config(state='disabled')
                ok.config(state='disabled')
                form_label = tk.Label(cloud_window,background="white",text='Account Successfully Linked | Click Upload Files to Cloud', font=('calibri', (10)),
                                      fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")
        except:
                form_label = tk.Label(cloud_window,background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                                      fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")
                submit.config(state='disabled')
                form_label = tk.Label(cloud_window,background="white",text='Please Enter Valid Access Code', font=('calibri', (10)),
                                      fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")

def upload_files_cloud():
        global client,auth,ok,submit
        global ph,te,flow,form_label,cloud_window
        
        f1 = open('First_Year.xlsx', 'rb')
        response = client.put_file('/First_Year.xlsx', f1, overwrite=True)

        f2 = open('Second_Year.xlsx', 'rb')
        response = client.put_file('/Second_Year.xlsx', f2, overwrite=True)

        f3 = open('Third_Year.xlsx', 'rb')
        response = client.put_file('/Third_Year.xlsx', f3, overwrite=True)

        f4 = open('Fourth_Year.xlsx', 'rb')
        response = client.put_file('/Fourth_Year.xlsx', f4, overwrite=True)
        
        form_label = tk.Label(cloud_window,background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                              fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")

        submit.config(state='disabled')

        form_label = tk.Label(cloud_window,background="white",text='Files are Uploaded Successfully to Cloud', font=('calibri', (10)),
                              fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")

def authentification():
        global client,auth,ok,submit
        global ph,te,flow,form_label,cloud_window
        conf = json.load(open('conf.json'))
        client = None
        ok.config(state='active')

        if conf["use_dropbox"]:
                # connect to dropbox and start the session authorization process
                flow = DropboxOAuth2FlowNoRedirect(conf["dropbox_key"], conf["dropbox_secret"])
                ph.insert(10,format(flow.start()))

        auth.config(state='disabled')

def destroy_window():
        global client,auth,ok,submit
        global ph,te,flow,form_label,cloud_window

        cloud_window.destroy()


def run_cloud_sys():
        global client,auth,ok,submit
        global ph,te,flow,form_label,cloud_window
        cloud_window = tk.Toplevel()
        cloud_window.geometry('800x479')
        cloud_window.config(background="white")
        cloud_window.wm_title("Cloud Uploading System")
        cloud_window.columnconfigure(0, weight=1)
        cloud_window.columnconfigure(1, weight=1)

        cloud_logo_image = Image.open("LOGO.png")
        cloud_logo_photo = ImageTk.PhotoImage(cloud_logo_image)
        cloud_label = tk.Label(cloud_window,image=cloud_logo_photo)
        cloud_label.cloud_logo_image = cloud_logo_photo
        cloud_label.place(relx=0.1, rely=0.08, anchor="c")

        form_border_image1 = Image.open("BORDER.png")
        form_border_photo1 = ImageTk.PhotoImage(form_border_image1)
        form_label = tk.Label(cloud_window,image=form_border_photo1)
        form_label.form_border_image1 = form_border_photo1 # keep a reference!
        form_label.place(relx=0.5, rely=0.95, anchor="c")

        mainlabel = tk.Label(cloud_window,background="white",text='SMART VOTING SYSTEM-Cloud Uploading', font=('calibri', (14)),
                             fg='dark blue').place(relx=0.5, rely=0.1, anchor="c")


        form_label = tk.Label(cloud_window,background="white",text='                                                                                                                                       ', font=('calibri', (14)),
                         fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")

        form_label = tk.Label(cloud_window,background="white",text='your status is here', font=('calibri', (10)),
                         fg='dark blue').place(relx=0.5, rely=0.68, anchor="c")

        ph =tk.Entry(cloud_window,width=70)
        ph.place(relx=0.5, rely=0.25, anchor="c")
        
        label1 =tk.Label(cloud_window,background="white",text="Generated URL")
        label1.place(relx=0.07, rely=0.25, anchor="c")

        te =tk.Entry(cloud_window,width=50)
        te.place(relx=0.5, rely=0.35, anchor="c")

        label1 =tk.Label(cloud_window,background="white",text="Enter Access code")
        label1.place(relx=0.15, rely=0.35, anchor="c")

        auth=tk.Button(cloud_window,text="Authentify", fg="black",
                     command=authentification, width=25,height=5)
        
        auth.place(relx=0.1, rely=0.8, anchor="c")
        auth.config(state='active',width="10",height="2")

        ok =tk.Button(cloud_window,text="OK", fg="black",
                    command=get_otp, width=5,height=2)
        ok.config(state='disabled')
        ok.place(relx=0.92, rely=0.42, anchor="c")

        back=tk.Button(cloud_window,text="BACK",command=destroy_window)
        back.place(relx=0.6, rely=0.8, anchor="c")
        back.config(width="5",height="2")

        submit=tk.Button(cloud_window,text="UPLOAD",command=upload_files_cloud)
        submit.place(relx=0.4, rely=0.8, anchor="c")
        submit.config(state='disabled',width="5",height="2")


