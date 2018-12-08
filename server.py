from tkinter import *
import mysql.connector
from openpyxl import Workbook
db = mysql.connector.connect( user='root',password='root',host='127.0.0.1',  database='data')
cur = db.cursor()

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
        q=self.entry.get()
        qrf=response(q)
        print(qrf)    



    def response(qr):
        r1= {
        'add new col to table': insert_col,
        'add new student': add_student,
        'add new info of student':update_info,
        'add new table':new_table,
        'get': getinfo,
        'delete':delete,
        }
        a=r1[qr]
        return a()
    
    def insert_col():
        newcol=input("Enter new col name")
        data_type=input("numbers or strings")
        if (data_type=='number'):
            SQL ="ALTER table info add %s double" %(newcol)
        else:
            SQL ="ALTER table info add %s varchar(20)" %(newcol)    
            cur.execute(SQL)
        db.commit()
        print("Created!!!!")    

    def add_student():
        new_student=input("Enter Student name")
        new_id=input("Enter ID")
        SQL ="INSERT INTO info(id,name) values(%s,'%s')" %(new_id,new_student) # to insert into only "name" wala column
        cur.execute(SQL)
        db.commit()

    def update_info():
        update_name=input("Enter Student name to update ")
        update_col=input("Enter col to update ")
        update=input("Enter update value ")
        if (isinstance(update_col, str)):
            SQL ="UPDATE INFO set %s='%s' WHERE name='%s'" %(update_col,update,update_name)
        else:
            SQL ="UPDATE INFO set %s=%s WHERE name='%s'" %(update_col,update,update_name)
        cur.execute(SQL)
        db.commit()

    def new_table():
        new_table=input("Enter table name ")
        SQL ="CREATE TABLE %s (No INT)" %new_table
        cur.execute(SQL)
        db.commit()

    def getinfo():
        print("Enter getcol and uname")
        getcol= input()
        uname= input()
        print(getcol,uname)
        SQL ="SELECT %s FROM info WHERE name='%s'" %(getcol,uname)
        cur.execute(SQL)
        result=cur.fetchall()
        #for x in result:
        print("{} of {} {} :".format(getcol,uname,result))

    def delete():
        return "You are in delete function"


        
frame=Tk()
student(frame)
frame.mainloop()


