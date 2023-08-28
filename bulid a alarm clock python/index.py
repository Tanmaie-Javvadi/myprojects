from tkinter.ttk import*
from tkinter import*
from PIL import ImageTk,Image
bgcolor='#F0F8FF'
color1="#566FC6"
#window
window=Tk()
window.title("alarm clock")
window.geometry('350x150')
window.configure(bg=bgcolor)
#frames
frame_item=Frame(window, width=350,height=5,bg=color1)
frame_item.grid(row=0,column=0)

frame_body=Frame(window, width=350,height=200,bg=bgcolor)
frame_item.grid(row=1,column=0)
#configuring frame body
def Labels():
    pic=PhotoImage(file="icon.png")
    frame_body_k=Label(image=pic,bg="#F0F8FF")
    frame_body_k.place(x=10,y=20)
Labels()
img=Image.open("icon.png")
img.resize((100,100))
img=ImageTk.PhotoImage(img)

appImage=Label(frame_body,height=100,image=img)
appImage.place(x=10,y=10)

title=Label(frame_body,text="Alarm",height=1,font=('Ivy 18 bold'))
title.place(x=125,y=10)

hour=Label(frame_body,text="Alarm",height=1,font=('Ivy 10 bold'))
hour.place(x=127,y=10)

window.mainloop()