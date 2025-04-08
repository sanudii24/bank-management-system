from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
import mysql.connector


con=mysql.connector.connect(user='root',
                                 password='#Dnyana@25.Fe',
                                 host='localhost',
                                 port=3306)
cur=con.cursor(buffered=True)
try:
    cur.execute("use save1")
except:
     cur.execute("create database save1")
     cur.execute("use save1")

try:
     cur.execute("describe savet1")
except:
     cur.execute('create table savet1(fname varchar(20),mname varchar(20),lname varchar(20),aadhar varchar(20),pan varchar(20),date int,month int,year int)')
 
obj=Tk()
obj.geometry("1000x1000")

obj.config(background="white")

l1=Label(obj,text=" THE BANK OF LATUR",font=("arial",15),background="black")
l1.place(x=30,y=0)
c=Canvas(obj,bg="#FEE0B0",height=200,width=1000)
c.place(x=0,y=50)
l=Label(obj,text="WELCOME to \n ",font=("algerian",20),background="#FEE0B0",foreground="red")
l.place(x=480,y=100)

l1=Label(obj,text=" THE BANK OF LATUR",font=("algerian",40),background="pink",foreground="red")
l1.place(x=280,y=140)

i=PhotoImage(file='path\\hi.png')
c.create_image(0,0,anchor=NW,image=i)



c1=Canvas(obj,bg="white",height=1000,width=1400)
c1.place(x=0,y=300)

