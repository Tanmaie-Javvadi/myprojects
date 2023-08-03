from twilio.rest import Client as twilio_client
#import twilio.rest as Client
import random
from tkinter import*
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super(otp_verifier,self).__init__()
        self.geometry("500x450")
        self.configure(bg="#FFFFFF")
        self.resizable(False,False)
        self.n=""
        self.twilio_client=twilio_client("ACfe3e27bad88af002454c5ef4a9b68300","95d95369ba31e555c710d2f95c52e13b")
        
    def OTP(self):
        self.n=str(random.randrange(1000,10000))
        #self.client=twilio_client("ACfe3e27bad88af002454c5ef4a9b68300","95d95369ba31e555c710d2f95c52e13b"),
        self.twilio_client.messages.create(to="+91-xxxxxxxxxx",
                                    from_="+xxxxxxxxx",
                                    body=self.n)
        
        return self.n
    def Labels(self):
        self.c=Canvas(self,bg="#808080",width=300,height=280)
        self.c.place(x=100,y=50)
        
        self.upper_frame=Frame(self,bg="#F0F8FF",width=500,height=100)
        self.upper_frame.place(x=0,y=0)
        
        self.pic=PhotoImage(file="otp.png")
        self.k=Label(self.upper_frame,image=self.pic,bg="#F0F8FF").place(x=75,y=10)
        
        self.j=Label(self.upper_frame,text="OTP VERIFICATION",font="TimesNewRoman 20 bold",bg="#F0F8FF",fg="black").place(x=180,y=30)
        
    def Entry(self):
        self.username=Text(self,font="calibri 16",borderwidth=2,wrap=WORD,width=20,height=1)
        self.username.place(x=140,y=140)
        
    def Buttons(self):
       self.submit=PhotoImage(file="submit.png")
       self.submitbutton=Button(self,image=self.submit,border=0,bg="#808080",command=self.checkOTP)
       self.submitbutton.place(x=160,y=220)
       
       self.resend=PhotoImage(file="resend.png")
       self.resendbutton=Button(self,image=self.resend,border=0,bg="white",command=self.resendOTP)
       self.resendbutton.place(x=205,y=360)
       
    def resendOTP(self):
        self.n=str(self.OTP())
        self.client=twilio_client("ACfe3e27bad88af002454c5ef4a9b68300","95d95369ba31e555c710d2f95c52e13b")
        self.client.messages.create(to=("+919392135462"),
                                    from_="+16413816146",
                                    body=self.n
                                    )
    def checkOTP(self):
        try:
            self.userInput=int(self.username.get(1.0,"end -1c"))
            if self.userInput == int(self.n):
                messagebox.showinfo("showinfo","Verification Successful")
                self.n="done"
            else:
                messagebox.showinfo("showinfo","wrong OTP")
        except:
            messagebox.showinfo("showinfo","INVALID OTP")
            
                             
if __name__ == "__main__":
    window=otp_verifier()
    window.OTP()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()
