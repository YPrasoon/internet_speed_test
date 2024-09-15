# Internet speed test

from tkinter import *
import speedtest

def speedcheck(secure = True):
    label_d.config(text = "downloading speed..")
    sp = speedtest.Speedtest()
    sp.get_servers()
    
    down = str(round(sp.download() / 1000000, 3)) + " Mbps"

    label_u.config(text = "uploading speed...")
    upload = str(round(sp.upload() / 1000000, 3)) + " Mbps"
    
    label_down.config(text= down)
    lab_upload.config(text= upload)

sp = Tk()
sp.title ("internet speed test")
sp.geometry("490x550")
sp.config(bg="Grey")

label = Label(sp, text="Internet Speed Test", font =("Ariel",30, "bold"),bg ="Grey")
label.place(x=40, y=40,height = 50, width = 380)

label_d = Label(sp, text="Downloading speed", font =("Ariel",30, "bold"),bg ="Grey")
label_d.place(x=40, y=140,height = 50, width = 380)

label_down = Label(sp, text="000", font =("Ariel",30, "bold"),bg ="Grey")
label_down.place(x=40, y=190,height = 50, width = 380)

label_u = Label(sp, text="Uploading Speed", font =("Ariel",30, "bold"),bg ="Grey")
label_u.place(x=40, y=270,height = 50, width = 380)

lab_upload = Label(sp, text="000", font =("Ariel",30, "bold"),bg ="Grey")
lab_upload.place(x=40, y=320,height = 50, width = 380)

button = Button(sp,text = "Check Speed", font =("Ariel",30, "bold"),bg ="Green",relief = RAISED,command = speedcheck)
button.place(x=40, y= 440,height= 50, width= 380)


sp.mainloop()