i1=PhotoImage(file='path\\download.png')
c1.create_image(0,0,anchor=NW,image=i1)
def n1():
    
   
    
    obj1=Toplevel(obj)
    obj1.geometry("800x560")
    obj1.configure(background="#FDCFFD")
    c1=Canvas(obj1,bg="white",height=306,width=400)
    c1.place(x=395,y=250)

    i1=PhotoImage(file='path\\account.png')
    c1.create_image(0,0,anchor=NW,image=i1)
    
    l=Label(obj1,text="Account Type",font=("algerian",30),fg="#C20202",bg="#FDCFFD")
    l.place(x=50,y=50)
    l=Label(obj1,text="-------------------------------------------------------",font=("broadway",10),fg="green",bg="#FDCFFD")
    l.place(x=45,y=90)
    l=Label(obj1,text="please Specify the type of account you want to open ?",font=("arial",20),fg="black",bg="#FDCFFD")
    l.place(x=50,y=150)
    c1=IntVar()
    d=IntVar()
    #saving account ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
    def n6():
        
        ob=Toplevel(obj1)
        ob.geometry("800x900")
        ob.configure(background="#FAF598")
        l=Label(ob,text="Customer Information",font=("algerian",30),bg="#FAF598",fg="#C20202")
        l.place(x=60,y=50)
        l=Label(ob,text="---------------------------------------------------------------------",font=("broadway",15),fg="green",bg="#FAF598")
        l.place(x=45,y=100)
        l=Label(ob,text=" First Name",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=160)
        l=Label(ob,text=" Middle Name",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=45,y=220)
        l=Label(ob,text=" Last Name",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=280)
        l=Label(ob,text="Aadhar Card No",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=340)
        l=Label(ob,text="PAN Card No",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=400)
        
        l=Label(ob,text="DOB",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=460)
        spin=Spinbox(ob,from_=1,to=31,font=("algerian",15),fg="black",width=5)
        spin.place(x=260,y=460)
        spin1=Spinbox(ob,from_=1,to=12,font=("algerian",15),fg="black",width=5)
        spin1.place(x=360,y=460)
        spin2=Spinbox(ob,from_=2000,to=2022,font=("algerian",15),fg="black",width=5)
        spin2.place(x=460,y=460)        

        e=Entry(ob,text="First Name",font=("arial",20),width=17)
        e1=Entry(ob,text="Middle Name",font=("arial",20),width=17)
        e2=Entry(ob,text="Last Name",font=("arial",20),width=17)
        e3=Entry(ob,font=("arial",20),width=17)
        e4=Entry(ob,font=("arial",20),width=17)
        e.place(x=260,y=160)
        e1.place(x=260,y=220)
        e2.place(x=260,y=280)
        e3.place(x=260,y=340)
        e4.place(x=260,y=400)
                       
         #saving account
        def n8():

            cur.execute(f"insert into savet1(fname,mname,lname,aadhar,pan,date,month,year)values ('{e.get()}','{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{spin.get()}','{spin1.get()}','{spin2.get()}')")
            con.commit()

            b=Toplevel(ob)
            b.geometry("800x900")
            b.configure(background="#FAF598")
            l=Label(b,text="Customer Information",font=("algerian",30),bg="#FAF598",fg="#C20202")
            l.place(x=60,y=50)
            l=Label(b,text="---------------------------------------------------------------------",font=("broadway",15),fg="green",bg="#FAF598")
            l.place(x=45,y=100)

           
            l=Label(b,text="Current Address :",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=160)
            l=Label(b,text="Permanant Address:",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=220)
            l=Label(b,text="Mobile No:",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=280)
            l=Label(b,text="Email id:",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=340)
            ed=Entry(b,font=("arial",20),width=17)
            ea=Entry(b,font=("arial",20),width=17)
            eb=Entry(b,font=("arial",20),width=17)
            ec=Entry(b,font=("arial",20),width=17)

            ed.place(x=360,y=160)
            ea.place(x=360,y=220)
            eb.place(x=360,y=280)
            ec.place(x=360,y=340)
         
             #saving account
            l=Label(b,text="select City",font=("algerian",20),fg="black",bg="#FAF598")
            l.place(x=50,y=410)        
       
            city=["Latur","parbhani","Ahmednagar","Akola","Amravati","Aurangabad","Beed","Bhandara","Buldhana","Chandrapu","Dhule","Gadchiroli","Gondia","Hingoli","J-R","Jalgaon","Jalna","Kolhapur","Latur","Mumbai City","Mumbai Suburban","Nagpur","Nanded","Nandurbar","Nashik","Osmanabad","Palghar","Parbhani","Pune"]
            cmb=ttk.Combobox(b,value=city,font=("algerian",20))
            cmb.place(x=30,y=460)
            cmb.current(0)
        
            l=Label(b,text="select State",font=("algerian",20),fg="black",bg="#FAF598")
            l.place(x=380,y=410)
            
            state=["Maharashtra","karnataka","UP","Bihar","rajsthan","hariyana","Keral","Madhyapradesh","Odisha"]
            cm=ttk.Combobox(b,value=state,font=("algerian",20))
            cm.place(x=380,y=460)   
            cm.current(0) 

            def n3():
                try:
                   cur.execute("use save1")
                except:
                  cur.execute("create database save1")
                  cur.execute("use save1")
                  

                try:
                     cur.execute("describe savet2")
     
                 
                except:
                    cur.execute('create table savet2(cadd varchar(20),padd varchar(20),mono varchar(20),email varchar(20),city varchar(30),state varchar(50))')
                               
                cur.execute(f"insert into savet2(cadd,padd,mono,email,city,state)values ('{ed.get()}','{ea.get()}','{eb.get()}','{ec.get()}','{cmb.get()}','{cm.get()}')")
                con.commit()
                                   
                o=Toplevel(b)
                o.geometry("800x700")
                o.configure(background="pink")
                l=Label(o,text="Terms And Conditions",font=("algerian",20),bg="pink",fg="#C20202")
                l.place(x=60,y=50)
                l=Label(o,text="---------------------------------------------------------------------",font=("broadway",15),fg="green",bg="pink")
                l.place(x=45,y=80)
                
                
                srcText=scrolledtext.ScrolledText(o,wrap=WORD)
                srcText.place(x=50,y=100)
                 #saving account
                srcText.insert('insert',"1)I confirm that I am not registered under GST, I am not exempted from GST and I am not a related person to IDFC FIRST Bank under GST. If I am then I will submit the GST annexure by visiting nearest IDFC FIRST Bank branch.\n\n2)I confirm that I have not opened an account nor will open any account with any other bank using Aadhaar OTP e-KYC authentication.\n\n3)I have understood the nature of information that may be shared upon authentication. I have been given to understand that my information submitted to the bank herewith                 shall not be used for any purpose other than mentioned above, or as per requirements of extant law.\n\n4)I confirm that all the information voluntarily furnished by me is true, correct and complete.\n\n5)I am aware that the deposits into this account cannot exceed ₹ 1,00,000 till I meet someone from IDFCFIRST Bank.\n\n6)I confirm that I will be available for a meeting with the bank at a mutually convenient time, in thecity I have declared I live in, within 6 months of account opening. If this meeting does not happen,                 the bankwill close the account.\n7)I hereby confirm that I do not wish to avail any Direct Benefit Transfer (DBT) benefits in my IDFCFIRST Bank Savings account. I further note and agree to seed my Aadhaar for DBT benefits later, if                 required, byvisiting nearest IDFC FIRST Bank branch.\n \n 8)I have no objection for authenticating myself with Aadhaar based Authentication system and voluntarilygive my consent to:\n9)• Use my Aadhaar details to authenticate myself from UIDAI\n\n10)• Link the Aadhaar number to all my existing / new accounts and customer ID with your bank\n\n11)I wish to avail the banking facilities/products from IDFC FIRST Bank Limited (“IDFC FIRST Bank”), andother products/services including Mutual Funds and/or insurance products that are offered by IDFC FIRST Bank in its capacity as an Intermediary and I have read, understood and agree to the Terms and Conditions displayed on the website of IDFC FIRST Bank i.e. www.idfcfirstbank.com , w.r.t. the said  banking facilities and other products/services which may be amended by IDFC FIRST Bank from time to time and hosted and notified on the website of IDFC FIRST Bank.\n" )
                def show():
                      msg=messagebox.showinfo("OTP ","your otp is sent on your Email")
                      pq=Toplevel(o)
                      pq.configure(background="#FEE0B0")
                      pq.geometry("500x200")
                      l=Label(pq,text="Enter OTP:",font=("algerian",20),fg="red",bg="#FEE0B0")
                      l.place(x=20,y=20)
                      mn=Entry(pq,font=("arial",20),width=7)
                      mn.place(x=240,y=20)
                      def show4():
                         if mn.get()=="1234":                          
                             msg=messagebox.showinfo("OTP","Congratulations! \n Your account Is Successfully Created !")
                             msg=messagebox.showinfo("UserId Password","Your UserId and Password For online banking is sent on Mobile No !")
                             msg=messagebox.showinfo("Login Info","You can Login using UserId and Password!")
                         else:
                             msg=messagebox.showinfo("OTP","Incorrect OTP !")

                      h=Button(pq,text="submit",font=("algerian",20),fg="red",bg="#FEE0B0",command=show4)
                      h.place(x=80,y=70)
                      mainloop()
                  
                c2=IntVar()

                c=Checkbutton(o,text=" I ACCEPT",variable=c2,onvalue=1,offvalue=0,height=2,width=10,command=show)
                
        
                c.place(x=50,y=490)
                              

                mainloop()
                
               
                     

            b9=Button(b,text="Next",font=("broadway",20),bg="yellow",fg="green",command=n3)
            b9.place(x=270,y=700)
        

            mainloop()


        g=Button(ob,text="Next",font=("algerian",20),fg="red",bg="pink",width=17,command=n8)
        g.place(x=300,y=550)


      
        mainloop()
    
    b9=Button(obj1,text="SAVING ACCOUNT",font=("algerian",20),command=n6,bg="#FBF4D1",fg="#C20202")
    b9.place(x=70,y=220)   



 #current account ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
  


    #current account
    def n2():
        
        ob=Toplevel(obj1)
        ob.geometry("800x900")
        ob.configure(background="#FAF598")
        l=Label(ob,text="Customer Information",font=("algerian",30),bg="#FAF598",fg="#C20202")
        l.place(x=60,y=50)
        l=Label(ob,text="---------------------------------------------------------------------",font=("broadway",15),fg="green",bg="#FAF598")
        l.place(x=45,y=100)
        l=Label(ob,text=" First Name",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=160)
        l=Label(ob,text=" Middle Name",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=45,y=220)
        l=Label(ob,text=" Last Name",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=280)
        l=Label(ob,text="Aadhar Card No",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=340)
        l=Label(ob,text="PAN Card No",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=400)
        l=Label(ob,text="DOB",font=("algerian",15),fg="black",bg="#FAF598")
        l.place(x=50,y=460)
        spin1=Spinbox(ob,from_=1,to=31,font=("algerian",15),fg="black",width=5)
        spin1.place(x=260,y=460)
        spin2=Spinbox(ob,from_=1,to=12,font=("algerian",15),fg="black",width=5)
        spin2.place(x=360,y=460)
        spin3=Spinbox(ob,from_=2000,to=2022,font=("algerian",15),fg="black",width=5)
        spin3.place(x=460,y=460)  
       

#current account

        ej=Entry(ob,font=("arial",20),width=17)
        ef=Entry(ob,font=("arial",20),width=17)
        eg=Entry(ob,font=("arial",20),width=17)
        eh=Entry(ob,font=("arial",20),width=17)
        ei=Entry(ob,font=("arial",20),width=17)


        ej.place(x=260,y=160)
        ef.place(x=260,y=220)
        eg.place(x=260,y=280)
        eh.place(x=260,y=340)
        ei.place(x=260,y=400)
         
       #current account
        
        def n8():
            try:
                 cur.execute("use save1")
   
            except:
              cur.execute("create database save1")
              cur.execute("use save1")

            try:
              cur.execute("describe current1")
            except:
              cur.execute('create table current1(fname varchar(20),mname varchar(20),lname varchar(20),aadhar varchar(20),pan varchar(20),date int,month int,year int)')
            
            cur.execute(f"insert into current1(fname,mname,lname,aadhar,pan,date,month,year)values ('{ej.get()}','{ef.get()}','{eg.get()}','{eh.get()}','{ei.get()}','{spin1.get()}','{spin2.get()}','{spin3.get()}')")

            con.commit()

            b=Toplevel(ob)
            b.geometry("800x900")
            b.configure(background="#FAF598")
            l=Label(b,text="Customer Information",font=("algerian",30),bg="#FAF598",fg="#C20202")
            l.place(x=60,y=50)
            l=Label(b,text="---------------------------------------------------------------------",font=("broadway",15),fg="green",bg="#FAF598")
            l.place(x=45,y=100)

            l=Label(b,text="Are You Salaried Person ?",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=160)
            c=IntVar()
            c1=IntVar()

            r=Radiobutton(b,variable=c,text="yes",font=("algerian",15),fg="black",bg="#FAF598")
            r.place(x=360,y=160)
            r1=Radiobutton(b,variable=c1,text="No",font=("algerian",15),fg="black",bg="#FAF598")
            r1.place(x=460,y=160)
            l=Label(b,text="Are You Businessman ?",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=220)
            c3=IntVar()
            c4=IntVar()
