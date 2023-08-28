from tkinter.ttk import*
from tkinter import*
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread
class alarm(Tk):
    def __init__(self):
        super(alarm,self).__init__()
        self.geometry("300x150")
        self.configure(bg="#F0F8FF")
        self.resizable(False,False)
    def Labels(self):
        #self.geometry('300x130')
        #self.configure(bg="#F0F8FF")
        self.upper_frame=Frame(self,bg="#566FC6",width=350,height=5)
        self.upper_frame.place(x=0,y=0)
        
        self.pic=PhotoImage(file="icon.png")
        self.k=Label(self,image=self.pic,bg="#F0F8FF").place(x=10,y=20)
        self.j=Label(self,text="Alarm",bg="#F0F8FF",height=1,font="Ivy 18 bold").place(x=100,y=10)
        self.i_c=Label(self,text="hour",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold").place(x=105,y=40)
        self.o_c=Label(self,text="min",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold").place(x=150,y=40)
        self.s_c=Label(self,text="sec",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold").place(x=200,y=40)
        self.p_c=Label(self,text="period",bg="#F0F8FF",fg="#566FC6",height=1,font="Ivy 10 bold").place(x=240,y=40)
    def activate_alarm(self):
        self.t=Thread(target=self.alarm_second)
        self.t.start()
    def deactivate_alarm(self):
        print('Deactivated alarm',self.selected.get())
        mixer.music.stop()
    def Combobox(self):
        self.combo_hour=Combobox(self,width=2,font="arial 15",values=["00","01","02","03","04","05","06","07","08","09","10","11","12"])
        self.combo_hour.place(x=105,y=60)
        self.combo_min=Combobox(self,width=2,font="arial 15",values=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"])
        self.combo_min.place(x=150,y=60)
        self.combo_sec=Combobox(self,width=2,font="arial 15",values=["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"])
        self.combo_sec.place(x=195,y=60)
        self.combo_period=Combobox(self,width=2,font="arial 15",values=["AM","PM"])
        self.combo_period.place(x=240,y=60)
    def Radiobutton(self):
        self.selected=IntVar()
        self.rad1=Radiobutton(self,font="arial 10 bold",value=0,text="Activate",bg="#F0F8FF",command=self.activate_alarm,variable=self.selected).place(x=100,y=95)
        self.rad2=Radiobutton(self,font="arial 10 bold",value=1,text="Deactivate",bg="#F0F8FF",command=self.deactivate_alarm,variable=self.selected).place(x=170,y=95)
    def sound_alarm(self):
        mixer.music.load('alarm.wav')
        mixer.music.play()
        self.rad2=Radiobutton(self,font="arial 10 bold",value=0,text="Deactivate",bg="#F0F8FF",command=self.deactivate_alarm,variable=self.selected).place(x=170,y=95)
    def alarm_second(self):
        while True:
            control=self.selected.get()
            print(control)
            self.alarm_hour= self.combo_hour.get()
            self.alarm_min=self.combo_min.get()
            self.alarm_sec=self.combo_sec.get()
            self.alarm_period=self.combo_period.get()
            self.alarm_period=str(self.alarm_period).upper()
            now= datetime.now()
            self.hour =now.strftime("%I")
            self.min=now.strftime("%M")
            self.sec=now.strftime("%S")
            self.period=now.strftime("%p")
            
            if control==1 :
                if self.alarm_period==self.period:
                    if self.alarm_hour==self.hour:
                        if self.alarm_min==self.min:
                            if self.alarm_sec==self.sec:
                                print("Time to take a break")
                                sleep(5)
                                self.sound_alarm()
   
sleep(1)
mixer.init()

if __name__ == "__main__":
    
    
    window=alarm()
    window.Labels()
    window.Combobox()
    window.Radiobutton()
    window.mainloop()