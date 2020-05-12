from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import random
from tkinter import ttk
import tkinter.messagebox
import datetime
from datetime import date
import time
import tempfile, os
import os, sys, subprocess


class Window:
	def __init__(self, master):
		self.master = master
		today = date.today()
		self.master.title("Login Details")
		#self.master.iconbitmap(me.ico)
		self.master.configure(bg= 'cornsilk')
		self.master.geometry('950x550+260+100')
		self.frame = Frame(self.master, bg='cornsilk')
		self.frame.pack()

		global mydb
		global my_cursor
		mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "asmanoorme456654",
		database = "BMS_DATABASE",
			)
		#check to see if the connection to mysql was created
		#print(mydb)

		#creat a cursor and initialize it
		my_cursor = mydb.cursor()

		#Create a database
		#my_cursor.execute("CREATE DATABASE BMS_DATABASE")

		#TEST to see if database was created
		#my_cursor.execute("SHOW DATABASES")
		#for a in my_cursor:
		#print(a)


		#Drop a table. this will delete the table which may or we may not want...instead we shod alter it..we do it below
		#my_cursor.execute("DROP TABLE Customers")


		#Database Names list
		#Full_Name, Mobile, Address, PostCode, City, State, E_Date,E_Total_Cost, PaymentMethod

		#Create a Table and after run comment it becos we only create tabel once
		my_cursor.execute("CREATE TABLE IF NOT EXISTS Customers (Full_Name VARCHAR(255), \
			Mobile VARCHAR(255), \
			Address VARCHAR(255), \
			PostCode VARCHAR(255),\
			City VARCHAR(255),\
			State VARCHAR(255),\
			E_Date VARCHAR(255),\
			E_Total_Cost VARCHAR(255),\
			PaymentMethod VARCHAR(255),\
			Customer_ID INT AUTO_INCREMENT PRIMARY KEY)")

		#Show everything in table
		#my_cursor.execute("SELECT * FROM Customers")
		#print(my_cursor.description)
		#also through for loop
		#for things in my_cursor.description:
			#print(things)



		
		#self.label1=Label(self.frame,text= today,font=('arial',35,'bold'), bg='cornsilk',fg='black')
		#self.label1.grid(row = 0, column=3, pady=4)
		#global self.lock 
		self.lock = 0
		#lock += 1
		#print(lock)
		self.Username = StringVar()
		self.Password = StringVar()

		self.lblTitle = Label(self.frame, text="Khyber Pass Restaurant Management", 
			font=('apple chancery',50,'bold'), bg='cornsilk',fg='black')
		self.lblTitle.grid(row=0, column=0, columnspan=1, pady =4)
		self.lblTitle1 = Label(self.frame, text=today, font=('apple chancery',30,'bold'), bg='cornsilk',fg='black')
		self.lblTitle1.grid(row=1, column=0, columnspan=2, sticky = S, pady=10)

		#======================================================================================================

		self.Loginframe1 = LabelFrame(self.frame, width=1350, height=600,
			font=('arial', 20, 'bold'), relief = 'ridge', bg='cornsilk', bd=20)
		self.Loginframe1.grid(row=2,column=0,pady=4)

		self.Loginframe2 = LabelFrame(self.frame, width=1350, height=600,
			font=('arial', 20, 'bold'), relief = 'ridge', bg='cornsilk', bd=20)
		self.Loginframe2.grid(row=3,column=0)

		#================================ Label and Entries =============================================================
		self.lblUsername=Label(self.Loginframe1, text= 'Username', font=('arial', 20,'bold'), bd=22,
			bg='cornsilk', fg='cornsilk')
		self.lblUsername.grid(row=0, column=0)
		self.txtUsername=Entry(self.Loginframe1 , textvariable=self.Username, font=('arial', 20,'bold'))
		self.txtUsername.grid(row=0, column=1,padx=119)


		self.lblPassword=Label(self.Loginframe1, text= 'Password', font=('arial', 20,'bold'), bd=22,
			bg='cornsilk', fg='cornsilk')
		self.lblPassword.grid(row=1, column=0)
		self.txtPassword=Entry(self.Loginframe1 , textvariable=self.Password, font=('arial', 20,'bold'), show='*')
		self.txtPassword.grid(row=1, column=1, columnspan=2,pady=30)

		self.Username.set('Afridi')
		self.Password.set('12345')
		#self.txtPassword.insert(END,self.Password.get())
		#self.txtUsername.insert(END,self.Username.get())

		#================================ Buttons ==========================================
		self.btnLogin=Button(self.Loginframe2, text="Login", width=17,font=('arial', 20,'bold'),command= self.Login_System)
		self.btnLogin.grid(row=3,column=0, pady = 20, padx=8)

		self.btnReset=Button(self.Loginframe2, text="Reset", width=17, font=('arial', 20,'bold'), command = self.Reset)
		self.btnReset.grid(row=3,column=1, pady = 20, padx=8)

		self.btnExit=Button(self.Loginframe2, text="Exit", width=17, font=('arial', 20,'bold'), command = self.Exit)
		self.btnExit.grid(row=3,column=2, pady = 20, padx=8)
		#=========================================================================================

	def Login_System(self):
		#self.Username.set('Afridi')
		#self.Password.set('12345')

		u = self.txtUsername.get()
		p = self.txtPassword.get()

		if (u == 'Afridi' and p == '12345'):
			self.newWindow = Toplevel(self.master)
			self.app = Window2(self.newWindow)
		else:
			
			if (self.lock == 2):
				tkinter.messagebox.showwarning("Multiple Tried With Wrong Details", "For Security Reason, We blocked your Password for 3 hours.")
				self.master.destroy()
				#print(res)
				#tkinter.messagebox.askyesno(""ok",For Security Reason, We blocked your Password for 3 hours")
			else:

				tkinter.messagebox.showwarning("Warning !! ", "Invalid Login Details Please Try Again.")
				self.txtUsername.delete(0,'end')
				self.txtPassword.delete(0,'end')
				self.txtUsername.focus()
				self.lock += 1

	def Reset(self):
		self.txtUsername.delete(0,'end')
		self.txtPassword.delete(0,'end')
		self.txtUsername.focus()

	def Exit(self):
		self.exit = tkinter.messagebox.askyesno("Warning! ","Are You Sure, You want to Exit")
		if self.exit > 0:
			self.master.destroy()
		else:
			command = self.New_Window # Even we dont need here but this guy has written it . dont know y
			#return

	def New_Window(self):
		self.newWindow = Toplevel(self.master)
		self.app = Window2(self.newWindow)