#current account
            r3=Radiobutton(b,variable=c3,text="yes",font=("algerian",15),fg="black",bg="#FAF598")
            r3.place(x=360,y=220)
            r4=Radiobutton(b,variable=c4,text="No",font=("algerian",15),fg="black",bg="#FAF598")
            r4.place(x=460,y=220)
            l=Label(b,text="Current Address :",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=280)
            l=Label(b,text="Permanant Address:",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=340)
            l=Label(b,text="Mobile No:",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=400)
            l=Label(b,text="Email id:",font=("algerian",15),fg="black",bg="#FAF598")
            l.place(x=50,y=460)
            ew=Entry(b,font=("arial",20),width=17)
            ex=Entry(b,font=("arial",20),width=17)
            ey=Entry(b,font=("arial",20),width=17)
            ez=Entry(b,font=("arial",20),width=17)

            ew.place(x=360,y=280)
            ex.place(x=360,y=340)
            ey.place(x=360,y=400)
            ez.place(x=360,y=460)
         
            
            l=Label(b,text="select City",font=("algerian",20),fg="black",bg="#FAF598")
            l.place(x=50,y=520)
        
 #current account      
            city=["Latur","parbhani","Ahmednagar","Akola","Amravati","Aurangabad","Beed","Bhandara","Buldhana","Chandrapu","Dhule","Gadchiroli","Gondia","Hingoli","J-R","Jalgaon","Jalna","Kolhapur","Latur","Mumbai City","Mumbai Suburban","Nagpur","Nanded","Nandurbar","Nashik","Osmanabad","Palghar","Parbhani","Pune"]
            cmb=ttk.Combobox(b,value=city,font=("algerian",20))
            cmb.place(x=30,y=570)
            cmb.current(0)
        
            l=Label(b,text="select State",font=("algerian",20),fg="black",bg="#FAF598")
            l.place(x=380,y=520)
            state=["Maharashtra","karnataka","UP","Bihar","rajsthan","hariyana","Keral","Madhyapradesh","Odisha"]
            cm=ttk.Combobox(b,value=state,font=("algerian",20))
            cm.place(x=380,y=570)   
            cm.current(0) 
 #current account           
            def n3():
                
                try:
                   cur.execute("use save1")
                except:
                  cur.execute("create database save1")
                  cur.execute("use save1")
                  

                try:
                     cur.execute("describe current2")
     
                 
                except:
                    cur.execute('create table current2(cadd varchar(20),padd varchar(20),mono varchar(20),email varchar(20))')

               
                cur.execute(f"insert into current2(cadd,padd,mono,email)values ('{ew.get()}','{ex.get()}','{ey.get()}','{ez.get()}')")
                con.commit()               
                
                o=Toplevel(b)
                o.geometry("800x700")
                o.configure(background="pink")
                l=Label(o,text="Terms And Conditions",font=("algerian",20),bg="pink",fg="#C20202")
                l.place(x=60,y=50)
                l=Label(o,text="---------------------------------------------------------------------",font=("broadway",15),fg="green",bg="pink")
                l.place(x=45,y=80)
                
                
                srcText=scrolledtext.ScrolledText(o,wrap=WORD)
                srcText.place(x=50,y=100)
                srcText.insert('insert',"1)I confirm that I am not registered under GST, I am not exempted from GST and I am not a related person to IDFC FIRST Bank under GST. If I am then I will submit the GST annexure by visiting nearest IDFC FIRST Bank branch.\n\n2)I confirm that I have not opened an account nor will open any account with any other bank using Aadhaar OTP e-KYC authentication.\n\n3)I have understood the nature of information that may be shared upon authentication. I have been given to understand that my information submitted to the bank herewith                 shall not be used for any purpose other than mentioned above, or as per requirements of extant law.\n\n4)I confirm that all the information voluntarily furnished by me is true, correct and complete.\n\n5)I am aware that the deposits into this account cannot exceed ₹ 1,00,000 till I meet someone from IDFCFIRST Bank.\n\n6)I confirm that I will be available for a meeting with the bank at a mutually convenient time, in thecity I have declared I live in, within 6 months of account opening. If this meeting does not happen,                 the bankwill close the account.\n7)I hereby confirm that I do not wish to avail any Direct Benefit Transfer (DBT) benefits in my IDFCFIRST Bank Savings account. I further note and agree to seed my Aadhaar for DBT benefits later, if                 required, byvisiting nearest IDFC FIRST Bank branch.\n \n 8)I have no objection for authenticating myself with Aadhaar based Authentication system and voluntarilygive my consent to:\n9)• Use my Aadhaar details to authenticate myself from UIDAI\n\n10)• Link the Aadhaar number to all my existing / new accounts and customer ID with your bank\n\n11)I wish to avail the banking facilities/products from IDFC FIRST Bank Limited (“IDFC FIRST Bank”), andother products/services including Mutual Funds and/or insurance products that are offered by IDFC FIRST Bank in its capacity as an Intermediary and I have read, understood and agree to the Terms and Conditions displayed on the website of IDFC FIRST Bank i.e. www.idfcfirstbank.com , w.r.t. the said  banking facilities and other products/services which may be amended by IDFC FIRST Bank from time to time and hosted and notified on the website of IDFC FIRST Bank.\n" )
                def show():
                      msg=messagebox.showinfo("OTP ","your otp is sent on your Email")
                      p=Toplevel(o)
                      p.configure(background="#FEE0B0")
                      p.geometry("500x200")
                      l=Label(p,text="Enter OTP:",font=("algerian",20),fg="red",bg="#FEE0B0")
                      l.place(x=20,y=20)
                      m=Entry(p,font=("arial",20),width=7)
                      m.place(x=240,y=20)
                      def show2():
                        if m.get()=="123":                          
                             msg=messagebox.showinfo("OTP","Congratulations! \n Your account Is Successfully Created !")
                             msg=messagebox.showinfo("UserId Password","Your UserId and Password For online banking is sent on Mobile No !")
                             msg=messagebox.showinfo("Login Info","You can Login using UserId and Password!")
                        else:
                             msg=messagebox.showinfo("OTP","Incorrect OTP !")
                        p.destroy()
                       
                          
                            

                      h=Button(p,text="submit",font=("algerian",20),fg="red",bg="#FEE0B0",command=show2)
                      h.place(x=80,y=70)
                      
                     
                      mainloop()
                  
                c2=IntVar()

                c=Checkbutton(o,text=" I ACCEPT",variable=c2,onvalue=1,offvalue=0,height=2,width=10,command=show)
                
        
                c.place(x=50,y=490)

              
                

                mainloop()
                
               
               
       

            b9=Button(b,text="Next",font=("broadway",20),bg="yellow",fg="green",command=n3)
            b9.place(x=270,y=700)
        

            mainloop()

        g=Button(ob,text="Next",font=("algerian",20),fg="red",bg="pink",width=17,command=n8)
        g.place(x=300,y=550)
       
        
                  
             
              
            
        
        ob.mainloop()
        
        
    b2=Button(obj1,text="CURRENT ACCOUNT",font=("algerian",20),command=n2,bg="#FBF4D1",fg="#C20202")
    b2.place(x=70,y=280)   
    obj1.mainloop()


    
