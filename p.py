from tkinter import *
class student:
    def __init__(self, master):
        
        frame.geometry("500x700")
        frame.title('Student Data Retrive ©.All rights reserved')
        Label(frame, text='>').grid(row=0,column=0)
        self.entry=StringVar()
        Entry(frame,textvariable=self.entry).grid(row=0,column=1)
        self.enter=Button(frame, text='Enter',command=self.send).grid(row=1,column=0)
        self.close=Button(frame, text='Close',command=frame.destroy).grid(row=2,column=1)
   


    def send(self):
        print("HIIII")
        print(self.entry.get())
        

frame=Tk()
student(frame)
frame.mainloop()


