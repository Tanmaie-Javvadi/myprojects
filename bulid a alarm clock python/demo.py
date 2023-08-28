from pygame import mixer
from tkinter.ttk import*
from datetime import datetime
from tkinter import*
from time import sleep
from threading import Thread
window=Tk()
window.title(" ")
window.geometry('350x150')
window.configure(bg="#F0F8FF")
def Labels():
        upper_frame=Frame(bg="#566FC6",width=350,height=5)
        upper_frame.place(x=0,y=0)
        
        pic=PhotoImage(file="icon.png")
        k=Label(k,image=pic,bg="#F0F8FF").place(x=10,y=20)
        j=Label(j,text="Alarm",bg="#F0F8FF",height=1,font="Ivy 18 bold").place(x=100,y=10)
        i=Label(window,text="hour",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold")
        i.place(x=105,y=40)
        o=Label(window,text="min",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold").place(x=150,y=40)
        s=Label(window,text="sec",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold").place(x=200,y=40)
        p=Label(window,text="period",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold").place(x=240,y=40)
def activate_alarm():
        t=Thread(target=alarm)
        t.start()
def deactivate_alarm():
        print('Deactivated alarm',Tk.selected.get())
        mixer.music.stop
def Combobox(Tk):
        i=Combobox(i,width=2,font="arial 15",values=["00","01","02","03","04","05","06","07","08","09","10","11","12"]).place(x=105,y=60)
        o=Combobox(o,width=2,font="arial 15",values=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","51","52","53","54","55","56","57","58","59"]).place(x=150,y=60)
        s=Combobox(s,width=2,font="arial 15",values=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","51","52","53","54","55","56","57","58","59"]).place(x=195,y=60)
        p=Combobox(p,width=2,font="arial 15",values=["AM","PM"]).place(x=240,y=60)
def Radiobutton():
        selected=IntVar()
        rad1=Radiobutton(rad1,font="arial 10 bold",value=1,text="Activate",bg="#F0F8FF",command=activate_alarm,variable=selected).place(x=100,y=95)
def sound_alarm():
    mixer.music.load('alarm.wav')
    mixer.music.play()
    rad2=Radiobutton(font="arial 10 bold",value=2,text="Deactivate",bg="#F0F8FF",command=deactivate_alarm,variable=selected).place(x=150,y=95)
def alarm(Tk):
    while True:
        control=1
        print(control)
        alarm_hour=i.get()
        alarm_min=o.get()
        alarm_sec=s.get()
        alarm_period=p.get()
        alarm_period=str(alarm_period).upper
        now= datetime.now()
        hour =now.strftime("%I")
        min=now.strftime("%M")
        sec=now.strftime("%S")
        period=now.strftime("%p")
        if control==1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_min==min:
                        if alarm_sec==sec:
                            print("Time to take a break")
                            sound_alarm()
        sleep(1)
        
mixer.init()
alarm(Tk)
    
window.mainloop()

    