b4=Button(obj,text="CREATE AN ACCOUNT",font=("algerian",20),fg="red",bg="pink",width=17,command=n1)
b4.place(x=500,y=400)

# account creation complete<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 #login account ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################  ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
  
  
def login():
    t=Toplevel(obj)
    t.geometry("800x940")
    t.configure(background="#66F49C")
    c2=Canvas(t,bg="#66F49C",height=250,width=900)
    c2.place(x=0,y=100)
    c1=Canvas(t,bg="white",height=408,width=900)
    c1.place(x=0,y=250)
#"C:\Users\tarte\Desktop\images\images (1).png"
    i1=PhotoImage(file='path\\bank.png')
    c1.create_image(0,0,anchor=NW,image=i1)

    l=Label(t,text="Login form",font=("Arial",30),bg="#66F49C",fg="white",width=30)
    l.place(x=150,y=130)

    l1=Label(t,text="User Name:",font=("Arial",20),bg="#66F49C",fg="white",width=10)
    l1.place(x=90,y=270)
    f1=Entry(t,font=("Arial",20),bg="white",fg="red",width=20)
    f1.place(x=270,y=270)

    l2=Label(t,text="Password:",font=("Arial",20),bg="#66F49C",fg="white",width=10)
    l2.place(x=90,y=340)
    f2=Entry(t,font=("Arial",20),bg="white",fg="red",width=20)
    f2.place(x=270,y=340)


    
    
    
    def ashowinfo():
        if f2.get()=="12345" and f1.get()=="dnyana":  
            msg=messagebox.showinfo("Login Information","Login Sucessfully !\n Welcome 👍 ")
            
        else :   
            msg=messagebox.showinfo("Login Information","Login not Sucessful ! ")
            n1.destroy()
        
           
      
        n1=Toplevel(t)
        n1.geometry("920x900")
        n1.configure(background="#66F49C")
        
        c1=Canvas(n1,bg="white",height=490,width=930)
        c1.place(x=0,y=200)

        i1=PhotoImage(file='path\\bank.png')
        c1.create_image(0,0,anchor=NW,image=i1)

        l1=Label(n1,text="Welcome To Bank of Latur",font=("broadway",20),bg="#66F49C",fg="#C20202",width=25)
        l1.place(x=120,y=80)

 #send money ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
  
        def sm():
            c1=Toplevel(n1)
            c1.geometry("920x900")
            c1.configure(background="#EECD04")

            l1=Label(c1,text="send Money",font=("broadway",20),bg="#EECD04",fg="#C20202",width=25)
            l1.place(x=80,y=80)

            d1=Canvas(c1,bg="white",height=490,width=930)
            d1.place(x=0,y=200)

            i1=PhotoImage(file='path\\sendb.png')
            d1.create_image(0,0,anchor=NW,image=i1)
            def cancle():
                c1.destroy()
            
            def tup():
                t1=Toplevel(c1)
                t1.geometry("920x900")
                t1.configure(background="#FC6868")

                l1=Label(t1,text="send Money",font=("broadway",20),bg="#FC6868",fg="#EECD04",width=25)
                l1.place(x=80,y=80)

                cs1=Canvas(t1,bg="white",height=490,width=930)
                cs1.place(x=0,y=200)

                i1=PhotoImage(file='path\\sendb.png')
                cs1.create_image(0,0,anchor=NW,image=i1)

                def bhi():
                     ts1=Toplevel(t1)
                     ts1.geometry("920x900")
                     ts1.configure(background="#EECD04")

                     l1=Label(ts1,text="send Money",font=("broadway",20),bg="#EECD04",fg="#C20202",width=25)
                     l1.place(x=80,y=80)

                     c1=Canvas(ts1,bg="white",height=490,width=930)
                     c1.place(x=0,y=200)

                     i1=PhotoImage(file='path\\sendb.png')
                     c1.create_image(0,0,anchor=NW,image=i1)
                    
                     txt=Text(ts1,width=40,height=1,font=("vijaya",20),bg="white",fg="#C20202")
                     txt.insert(INSERT,"Beneneficry id")

                     def verify():
                         if txt.get("1.0","1.4")=="79":
                            m=messagebox.showinfo("info","varified")   
                         else:
                            m=messagebox.showwarning("info"," not varified")   
                            v1.destroy()  
                                       
                                               
                         v1=Toplevel(ts1)
                        
                         v1.geometry("920x900")
                         v1.configure(background="#FC6868")

                         l1=Label(v1,text="send Money",font=("broadway",20),bg="#FC6868",fg="Yellow",width=25)
                         l1.place(x=180,y=80)

                         l3=Label(v1,text="Amount*",font=("broadway",20),bg="white",fg="#C20202",width=10)
                         l3.place(x=80,y=210)
                         l2=Label(v1,text="Remarks(optional)",font=("broadway",20),bg="white",fg="#C20202",width=10)
                         l2.place(x=80,y=250)

                         c1=Canvas(v1,bg="white",height=490,width=930)
                         c1.place(x=0,y=200)

                         i1=PhotoImage(file='path\\request.png')
                         c1.create_image(0,0,anchor=NW,image=i1)                     
                         
                         lc1=Label(v1,text="Beneneficry id",font=("algerian",20),bg="white",fg="#C20202")
                         lc1.place(x=510,y=220)
                         lb1=Label(v1,text="Amount*",font=("algerian",20),bg="white",fg="#C20202")
                         lb1.place(x=510,y=260)
                         l2=Label(v1,text="Remarks",font=("algerian",20),bg="white",fg="#C20202")
                         l2.place(x=510,y=340)
                         
                         tx1t=Text(v1,width=40,height=1,font=("vijaya",20),bg="white",fg="#C20202")

                         tx1t.insert(INSERT,txt.get("1.0","1.4"))
                         tx1t.place(x=730,y=220)

                         l1e=Entry(v1,font=("Arial",20),bg="white",fg="blue",width=10)
                         l1e.place(x=730,y=260)
                         l2e=Entry(v1,font=("arial",20),bg="white",fg="blue",width=10)
                         l2e.place(x=730,y=340)    
                                      
                         def show():
                            if(tx1t.get("1.0","1.4")==txt.get("1.0","1.4")):
                                msg=messagebox.showinfo("OTP ","your otp is sent on your Email")
                            else:
                                msg=messagebox.showwarning("OTP ","something is wrong !")
                                p2.destroy()

                            
                            
                            try:
                              cur.execute("use save1")
                            except:
                               cur.execute("create database save1")
                               cur.execute("use save1")
                  
   
                            try:
                                cur.execute("describe amount")
     
                 
                            except:
                               cur.execute('create table amount(amount varchar(20),remarks varchar(60))')            
                            cur.execute(f"insert into amount(amount,remarks)values ('{l1e.get()}','{l2e.get()}')")
                            con.commit()
                            
                            p2=Toplevel(v1)
                            p2.configure(background="#FEE0B0")
                            p2.geometry("500x200")

                            l=Label(p2,text="Enter OTP:",font=("algerian",20),fg="red",bg="#FEE0B0")
                            l.place(x=20,y=20)
                            m=Entry(p2,font=("arial",20),width=7)
                            m.place(x=240,y=20)

                            def show2():
                                if m.get()=="123":       
                                   msg=messagebox.showinfo("OTP","Congratulations! \n Your Transtion is  Successfully  !")      

                                else:
                                   msg=messagebox.showinfo("OTP","Incorrect OTP !")  
                            

                            h=Button(p2,text="submit",font=("algerian",20),fg="red",bg="#FEE0B0",command=show2)
                            h.place(x=80,y=70)                                            
                            mainloop()
                            
                          

                         l1b=Button(v1,text="continue",font=("vijaya",20),bg="white",fg="#C20202",command=show)
                         l1b.place(x=650,y=450)

                        
                           

                         ldb=Button(v1,text="cancle",font=("vijaya",20),bg="white",fg="#C20202",command=cancle)
                         ldb.place(x=530,y=450)
                         
                         
                         txt1=Text(v1,width=40,height=1,font=("arial",20),bg="white",fg="#C20202")
                         txt1.insert(INSERT,"Amount\n")
                       
                         
                         v1.mainloop()
                    

                        
                     l1=Button(ts1,text="Varify",font=("vijaya",20),bg="white",fg="#C20202",command=verify)
                     l1.place(x=80,y=230)
                     
                     txt.place(x=180,y=230)
                     ts1.mainloop()

                l1=Button(t1,text="BHIM UPI ID",font=("arial",20),bg="white",fg="#C20202",command=bhi)
                l1.place(x=40,y=280)
                
                t1.mainloop()


            l1=Button(c1,text="Transfer Using UPI",font=("arial",20),bg="white",fg="#C20202",width=25,command=tup)
            l1.place(x=40,y=280)
            
            
           
            c1.mainloop()
        
       
        e1=Button(n1,text=" send money",font=("Arial",15),bg="#95F9F4",fg="#C20202",width=13,command=sm)
        e1.place(x=290,y=220)

 #pay bills ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
  

        def pb():
            p1=Toplevel(n1)
            p1.geometry("920x900")
            p1.configure(background="#FC6868")
            l1=Label(p1,text="Pay Bills ",font=("broadway",30),bg="#FC6868",fg="#C20202",width=25)
            l1.place(x=80,y=80)
            p1=Canvas(p1,bg="white",height=490,width=930)
            p1.place(x=0,y=200)

            i1=PhotoImage(file='path\\sendb.png')
            p1.create_image(0,0,anchor=NW,image=i1)
            
            def sbc():
                sc1=Toplevel(n1)
                sc1.geometry("920x900")
                sc1.configure(background="#EECD04")
                l1=Label(sc1,text="Pay Electricity Bills ",font=("Algerian",20),bg="#EECD04",fg="#C20202",    width=25)
                l1.place(x=40,y=80)

                p1=Canvas(sc1,bg="white",height=490,width=930)
                p1.place(x=0,y=200)
                i1=PhotoImage(file='path\\sendb.png')
                p1.create_image(0,0,anchor=NW,image=i1)

                l1=Label(p1,text="Select Biller",font=("arial",20),bg="white",fg="#C20202")
                l1.place(x=0,y=10)
                ebill=["central power distribution","Estern power distribution","Southern power distribution","northern power distribution"]
                cm=ttk.Combobox(p1,value=ebill,font=("arial",20))
                cm.place(x=190,y=10)
                
                def ok3():
                     o1=Toplevel(sc1)
                     o1.geometry("920x900")
                     o1.configure(background="#EECD04")
                     
                     l1=Label(o1,text="Enter Details ",font=("algerian",30),bg="#EECD04",fg="#C20202")
                     l1.place(x=10,y=100)
                     
                     
                     p1=Canvas(o1,bg="white",height=490,width=930)
                     p1.place(x=0,y=200)

                     i1=PhotoImage(file='path\\sendb.png')
                     p1.create_image(0,0,anchor=NW,image=i1)
                     
                     l1=Label(o1,text="power distribution  Details ",font=("arial",30),bg="white",fg="#66F49C")
                     l1.place(x=120,y=210)

                     l1=Label(o1,text="service Number:",font=("Arial",20),bg="white",fg="#66F49C", width=13)
                     l1.place(x=10,y=400)
                     l1=Label(o1,text="Biller:",font=("Arial",20),bg="white",fg="#66F49C", width=13)
                     l1.place(x=10,y=300)
                     
                     e1=Entry(o1,font=("Arial",20),bg="white",fg="black",width=20)
                     e1.place(x=210,y=400)
                     txt=Text(o1,width=40,height=1,font=("vijaya",20),bg="white",fg="#C20202")
                     txt.insert(INSERT,cm.get())
                     txt.place(x=210,y=300)
                     

                     def pay2():
                        me=messagebox.showinfo("payment","payment successfull!")
                        sc1.destroy()
                     f4=Button(o1,text="Get Bill",font=("arial",20),bg="skyblue",fg="red",command=pay2)
                     f4.place(x=190,y=480)

                     mainloop()

                

                bt=Button(p1,text="ok",font=("arial",20),bg="skyblue",fg="red",command=ok3)
                bt.place(x=190,y=80)
                    
                mainloop()
               

              


            l1=Button(p1,text="Electricity",font=("arial",20),bg="white",fg="#C20202",width=25,command=sbc)
            l1.place(x=30,y=30)
            def mp():
                m1=Toplevel(p1)
                m1.geometry("920x900")
                m1.configure(background="#EECD04")
                l1=Label(m1,text="Pay Bills ",font=("Algerian",30),bg="#EECD04",fg="#C20202",width=25)
                l1.place(x=90,y=80)
                l1=Label(m1,text="Select Biller",font=("arial",20),bg="#EECD04",fg="#C20202")
                l1.place(x=0,y=140)
                d1=Canvas(m1,bg="white",height=490,width=930)
                d1.place(x=0,y=200)

                i1=PhotoImage(file='path\\sendb.png')
                d1.create_image(0,0,anchor=NW,image=i1)
                c1=IntVar()
                c2=IntVar()

                rp=Radiobutton(m1,value=c1,text="Prepaid Recharge",font=("arial",20),bg="white",fg="#C20202")
                rp1=Radiobutton(m1,value=c2,text="Prepaid Recharge",font=("arial",20),bg="white",fg="#C20202")
                rp.place(x=0,y=210)
                rp1.place(x=0,y=260)
                l1=Label(m1,text="Prepaid Mobile Number",font=("arial",20),bg="white",fg="#C20202")
                l1.place(x=0,y=320)
                e2=Entry(m1,font=("Arial",20),bg="white",fg="black")
                e2.place(x=290,y=320)

                l1=Label(m1,text="choose operator",font=("arial",20),bg="white",fg="#C20202")
                l1.place(x=0,y=370)
                ebill=["Jio prepaid","Airtel Prepaid","BSNL","VI prepaid","MTNL Mumbai Prepaid"]
                cm1=ttk.Combobox(m1,value=ebill,font=("arial",20))
                cm1.place(x=290,y=370)
                cm1.current(0)
              
                l1=Label(m1,text="choose circle",font=("arial",20),bg="white",fg="#C20202")
                l1.place(x=1,y=420)
                ebilll=["Maharashtra And Goa","Andra Pradesh","Assam","chennai","all"]
                cm=ttk.Combobox(m1,value=ebilll,font=("arial",20))
                cm.place(x=290,y=420)
                cm.current(0)
                l1=Label(m1,text="Amount",font=("arial",20),bg="white",fg="#C20202")
                l1.place(x=1,y=470)
                billl=["15","25","139","250","299"]
                cm=ttk.Combobox(m1,value=billl,font=("arial",20))
                cm.place(x=290,y=470)
                cm.current(0)

                def show6():
                      msg=messagebox.showinfo("OTP ","your otp is sent on your Email")
                      
                      pq=Toplevel(m1)
                      pq.configure(background="#FEE0B0")
                      pq.geometry("500x200")
                      l=Label(pq,text="Enter OTP:",font=("algerian",20),fg="red",bg="#FEE0B0")
                      l.place(x=20,y=20)
                      m=Entry(pq,font=("arial",20),width=7)
                      m.place(x=240,y=20)
                      def show3():
                        if m.get()=="123":                          
                             msg=messagebox.showinfo("OTP","Congratulations! \n Recharge  Successfull !")
                        else:
                             msg=messagebox.showinfo("OTP","Incorrect OTP !")
                       
                                                   

                      h=Button(pq,text="submit",font=("algerian",20),fg="red",bg="#FEE0B0",command=show3)
                      h.place(x=80,y=70)
                

                l1=Button(m1,text="Recharge",font=("arial",20),bg="white",fg="#C20202",command=show6)
                l1.place(x=190,y=540)
                
              
                
                mainloop()
                

            l1=Button(p1,text="Mobile pre-\npaid postpaid",font=("arial",20),bg="white",fg="#C20202",width=25,command=mp)
            l1.place(x=30,y=90)
            def sbc():
                s1=Toplevel(n1)
                s1.geometry("920x900")
                s1.configure(background="#EECD04")
                l1=Label(s1,text="Pay Bills ",font=("Algerian",20),bg="#EECD04",fg="#C20202",    width=25)
                l1.place(x=40,y=80)
                p1=Canvas(s1,bg="white",height=490,width=930)
                p1.place(x=0,y=200)

                i1=PhotoImage(file='path\\sendb.png')
                p1.create_image(0,0,anchor=NW,image=i1)
                l1=Label(p1,text="Select Biller",font=("arial",20),bg="white",fg="#C20202")
                l1.place(x=0,y=10)
                bill=["American Express credit card","Axis Bank Credit Card","Bank Of India credit card","Central Bank Of India Credit Card"]
                cm=ttk.Combobox(p1,value=bill,font=("arial",20))
                cm.place(x=190,y=10)
                def ok1():
                     o1=Toplevel(s1)
                     o1.geometry("920x900")
                     o1.configure(background="#EECD04")
                     
                     l1=Label(o1,text="Enter Details ",font=("algerian",30),bg="#EECD04",fg="#C20202")
                     l1.place(x=10,y=100)
                     
                     
                     p1=Canvas(o1,bg="white",height=490,width=930)
                     p1.place(x=0,y=200)

                     i1=PhotoImage(file='path\\sendb.png')
                     p1.create_image(0,0,anchor=NW,image=i1)
                     
                     l1=Label(o1,text="Credit Card Details ",font=("arial",30),bg="white",fg="#66F49C")
                     l1.place(x=120,y=210)
                     l1=Label(o1,text="Card Number:",font=("Arial",20),bg="white",fg="#66F49C", width=10)
                     l1.place(x=10,y=300)
                     e1=Entry(o1,font=("Arial",20),bg="white",fg="black",width=20)
                     e1.place(x=210,y=300)

                     l2=Label(o1,text="Amount:",font=("Arial",20),bg="white",fg="#66F49C", width=10)
                     l2.place(x=10,y=400)
                     e2=Entry(o1,font=("Arial",20),bg="white",fg="black",width=20)
                     e2.place(x=210,y=400)
                     def pay():
                        me=messagebox.showinfo("payment","payment successfull!")
                        
                     f4=Button(o1,text="PAY",font=("arial",20),bg="skyblue",fg="red",command=pay)
                     f4.place(x=190,y=480)
                    

                     mainloop()


                b1=Button(p1,text="OK",font=("arial",20),bg="skyblue",fg="red",command=ok1)
                b1.place(x=40,y=80)
                
                mainloop()
            l1=Button(p1,text="Credit Card",font=("arial",20),bg="white",fg="#C20202",width=25,command=sbc)
            l1.place(x=30,y=180)
           
            mainloop()

      
        e1=Button(n1,text="pay bills ",font=("Arial",15),bg="#95F9F4",fg="#C20202",width=13,command=pb)
        e1.place(x=130,y=290)
    
 
        #request money  ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
  
     
        def rem():
            ps1=Toplevel(n1)
            ps1.geometry("920x900")
            ps1.configure(background="#FC6868")
            l1=Label(ps1,text="Request Money ",font=("algerian",30),bg="#FC6868",fg="Yellow",width=25)
            l1.place(x=80,y=80)
            pq1=Canvas(ps1,bg="white",height=490,width=930)
            pq1.place(x=0,y=200)

            i1=PhotoImage(file='path\\request.png')
            pq1.create_image(0,0,anchor=NW,image=i1)
            def rcon():
                 vl1=Toplevel(ps1)
                
                 vl1.geometry("920x900")
                 vl1.configure(background="#FC6868")
                 l1=Label(vl1,text="Request Money",font=("broadway",20),bg="#FC6868",fg="Yellow",width=25)
                 l1.place(x=180,y=80)
                
                 c1=Canvas(vl1,bg="white",height=490,width=930)
                 c1.place(x=0,y=200)
                 i1=PhotoImage(file='path\\request.png')
                 c1.create_image(0,0,anchor=NW,image=i1)                     
                
                 lb1=Label(vl1,text="select conatact : ",font=("algerian",20),bg="white",fg="#C20202")
                 lb1.place(x=440,y=260)

                 contacts=["sonal : 9657845879","mona : 4578965874","raj : 9845789658","punam : 9854654874","sanket : 9446587425","Nita : 9875462344","sonali : 9578965874","abc : 4578965874","abc\n4578965874"]
                 conl=ttk.Combobox(vl1,value=contacts,font=("algerian",17),width=15)
                 conl.place(x=700,y=260)
                 conl.current(1)   
                
                 

                 kl1=Label(vl1,text="Enter amount :",font=("algerian",20),bg="white",fg="#C20202")
                 kl1.place(x=440,y=330)

                 lf2=Entry(vl1,font=("Arial",20),bg="white",fg="red",width=10)
                 lf2.place(x=660,y=330)

                 kll1=Label(vl1,text="Valid Up To:",font=("algerian",20),bg="white",fg="#C20202")
                 kll1.place(x=440,y=420)
                
                 spin=Spinbox(vl1,from_=1,to=31,font=("algerian",15),fg="black",width=2)
                 spin.place(x=650,y=420)
                 spin=Spinbox(vl1,from_=1,to=12,font=("algerian",15),fg="black",width=2)
                 spin.place(x=720,y=420)
                 spin=Spinbox(vl1,from_=2000,to=2022,font=("algerian",15),fg="black",width=4)
                 spin.place(x=780,y=420)  
                      
                                
                 def uco():
                   cme=messagebox.askokcancel("confirmation","do you want to send request ?")
                   icme=messagebox.showinfo("confirmation","requested ")            
                #    conl.destroy()
                   ps1.destroy()
                  
                 eb1=Button(vl1,text="continuoue",font=("Arial",15),bg="white",fg="#C20202",command=uco)
                 eb1.place(x=580,y=500)                       
                          
                 mainloop()
            
           
            
            def rupi():
                vl1=Toplevel(ps1)
                
                vl1.geometry("920x900")
                vl1.configure(background="#FC6868")
                l1=Label(vl1,text="Request Money throught UPI",font=("broadway",20),bg="#FC6868",fg="Yellow",width=25)
                l1.place(x=180,y=80)
                
                c1=Canvas(vl1,bg="white",height=490,width=930)
                c1.place(x=0,y=200)
                i1=PhotoImage(file='path\\request.png')
                c1.create_image(0,0,anchor=NW,image=i1)                     
                
                lb1=Label(vl1,text="select REcent UPI:",font=("algerian",20),bg="white",fg="#C20202")
                lb1.place(x=440,y=260)

                ids=[" 4578965874@ybl "," 4578965874@ybl "," 4578965874@ybl "," 4578965874@ybl "," 4578965874@ybl "," 4578965874@ybl "," 4578965874@ybl "," 4578965874@ybl ","abc\n4578965874"]
                col=ttk.Combobox(vl1,value=ids,font=("algerian",17),width=15)
                col.place(x=700,y=260)
                col.current(0)     


                kl1=Label(vl1,text="Enter amount :",font=("algerian",20),bg="white",fg="#C20202")
                kl1.place(x=440,y=330)
                lf2=Entry(vl1,font=("Arial",20),bg="white",fg="red",width=10)
                lf2.place(x=660,y=330)
                kll1=Label(vl1,text="Valid Up To:",font=("algerian",20),bg="white",fg="#C20202")
                kll1.place(x=440,y=420)
                
                spin=Spinbox(vl1,from_=1,to=31,font=("algerian",15),fg="black",width=2)
                spin.place(x=650,y=420)
                spin=Spinbox(vl1,from_=1,to=12,font=("algerian",15),fg="black",width=2)
                spin.place(x=720,y=420)
                spin=Spinbox(vl1,from_=2000,to=2022,font=("algerian",15),fg="black",width=4)
                spin.place(x=780,y=420)  
       
                
                


                def ucon():
                    cme=messagebox.askokcancel("confirmation","do you want to send request ?")
                    jcme=messagebox.showinfo("confirmation","requested ")            
                    # col.destroy()
                    ps1.destroy()
                  
                eb1=Button(vl1,text="continuoue",font=("Arial",15),bg="white",fg="#C20202",command=ucon)
                eb1.place(x=580,y=500)                       

                mainloop()
           
            lc=IntVar()
            c=Radiobutton(ps1,text="Contacts",variable=lc,font=("arial",20),bg="white",fg="pink",command=rcon)
            
            c.place(x=540,y=240)

            
          
            cl1=IntVar()
            c1=Radiobutton(ps1,text=" BHIM UPI ID ",variable=cl1,font=("arial",20),bg="white",fg="pink",command=rupi)         
            c1.place(x=540,y=280)
            
            
            
            
           
           
            mainloop()


       
        e1=Button(n1,text="Request Money ",font=("Arial",15),bg="#95F9F4",fg="#C20202",width=13,command=rem)
        e1.place(x=130,y=360)

 #pending request  ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
  

        def prq():
            
            s1=Toplevel(n1)
            s1.geometry("870x900")
            s1.configure(background="#FC6868")
            l1=Label(s1,text="Request Money ",font=("algerian",30),bg="#FC6868",fg="Yellow",width=25)
            l1.place(x=80,y=80)
            pi1=Canvas(s1,bg="white",height=490,width=930)
            pi1.place(x=0,y=200)

            i1=PhotoImage(file='path\\pending rq.png')
            pi1.create_image(270,100,anchor=NW,image=i1)
            kl1=Label(s1,text="No Pending requests To Display",font=("elephant",20),bg="white",fg="#C20202",width=25)
            kl1.place(x=190,y=420)
            mainloop()
            

        e1=Button(n1,text="Pending Request",font=("Arial",15),bg="#95F9F4",fg="#C20202",width=13,command=prq)
        e1.place(x=450,y=280)