class Window2:
	def __init__(self,master):
		self.master = master
		self.master.title("Restaurant Management System")
		self.master.configure(bg='cornsilk')
		self.master.geometry('1450x1350+0+0')
		self.today = date.today()
		
		######################### Title##################################################
		self.Top_Title = Frame(self.master, bg='cornsilk', bd=20, relief=SUNKEN)
		self.Top_Title.pack(fill = X)
		self.MainFram = Frame(self.master, bg='cornsilk', bd=20, pady=4,relief=SUNKEN)
		self.MainFram.pack(fill=BOTH, expand=1)
		
		self.lblTitle= Label(self.Top_Title, bg='cornsilk',font=('apple chancery', 30, 'bold','italic'), text="Welcom T0 Khyber Pass Restaurant, An Afghani Cuisine",bd=1, 
			fg='black', justify=CENTER)
		self.lblTitle.pack(fill=X)	

		############################################# Customers frames. #############################################

		self.CustomerFrame=Frame(self.MainFram, bg='cornsilk', bd=15, pady=4,relief=SUNKEN)
		self.CustomerFrame.pack(side=LEFT, fill=BOTH, expand=1)
		self.CustomerTitleframe= Frame(self.CustomerFrame, bg='cornsilk',bd=15, pady=4,relief=SUNKEN) ###### relief ridge check later
		self.CustomerTitleframe.pack(side=TOP, fill=X)
		self.Customer_DataFrame = Frame(self.CustomerFrame, bg='cornsilk', bd=15, pady=4,relief=SUNKEN)
		self.Customer_DataFrame.pack(side=BOTTOM,fill=BOTH, expand=1)
		self.Customer_EntryFrame = Frame(self.Customer_DataFrame, bg='cornsilk', bd=15, pady=4)
		self.Customer_EntryFrame.pack(side=TOP)
		self.Customer_Buttonframe = Frame(self.Customer_DataFrame, bg='cornsilk', bd=7, pady=4,relief=SUNKEN)
		self.Customer_Buttonframe.pack(side=BOTTOM,fill=X)	

		#################################### variables ##############################################

		self.var1 = IntVar()
		self.var2 = IntVar()
		self.var3 = IntVar()
		self.var4 = IntVar()
		self.var5 = IntVar()
		self.var6 = IntVar()
		self.var7 = IntVar()
		self.var8 = IntVar()
		self.var9 = IntVar()
		self.var10 = IntVar()
		self.var11 = IntVar()
		self.var12 = IntVar()
		self.var13 = IntVar()
		self.var14 = IntVar()
		self.var15 = IntVar()
		self.var16 = IntVar()
		self.var17 = IntVar()
		self.var18 = IntVar()
		self.var19 = IntVar()
		self.var20 = IntVar()
		self.var21 = IntVar()
		self.var22 = IntVar()
		self.var23 = IntVar()
		self.var24 = IntVar()
		self.var25 = IntVar()
		self.var26 = IntVar()
		self.var27 = IntVar()
		self.var28 = IntVar()
		self.var29 = IntVar()
		self.var30 = IntVar()
		self.var31 = IntVar()
		self.var32 = IntVar()
		self.var33 = IntVar()
		self.var34 = IntVar()
		self.var35 = IntVar()
		self.var36 = IntVar()
		self.var37 = IntVar()
		self.var38 = IntVar()
		self.var39 = IntVar()
		self.var40 = IntVar()
		self.var41 = IntVar()

		self.Total_Cost_forFood = IntVar()
		self.TotalCost = StringVar()
		self.CostofFoods= StringVar()
		self.CostofDrinks = StringVar()

		self.E_Full_Name = StringVar()
		self.E_Mobile = StringVar()
		self.E_Address = StringVar()
		self.E_City = StringVar()
		self.E_State = StringVar()
		self.E_PostCode = StringVar()
		self.E_Date = StringVar()
		self.E_Total_Cost = StringVar()
		self.E_Payment_Method = StringVar()
		self.Payment_Drop = StringVar()

		self.E_Date.set(self.today)
		self.E_State.set("Scotland")
		self.E_City.set("Glasgow")

		self.DateOfOrder = StringVar()

		self.DateOfOrder.set(time.strftime("%d/%m/%y"))

		###########################################. Menue Frames to the Right #####################################
		self.Menue_ButtonFrame=Frame(self.MainFram, bg='cornsilk', bd=15,width=1250,height=300,relief=SUNKEN)
		self.Menue_ButtonFrame.pack(side = BOTTOM)
		self.Buttons_Frame=Frame(self.Menue_ButtonFrame,bg='cornsilk', bd=3,relief=SUNKEN)
		self.Buttons_Frame.grid(row=0,column=0,sticky=W)  #pack(side=LEFT)
		self.Label_Entries_Frame=Frame(self.Menue_ButtonFrame,bg='cornsilk', bd=3,relief=SUNKEN)
		self.Label_Entries_Frame.grid(row=0, column=1)   #pack(side=RIGHT)
		self.Label_SummeryButton_Frame=Frame(self.Menue_ButtonFrame,bg='cornsilk',width=550,bd=3,relief=SUNKEN)
		self.Label_SummeryButton_Frame.grid(row=1,column=0, sticky=W) #pack(side=BOTTOM)

		############################### Reset Button , Total Button, Exit Button ###################

		self.Total_Button=Button(self.Buttons_Frame, text="Total",bd=20, width=6, font=('arial', 16,'bold'),command = self.Total_Cost)
		self.Total_Button.grid(row=0,column=0, padx=10,pady=5)
		self.Reset_Button=Button(self.Buttons_Frame, text="Reset",bd=20, width=6, font=('arial', 16,'bold'), command= self.Reset_Boxes)
		self.Reset_Button.grid(row=0,column=1, padx=10,pady=5)
		self.Show_Sale_Button=Button(self.Buttons_Frame, text="Receipt ", width=8, state=DISABLED,bd=20,font=('arial', 16,'bold'), command=self.Receipt)
		self.Show_Sale_Button.grid(row=0,column=2, padx=10,pady=5)
		self.Exit_Button=Button(self.Buttons_Frame, text="Exit", width=5, bd=20,font=('arial', 16,'bold'),command = self.Exit_win2)
		self.Exit_Button.grid(row=0,column=3, padx=10,pady=5)
		self.TodaySale_Button=Button(self.Label_SummeryButton_Frame, text="Today Sales", bd=20,font=('arial', 16,'bold'),command = lambda: self.Today_Sale("TodaySummery")) # function at 1381
		self.TodaySale_Button.grid(row=0,column=0, padx=10,pady=5, sticky=W)
		self.btnTotal_Sales = Button(self.Label_SummeryButton_Frame, text="All Times Business Sales",bd=20,font=('arial', 16,'bold'),command=lambda:self.Today_Sale("Total Transactions"))
		self.btnTotal_Sales.grid(row=0, column=2, padx=10,pady=5, sticky=E)


		self.Menue_Frame = Frame(self.MainFram, bg='cornsilk', bd=15, width=1350,height=1350,relief=SUNKEN)
		self.Menue_Frame.pack(side=TOP,fill=BOTH, expand=1)
		self.Top3_CheckBox = Frame(self.Menue_Frame, bg='cornsilk', bd=15, relief=SUNKEN)
		self.Top3_CheckBox.pack(side=RIGHT,fill=BOTH, expand=1)
		self.Top2_CheckBox = Frame(self.Menue_Frame, bg='cornsilk', bd=15, relief=SUNKEN)
		self.Top2_CheckBox.pack(side=RIGHT,fill=BOTH, expand=1)
		self.Top1_CheckBox = Frame(self.Menue_Frame, bg='cornsilk', bd=15, relief=SUNKEN)
		self.Top1_CheckBox.pack(side=RIGHT,fill=BOTH, expand=1)

		
		######################################## CUSTOMER ORDERS ####################################################

		self.lblCustomerTitle= Label(self.CustomerTitleframe, bg='cornsilk',font=('apple chancery', 22, 'bold','italic'), text="SERVED The CUSTOMERS",bd=4, 
			fg='black', justify=CENTER)
		self.lblCustomerTitle.pack()

		global txt_f_name
		txt_f_name=""
		self.lblFull_Name = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="Full Name ", bg='cornsilk', fg='black')
		self.lblFull_Name.grid(row=1,column=0,sticky=W)
		self.txtFullname= Entry(self.Customer_EntryFrame, font=('arial',12,'bold'), bd=7, bg="white", insertwidth=2, justify='right', textvariable=self.E_Full_Name)
		self.txtFullname.grid(row=1,column=1,padx=4,pady=2,sticky=W)
		

		self.lblMobile = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="Mobile ", bg='cornsilk', fg='black')
		self.lblMobile.grid(row=2,column=0,sticky=W)
		self.txtMobile= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_Mobile , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txtMobile.grid(row=2,column=1,padx=4,pady=2,sticky=W)

		self.lblAddress = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="Address ", bg='cornsilk', fg='black')
		self.lblAddress.grid(row=3,column=0,sticky=W)
		self.txtAddress= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_Address , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txtAddress.grid(row=3,column=1,padx=4,pady=2,sticky=W)

		self.lblPostCode = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="PostCode", bg='cornsilk', fg='black')
		self.lblPostCode.grid(row=4,column=0,sticky=W)
		self.txtPostCode= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_PostCode , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txtPostCode.grid(row=4,column=1,padx=4,pady=2,sticky=W)

		self.lblCity = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="City ", bg='cornsilk', fg='black')
		self.lblCity.grid(row=5,column=0,sticky=W)
		self.txtCity= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_City , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txtCity.grid(row=5,column=1,padx=4,pady=2,sticky=W)

		self.lblState = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="State ", bg='cornsilk', fg='black')
		self.lblState.grid(row=6,column=0,sticky=W)
		self.txtState= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_State , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txtState.grid(row=6,column=1,padx=4,pady=2,sticky=W)

		self.lblDate = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="Date  ", bg='cornsilk', fg='black')
		self.lblDate.grid(row=7,column=0,sticky=W)  
		self.txtDate= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"), textvariable=self.E_Date , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txtDate.grid(row=7,column=1,padx=4,pady=2,sticky=W)

		self.lbl_Total_Cost = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="Total Cost  ", bg='cornsilk', fg='black')
		self.lbl_Total_Cost.grid(row=8,column=0,sticky=W)  
		self.txt_Total_Cost= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"), textvariable=self.E_Total_Cost , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txt_Total_Cost.grid(row=8,column=1,padx=4,pady=4,sticky=W)


		self.lbl_Pay_Method = Label(self.Customer_EntryFrame,font=('apple chancery', 14, 'bold'), text="Payment Method  ", bg='cornsilk', fg='black')
		self.lbl_Pay_Method.grid(row=9,column=0,sticky=W)  
		self.Payment_Drop = ttk.Combobox(self.Customer_EntryFrame,width=20, font=('arial', 12, 'bold'),value=["Cash Payment", "Card Payment "])
		self.Payment_Drop.current(0)
		self.Payment_Drop.grid(row=9, column = 1)

		#self.txt_Pay_Method= Entry(self.Customer_EntryFrame, font=("arial", 12, "bold"), textvariable=self.E_Payment_Method , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		#self.txt_Pay_Method.grid(row=9,column=1,padx=4,pady=4,sticky=W)

		############################## DataBase Entries Button #########################################################

		self.btnAdd = Button(self.Customer_Buttonframe, text="Add Record",bd=20,font=('arial', 14,'bold'), command= self.AddRecod)
		self.btnAdd.grid(row=0, column=0,padx=15,pady=4)
		self.btnDelete = Button(self.Customer_Buttonframe, text="Delete Record",bd=20,font=('arial', 14,'bold'),command=lambda:self.Today_Sale("Del"))
		self.btnDelete.grid(row=0, column=1,padx=15,pady=4)
		#self.btnTotal_Sales = Button(self.Customer_Buttonframe, text="Total Sales",bd=20,font=('arial', 14,'bold'),command=lambda:self.Today_Sale("Total Sales"))
		#self.btnTotal_Sales.grid(row=0, column=2,padx=2,pady=4)
		self.btnSearch = Button(self.Customer_Buttonframe, text="Edit / Search",font=('arial', 14,'bold'),command=lambda:self.Today_Sale("Search"))
		self.btnSearch.grid(row=0, column=3,padx=6,pady=4)

		############################## STARTERS #####################################################################
		self.lblMenueleft1= Label(self.Top1_CheckBox,text="Starters: ", font=('arial',12,'bold'),
			bg='cornsilk').grid(row=0,column=0, sticky=W)

		self.Potato_Wedges= Checkbutton(self.Top1_CheckBox,text="Potato Wedges  £3.50", variable=self.var1, onvalue=1, offvalue=0,font=('arial',10,'bold'),
			bg='cornsilk',command = self.Potato_Wedges)
		self.Potato_Wedges.grid(row=1,column=0, sticky=W, pady=2, padx=3)

		self.Onion_Rings= Checkbutton(self.Top1_CheckBox, text="Onion Rings  £2.50", variable=self.var2, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Onion_Rings).grid(row=2,column=0, sticky = W, pady=2, padx=3)

		self.Garlic_Bread = Checkbutton(self.Top1_CheckBox, text="Garlic Bread  £2.50", variable=self.var3, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Garlic_Bread).grid(row=3,sticky=W, pady=2, padx=3)

		self.Garlic_Bread_Cheese = Checkbutton(self.Top1_CheckBox, text="Garlic Bread & Cheese  £3.50", variable=self.var4, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Garlic_Bread_Cheese).grid(row=4,sticky=W, pady=2, padx=3)

		self.Chips = Checkbutton(self.Top1_CheckBox, text="Chips  £2.00", variable=self.var5, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Chips).grid(row=5,sticky=W, pady=2, padx=3)

		self.Chips_Cheese = Checkbutton(self.Top1_CheckBox, text="Chips Cheese  £3.00", variable=self.var6, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Chips_Cheese).grid(row=6,sticky=W, pady=2, padx=3)

		self.Hummus = Checkbutton(self.Top1_CheckBox, text="Hummus   £2.99", variable=self.var7, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Hummus).grid(row=7,sticky=W, pady=2, padx=3)

		self.Greek_Salad = Checkbutton(self.Top1_CheckBox, text="Greek Salad  £2.99", variable=self.var8, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Greek_Salad).grid(row=8,sticky=W, pady=2, padx=3)

		self.lblMenueleft2= Label(self.Top1_CheckBox,text="Rice: ", font=('arial',12,'bold'),
			bg='cornsilk').grid(row=9,column=0, sticky=W)

		self.Kabuli_Pulao = Checkbutton(self.Top1_CheckBox, text="Kabuli Pulao  £7.99", variable=self.var9, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Kabuli_Pulao).grid(row=10,sticky=W, pady=2, padx=3)

		self.Chicken_Biryani = Checkbutton(self.Top1_CheckBox, text="Chicken Biryani  £4.40 ", variable=self.var10, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chicken_Biryani).grid(row=11,sticky=W, pady=2, padx=3)

		self.Plain_Rice = Checkbutton(self.Top1_CheckBox, text="Plain Rice  £2.50", variable=self.var11, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command = self.Plain_Rice).grid(row=12,sticky=W, pady=2, padx=3)

		self.Large_Plain_Rice = Checkbutton(self.Top1_CheckBox, text="Large Plain Rice  £3.99", variable=self.var12, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Large_Plain_Rice).grid(row=13,sticky=W, pady=2, padx=3)

		self.Plain_Kabuli_Rice = Checkbutton(self.Top1_CheckBox, text="Plain Kabuli Rice £3.99", variable=self.var13, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk',command=self.Plain_Kabuli_Rice).grid(row=14,sticky=W, pady=2, padx=3)

		self.DrinksMenueleft= Checkbutton(self.Top1_CheckBox,text="Drinks:  £1.10", variable=self.var14, onvalue=1, offvalue=0, font=('arial',12,'bold'),
			bg='cornsilk',command=self.DrinksMenueleft).grid(row=15,column=0, sticky=W)

												############## ComboBox for each Order in Menue 1 ##########
		global drop1
		drop1 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop1.current(0)
		drop1.grid(row=1, column = 1)

		global drop2
		drop2 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop2.current(0)
		drop2.grid(row=2, column = 1)

		global drop3
		drop3 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop3.current(0)
		drop3.grid(row=3, column = 1)

		global drop4
		drop4 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop4.current(0)
		drop4.grid(row=4, column = 1)
		
		global drop5
		drop5 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop5.current(0)
		drop5.grid(row=5, column = 1)
		
		global drop6
		drop6 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop6.current(0)
		drop6.grid(row=6, column = 1)
		
		global drop7
		drop7 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop7.current(0)
		drop7.grid(row=7, column = 1)
		
		global drop8
		drop8 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop8.current(0)
		drop8.grid(row=8, column = 1)
		
		global drop9
		drop9 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop9.current(0)
		drop9.grid(row=10, column = 1)
		
		global drop10
		drop10 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop10.current(0)
		drop10.grid(row=11, column = 1)
		
		global drop11
		drop11 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop11.current(0)
		drop11.grid(row=12, column = 1)
		
		global drop12
		drop12 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop12.current(0)
		drop12.grid(row=13, column = 1)
		
		global drop13
		drop13 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop13.current(0)
		drop13.grid(row=14, column = 1)

		global drop14
		drop14 = ttk.Combobox(self.Top1_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop14.current(0)
		drop14.grid(row=15, column = 1)

				
		################################ LAMB DISHES #####################################################################

		self.lblMenueleft3= Label(self.Top2_CheckBox,text="Lamb Dishes: ", font=('arial',12,'bold'),
			bg='cornsilk').grid(row=0,column=0, sticky=W)
		self.Dampokh = Checkbutton(self.Top2_CheckBox, text="Dampokh(1kg 3h Notice req)  £18.00", variable=self.var15, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Dampokh).grid(row=1,sticky=W, pady=2, padx=3)
		self.Lamb_Charsi_Karahi = Checkbutton(self.Top2_CheckBox, text="Lamb Charsi Karahi(1/2 kg)  £11.99", variable=self.var16, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Lamb_Charsi_Karahi).grid(row=2,sticky=W, pady=2, padx=3)
		self.Namkeen_Karahi = Checkbutton(self.Top2_CheckBox, text="Namkeen Karahi (1/2)  £11.99", variable=self.var17, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Namkeen_Karahi).grid(row=3,sticky=W, pady=2, padx=3)
		self.Lamb_Shank_Rish = Checkbutton(self.Top2_CheckBox, text="Lamb Shank Rish  £9.99 ", variable=self.var18, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Lamb_Shank_Rish).grid(row=4,sticky=W, pady=2, padx=3)
		self.Nihari = Checkbutton(self.Top2_CheckBox, text="Nihari  £7.99", variable=self.var19, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Nihari).grid(row=5,sticky=W, pady=2, padx=3)
		self.Paya = Checkbutton(self.Top2_CheckBox, text="Paya  £5.99", variable=self.var20, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Paya).grid(row=6,sticky=W, pady=2, padx=3)
		self.Haleem = Checkbutton(self.Top2_CheckBox, text="Haleem £4.99", variable=self.var21, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Haleem).grid(row=7,sticky=W, pady=2, padx=3)
		self.Kobeda_Kebab_portion = Checkbutton(self.Top2_CheckBox, text="Kobeda Kebab Portion  £6.99", variable=self.var22, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Kobeda_Kebab_portion).grid(row=8,sticky=W, pady=2, padx=3)
		self.Grilled_Lamb_Chops = Checkbutton(self.Top2_CheckBox, text="Grilled Lamb Chops  £6.50", variable=self.var23, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Grilled_Lamb_Chops).grid(row=9,sticky=W, pady=2, padx=3)
		self.Chapli_Kebab = Checkbutton(self.Top2_CheckBox, text="Chapli Kebab (Single)  £1.99", variable=self.var24, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chapli_Kebab).grid(row=10,sticky=W, pady=2, padx=3)
		self.Chapli_Kebab_Meal = Checkbutton(self.Top2_CheckBox, text="Chapli Kebab Meal £6.99", variable=self.var25, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chapli_Kebab_Meal).grid(row=11,sticky=W, pady=2, padx=3)

		################################ Mix Grills  #####################################################################

		self.lblMenueleft5= Label(self.Top2_CheckBox,text="Mixed Grills: ", font=('arial',12,'bold'),
			bg='cornsilk').grid(row=12,column=0, sticky=W)
		self.Mixed_Grills = Checkbutton(self.Top2_CheckBox, text="Chicken Charsi Karahi(1/2kg) £7.50", variable=self.var26, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Mixed_Grills).grid(row=13,sticky=W, pady=2, padx=3)

		self.lblMenueleft6= Label(self.Top2_CheckBox,text="Sea Foods: ", font=('arial',12,'bold'),
			bg='cornsilk').grid(row=14,column=0, sticky=W)
		self.Sea_Food = Checkbutton(self.Top2_CheckBox, text="Sea Food(Lahori Masala Fish)  £9.99", variable=self.var27, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Sea_Food).grid(row=15,sticky=W, pady=2, padx=3)

												############## ComboBox for each Order in Menue 2 ##########
		global drop15
		drop15 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop15.current(0)
		drop15.grid(row=1, column = 1)

		global drop16
		drop16 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop16.current(0)
		drop16.grid(row=2, column = 1)
		
		global drop17
		drop17 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop17.current(0)
		drop17.grid(row=3, column = 1)
		
		global drop18
		drop18 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop18.current(0)
		drop18.grid(row=4, column = 1)
		
		global drop19
		drop19 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop19.current(0)
		drop19.grid(row=5, column = 1)
		
		global drop20
		drop20 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop20.current(0)
		drop20.grid(row=6, column = 1)
		
		global drop21
		drop21 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop21.current(0)
		drop21.grid(row=7, column = 1)
		
		global drop22
		drop22 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop22.current(0)
		drop22.grid(row=8, column = 1)
		
		global drop23
		drop23 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop23.current(0)
		drop23.grid(row=9, column = 1)
		
		global drop24
		drop24 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop24.current(0)
		drop24.grid(row=10, column = 1)
		
		global drop25
		drop25 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop25.current(0)
		drop25.grid(row=11, column = 1)
		
		global drop26
		drop26 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop26.current(0)
		drop26.grid(row=13, column = 1)

		global drop27
		drop27 = ttk.Combobox(self.Top2_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop27.current(0)
		drop27.grid(row=15, column = 1)

		################################ Chicken Dishes #####################################################################

		self.lblMenueleft4= Label(self.Top3_CheckBox,text="Chicken Dishes: ", font=('arial',12,'bold'),
			bg='cornsilk').grid(row=0,column=0, sticky=W)
		self.Chicken_Charsi_Karahi = Checkbutton(self.Top3_CheckBox, text="Chicken Charsi Karahi(hfkg) £7.50", variable=self.var28, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chicken_Charsi_Karahi).grid(row=1,sticky=W, pady=2, padx=3)
		self.Chicken_Tikka = Checkbutton(self.Top3_CheckBox, text="Chicken Tikka  £4.99", variable=self.var29, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chicken_Tikka).grid(row=2,sticky=W, pady=2, padx=3)
		self.Full_Chikken = Checkbutton(self.Top3_CheckBox, text="Full Chikken  £7.99", variable=self.var30, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Full_Chikken).grid(row=3,sticky=W, pady=2, padx=3)
		self.Half_Chicken = Checkbutton(self.Top3_CheckBox, text="Half Chicken  £4.99 ", variable=self.var31, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Half_Chicken).grid(row=4,sticky=W, pady=2, padx=3)
		self.Chicken_Legs = Checkbutton(self.Top3_CheckBox, text="Chicken Legs  £3.50", variable=self.var32, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chicken_Legs).grid(row=5,sticky=W, pady=2, padx=3)
		self.Chicken_Wings_Chips = Checkbutton(self.Top3_CheckBox, text="Chicken Wings & Chips  £4.50", variable=self.var33, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chicken_Wings_Chips).grid(row=6,sticky=W, pady=2, padx=3)
		self.Shwarma = Checkbutton(self.Top3_CheckBox, text="Shwarma £4.99", variable=self.var34, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Shwarma).grid(row=7,sticky=W, pady=2, padx=3)

		############################ Accompaniments #################

		self.lblMenueleft2= Label(self.Top3_CheckBox,text="Accompaniments: ", font=('arial',12,'bold'),
			bg='cornsilk').grid(row=8,column=0, sticky=W)
		self.Peshawari_Nan = Checkbutton(self.Top3_CheckBox, text="Peshawari Nan(Sweet) £2.99", variable=self.var35, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Peshawari_Nan).grid(row=9,sticky=W, pady=2, padx=3)
		self.Keema_Nan = Checkbutton(self.Top3_CheckBox, text="Keema Nan(Lamb)  £2.50", variable=self.var36, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Keema_Nan).grid(row=10,sticky=W, pady=2, padx=3)
		self.Roghani_Nan = Checkbutton(self.Top3_CheckBox, text="Roghani Nan  £1.50", variable=self.var37, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Roghani_Nan).grid(row=11,sticky=W, pady=2, padx=3)
		self.Garlic_Nan = Checkbutton(self.Top3_CheckBox, text="Garlic Nan  £1.50", variable=self.var38, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Garlic_Nan).grid(row=12,sticky=W, pady=2, padx=3)
		self.Chilli_Nan = Checkbutton(self.Top3_CheckBox, text="Chilli Nan  £1.50", variable=self.var39, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Chilli_Nan).grid(row=13,sticky=W, pady=2, padx=3)
		self.Cheese_Nan = Checkbutton(self.Top3_CheckBox, text="Cheese Nan  £2.50", variable=self.var40, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Cheese_Nan).grid(row=14,sticky=W, pady=2, padx=3)
		self.Plain_Nan = Checkbutton(self.Top3_CheckBox, text="Plain Nan £0.70", variable=self.var41, onvalue=1, offvalue=0, font=('arial',10,'bold'),
			bg='cornsilk', command=self.Plain_Nan).grid(row=15,sticky=W, pady=2, padx=3)
	

												############## ComboBox for each Order in Menue 2 ##########
		global drop28
		drop28 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop28.current(0)
		drop28.grid(row=1, column = 1)

		global drop29
		drop29 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop29.current(0)
		drop29.grid(row=2, column = 1)
		
		global drop30
		drop30 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop30.current(0)
		drop30.grid(row=3, column = 1)
		
		global drop31
		drop31 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop31.current(0)
		drop31.grid(row=4, column = 1)
		
		global drop32
		drop32 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop32.current(0)
		drop32.grid(row=5, column = 1)
		
		global drop33
		drop33 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop33.current(0)
		drop33.grid(row=6, column = 1)
		
		global drop34
		drop34 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2"],width=4,state=DISABLED)
		drop34.current(0)
		drop34.grid(row=7, column = 1)
		
		global drop35
		drop35 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop35.current(0)
		drop35.grid(row=9, column = 1)
		
		global drop36
		drop36 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop36.current(0)
		drop36.grid(row=10, column = 1)
		
		global drop37
		drop37 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop37.current(0)
		drop37.grid(row=11, column = 1)
		
		global drop38
		drop38 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop38.current(0)
		drop38.grid(row=12, column = 1)
		
		global drop39
		drop39 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop39.current(0)
		drop39.grid(row=13, column = 1)
		
		global drop40
		drop40 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop40.current(0)
		drop40.grid(row=14, column = 1)

		global drop41
		drop41 = ttk.Combobox(self.Top3_CheckBox, value=["0", "1", "2","3","4","5"],width=4,state=DISABLED)
		drop41.current(0)
		drop41.grid(row=15, column = 1)

		
		####################################### Total Cost ####################################################################

		self.lblCostofFoods = Label(self.Label_Entries_Frame,font=('arial', 12, 'bold'), text=" Cost of Foods: ", bg='cornsilk', fg='black')
		self.lblCostofFoods.grid(row=0,column=0,sticky=W)
		self.txtCostofFoods= Entry(self.Label_Entries_Frame, font=("arial", 12, "bold"), width=12,bd=7, bg="white", textvariable=self.CostofFoods , insertwidth=2, justify= RIGHT)
		self.txtCostofFoods.grid(row=0,column=1)

		self.lblCostofDrinks = Label(self.Label_Entries_Frame,font=('arial', 12, 'bold'), text=" Cost of Drinks: ", bg='cornsilk', fg='black')
		self.lblCostofDrinks.grid(row=0,column=2,sticky=W)  
		self.txtCostofDrinks= Entry(self.Label_Entries_Frame, font=("arial", 12, "bold"),width=12, textvariable=self.CostofDrinks , bd=7, bg="white", insertwidth=2, justify= RIGHT)
		self.txtCostofDrinks.grid(row=0,column=3)

		self.lblTotalCost = Label(self.Label_Entries_Frame,font=('arial', 12, 'bold'),  text=" Total Cost ",bd=7, bg='cornsilk', fg='black')
		self.lblTotalCost.grid(row=0,column=4, sticky=W)
		self.txtTotalCost = Entry(self.Label_Entries_Frame,font=('arial', 12, 'bold'), width=12,textvariable=self.TotalCost , bd=7, bg='white',insertwidth=2, justify=RIGHT)
		self.txtTotalCost.grid(row=0,column=5)

#################################################### Exit Window Function #############################

	def Exit_win2(self):
		self.master.destroy()

####################################################### Total Cost for the Customer ##########################
	def Total_Cost(self):
		#self.item1 = ("£ " + str(float(self.drop1.get()) * float(3.50)))
		self.item1 = float(drop1.get()) * float(3.50)
		self.item2 = float(drop2.get()) * float(2.50)
		self.item3 = float(drop3.get()) * float(2.50)
		self.item4 = float(drop4.get()) * float(3.50)
		self.item5 = float(drop5.get()) * float(2.00)
		self.item6 = float(drop6.get()) * float(3.00)
		self.item7 = float(drop7.get()) * float(2.99)
		self.item8 = float(drop8.get()) * float(2.99)
		self.item9 = float(drop9.get()) * float(7.99)
		self.item10 = float(drop10.get()) * float(4.40)
		self.item11 = float(drop11.get()) * float(2.50)
		self.item12 = float(drop12.get()) * float(3.99)
		self.item13= float(drop13.get()) * float(3.99)

		############# Drink Cost #######################
		self.item14 = float(drop14.get()) * float(1.10)

		self.item15 = float(drop15.get()) * float(18.00)
		self.item16 = float(drop16.get()) * float(11.99)
		self.item17 = float(drop17.get()) * float(11.99)
		self.item18 = float(drop18.get()) * float(9.99)
		self.item19 = float(drop19.get()) * float(7.99)
		self.item20 = float(drop20.get()) * float(5.99)
		self.item21 = float(drop21.get()) * float(4.99)
		self.item22 = float(drop22.get()) * float(6.99)
		self.item23 = float(drop23.get()) * float(6.50)
		self.item24 = float(drop24.get()) * float(1.99)
		self.item25 = float(drop25.get()) * float(6.99)
		self.item26 = float(drop26.get()) * float(7.50)
		self.item27 = float(drop27.get()) * float(9.99)


		self.item28 = float(drop28.get()) * float(7.50)
		self.item29= float(drop29.get()) * float(4.99)
		self.item30 = float(drop30.get()) * float(7.99)
		self.item31 = float(drop31.get()) * float(4.99)
		self.item32 = float(drop32.get()) * float(3.50)
		self.item33 = float(drop33.get()) * float(4.50)

		self.item34 = float(drop34.get()) * float(4.99)
		self.item35 = float(drop35.get()) * float(2.50)
		self.item36 = float(drop36.get()) * float(1.50)
		self.item37 = float(drop37.get()) * float(1.50)
		self.item38= float(drop38.get()) * float(1.50)
		self.item39 = float(drop39.get()) * float(2.50)
		self.item40 = float(drop40.get()) * float(3.00)
		self.item41 = float(drop41.get()) * float(0.70)

		global Total_Cost_forFood
		
		drinkcost ='£', str('%0.2f'%(self.item14))

		self.CostofDrinks.set(drinkcost)  ### Converted to 2 decimal point
		
		self.Total_Cost_forFood = ( self.item1 +  self.item2 +  self.item3 +  self.item4 +  self.item5 +  self.item6 +  self.item7 +  self.item8 + \
						 self.item9 +  self.item10 +  self.item11 +  self.item12 +  self.item13 +  self.item15 +  self.item16 +  self.item17 +  self.item18 + \
						  self.item19 +  self.item20 +  self.item21 +  self.item22 +  self.item23 +  self.item24 +  self.item25 +  self.item26 +  self.item27 + \
						   self.item28 +  self.item29 +  self.item30 +  self.item31 +  self.item32 +  self.item33 +  self.item34 +  self.item35 +  self.item36 + \
						    self.item37 +  self.item38 +  self.item39 +  self.item40 +  self.item41 )
		#self.TotalCost.set("£" + str(self.Total_Cost_forFood + self.item14))
		

		#CakePrice= '£', str('%0.2f'%(priceofcakes))
		#self.CostofFoods.set("£" + str(self.Total_Cost_forFood)) #without conversion to decimal point
		foodprice = '£', str('%0.2f'%(self.Total_Cost_forFood))
		self.CostofFoods.set(foodprice) # converted to 2 decimal points

		tprice = str('%0.2f'%((self.Total_Cost_forFood + self.item14)))
		self.TotalCost.set("£" + tprice)
		self.E_Total_Cost.set(tprice)
		if (self.Total_Cost_forFood >0 or self.item14 > 0):
			self.Show_Sale_Button=Button(self.Buttons_Frame, text="Receipt ",bd=20,font=('arial', 16,'bold'), command=self.Receipt)
			self.Show_Sale_Button.grid(row=0,column=2, padx=10,pady=5)
		#check = float(self.Total_Cost_forFood + self.item14) # this is a condition in Receipt function
		#localtotal = self.TotalCost.get()
		#totalprice = localtotal
		#print(totalprice)
		txt_f_name = self.txtFullname.get()
######################################### DataBase Functions ##########################################
	def AddRecod(self):

		if (str(self.E_Full_Name.get()) !='' and str(self.E_Address.get())!='' and str(self.E_PostCode.get()) !='' and str(self.E_Mobile.get()) !='' and str(self.E_Total_Cost.get())!=''):
		
			sql_command = " INSERT INTO Customers (Full_Name, Mobile, Address, PostCode, City, State, E_Date, E_Total_Cost, PaymentMethod) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			values = (str(self.E_Full_Name.get()), str(self.E_Mobile.get()), str(self.E_Address.get()), str(self.E_PostCode.get()), str(self.E_City.get()), str(self.E_State.get()), str(self.E_Date.get()), str(self.E_Total_Cost.get()),str(self.Payment_Drop.get()))
			my_cursor.execute(sql_command, values)
			mydb.commit()

			#clear all fields after data submission
			self.E_Mobile.set("")
			self.E_Full_Name.set("")
			self.E_Address.set("")
			self.E_PostCode.set("")
			#print(self.E_City.get())
			#self.E_State.set("")
			self.E_Total_Cost.set("")
			print(my_cursor.rowcount, "record inserted.")
		else:
			tkinter.messagebox.showwarning("Warning !! ", "Please Check, Full Records have not been Entered!!")

		
		

################################################ Reset all boxes #######################################
	def Reset_Boxes(self):
		self.var1.set("0")
		self.var2.set("0")
		self.var3.set("0")
		self.var4.set("0")
		self.var5.set("0")
		self.var6.set("0")
		self.var7.set("0")
		self.var8.set("0")
		self.var9.set("0")
		self.var10.set("0")
		self.var11.set("0")
		self.var12.set("0")
		self.var13.set("0")
		self.var14.set("0")
		self.var15.set("0")
		self.var16.set("0")
		self.var17.set("0")
		self.var18.set("0")
		self.var19.set("0")
		self.var20.set("0")
		self.var21.set("0")
		self.var22.set("0")
		self.var23.set("0")
		self.var24.set("0")
		self.var25.set("0")
		self.var26.set("0")
		self.var27.set("0")
		self.var28.set("0")
		self.var29.set("0")
		self.var30.set("0")
		self.var31.set("0")
		self.var32.set("0")
		self.var33.set("0")
		self.var34.set("0")
		self.var35.set("0")
		self.var36.set("0")
		self.var37.set("0")
		self.var38.set("0")
		self.var39.set("0")
		self.var40.set("0")
		self.var41.set("0")
		
		drop1.set(0)
		drop1.configure(state=DISABLED)
		drop2.set(0)
		drop2.configure(state=DISABLED)
		drop3.set(0)
		drop3.configure(state=DISABLED)
		drop4.set(0)
		drop4.configure(state=DISABLED)
		drop5.set(0)
		drop5.configure(state=DISABLED) 
		drop6.set(0)
		drop6.configure(state=DISABLED) 
		drop7.set(0)
		drop7.configure(state=DISABLED) 
		drop8.set(0)
		drop8.configure(state=DISABLED)
		drop9.set(0)
		drop9.configure(state=DISABLED)
		drop10.set(0)
		drop10.configure(state=DISABLED)
		drop11.set(0)
		drop11.configure(state=DISABLED)
		drop12.set(0)
		drop12.configure(state=DISABLED)
		drop13.set(0)
		drop13.configure(state=DISABLED) 
		drop14.set(0)
		drop14.configure(state=DISABLED) 
		drop15.set(0)
		drop15.configure(state=DISABLED) 
		drop16.set(0)
		drop16.configure(state=DISABLED)
		drop17.set(0)
		drop17.configure(state=DISABLED)
		drop18.set(0)
		drop18.configure(state=DISABLED)
		drop19.set(0)
		drop19.configure(state=DISABLED)
		drop20.set(0)
		drop20.configure(state=DISABLED)
		drop21.set(0)
		drop21.configure(state=DISABLED) 
		drop22.set(0)
		drop22.configure(state=DISABLED) 
		drop23.set(0)
		drop23.configure(state=DISABLED)
		drop24.set(0) 
		drop24.configure(state=DISABLED)
		drop25.set(0)
		drop25.configure(state=DISABLED)
		drop26.set(0)
		drop26.configure(state=DISABLED)
		drop27.set(0)
		drop27.configure(state=DISABLED)
		drop28.set(0)
		drop28.configure(state=DISABLED)
		drop29.set(0)
		drop29.configure(state=DISABLED) 
		drop30.set(0)
		drop30.configure(state=DISABLED) 
		drop31.set(0)
		drop31.configure(state=DISABLED) 
		drop32.set(0)
		drop32.configure(state=DISABLED)
		drop33.set(0)
		drop33.configure(state=DISABLED)
		drop34.set(0)
		drop34.configure(state=DISABLED)
		drop35.set(0)
		drop35.configure(state=DISABLED)
		drop36.set(0)
		drop36.configure(state=DISABLED)
		drop37.set(0)
		drop37.configure(state=DISABLED) 
		drop38.set(0)
		drop38.configure(state=DISABLED) 
		drop39.set(0)
		drop39.configure(state=DISABLED) 
		drop40.set(0)
		drop40.configure(state=DISABLED)
		drop41.set(0)
		drop41.configure(state=DISABLED)


		self.CostofDrinks.set("")
		self.TotalCost.set("")
		self.CostofFoods.set("")

		self.Show_Sale_Button=Button(self.Buttons_Frame, text="Receipt ", state=DISABLED,bd=20,font=('arial', 16,'bold'), command=self.Receipt)
		self.Show_Sale_Button.grid(row=0,column=2, padx=10,pady=5)

		#self.E_Date.set("")
		#self.E_State.set("")
		#self.E_City.set("")
		check = 0
		self.TotalCost.set("")
		self.E_Total_Cost.set("")

######################################################## First Menue Functions #########################

	def Potato_Wedges(self):
		if(self.var1.get()==1):
			drop1.configure(state=NORMAL)
			drop1.focus()
			drop1.set(1)
		else:
			drop1.configure(state = DISABLED)
			drop1.set(0)

	def Onion_Rings(self):
		if(self.var2.get()==1):
			drop2.configure(state=NORMAL)
			drop2.focus()
			drop2.set(1)
		else:
			drop2.configure(state = DISABLED)
			drop2.set(0) 	
								# When you uncheck the Check combobox, the dropbox will come automatically to 0

	def Garlic_Bread(self):
		if(self.var3.get()==1):
			drop3.configure(state=NORMAL)
			drop3.focus()
			drop3.set(1)	
		else:
			drop3.configure(state = DISABLED)
			drop3.set(0)

	def Garlic_Bread_Cheese(self):
		if(self.var4.get()==1):
			drop4.configure(state=NORMAL)
			drop4.focus()
			drop4.set(1)	
		else:
			drop4.configure(state = DISABLED)
			drop4.set(0)

	def Chips(self):
		if(self.var5.get()==1):
			drop5.configure(state=NORMAL)
			drop5.focus()
			drop5.set(1)	
		else:
			drop5.configure(state = DISABLED)
			drop5.set(0)

	def Chips_Cheese(self):
		if(self.var6.get()==1):
			drop6.configure(state=NORMAL)
			drop6.focus()
			drop6.set(1)	
		else:
			drop6.configure(state = DISABLED)
			drop6.set(0)

	def Hummus(self):
		if(self.var7.get()==1):
			drop7.configure(state=NORMAL)
			drop7.focus()
			drop7.set(1)	
		else:
			drop7.configure(state = DISABLED)
			drop7.set(0)

	def Greek_Salad(self):
		if(self.var8.get()==1):
			drop8.configure(state=NORMAL)
			drop8.focus()
			drop8.set(1)	
		else:
			drop8.configure(state = DISABLED)
			drop8.set(0)

	def Kabuli_Pulao(self):
		if(self.var9.get()==1):
			drop9.configure(state=NORMAL)
			drop9.focus()
			drop9.set(1)	
		else:
			drop9.configure(state = DISABLED)
			drop9.set(0)

	def Chicken_Biryani(self):
		if(self.var10.get()==1):
			drop10.configure(state=NORMAL)
			drop10.focus()
			drop10.set(1)	
		else:
			drop10.configure(state = DISABLED)
			drop10.set(0)


	def Plain_Rice(self):
		if(self.var11.get()==1):
			drop11.configure(state=NORMAL)
			drop11.focus()
			drop11.set(1)	
		else:
			drop11.configure(state = DISABLED)
			drop11.set(0)

	def Large_Plain_Rice(self):
		if(self.var12.get()==1):
			drop12.configure(state=NORMAL)
			drop12.focus()
			drop12.set(1)	
		else:
			drop12.configure(state = DISABLED)
			drop12.set(0)

	def Plain_Kabuli_Rice(self):
		if(self.var13.get()==1):
			drop13.configure(state=NORMAL)
			drop13.focus()
			drop13.set(1)	
		else:
			drop13.configure(state = DISABLED)
			drop13.set(0)

	def DrinksMenueleft(self):
		if(self.var14.get()==1):
			drop14.configure(state=NORMAL)
			drop14.focus()
			drop14.set(1)	
		else:
			drop14.configure(state = DISABLED)
			drop14.set(0)
##################################################### Second Menue Functions ########################################################

	def Dampokh(self):
		if(self.var15.get()==1):
			drop15.configure(state=NORMAL)
			drop15.focus()
			drop15.set(1)	
		else:
			drop15.configure(state = DISABLED)
			drop15.set(0)

	def Lamb_Charsi_Karahi(self):
		if(self.var16.get()==1):
			drop16.configure(state=NORMAL)
			drop16.focus()
			drop16.set(1)	
		else:
			drop16.configure(state = DISABLED)
			drop16.set(0)

	def Namkeen_Karahi(self):
		if(self.var17.get()==1):
			drop17.configure(state=NORMAL)
			drop17.focus()
			drop17.set(1)	
		else:
			drop17.configure(state = DISABLED)
			drop17.set(0)

	def Lamb_Shank_Rish(self):
		if(self.var18.get()==1):
			drop18.configure(state=NORMAL)
			drop18.focus()
			drop18.set(1)	
		else:
			drop18.configure(state = DISABLED)
			drop18.set(0)

	def Nihari(self):
		if(self.var19.get()==1):
			drop19.configure(state=NORMAL)
			drop19.focus()
			drop19.set(1)

		else:
			drop19.configure(state = DISABLED)
			drop19.set(0)

	def Paya(self):
		if(self.var20.get()==1):
			drop20.configure(state=NORMAL)
			drop20.focus()
			drop20.set(1)	
		else:
			drop20.configure(state = DISABLED)
			drop20.set(0)

	def Haleem(self):
		if(self.var21.get()==1):
			drop21.configure(state=NORMAL)
			drop21.focus()
			drop21.set(1)	
		else:
			drop21.configure(state = DISABLED)
			drop21.set(0)

	def Kobeda_Kebab_portion(self):
		if(self.var22.get()==1):
			drop22.configure(state=NORMAL)
			drop22.focus()
			drop22.set(1)	
		else:
			drop22.configure(state = DISABLED)
			drop22.set(0)

	def Grilled_Lamb_Chops(self):
		if(self.var23.get()==1):
			drop23.configure(state=NORMAL)
			drop23.focus()
			drop23.set(1)	
		else:
			drop23.configure(state = DISABLED)
			drop23.set(0)

	def Chapli_Kebab(self):
		if(self.var24.get()==1):
			drop24.configure(state=NORMAL)
			drop24.focus()
			drop24.set(1)	
		else:
			drop24.configure(state = DISABLED)
			drop24.set(0)

	def Chapli_Kebab_Meal(self):
		if(self.var25.get()==1):
			drop25.configure(state=NORMAL)
			drop25.focus()
			drop25.set(1)	
		else:
			drop25.configure(state = DISABLED)
			drop25.set(0)

	def Mixed_Grills(self):
		if(self.var26.get()==1):
			drop26.configure(state=NORMAL)
			drop26.focus()
			drop26.set(1)	
		else:
			drop26.configure(state = DISABLED)
			drop26.set(0)

	def Sea_Food(self):
		if(self.var27.get()==1):
			drop27.configure(state=NORMAL)
			drop27.focus()
			drop27.set(1)	
		else:
			drop27.configure(state = DISABLED)
			drop27.set(0)

############################################### Third Menue Funtions ##########################################


	def Chicken_Charsi_Karahi(self):
		if(self.var28.get()==1):
			drop28.configure(state=NORMAL)
			drop28.focus()
			drop28.set(1)	
		else:
			drop28.configure(state = DISABLED)
			drop28.set(0)

	def Chicken_Tikka(self):
		if(self.var29.get()==1):
			drop29.configure(state=NORMAL)
			drop29.focus()
			drop29.set(1)	
		else:
			drop29.configure(state = DISABLED)
			drop29.set(0)

	def Full_Chikken(self):
		if(self.var30.get()==1):
			drop30.configure(state=NORMAL)
			drop30.focus()
			drop30.set(1)	
		else:
			drop30.configure(state = DISABLED)
			drop30.set(0)

	def Half_Chicken(self):
		if(self.var31.get()==1):
			drop31.configure(state=NORMAL)
			drop31.focus()
			drop31.set(1)	
		else:
			drop31.configure(state = DISABLED)
			drop31.set(0)

	def Chicken_Legs(self):
		if(self.var32.get()==1):
			drop32.configure(state=NORMAL)
			drop32.focus()
			drop32.set(1)	
		else:
			drop32.configure(state = DISABLED)
			drop32.set(0)

	def Chicken_Wings_Chips(self):
		if(self.var33.get()==1):
			drop33.configure(state=NORMAL)
			drop33.focus()
			drop33.set(1)	
		else:
			drop33.configure(state = DISABLED)
			drop33.set(0)

	def Shwarma(self):
		if(self.var34.get()==1):
			drop34.configure(state=NORMAL)
			drop34.focus()
			drop34.set(1)	
		else:
			drop34.configure(state = DISABLED)
			drop34.set(0)

	def Peshawari_Nan(self):
		if(self.var35.get()==1):
			drop35.configure(state=NORMAL)
			drop35.focus()
			drop35.set(1)	
		else:
			drop35.configure(state = DISABLED)
			drop35.set(0)

	def Keema_Nan(self):
		if(self.var36.get()==1):
			drop36.configure(state=NORMAL)
			drop36.focus()
			drop36.set(1)	
		else:
			drop36.configure(state = DISABLED)
			drop36.set(0)

	def Roghani_Nan(self):
		if(self.var37.get()==1):
			drop37.configure(state=NORMAL)
			drop37.focus()
			drop37.set(1)	
		else:
			drop37.configure(state = DISABLED)
			drop37.set(0)

	def Garlic_Nan(self):
		if(self.var38.get()==1):
			drop38.configure(state=NORMAL)
			drop38.focus()
			drop38.set(1)	
		else:
			drop38.configure(state = DISABLED)
			drop38.set(0)

	def Chilli_Nan(self):
		if(self.var39.get()==1):
			drop39.configure(state=NORMAL)
			drop39.focus()
			drop39.set(1)	
		else:
			drop39.configure(state = DISABLED)
			drop39.set(0)

	def Cheese_Nan(self):
		if(self.var40.get()==1):
			drop40.configure(state=NORMAL)
			drop40.focus()
			drop40.set(1)	
		else:
			drop40.configure(state = DISABLED)
			drop40.set(0)

	def Plain_Nan(self):
		if(self.var41.get()==1):
			drop41.configure(state=NORMAL)
			drop41.focus()
			drop41.set(1)	
		else:
			drop41.configure(state = DISABLED)
			drop41.set(0)

	######################################## Receipt for the Shopping #####################################

	def Receipt(self):

		check =  self.Total_Cost_forFood + self.item14
		if (check > 0):
			self.newWindow = Toplevel(self.master)
			self.app = Window3(self.newWindow)
		else:
			tkinter.messagebox.showwarning("Warning !! ", "Sorry No Shopping has been listed yet ¡¡")

	################################### Today Sale Function ############################################
	def Today_Sale(self,message): # button at 299

		self.message = message
		self.newWindow = Toplevel(self.master)
		self.app = Window4(self.newWindow,self.message)
		

class Window4:
	def __init__(self,master,message):
		self.master = master
		self.message = message
		self.today = date.today()
		self.master.title("Welcome to Khyber Pass " + str(self.today))
		self.master.configure(bg='cornsilk')
		
		
		if (self.message == "TodaySummery"):
			self.master.geometry('1100x550+0+0')
			sql = "SELECT * FROM Customers WHERE E_Date = %s ORDER BY E_Total_Cost DESC"
			name = (self.today,)    # i will investigate the brakets
			result = my_cursor.execute(sql, name)
			result = my_cursor.fetchall()

			#my_cursor.execute("SELECT * FROM Customers ORDER BY E_Total_Cost DESC") #By default its always coming in accending order i.e from low to high  
			#result = my_cursor.fetchall()
			#print(result)
		
			#Full_Name, Mobile, Address, PostCode, City, State, E_Date,E_Total_Cost, PaymentMethod
			self.RecordsFrame = Frame(self.master, bg='cornsilk', bd=20, relief='ridge')
			self.RecordsFrame.pack()

			self.lblsalesummery = Label(self.RecordsFrame, text="Today's Sale Summery",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblsalesummery.grid(row=0,column=0)
			self.lbldate = Label(self.RecordsFrame, text=self.today,bg='cornsilk',font=('apple chancery', 18, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lbldate.grid(row=1,column=0)

			self.Top_Title4 = Frame(self.master, bg='cornsilk', bd=20, relief='ridge')
			self.Top_Title4.pack()
		

			self.lblFull_Name = Label(self.Top_Title4, bg='cornsilk',text="Full Name",font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblFull_Name.grid(row=0,column=0)

			self.lblMobile = Label(self.Top_Title4, text="Mobile",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblMobile.grid(row=0,column=1)

			self.lblAddress = Label(self.Top_Title4, text="Address",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblAddress.grid(row=0,column=2)

			self.lblPostCode = Label(self.Top_Title4, text="PostCode",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblPostCode.grid(row=0,column=3)
		
			self.lblCity = Label(self.Top_Title4, text="City",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblCity.grid(row=0,column=4)
			self.lblState = Label(self.Top_Title4, text="State",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblState.grid(row=0,column=5)
			self.lblDate = Label(self.Top_Title4, text="Date",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblDate.grid(row=0,column=6)
			self.lblTotalCost = Label(self.Top_Title4, text="TotalCost",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblTotalCost.grid(row=0,column=7)

			self.lbl_Pay_Method = Label(self.Top_Title4,bg='cornsilk', text="Payment Method",font=('apple chancery', 16, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lbl_Pay_Method.grid(row=0,column=8)

			self.lblcustomer_ID = Label(self.Top_Title4,bg='cornsilk', text="Customer_ID",font=('apple chancery', 16, 'bold','italic'),bd=10,
				fg ='black', justify=CENTER )
			self.lblcustomer_ID.grid(row=0,column=9)

			def btn_Return_To_Main():
				self.master.destroy()

			Total_Sale = 0
			for index, x in enumerate(result): 
				index += 1
				col = 0
				for y in x:
					if col ==7:
						Total_Sale += float(y)
						self.lblcustomersRecord = Label(self.Top_Title4, text=y ,font=('times new roman', 14),bd=2,
						fg ='black',bg='light green' , justify=CENTER)
						self.lblcustomersRecord.grid(row= index,column=col)
					else:
						self.lblcustomersRecord = Label(self.Top_Title4, text=y ,font=('Times new roman', 12),bd=2,
							fg ='black',bg='cornsilk' )
						self.lblcustomersRecord.grid(row= index,column=col,sticky=W)
					col +=1

			self.lblcustomersRecord = Label(self.Top_Title4, text="<--------------------->" ,font=('apple chancery', 14, 'bold','italic'),bd=2,
				fg ='black',bg='cornsilk' )
			self.lblcustomersRecord.grid(row= index+1,column=col-3,sticky=W)

			self.lblcustomersRecord = Label(self.Top_Title4, text="Today Sale" ,font=('apple chancery', 14, 'bold','italic'),bd=2,
				fg ='black',bg='cornsilk' , justify=CENTER)
			self.lblcustomersRecord.grid(row= index+2,column=col-4)
			self.lblcustomersRecord = Label(self.Top_Title4, text="£"+ str('%0.2f'%(float(Total_Sale))) ,font=('apple chancery', 18, 'bold','italic'),bd=2,
				fg ='black',bg='cornsilk' , justify=CENTER)
			self.lblcustomersRecord.grid(row= index+2,column=col-3)
			btn_Return_To_Main=Button(self.Top_Title4, text="ReturnToMain",font=('apple chancery', 16, 'bold','italic'), command=btn_Return_To_Main)
			btn_Return_To_Main.grid(row=index+2, column=col)
			

		# Delete Function
		if (self.message == "Del"):
			self.master.geometry('1350x550+0+0')
			self.RecordsFrame = Frame(self.master, bg='cornsilk', bd=20, relief='ridge')
			self.RecordsFrame.pack()
			self.RecordsSummaryFrame = Frame(self.master, bg='cornsilk', bd=20, relief='ridge')
			self.RecordsSummaryFrame.pack()

			self.lblsalesummery = Label(self.RecordsFrame, text="Deleting Records",bg='cornsilk',font=('apple chancery', 20, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblsalesummery.grid(row=0,column=0)
			#Entry box for search to customer
			search_box=Entry(self.RecordsFrame)
			search_box.grid(row=2, column=1, pady=10, padx=10)
			#entry box label
			search_box_label=Label(self.RecordsFrame, text="Search..",font=("Ariel", 12, 'bold'))
			search_box_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
			#drop down box
			drop = ttk.Combobox(self.RecordsFrame, value=["search by...","Customer ID", "Mobile"],font=("Ariel", 12, 'bold'))
			drop.current(0)
			drop.grid(row=2, column = 2)

			def Search_Record(): # Called from line 1524
				selected = drop.get()
				sql = ""
				if selected == "search by...":
					test = Label(self.RecordsFrame, text="Hey you forgot to pick the right selection!!")
					test.grid(row = 4, column=0)

				if selected == "Customer ID":
					sql = "SELECT * FROM Customers WHERE Customer_ID = %s"

				if selected == "Mobile":
					sql = "SELECT * FROM Customers WHERE Mobile = %s"

				searched = search_box.get()
				name = (searched,)    
				result = my_cursor.execute(sql, name)
				result = my_cursor.fetchall()
				
				if not result:
					result="Sorry No Record has been found for this " + str(drop.get())+ ". Try other option or check in all time sales"
					searched_label=Label(self.RecordsFrame, text= result,bg='cornsilk',font=('apple chancery', 18, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					searched_label.grid(row=4, column=0)
				else:

					#labels for searched records columns
					self.lblFull_Name = Label(self.RecordsSummaryFrame, bg='cornsilk',text="Full Name",font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblFull_Name.grid(row=1,column=1)

					self.lblMobile = Label(self.RecordsSummaryFrame, text="Mobile",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblMobile.grid(row=1,column=2)

					self.lblAddress = Label(self.RecordsSummaryFrame, text="Address",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblAddress.grid(row=1,column=3)

					self.lblPostCode = Label(self.RecordsSummaryFrame, text="PostCode",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblPostCode.grid(row=1,column=4)
		
					self.lblCity = Label(self.RecordsSummaryFrame, text="City",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblCity.grid(row=1,column=5)
					self.lblState = Label(self.RecordsSummaryFrame, text="State",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblState.grid(row=1,column=6)
					self.lblDate = Label(self.RecordsSummaryFrame, text="Date",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblDate.grid(row=1,column=7)
					self.lblTotalCost = Label(self.RecordsSummaryFrame, text="TotalCost",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblTotalCost.grid(row=1,column=8)

					self.lbl_Pay_Method = Label(self.RecordsSummaryFrame,bg='cornsilk', text="Payment Method",font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lbl_Pay_Method.grid(row=1,column=9)

					self.lblcustomer_ID = Label(self.RecordsSummaryFrame,bg='cornsilk', text="Customer_ID",font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblcustomer_ID.grid(row=1,column=10)

					for index, x in enumerate(result): #for enumerate watch video 31
						col = 0
						index +=2 
						id_reference = str(x[9])
						Delete_button=Button(self.RecordsSummaryFrame, text="Delete " + id_reference,fg ='Red',font=("apple chancery", 16 , 'bold'),bd=30, command=lambda:Delete_now(id_reference))
						Delete_button.grid(row=index, column=col, padx=10, sticky=W)
						for y in x:
							searched_label=Label(self.RecordsSummaryFrame, text= y,bg='cornsilk',font=('Times new roman', 12),bd=2,
							fg ='black', justify=CENTER)
							searched_label.grid(row=index, column=col+1,pady=10)
							col +=1
					#self.btnGoBack= Button(self.RecordsSummaryFrame, text="Return to MainMenue",bg='cornsilk',font=('apple chancery', 20, 'bold','italic'),bd=10,
						#fg ='black', justify=CENTER , command=GoBack)
					#self.btnGoBack.grid(row=index+1, column=col+1)
			def Delete_now(id):
				#search_customers.geometry("1500x1100")
				self.exit = tkinter.messagebox.askyesno("Warning! ","Are you sure, you want to delete this Record?")
				if self.exit > 0:
					sql2 = "DELETE FROM Customers WHERE Customer_ID = %s"
					name2 = (id,)    # i will investigate the braket
					my_cursor.execute(sql2, name2)
					#result2 = my_cursor.fetchall()
					mydb.commit()
					#print(my_cursor).rowcount, " Record deleted"
					tkinter.messagebox.showwarning("You are Welcome !! ", "Your Record has been deleted.")
					self.master.destroy()
				
				else:
					self.master.destroy()
				
			#entry box search button for customer
			search_button=Button(self.RecordsFrame, text="Search Record",font=("Ariel", 16,'bold'),fg="black", bd=30, command= Search_Record)
			search_button.grid(row = 3, column=0, padx=10, pady=15)
		
		#Full_Name, Mobile, Address, PostCode, City, State, E_Date,E_Total_Cost, PaymentMethod
		# Total Sales Function in TEXT widget
		if (self.message == "Total Transactions"):
			self.master.geometry('1450x750+0+0')
			self.SalesTitle_Top_Frame = Frame(self.master,bd=20, bg='cornsilk', relief='ridge')
			self.SalesTitle_Top_Frame.pack(side = TOP)
			self.lblTotal_Sales = Label(self.SalesTitle_Top_Frame, text="All Time Business Sale",bg='cornsilk',font=('apple chancery', 24, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblTotal_Sales.grid(row=0,column=0)

			self.Total_Sales_Frame = Frame(self.master, bg='cornsilk',bd=30, relief='ridge')
			self.Total_Sales_Frame.pack(side = TOP)
			self.Return_Button_Frame = Frame(self.master, bg='cornsilk',bd=10, relief='ridge')
			self.Return_Button_Frame.pack(side = TOP)
			

			scroll = Scrollbar(self.Total_Sales_Frame)
			scroll.pack(side=RIGHT, fill=Y)

			textbox=Text(self.Total_Sales_Frame, yscrollcommand=scroll.set,width=200,height=35)
			textbox.pack(side=LEFT)
			textbox.delete("1.0","end")
			textbox.insert('end',"\tFull Name\t\t\t Mobile\t\t  Address\t\t\t PostCode\t\t City\t\t State\t\t Data\t \tTotal Cost\t\t Payment Method\t\t\t Customer ID\t\n ")
			#for i in range(1,100):
				#textbox.insert(END, "list "+str(i) + "\n")
			scroll.config(command=textbox.yview)

			def btn_Return_To_Main():
				self.master.destroy()

			sql = "SELECT * FROM Customers ORDER BY E_Date " #DESC"
			result = my_cursor.execute(sql)
			result = my_cursor.fetchall()

			for index, x in enumerate(result): #for enumerate watch video 31 
				textbox.insert('end',"\t" +str(result[index][0])+ "\t\t\t" + str(result[index][1]) + "\t\t" + str(result[index][2])  + "\t\t\t" + str(result[index][3]) 
					+ "\t\t" + str(result[index][4]) +  "\t\t" + str(result[index][5]) + "\t\t" + str(result[index][6]) + "\t\t" + str(result[index][7]) + "\t\t"+ "   " 
					+ str(result[index][8]) + "\t\t\t" +"   "+ str(result[index][9]) + "\t\n ")
			
			Return_Button = Button(self.Return_Button_Frame, text="ReturnToMain",font=('apple chancery', 14, 'bold','italic'), width=20,command = btn_Return_To_Main)
			Return_Button.pack()




		# Total Sales Function in Frame Widget but it wont work untill you select the condition in button to "Total sales" instead of "Total Transactions"
		if (self.message == "Total Sales"):
			self.master.geometry('1450x650+0+0')
			self.SalesTitle_Top_Frame = Frame(self.master, bg='cornsilk',bd=4, relief='ridge')
			self.SalesTitle_Top_Frame.pack()
			self.lblTotal_Sales = Label(self.SalesTitle_Top_Frame, text="All Time Business Records",bg='cornsilk',font=('apple chancery', 24, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblTotal_Sales.grid(row=0,column=0)

			sql = "SELECT * FROM Customers ORDER BY E_Total_Cost DESC"

			result = my_cursor.execute(sql)
			result = my_cursor.fetchall()
			
			#if not result:
				#tkinter.messagebox("Alert!", "Sorry No Record has been found")
			#else:

			self.RecordsSummaryFrame = Frame(self.master, bg='cornsilk', bd=4,relief='ridge')
			self.RecordsSummaryFrame.pack()
			
			self.lblFull_Name = Label(self.RecordsSummaryFrame, bg='cornsilk',text="Full Name",font=('apple chancery', 14, 'bold','italic'),bd=10,
			fg ='black')
			self.lblFull_Name.grid(row=1,column=0 , sticky=W)

			self.lblMobile = Label(self.RecordsSummaryFrame, text="Mobile",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black')
			self.lblMobile.grid(row=1,column=1, sticky=W)

			self.lblAddress = Label(self.RecordsSummaryFrame, text="Address",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black' )
			self.lblAddress.grid(row=1,column=2, sticky=W)

			self.lblPostCode = Label(self.RecordsSummaryFrame, text="PostCode",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black')
			self.lblPostCode.grid(row=1,column=3, sticky=W)
		
			self.lblCity = Label(self.RecordsSummaryFrame, text="City",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black')
			self.lblCity.grid(row=1,column=4, sticky=W)
			self.lblState = Label(self.RecordsSummaryFrame, text="State",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black')
			self.lblState.grid(row=1,column=5, sticky=W)
			self.lblDate = Label(self.RecordsSummaryFrame, text="Date",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black' )
			self.lblDate.grid(row=1,column=6, sticky=W)
			self.lblTotalCost = Label(self.RecordsSummaryFrame, text="TotalCost",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black' )
			self.lblTotalCost.grid(row=1,column=7, sticky=W)

			self.lbl_Pay_Method = Label(self.RecordsSummaryFrame,bg='cornsilk', text="Payment Method",font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black')
			self.lbl_Pay_Method.grid(row=1,column=8, sticky=W)

			self.lblcustomer_ID = Label(self.RecordsSummaryFrame,bg='cornsilk', text="Customer_ID",font=('apple chancery', 14, 'bold','italic'),bd=10,
				fg ='black' )
			self.lblcustomer_ID.grid(row=1,column=9, sticky=W)

			def btn_Return_To_Main():
				self.master.destroy()

			for index, x in enumerate(result): #for enumerate watch video 31
				col = 0
				index +=2 
				
				for y in x:
					
					searched_label=Label(self.RecordsSummaryFrame, text= y,bg='cornsilk',font=('Times new roman', 12),
						fg ='black')
					searched_label.grid(row=index, column=col,pady=2,sticky=W)
					col +=1	
			btn_Return_To_Main=Button(self.RecordsSummaryFrame, text="ReturnToMain",font=('apple chancery', 14, 'bold','italic'), command=btn_Return_To_Main)
			btn_Return_To_Main.grid(row=index+1, column=col+1)




		# Search Function
		if(self.message == "Search"):
			self.master.geometry('1450x650+0+0')
			self.Fram4All= Frame(self.master, bg='cornsilk', bd=20, width=1450, height=500, relief='ridge')
			self.Fram4All.pack()
			self.Titel_Frame = Frame(self.Fram4All, bg='cornsilk', bd=20, relief='ridge')
			self.Titel_Frame.pack()

			self.lblsalesummery = Label(self.Titel_Frame, text="Search / Edit Records",bg='cornsilk',font=('apple chancery', 30, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblsalesummery.grid(row=0,column=0)

			self.Holder4Summary_and_Editer = Frame(self.Fram4All, bg='cornsilk', bd=20, width=1380, height=500, relief='ridge')
			self.Holder4Summary_and_Editer.pack(side=LEFT)
			self.RecordsEditFrame = Frame(self.Fram4All, bg='cornsilk', bd=20, relief='ridge')
			self.RecordsEditFrame.pack(side=RIGHT)

			self.RecordsFrame = Frame(self.Holder4Summary_and_Editer, bg='cornsilk', bd=20, relief='ridge')
			self.RecordsFrame.pack(side=TOP) #grid(row=0,column=0)

			#Entry box for search to customer
			search_box=Entry(self.RecordsFrame)
			search_box.grid(row=0, column=1, pady=10, padx=10)
			#entry box label
			search_box_label=Label(self.RecordsFrame, text="Search..",font=("Ariel", 12, 'bold'))
			search_box_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
			#drop down box
			drop = ttk.Combobox(self.RecordsFrame, value=["search by...", "Customer Name", "Customer ID", "Mobile"],font=("Ariel", 12, 'bold'))
			drop.current(0)
			drop.grid(row=0, column = 2)
			self.RecordsSummaryFrame = Frame(self.Holder4Summary_and_Editer, bg='cornsilk', bd=20, relief='ridge')
			self.RecordsSummaryFrame.pack(side=LEFT)
			
			
			


			def Update():

				#print("i am in Update")
				seq_command = """ UPDATE Customers SET Full_Name = %s, Mobile = %s, Address = %s, PostCode = %s, City = %s, State = %s, E_Date = %s, E_Total_Cost = %s, PaymentMethod =%s WHERE Customer_ID = %s"""
				#Full_Name, Mobile, Address, PostCode, City, State, E_Date,E_Total_Cost, PaymentMethod
				Full_Name =txtFullname.get()
				Mobile =txtMobile.get()
				Address =txtAddress.get()
				PostCode=txtPostCode.get()
				City=txtCity.get()
				State=txtState.get()
				E_Date=txtDate.get()
				E_Total_Cost=txt_Total_Cost.get()
				PaymentMethod=txtpayment_Method.get()
				Customer_ID = txt_Customer_ID.get()

				inputs = (Full_Name, Mobile, Address, PostCode, City, State, E_Date,E_Total_Cost, PaymentMethod, Customer_ID )
				my_cursor.execute(seq_command, inputs)
				mydb.commit()

				txtFullname.delete(0, END)
				txtMobile.delete(0, END)
				txtAddress.delete(0, END)
				txtPostCode.delete(0, END)
				txtCity.delete(0, END)
				txtState.delete(0, END)
				txtDate.delete(0, END)
				txt_Total_Cost.delete(0, END)
				txtpayment_Method.delete(0, END)
				txt_Customer_ID.delete(0, END)

			def Search_Record(): # Called from line 1524
				selected = drop.get()
				sql = ""
				if selected == "search by...":
					test = Label(self.RecordsFrame, text="Hey you forgot to pick the right selection!!")
					test.grid(row = 4, column=0)

				if selected == "Customer Name":
					sql = "SELECT * FROM Customers WHERE Full_Name = %s"
					

				if selected == "Customer ID":
					sql = "SELECT * FROM Customers WHERE Customer_ID = %s"

				if selected == "Mobile":
					sql = "SELECT * FROM Customers WHERE Mobile = %s"

				searched = search_box.get()
				name = (searched,)    # i will investigate the brakets
				result = my_cursor.execute(sql, name)
				result = my_cursor.fetchall()
				
				if not result:
					result="Sorry No Record has been found for this " + str(drop.get())+ ". Try other option or check in all time sales"
					searched_label=Label(self.RecordsFrame, text= result,bg='cornsilk',font=('apple chancery', 18, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					searched_label.grid(row=4, column=0)
				else:

					#labels for searched records columns
					self.lblFull_Name = Label(self.RecordsSummaryFrame, bg='cornsilk',text="Full Name",font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblFull_Name.grid(row=1,column=1)

					self.lblMobile = Label(self.RecordsSummaryFrame, text="Mobile",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblMobile.grid(row=1,column=2)

					self.lblAddress = Label(self.RecordsSummaryFrame, text="Address",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblAddress.grid(row=1,column=3)

					self.lblPostCode = Label(self.RecordsSummaryFrame, text="PostCode",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblPostCode.grid(row=1,column=4)
		
					self.lblCity = Label(self.RecordsSummaryFrame, text="City",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblCity.grid(row=1,column=5)
					self.lblState = Label(self.RecordsSummaryFrame, text="State",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lblState.grid(row=1,column=6)
					self.lblDate = Label(self.RecordsSummaryFrame, text="Date",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblDate.grid(row=1,column=7)
					self.lblTotalCost = Label(self.RecordsSummaryFrame, text="TotalCost",bg='cornsilk',font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblTotalCost.grid(row=1,column=8)

					self.lbl_Pay_Method = Label(self.RecordsSummaryFrame,bg='cornsilk', text="Payment Method",font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER)
					self.lbl_Pay_Method.grid(row=1,column=9)

					self.lblcustomer_ID = Label(self.RecordsSummaryFrame,bg='cornsilk', text="Customer_ID",font=('apple chancery', 14, 'bold','italic'),bd=10,
						fg ='black', justify=CENTER )
					self.lblcustomer_ID.grid(row=1,column=10)

					for index, x in enumerate(result): #for enumerate watch video 31
						col = 0
						index +=2 
						id_reference = str(x[9])
						edit_button=Button(self.RecordsSummaryFrame, text="Edit " + id_reference,font=("Ariel", 16, 'bold'),fg="black", command=lambda:edit_now(id_reference))
						edit_button.grid(row=index, column=col, padx=10, sticky=W)
						for y in x:
							searched_label=Label(self.RecordsSummaryFrame, text= y,bg='cornsilk',font=('Times new roman', 12),bd=2,
							fg ='black', justify=CENTER)
							searched_label.grid(row=index, column=col+1,pady=10)
							col +=1

			def GoBack():
				self.master.destroy()
			#entry box search button for customer
			search_button=Button(self.RecordsFrame, text="Search Record",font=("Ariel", 16, 'bold'),fg="black", bd=30, command= Search_Record)
			search_button.grid(row = 3, column=0, padx=10, pady=15)

				#Edit slected record
			def edit_now(id):
				
				sql2 = "SELECT * FROM Customers WHERE Customer_ID = %s"
				name2 = (id,)    # i will investigate the braket
				result2 = my_cursor.execute(sql2, name2)
				result2 = my_cursor.fetchall()
				#print("result2"+ str(result2))
				txtFullname.insert(0,result2[0][0])
				txtMobile.insert(0,result2[0][1])
				txtAddress.insert(0,result2[0][2])
				txtPostCode.insert(0,result2[0][3])
				txtCity.insert(0,result2[0][4])
				txtState.insert(0,result2[0][5])
				txtDate.insert(0,result2[0][6])
				txt_Total_Cost.insert(0,result2[0][7])
				txtpayment_Method.insert(0,result2[0][8])
				txt_Customer_ID.insert(0,result2[0][9])

			# Labels and Entries Boxes for Editing records
			lblFull_Name = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="Full Name ", bg='cornsilk', fg='black')
			lblFull_Name.grid(row=1,column=0,sticky=W)
			txtFullname= Entry(self.RecordsEditFrame, font=('arial',12,'bold'), bd=7, bg="white", insertwidth=2, justify='right')
			txtFullname.grid(row=1,column=1,padx=4,pady=2,sticky=W)
		

			lblMobile = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="Mobile ", bg='cornsilk', fg='black')
			lblMobile.grid(row=2,column=0,sticky=W)
			txtMobile= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txtMobile.grid(row=2,column=1,padx=4,pady=2,sticky=W)

			lblAddress = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="Address ", bg='cornsilk', fg='black')
			lblAddress.grid(row=3,column=0,sticky=W)
			txtAddress= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txtAddress.grid(row=3,column=1,padx=4,pady=2,sticky=W)

			lblPostCode = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="PostCode", bg='cornsilk', fg='black')
			lblPostCode.grid(row=4,column=0,sticky=W)
			txtPostCode= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txtPostCode.grid(row=4,column=1,padx=4,pady=2,sticky=W)

			lblCity = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="City ", bg='cornsilk', fg='black')
			lblCity.grid(row=5,column=0,sticky=W)
			txtCity= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txtCity.grid(row=5,column=1,padx=4,pady=2,sticky=W)

			lblState = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="State ", bg='cornsilk', fg='black')
			lblState.grid(row=6,column=0,sticky=W)
			txtState= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txtState.grid(row=6,column=1,padx=4,pady=2,sticky=W)

			lblDate = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="Date  ", bg='cornsilk', fg='black')
			lblDate.grid(row=7,column=0,sticky=W)  
			txtDate= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txtDate.grid(row=7,column=1,padx=4,pady=2,sticky=W)

			lbl_Total_Cost = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="Total Cost  ", bg='cornsilk', fg='black')
			lbl_Total_Cost.grid(row=8,column=0,sticky=W)  
			txt_Total_Cost= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txt_Total_Cost.grid(row=8,column=1,padx=4,pady=4,sticky=W)

			lblPayMent_Method = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="Date  ", bg='cornsilk', fg='black')
			lblPayMent_Method.grid(row=9,column=0,sticky=W)  
			txtpayment_Method= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txtpayment_Method.grid(row=9,column=1,padx=4,pady=2,sticky=W)

			lbl_Customer_ID = Label(self.RecordsEditFrame,font=('apple chancery', 14, 'bold'), text="Customer_ID", bg='cornsilk', fg='black')
			lbl_Customer_ID.grid(row=10,column=0,sticky=W)  
			txt_Customer_ID= Entry(self.RecordsEditFrame, font=("arial", 12, "bold") , bd=7, bg="white", insertwidth=2, justify= RIGHT)
			txt_Customer_ID.grid(row=10,column=1,padx=4,pady=4,sticky=W)
			Update_button=Button(self.RecordsEditFrame, text="Update Record " ,font=("Ariel", 16, 'bold'),fg="black",command= Update)
			Update_button.grid(row=11, column=0, padx=10, sticky=E)

class Window3:
	def __init__(self,master):
		self.master = master
		self.master.title("Customer Detailed Receipt")
		self.master.configure(bg='cornsilk')
		self.master.geometry('750x750+0+0')
		self.today = date.today()
		print(txt_f_name)
		l = [("Potato Wedges £3.50",drop1.get(),3.50),("Onion Rings £2.50",drop2.get(),2.50),("Garlic Bread £2.50",drop3.get(),2.50),("Garlic Bread Cheese £3.50",drop4.get(),3.50),
		("Chips £2.00",drop5.get(),2.00),("Chips Cheese £3.00",drop6.get(),3.00),("Hummus £2.99",drop7.get(),2.99),("Greek Salad £2.99",drop8.get(),2.99),("Kabuli Pulao £7.99",drop9.get(),7.99)
		,("Chicken Biryani £4,40",drop10.get(),4.40),("Plain Rice £2.50",drop11.get(),2.50),("Large Plain Rice £3.99",drop12.get(),3.99),("Plain Kabuli Rice £3,99",drop13.get(),3.99),
		("Cost of Drink £1.10",drop14.get(),1.10),("Dampokh £18.00",drop15.get(),18.00),("Lamb Charsi Karahi £11.99",drop16.get(),11.99),("Namkeen Karahi £11.99",drop17.get(),11.99),("Lamb Shank Rish £9.99",drop18.get(),9.99), ("Nihari £7.99",drop19.get(),7.99), ("Paya £5.99",drop20.get(),5.99)
				 , ("Haleem £4.99",drop21.get(),4.99), ("Kobeda_Kebab_portion £6.99",drop22.get(),6.99), ("Grilled Lamb Chops £6.50",drop23.get(),6.50), 
				 ("Chapli_Kebab single £1.99",drop24.get(),1.99), ("Chapli Kebab Meal £6.99",drop25.get(),6.99), ("Chicken Charsi Karahi 1/2 £7.50",drop26.get(),7.50)
				 , ("Sea_Food £9.99",drop27.get(),9.99), ("Chicken Charsi Karahi £7.50",drop28.get(),7.50), ("Chicken Tikka £4.99",drop29.get(),4.99), 
				 ("Full_Chikken £7.99",drop30.get(),7.99), ("Half_Chicken £4.99",drop31.get(),4.99), ("Chicken Legs £3.50",drop32.get(),3.50)
				 , ("Chicken Wings Chips £4.50",drop33.get(),4.50), ("Shwarma £4.99",drop34.get(),4.99), ("Peshawari Nan(Sweet) £2.99",drop35.get(),2.99), 
				 ("Keema Nan £2.50",drop36.get(),2.50), ("Roghani Nan £1.50",drop37.get(),1.50), ("Garlic Nan £1.50",drop38.get(),1.50)
				 , ("Chilli_Nan £1.50",drop39.get(),1.50), ("Cheese Nan £2.50",drop40.get(),2.50), ("Plain Nan £0.70",drop41.get(),0.70)]

		#print(l)

		self.MainFram = Frame(self.master, bg='cornsilk', bd=20, pady=4,relief='ridge')
		self.MainFram.pack()

		self.Receipt_Title_Frame = Frame(self.MainFram, bg='powder blue', bd=20, relief='ridge')
		self.Receipt_Title_Frame.pack(side=TOP)
		self.lblReceipt= Label(self.Receipt_Title_Frame, text="Customer Receipt",bg='cornsilk',font=('apple chancery', 30, 'bold','italic'),bd=10,
			fg ='black', justify=CENTER )
		self.lblReceipt.pack()

		self.Employee_Receipt_Ref = StringVar()
		self.randomref = IntVar()

		r = random.randint(10900, 609235)

		self.randomref= str(r)
		self.Employee_Receipt_Ref.set("Mehar" + self.randomref) #  Employee Random IDref created


		self.Receipt_Detail_Frame =Frame(self.MainFram, bg='cornsilk', bd=20, pady=4,relief='ridge')
		self.Receipt_Detail_Frame.pack(side=TOP)
		self.Print_Frame =Frame(self.MainFram, bg='cornsilk', bd=20, pady=4,relief='ridge')
		self.Print_Frame.pack(side=TOP)


		self.scroll = Scrollbar(self.Receipt_Detail_Frame)
		self.scroll.pack(side=RIGHT, fill=Y)
		self.textbox=Text(self.Receipt_Detail_Frame, yscrollcommand=self.scroll.set,width=190)
		self.textbox.pack(side=LEFT)
		

			#Address\t\t\t PostCode\t\t City\t\t State\t\t Data\t \tTotal Cost\t\t Payment Method\t\t\t Customer ID\t\n ")	
		self.scroll.config(command=self.textbox.yview)


		self.textbox.delete("1.0","end")
		self.textbox.insert('end', "\n\n\n" )
		self.textbox.insert('end',"\t\t\t\t\tCustomer Receipt\t\t\t"  + "\n\n\n" )
		self.textbox.insert('end',"\tSale Date:\t\t\t" + str(self.today) + "\t\n" )
		self.textbox.insert('end',"\tCustomer Attender:\t\t\t" + "Mehar Ullah" + "\t\n" )
		self.textbox.insert('end',"\tAttender ID:\t\t\t" + str("Meh" + self.randomref) + "\n\n\n\n" )
		self.textbox.insert('end',"\tDishes:\t\t\t\t\t" + "Quantity\t\t\t\t" + "Price\t\t\t" + "\n" )

		totalprice = 0.00
		#r = 4
		for index, x in enumerate(l): #for enumerate watch video 31
			col = 0
			for y in x:

				if (int(l[index][1]) > 0):

					if(int(l[index][2] == y)):
						totalprice += float(l[index][1])*y
						self.textbox.insert('end',  "£"+ str('%0.2f'%(float(y)*float(l[index][1]))) +"\t\n" )
					else:
						if (col==0):
							self.textbox.insert('end',"\t" + str(y) + "\t\t\t\t")
						else:
							self.textbox.insert('end', str(y) + "\t\t\t")
			col +=1
			
		totalprice = str('%0.2f'%(totalprice))

		self.textbox.insert('end', "\n\n\t\t\t\t\t\t\t\t" + "Total Cost:    £" + str(totalprice))

		self.btnReceipt= Button(self.Print_Frame, text="Print The Receipt",bg='cornsilk',font=('apple chancery', 18, 'bold','italic'),bd=10,
			fg ='black', justify=CENTER, command= self.Print )
		self.btnReceipt.pack()


	def Print(self):
		#tkinter.messagebox.showwarning("Warning !! ", "Please first Attach the Printer")
		hold = self.textbox.get("1.0", "end-1c")
		filename = tempfile.mktemp(".doc")
		open (filename, "w").write (hold)
		os.startfile(filename, "print")
		
		


	
		

if __name__ == '__main__':
	root = Tk()
	global r 
	global check
	global l
	global totalprice
	
	application = Window(root)

	root.mainloop()