# services ####################################################################################################################################################################
    #######################################################################################################################################################3
    #######################################################################################
  


        def service():
            se1=Toplevel(n1)
            se1.geometry("930x900")
            se1.configure(background="#9B60BC")
            l1=Label(se1,text="Bank Services ",font=("algerian",30),bg="#9B60BC",fg="#C20202",width=25)
            l1.place(x=80,y=80)
            pi1=Canvas(se1,bg="white",height=470,width=930)
            pi1.place(x=0,y=200)

            i1=PhotoImage(file='path\\services1.png')
            pi1.create_image(0,0,anchor=NW,image=i1)
         
            def unm():
                
                 ue1=Toplevel(se1)
                 ue1.geometry("930x900")
                 ue1.configure(background="#9B60BC")
                 l1=Label(ue1,text="Bank Services ",font=("algerian",30),bg="#9B60BC",fg="#C20202",width=25)
                 l1.place(x=80,y=80)
                 pi1=Canvas(ue1,bg="white",height=470,width=930)
                 pi1.place(x=0,y=200)

                 i1=PhotoImage(file='path\\services1.png')
                 pi1.create_image(0,0,anchor=NW,image=i1)
                 ll1=Label(ue1,text="Name :",font=("algerian",20),bg="white",fg="RED")
                 ll1.place(x=500,y=240)
                 K1=Entry(ue1,text="Name",font=("arial",20),bg="white",fg="black")
                 K1.place(x=600,y=240)

                 
                
                 ll1=Label(ue1,text=" DOB :",font=("algerian",20),bg="white",fg="RED")
                 ll1.place(x=520,y=300)

                 spin4=Spinbox(ue1,from_=1,to=31,font=("algerian",15),fg="black",width=2)
                 spin4.place(x=600,y=300)
                 spin5=Spinbox(ue1,from_=1,to=12,font=("algerian",15),fg="black",width=2)
                 spin5.place(x=660,y=300)
                 spin6=Spinbox(ue1,from_=2000,to=2022,font=("algerian",15),fg="black",width=4)
                 spin6.place(x=720,y=300)  

                 ll1=Label(ue1,text="Address :",font=("algerian",20),bg="white",fg="RED")
                 ll1.place(x=460,y=360)
                 K2=Entry(ue1,text="Address",font=("arial",20),bg="white",fg="black")
                 K2.place(x=600,y=360)
                
                
                 ll1=Label(ue1,text="pincode:",font=("algerian",20),bg="white",fg="RED")
                 ll1.place(x=480,y=420)
                 K3=Entry(ue1,text="pincode",font=("arial",20),bg="white",fg="black")
                 K3.place(x=600,y=420)
                 
                
                 
                


                 def capnn():
                   
                    cme=messagebox.askokcancel("confirmation","do you want to cancle ?")
                    ue1.destroy()

                 def uco():
                    try:
                     cur.execute("use save1")
                    except:
                     cur.execute("create database save1")
                     cur.execute("use save1")
                                 
                    try:
                     cur.execute("describe nomeeni")
                    except:
                     cur.execute('create table nomeeni(name varchar(20),address varchar(20),pincode varchar(20),date int,month int,year int)')            

                    cur.execute(f"insert into nomeeni(name,address,pincode,date,month,year)values('{K1.get()}','{K2.get()}','{K3.get()}','{spin4.get()}','{spin5.get()}','{spin6.get()}')")
                    con.commit()
                    cme=messagebox.askokcancel("Update Nomeeni","Updated Nomeeni successfully")
                    ue1.destroy()
                   
                  
                  
                 eb1=Button(ue1,text="Update Nomeeni",font=("Arial",15),bg="white",fg="#C20202",command=uco)
                 eb1.place(x=570,y=500)  
                

                 eb1=Button(ue1,text="Cancle",font=("Arial",15),bg="white",fg="#C20202",command=capnn)
                 eb1.place(x=750,y=500)  
                 ebe1=Button(ue1,text="<<==",font=("Arial",15),bg="#9B60BC",fg="#C20202",command=capnn)
                 ebe1.place(x=0,y=50) 

                 
                 mainloop()
                 
                 
         
            eed1=Button(se1,text="Update Nomeeni",font=("elephant",15),bg="white",fg="#4766FF",width=13,command=unm)
            eed1.place(x=710,y=360)
                     

            def upn():
                
                 sue1=Toplevel(se1)
                 sue1.geometry("930x900")
                 sue1.configure(background="#9B60BC")
                 l1=Label(sue1,text="Bank Services ",font=("algerian",30),bg="#9B60BC",fg="#C20202",width=25)
                 l1.place(x=80,y=80)
                 pi1=Canvas(sue1,bg="white",height=470,width=930)
                 pi1.place(x=0,y=200)

                 i1=PhotoImage(file='path\\services1.png')
                 pi1.create_image(0,0,anchor=NW,image=i1)
                    #for pan
                 
                 pqi1=Canvas(sue1,bg="white",height=170,width=270)
                 pqi1.place(x=560,y=200)

                 ei1=PhotoImage(file='path\\pancard.png')
                 pqi1.create_image(0,0,anchor=NW,image=ei1)
                 ll1=Label(sue1,text="PAN :",font=("algerian",20),bg="white",fg="RED")
                 ll1.place(x=560,y=400)
                 lh1=Entry(sue1,text="pan",font=("arial",20),bg="white",fg="black")
                 lh1.place(x=630,y=400)
                

                 
                 def capn():
                    sue1.destroy()
                    cme=messagebox.askokcancel("confirmation","do you want to cancle ?")

                 def uco():
                   cme=messagebox.askokcancel("confirmation","Updated Pan successfully")
                        
                   sue1.destroy()
                  
                  
                 eb1=Button(sue1,text="Update",font=("Arial",15),bg="white",fg="#C20202",command=uco)
                 eb1.place(x=680,y=500)  
                

                 eb1=Button(sue1,text="Cancle",font=("Arial",15),bg="white",fg="#C20202",command=capn)
                 eb1.place(x=580,y=500)  
                 ebe1=Button(sue1,text="<<==",font=("Arial",15),bg="#9B60BC",fg="#C20202",command=capn)
                 ebe1.place(x=0,y=50) 

                 
                 mainloop()
                
           
            ee1=Button(se1,text="Update Pan",font=("elephant",15),bg="white",fg="#4766FF",width=13,command=upn)
            ee1.place(x=710,y=420)

            def ueid():
                
                 seo1=Toplevel(se1)
                 seo1.geometry("930x900")
                 seo1.configure(background="#9B60BC")
                 l1=Label(seo1,text="Bank Services ",font=("algerian",30),bg="#9B60BC",fg="#C20202",width=25)
                 l1.place(x=80,y=80)
                 pi1=Canvas(seo1,bg="white",height=470,width=930)
                 pi1.place(x=0,y=200)

                 i1=PhotoImage(file='path\\services1.png')
                 pi1.create_image(0,0,anchor=NW,image=i1)
                
                


                 def capn1():
                    cme=messagebox.askokcancel("confirmation","do you want to cancle ?")
                    seo1.destroy()
                    
                 def uc1o():
                    cme=messagebox.showinfo("confirmation","Updated Email ID successfully")                       
                    seo1.destroy()
                  
                 eb1=Button(seo1,text="Update Email ID",font=("Arial",15),bg="white",fg="#C20202",command=uc1o)
                 eb1.place(x=580,y=340)  
                 ll1=Label(seo1,text="Email id :",font=("algerian",20),bg="white",fg="RED")
                 ll1.place(x=460,y=240)
                 lh1=Entry(seo1,text="Email Id",font=("arial",20),bg="white",fg="red")
                 lh1.place(x=600,y=240)
                

                 eb1=Button(seo1,text="Cancle",font=("Arial",15),bg="white",fg="#C20202",command=capn1)
                 eb1.place(x=500,y=340)  
                 ebe1=Button(seo1,text="<--",font=("elephant",15),bg="#9B60BC",fg="#C20202",command=capn1)
                 ebe1.place(x=0,y=50)
                 mainloop()
                
            de1=Button(se1,text="Update Email ID",font=("elephant",15),bg="white",fg="#4766FF",width=13,command=ueid)
            de1.place(x=710,y=300)
            
            
           
            mainloop()
      

        e1=Button(n1,text="Services",font=("Arial",15),bg="#95F9F4",fg="#C20202",width=13,command=service)
        e1.place(x=450,y=360)
         
        
       
        mainloop()
   
    d=Button(t,text="login",font=("algerian",20),fg="red",bg="pink",width=17,command=ashowinfo)
    d.place(x=150,y=420)  

     
    t.mainloop() 
       

b1=Button(obj,text="LOGIN ACCOUNT",font=("algerian",20),fg="red",bg="pink",width=17,command=login)
b1.place(x=500,y=500)



obj.mainloop()

