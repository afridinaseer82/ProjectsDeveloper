from tkinter import *
import mysql.connector
import random
from tkinter import ttk
import tkinter.messagebox
import datetime
from datetime import date
import time
import tempfile, os
from PIL import ImageTk,Image

class LoginWindow:
	def __init__(self, master):
		self.master = master
		today = date.today()
		self.master.title("Taxi Login Details")
		#self.master.iconbitmap(me.ico)
		self.master.configure(bg= 'gainsboro')
		self.master.geometry('950x550+260+100')
		self.frame = Frame(self.master, bg='gainsboro')
		self.frame.pack()

		global mydb
		global my_cursor
		mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "asmanoorme456654",
		database = "Rent_Taxi_DATABASE",
			)
		#check to see if the connection to mysql was created
		#print(mydb)

		#creat a cursor and initialize it
		my_cursor = mydb.cursor()

		#Create a database
		#my_cursor.execute("CREATE DATABASE Rent_Taxi_DATABASE")

		#TEST to see if database was created
		#my_cursor.execute("SHOW DATABASES")
		#for a in my_cursor:
			#print(a)

		#my_cursor.execute("DROP DATABASE Rent_Taxi_DATABASE")
		#Drop a table. this will delete the table which may or we may not want...instead we shod alter it..we do it below
		#my_cursor.execute("DROP TABLE Drivers")
		#my_cursor.execute("DROP TABLE Taxi_Registration")
		#my_cursor.execute("DROP TABLE Taxi_Rent")
		#Database Names list
		
		#Full_Name DOB Mobile Address PostCode City State Registration_Date
		#Create a Table and after run comment it becos we only create tabel once
		

		#Driver_ID Registration_No Pay_Date  Pay_Day Weekly_Access Weekly_Rent
		my_cursor.execute("CREATE TABLE IF NOT EXISTS Drivers (Full_Name VARCHAR(255),\
			DOB VARCHAR(255),\
			Mobile VARCHAR(255), \
			Address VARCHAR(255), \
			PostCode VARCHAR(255),\
			City VARCHAR(255),\
			State VARCHAR(255),\
			Registration_Date VARCHAR(255),\
			P_D VARCHAR(255),\
			Status VARCHAR(255),\
			Week_R VARCHAR(255),\
			Week_A VARCHAR(255),\
			Driver_ID INT AUTO_INCREMENT PRIMARY KEY)")

			#P_D VARCHAR(255),\
			#Status VARCHAR(255),\
			#Week_R VARCHAR(255),\
			#Week_A VARCHAR(255),\


		my_cursor.execute("CREATE TABLE IF NOT EXISTS Taxi_Registration (Driver_ID INT,\
			Car_Millage VARCHAR(255),\
			Registration_No VARCHAR(255),\
			Car_Colour VARCHAR(255),\
			Car_Manufacturer VARCHAR(255),\
			Car_Made_In VARCHAR(255),\
			Transmission VARCHAR(255),\
			Engine_Size VARCHAR(255),\
			Fuel_Type VARCHAR(255),\
			Taxi_ID INT AUTO_INCREMENT PRIMARY KEY)")
			
		my_cursor.execute("CREATE TABLE IF NOT EXISTS Taxi_Rent (Driver_ID INT,\
			Pay_Date VARCHAR(255),\
			Pay_Day VARCHAR(255),\
			Weekly_Access VARCHAR(255),\
			Weekly_Rent VARCHAR(255),\
			Rent_ID INT AUTO_INCREMENT PRIMARY KEY)")

		#Alter table
# once we alter it then hide it cose every time we dont alter the table
		#my_cursor.execute("ALTER TABLE Drivers ADD (\
		#VARCHAR(255),\
		#address_1 VARCHAR(255),\
		#address_2 VARCHAR(255),\
		#city VARCHAR(50),\
		#state VARCHAR(50),\
		#country VARCHAR(255),\
		#phone VARCHAR(255),\
		#payment_method VARCHAR(50),\
		#discount_code VARCHAR(255))")

		SQL = "SELECT  Drivers.Driver_ID,\
		Drivers.Full_Name, Drivers.Address,Drivers.City,\
		Drivers.State, Drivers.Mobile,Taxi_Registration.Registration_No,\
		Drivers.P_D FROM Drivers  INNER JOIN Taxi_Registration ON Drivers.Driver_ID = Taxi_Registration.Driver_ID;"
		result = my_cursor.execute(SQL)
		result = my_cursor.fetchall()
		#for r in result:
			#print (r)


		##SQL = "SELECT  Drivers.Driver_ID,Taxi_Rent.Rent_ID,Drivers.Full_Name,Taxi_Rent.Weekly_Rent, Taxi_Rent.Weekly_Access, Taxi_Rent.Pay_Date, Drivers.Mobile,Drivers.City FROM Drivers  INNER JOIN Taxi_Rent ON Drivers.Driver_ID = Taxi_Rent.Driver_ID;"
		#result = my_cursor.execute(SQL)
		#result = my_cursor.fetchall()



		#command = " SELECT Drivers.Full_Name AS Driver, Taxi_Rent.Pay_Date AS Pay_Date FROM Drivers \
		#INNER JOIN Taxi_Rent ON Drivers.Driver_ID = Taxi_Rent.Driver_ID"
		#my_cursor.execute(command)
		#result = my_cursor.fetchall()
		#for x in result:
			# print(x)

		#print(result)

		#Show everything in table
		#my_cursor.execute("SELECT * FROM Taxi_Rent")
		#print(my_cursor.description)
		#also through for loop
		#for things in my_cursor.description:
			#print(things)
		sql_command = "SELECT * FROM Drivers"
		result = my_cursor.execute(sql_command)
		result = my_cursor.fetchall()
		#print(result)
		sql_command = "SELECT * FROM Taxi_Rent"
		result = my_cursor.execute(sql_command)
		result = my_cursor.fetchall()
		#for row in result:
		#print(result)
		
		#self.label1=Label(self.frame,text= today,font=('arial',35,'bold'), bg='cornsilk',fg='black')
		#self.label1.grid(row = 0, column=3, pady=4)
		#global self.lock 
		self.lock = 0
		#lock += 1
		#print(lock)
		self.Username = StringVar()
		self.Password = StringVar()

		self.lblTitle = Label(self.frame, text="Private Hire Taxi Login System.", 
			font=('apple chancery',50,'bold'), bg='gainsboro',fg='black')
		self.lblTitle.grid(row=0, column=0, columnspan=1, pady =4)
		self.lblTitle1 = Label(self.frame, text=today, font=('apple chancery',30,'bold'), bg='gainsboro',fg='black')
		self.lblTitle1.grid(row=1, column=0, columnspan=2, sticky = S, pady=10)

		#======================================================================================================

		self.Loginframe1 = LabelFrame(self.frame, width=1350, height=600,
			font=('arial', 20, 'bold'), bg='gainsboro', bd=20,relief=SUNKEN)
		self.Loginframe1.grid(row=2,column=0,pady=4)

		self.Loginframe2 = LabelFrame(self.frame, width=1350, height=600,
			font=('arial', 20, 'bold'), bg='gainsboro', bd=20,relief=SUNKEN)
		self.Loginframe2.grid(row=3,column=0)

		#================================ Label and Entries =============================================================
		self.lblUsername=Label(self.Loginframe1, text= 'Username', font=('arial', 20,'bold'), bd=22,
			bg='gainsboro', fg='gainsboro')
		self.lblUsername.grid(row=0, column=0)
		self.txtUsername=Entry(self.Loginframe1 , textvariable=self.Username, font=('arial', 20,'bold'))
		self.txtUsername.grid(row=0, column=1,padx=119)


		self.lblPassword=Label(self.Loginframe1, text= 'Password', font=('arial', 20,'bold'), bd=22,
			bg='gainsboro', fg='gainsboro')
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
			self.app = FrontWindow(self.newWindow)
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
			command = self.New_Window

	def New_Window(self):
		self.newWindow = Toplevel(self.master)
		self.app = Window2(self.newWindow)

class FrontWindow:
	def __init__(self,master):
		self.master = master
		self.master.title("Taxi Private Hire Glasgwo Ltd.")
		self.master.configure(bg='gainsboro')
		self.master.geometry('1350x1060+150+100')
		self.today = date.today()

		global my_label
		global button_backward
		global button_forward

		self.Title_Frame = Frame(self.master, bg='gainsboro', height=80, bd=20, relief=SUNKEN)
		self.Title_Frame.pack( fill=X)
		self.lblTitle_Frame= Label(self.Title_Frame, bg='gainsboro',font=('apple chancery', 30, 'bold','italic'), text="Welcom T0 Hampden Taxi Private Hire Glasgow",bd=1, 
			fg='black', justify=CENTER)

		self.lblTitle_Frame.pack( fill=BOTH, expand=1)
		self.MainFram = Frame(self.master, bg='gainsboro', bd=20, pady=4, width=1050, height=1050,relief=SUNKEN)
		self.MainFram.pack(fill=BOTH, expand = 1)
		self.Right_Holder_Frame=Frame(self.MainFram, bg='gainsboro', bd=15, width=850, height=400, pady=4,relief=SUNKEN)
		self.Right_Holder_Frame.pack(side=RIGHT,fill=BOTH,expand=1)

		self.Pictures_Frame=Frame(self.Right_Holder_Frame, bg='gainsboro', bd=15, width=850, height=400, pady=4)
		self.Pictures_Frame.pack(side=TOP,fill=BOTH,expand=1)

		self.Button_Frame=Frame(self.MainFram, bg='gainsboro', bd=15, width=300, height=540, pady=4,relief=SUNKEN)
		self.Button_Frame.pack(side=LEFT,fill=Y)

		self.pic_bottom_frame=Frame(self.Right_Holder_Frame, bg='gainsboro', bd=15, width=300, height=40, pady=4)
		self.pic_bottom_frame.pack(side=TOP,fill=X)

		###########################################.  All Buttons on the Right Frames

		self.Task5_frame= Frame(self.Button_Frame, bg='gainsboro',bd=15, pady=4,relief=SUNKEN) ###### relief ridge check later
		self.Task5_frame.pack(side=TOP)
		self.btnDrivers_Registration_Details = Button(self.Task5_frame, text="Drivers Registration Forms",width=28,height=3,font=('arial', 14,'bold'),command=  lambda:self.One_For_All("New Registration"))#lambda:self.One_For_All("New Registration"))
		self.btnDrivers_Registration_Details.grid(row=0, column=0,padx=2,pady=4)
		#self.btnTotal_Sales = Button(self.Label_SummeryButton_Frame, text="All Times Business Sales",bd=20,font=('arial', 16,'bold'),command=lambda:self.Today_Sale("Total Transactions"))
		#self.btnTotal_Sales.grid(row=0, column=2, padx=10,pady=5, sticky=E)


		self.Task4_frame= Frame(self.Button_Frame, bg='gainsboro',bd=15, pady=4,relief=SUNKEN) ###### relief ridge check later
		self.Task4_frame.pack(side=TOP)
		self.btnDriverExitAgreement = Button(self.Task4_frame , text="Exit Agreement", width=28,height=3,bd=20,font=('arial', 14,'bold'),command=lambda:self.One_For_All("TAXI DRIVERS Agreement"))# ,command=lambda:self.One_For_All("Drivers Profile") )
		self.btnDriverExitAgreement.grid(row=0, column=0,padx=2,pady=4)

		self.Task1_frame= Frame(self.Button_Frame, bg='gainsboro',bd=15, pady=4,relief=SUNKEN) ###### relief ridge check later
		self.Task1_frame.pack(side=TOP)
		self.btnAllTaxiDrivers = Button(self.Task1_frame, text="All Taxi Drivers", width=28,height=3, font=('arial', 14,'bold'),command=lambda:self.One_For_All("ALL TAXI DRIVERS"))#,command=lambda:self.Today_Sale("Search"))
		self.btnAllTaxiDrivers.grid(row=0, column=0,padx=2,pady=4)

		self.Task2_frame= Frame(self.Button_Frame, bg='gainsboro',bd=15, pady=4,relief=SUNKEN) ###### relief ridge check later
		self.Task2_frame.pack(side=TOP)
		self.btnPay_The_Rent = Button(self.Task2_frame, text="Pay The Rent", width=28,height=3,font=('arial', 14,'bold'),command=lambda:self.One_For_All("Pay_The_Rent"))
		self.btnPay_The_Rent.grid(row=0, column=0,padx=2,pady=4)
		#self.Task3_frame= Frame(self.Button_Frame, bg='cornsilk',bd=15, pady=4,relief=SUNKEN) ###### relief ridge check later
		#self.Task3_frame.pack(side=TOP)
		#self.btnEdit_Driver_Details = Button(self.Task3_frame, text="Update Drivers Details",width=28,height=3,font=('arial', 14,'bold'))#,command=lambda:self.Today_Sale("Search"))
		#self.btnEdit_Driver_Details.grid(row=0, column=0,padx=2,pady=4)
		

		############################################ Images uploading 

		self.button_backward = Button(self.pic_bottom_frame, text="<<",width=15,height=2, font=('arial', 12,'bold'),state= DISABLED, command= self.backward)
		self.button_backward.grid(row=0, column=0,padx=90,pady=10)
		self.button_forward = Button(self.pic_bottom_frame, text= ">>",width=15,height=2,font=('arial', 12,'bold'), command= lambda: self.forward(2))
		self.button_forward.grid(row=0, column=3, padx=90,pady=10)
		self.my_image1 = ImageTk.PhotoImage(Image.open("CarImages/i1.png"))
		self.my_image2 = ImageTk.PhotoImage(Image.open("CarImages/i2.png"))
		self.my_image3 = ImageTk.PhotoImage(Image.open("CarImages/i3.png"))
		self.my_image4 = ImageTk.PhotoImage(Image.open("CarImages/i4.png"))
		self.my_image5 = ImageTk.PhotoImage(Image.open("CarImages/i5.png"))
		self.my_image6 = ImageTk.PhotoImage(Image.open("CarImages/i6.png"))

		self.image_list = [self.my_image1,self.my_image2,self.my_image3,self.my_image4,self.my_image5,self.my_image6]
		self.my_label= Label(self.Pictures_Frame, image=self.my_image1,relief=SUNKEN,bd=10)
		self.my_label.grid(row =0, column =0, columnspan = 3, padx = 100, pady= 50)
		self.statusbar = Label(self.pic_bottom_frame,height=2,width=15, bg='gainsboro',relief=SUNKEN,bd=2, text = "Image " + str(1) + " of " + str(len(self.image_list)), justify=CENTER)
		self.statusbar.grid(row=0,column=2, padx=90,pady=10)

	def forward(self, image_number):
		self.image_number = image_number
		self.my_label.grid_forget()
		self.my_label = Label(self.Pictures_Frame, image= self.image_list[self.image_number-1],relief=SUNKEN,bd=10)
		self.my_label.grid(row=0, column=0, columnspan=3, padx = 100, pady= 50)

		self.button_forward= Button(self.pic_bottom_frame, text=">>", width=15,height=2,font=('arial', 12,'bold'),command=lambda: self.forward(self.image_number+1))
		self.button_backward = Button(self.pic_bottom_frame, text="<<",width=15,height=2,font=('arial', 12,'bold'), command = lambda:self.backward(self.image_number-1))
		self.statusbar = Label(self.pic_bottom_frame,height=2,width=15, bg='gainsboro', text ="Image " + str(self.image_number) + " of " + str(len(self.image_list)), bd=1, relief=SUNKEN, justify=CENTER)
		if self.image_number == 6:
			self.button_forward = Button(self.pic_bottom_frame,width=15,font=('arial', 12,'bold'), height=2,text=">>", state=DISABLED)
		self.button_backward.grid(row=0, column=0, padx=90,pady=10)
		self.button_forward.grid(row=0, column=3, padx=90,pady=10)
		self.statusbar.grid(row=0,column=2, padx=90,pady=10)


	def backward(self, image_number):
		self.image_number = image_number
		self.my_label.grid_forget()
		self.my_label = Label(self.Pictures_Frame, image= self.image_list[self.image_number-1],relief=SUNKEN,bd=10)
		self.my_label.grid(row=0, column=0, columnspan=3, padx = 100, pady= 50)

		self.button_forward= Button(self.pic_bottom_frame,width=15, text=">>",height=2,font=('arial', 12,'bold'), command=lambda: self.forward(self.image_number+1))
		self.button_backward = Button(self.pic_bottom_frame, text="<<",height=2,width=15,font=('arial', 12,'bold'), command = lambda:self.backward(self.image_number-1))
		self.statusbar = Label(self.pic_bottom_frame, width=15,height=2,text ="Image " + str(self.image_number) + " of " + str(len(self.image_list)),bg='gainsboro', bd=1, relief=SUNKEN, justify=CENTER)
		if self.image_number == 1:
			self.button_backward = Button(self.pic_bottom_frame,height=2,font=('arial', 12,'bold'), width=15,text="<<", state=DISABLED)

		self.button_backward.grid(row=0, column=0, padx=90,pady=10)
		self.button_forward.grid(row=0, column=3, padx=90,pady=10)
		self.statusbar.grid(row=0,column=2, padx=90,pady=10)

	def One_For_All(self, message):
		print("I in one for all func")
		self.message = message
		self.newWindow = Toplevel(self.master)
		self.app = Controller(self.newWindow,self.message)

class Controller:
	def __init__(self, master,message):
		self.master = master
		self.message = message
		self.today = date.today()
		self.master.title("Welcome to the PHTR Ltd " + str(self.today))
		self.master.configure(bg='gainsboro')
		
		self.E_Driver_ID = StringVar()
		self.E_Full_Name = StringVar()
		self.E_Pay_Date = StringVar()

		self.E_Driver_ID.set("")
		self.E_Full_Name.set("")
		self.E_Pay_Date.set("")

		if (self.message == "New Registration"):
			self.master = master
			self.master.title("Taxi Private Hire Glasgwo Ltd.")
			self.master.configure(bg='gainsboro')
			self.master.geometry('1250x950+150+100')
			self.today = date.today()

			self.Title_Frame = Frame(self.master, bg='gainsboro', bd=10, relief=SUNKEN)
			self.Title_Frame.pack(fill=X)
			self.lblTitle_Frame= Label(self.Title_Frame, bg='gainsboro',font=('apple chancery', 20, 'bold','italic'), text="Welcom T0 Hampden Taxi Private Hire Glasgow",bd=1, 
			fg='black', justify=CENTER)
			self.lblTitle_Frame.pack(fill=X)

			self.MainFram = Frame(self.master, bg='gainsboro', bd=10, pady=4,relief=SUNKEN)
			self.MainFram.pack(fill=BOTH, expand=1)
			self.Button_Frame=Frame(self.MainFram, bg='gainsboro', bd=10, pady=4,relief=SUNKEN)
			self.Button_Frame.pack(side=LEFT)
			#self.Empty_Frame = Frame(self.MainFram, bg='cornsilk', bd=3, pady=4)
			#self.Empty_Frame.pack(side=LEFT)
			self.Driver_Entry_Frame=Frame(self.MainFram, bg='gainsboro', bd=10, pady=4,relief=SUNKEN)
			self.Driver_Entry_Frame.pack(side=LEFT,fill=BOTH,expand=1)
			self.OldDriver_Entry_Frame=Frame(self.MainFram, bg='gainsboro', bd=10, pady=4,relief=SUNKEN)
			self.OldDriver_Entry_Frame.pack(side=RIGHT,fill=BOTH, expand=1)
			#self.Lbl_Empty = Label(self.Empty_Frame, text="",bg='cornsilk', width=20,font=('arial', 14,'bold'))#,command=lambda:self.Today_Sale("Search"))
			#self.Lbl_Empty.grid(row=1, column=3,padx=2)


			############################### Variables Declarations ######################################
			self.E_Full_Name = StringVar()
			self.E_DOB = StringVar()
			self.E_Mobile = StringVar()
			self.E_Address = StringVar()
			self.E_City = StringVar()
			self.E_State = StringVar()
			self.E_PostCode = StringVar()
			self.E_Registration_Date = StringVar()

			self.E_Status= StringVar()
			self.E_W_A = StringVar()
			self.E_W_R = StringVar()
			self.E_P_D = StringVar()

			self.E_Driver_ID = IntVar()
			self.E_Car_Millage = StringVar()
			self.E_Taxi_Registration  = StringVar()
			self.E_Car_Colour = StringVar()
			self.E_Car_Manufacturer = StringVar()
			self.E_Car_Made_IN = StringVar()
			self.E_Transmission = StringVar()
			self.E_Engine_Size = StringVar()
			self.E_Fuel_Type = StringVar()

			self.E_Driver_ID.set('')
			self.E_Car_Millage.set("")
			self.E_Payment_Method = StringVar()
			self.Payment_Drop = StringVar()
			self.E_Registration_Date.set(self.today)
			self.E_State.set("Scotland")
			self.E_City.set("Glasgow")

			def AddRecord():
				print(str(self.E_P_D.get()))
				print(str(self.E_Status.get()))
				print(str(self.E_W_R.get()))
				print(str(self.E_W_A.get()))
			
				if (str(self.E_Full_Name.get()) !='' and str(self.E_DOB.get())!='' and str(self.E_Address.get())!='' and str(self.E_PostCode.get()) !='' and str(self.E_Mobile.get()) !=''and str(self.E_Registration_Date.get())!='' and str(self.E_Status.get()) !="Please Select" and str(self.E_W_R.get())!="Please Select" and str(self.E_W_A.get())!="Please Select"and str(self.E_P_D.get())!='Please Select'):
		
					sql_command = " INSERT INTO Drivers (Full_Name, DOB, Mobile, Address, PostCode, City, State, Registration_Date , P_D, Status, Week_R, Week_A) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s)"
					values = (str(self.E_Full_Name.get()), str(self.E_DOB.get()),str(self.E_Mobile.get()), str(self.E_Address.get()), str(self.E_PostCode.get()), str(self.E_City.get()), str(self.E_State.get()),str(self.E_Registration_Date.get()),str(self.E_P_D.get()),str(self.E_Status.get()),str(self.E_W_R.get()),str(self.E_W_A.get()))
					my_cursor.execute(sql_command, values)
					mydb.commit()
			
					self.E_Mobile.set("")
					self.E_Full_Name.set("")
					self.E_Address.set("")
					self.E_PostCode.set("")
					self.E_Status.set("Please Select")
					self.E_W_A.set("Please Select")
					self.E_W_R.set("Please Select")
					self.E_P_D.set("Please Select")
					#print(self.E_City.get())
					#self.E_State.set("")
					self.E_DOB.set("")
					print(my_cursor.lastrowid)
					self.E_Driver_ID.set(my_cursor.lastrowid)
			
					self.E_Taxi_Registration.configure(state=NORMAL)
					#self.E_Car_Millage.configure(state="normal")
					self.E_Car_Colour.configure(state=NORMAL)
					self.E_Car_Manufacturer.configure(state=NORMAL)
					self.E_Car_Made_IN.configure(state=NORMAL)
					self.E_Transmission.configure(state=NORMAL)
					self.E_Engine_Size.configure(state=NORMAL)
					self.E_Fuel_Type.configure(state=NORMAL)

					btnComplete_Registration.configure(state="normal")
				else:
					tkinter.messagebox.showwarning("Warning !! ", "Please Check, Full Records have not been Entered!!")

			def AddRegistration():

				if (str(self.E_Car_Millage.get())!="" and str(self.E_Taxi_Registration.get())!='Please Select' and str(self.E_Car_Colour.get())!='Please Select' and str(self.E_Car_Manufacturer.get()) !='Please Select' and str(self.E_Car_Made_IN.get()) !='Please Select'and str(self.E_Transmission.get())!='Please Select'and str(self.E_Engine_Size.get())!='Please Select' and str(self.E_Fuel_Type.get())!='Please Select'):
		
					sql_command = " INSERT INTO Taxi_Registration (Driver_ID, Car_Millage, Registration_No, Car_Colour, Car_Manufacturer, Car_Made_In, Transmission, Engine_Size, Fuel_Type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
					values = (str(self.E_Driver_ID.get()),str(self.E_Car_Millage.get()), str(self.E_Taxi_Registration.get()),str(self.E_Car_Colour.get()), str(self.E_Car_Manufacturer.get()), str(self.E_Car_Made_IN.get()), str(self.E_Transmission.get()),str(self.E_Engine_Size.get()),str(self.E_Fuel_Type.get()))
					my_cursor.execute(sql_command, values)
					mydb.commit()

					#self.txtDriver_ID.configure(state=DISABLED)
			
					#self.E_Driver_ID.set(my_cursor.lastrowid)

					self.E_Driver_ID.set("")
					self.E_Taxi_Registration.set("Please Select")
					self.E_Car_Millage.set("")
					self.E_Car_Colour.set("Please Select")
					self.E_Car_Manufacturer.set("Please Select")
					self.E_Car_Made_IN.set("Please Select")
					self.E_Transmission.set("Please Select")
					self.E_Engine_Size.set("Please Select")
					self.E_Fuel_Type.set("Please Select")

					#self.E_Driver_ID.configure(state=NORMAL)
					self.E_Taxi_Registration.configure(state=DISABLED)
					#self.E_Car_Millage.configure(state=DISABLED)
					self.E_Car_Colour.configure(state=DISABLED)
					self.E_Car_Manufacturer.configure(state=DISABLED)
					self.E_Car_Made_IN.configure(state=DISABLED)
					self.E_Transmission.configure(state=DISABLED)
					self.E_Engine_Size.configure(state=DISABLED)
					self.E_Fuel_Type.configure(state=DISABLED)

					btnComplete_Registration.configure(state=DISABLED)
					
			
				else:
					tkinter.messagebox.showwarning("Warning !! ", "Please Check, Full Records have not been Entered!!")
			######################################## Frames for New Drivers and Button frames ##########

			self.NewDriver_Titleframe= Frame(self.Driver_Entry_Frame, bg='gainsboro',bd=10,width=400, height=110, pady=4,relief=SUNKEN) ###### relief ridge check later
			self.NewDriver_Titleframe.pack(side=TOP,fill=X)
			
			self.NewDriver_EntryFrame = Frame(self.Driver_Entry_Frame, width=460, height=680,bg='gainsboro', bd=15, pady=4)
			self.NewDriver_EntryFrame.pack(side=TOP,fill=BOTH, expand=1)


			self.NewDrivers_Buttonframe = Frame(self.Driver_Entry_Frame, bg='gainsboro', bd=7, pady=4,relief=SUNKEN)
			self.NewDrivers_Buttonframe.pack(side=TOP)	

			self.lblCustomerTitle= Label(self.NewDriver_Titleframe, bg='gainsboro',font=('apple chancery', 20, 'bold','italic'), text="New Taxi Drivers Form",bd=3, 
				fg='black', justify=CENTER)
			self.lblCustomerTitle.pack(fill=X)

			self.lblFull_Name = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Full Name ", bg='gainsboro', fg='black')
			self.lblFull_Name.grid(row=1,column=0,sticky=W)
			self.txtFullname= Entry(self.NewDriver_EntryFrame, font=('arial',12,'bold'), bd=7, bg="white", insertwidth=2, justify='right',width=22, textvariable=self.E_Full_Name)
			self.txtFullname.grid(row=1,column=1,padx=50,pady=4,sticky=W)
		
			self.lbl_DOB = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Date of Birth  ", bg='gainsboro', fg='black')
			self.lbl_DOB.grid(row=2,column=0,sticky=W)  
			self.txt_DOB= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"), textvariable=self.E_DOB , bd=7, bg="white", insertwidth=2,width=22, justify= RIGHT)
			self.txt_DOB.grid(row=2,column=1,padx=50,pady=4,sticky=W)

			self.lblMobile = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Mobile ", bg='gainsboro', fg='black')
			self.lblMobile.grid(row=3,column=0,sticky=W)
			self.txtMobile= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_Mobile , bd=7, bg="white", insertwidth=2,width=22, justify= RIGHT)
			self.txtMobile.grid(row=3,column=1,padx=50,pady=4,sticky=W)

			self.lblAddress = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Address ", bg='gainsboro', fg='black')
			self.lblAddress.grid(row=4,column=0,sticky=W)
			self.txtAddress= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_Address , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txtAddress.grid(row=4,column=1,padx=50,pady=4,sticky=W)

			self.lblPostCode = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="PostCode", bg='gainsboro', fg='black')
			self.lblPostCode.grid(row=5,column=0,sticky=W)
			self.txtPostCode= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_PostCode , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txtPostCode.grid(row=5,column=1,padx=50,pady=4,sticky=W)

			self.lblCity = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="City ", bg='gainsboro', fg='black')
			self.lblCity.grid(row=6,column=0,sticky=W)
			self.txtCity= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_City , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txtCity.grid(row=6,column=1,padx=50,pady=4,sticky=W)

			self.lblState = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="State ", bg='gainsboro', fg='black')
			self.lblState.grid(row=7,column=0,sticky=W)
			self.txtState= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_State , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txtState.grid(row=7,column=1,padx=50,pady=4,sticky=W)

			self.lblDate = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Registration Date  ", bg='gainsboro', fg='black')
			self.lblDate.grid(row=8,column=0,sticky=W)  
			self.txtDate= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"), textvariable=self.E_Registration_Date , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txtDate.grid(row=8,column=1,padx=50,pady=4,sticky=W)
			self.lblEmpty = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="  ", bg='gainsboro', fg='black')
			self.lblEmpty.grid(row=9,column=0,sticky=W) 

			self.E_Status = ttk.Combobox(self.NewDriver_EntryFrame,width=22, font=('arial', 12, 'bold'),value=["Please Select", "Active","DeActive"])
			self.E_Status.current(0)
			self.E_Status.grid(row=9, column = 1, pady=6, padx=10)

			self.lblstatus = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Status ", bg='gainsboro', fg='black')
			self.lblstatus.grid(row=9,column=0,sticky=W)

			self.E_P_D = ttk.Combobox(self.NewDriver_EntryFrame,width=22, font=('arial', 12, 'bold'),value= ["Please Select","Monday", "Tuesday", "Wednesday","Thursday", "Friday","Saturday","Sunday"])
			self.E_P_D.current(0)
			self.E_P_D.grid(row=10, column = 1, pady=6, padx=10)

			self.lblP_D = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Pay Day ", bg='gainsboro', fg='black')
			self.lblP_D.grid(row=10,column=0,sticky=W)


			self.E_W_R = ttk.Combobox(self.NewDriver_EntryFrame,width=22, font=('arial', 12, 'bold'),value=["Please Select", "150","160","170", "175","180","185","190"])
			self.E_W_R.current(0)
			self.E_W_R.grid(row=11, column = 1, pady=6, padx=10)

			self.lblw_r = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Weekly Rent ", bg='gainsboro', fg='black')
			self.lblw_r.grid(row=11,column=0,sticky=W)

			self.E_W_A = ttk.Combobox(self.NewDriver_EntryFrame,width=22, font=('arial', 12, 'bold'),value=["Please Select","0", "10","15","20", "30","40","50","100"])
			self.E_W_A.current(0)
			self.E_W_A.grid(row=12, column = 1, pady=6, padx=10)

			self.lblw_a = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Weekly Access ", bg='gainsboro', fg='black')
			self.lblw_a.grid(row=12,column=0,sticky=W)
			btnSubmitDriverDetails = Button(self.NewDrivers_Buttonframe, text="Submit Driver Details", width=22,height=2,bd=6,font=('arial', 14,'bold'),relief=SUNKEN, command= AddRecord)
			btnSubmitDriverDetails.grid(row=0, column=0,padx=4)


			############################################. Buttons for Records Entries, Record Deletion #######################################
			#self.btnAdd = Button(self.NewDrivers_Buttonframe , text="Add Record",bd=20,font=('arial', 14,'bold'))#, command= self.AddRecod)
			#self.btnAdd.grid(row=0, column=0,padx=2,pady=4)
			#self.btnDelete = Button(self.NewDrivers_Buttonframe , text="Delete Record",bd=20,font=('arial', 14,'bold'))#,command=lambda:self.Today_Sale("Del"))
			#self.btnDelete.grid(row=0, column=1,padx=2,pady=4)
			#self.btnSearch = Button(self.NewDrivers_Buttonframe , text="Edit / Search",font=('arial', 14,'bold'))#,command=lambda:self.Today_Sale("Search"))
			#self.btnSearch.grid(row=0, column=3,padx=2,pady=4)

			#############################################   Registratons complete form ###################################################

			self.NewRegistration_Titleframe= Frame(self.OldDriver_Entry_Frame, bg='gainsboro',bd=10, pady=2,relief=SUNKEN) ###### relief ridge check later
			self.NewRegistration_Titleframe.pack(side=TOP,fill = X)

			self.lblNewRegistration_Title= Label(self.NewRegistration_Titleframe, bg='gainsboro',font=('apple chancery', 22, 'bold','italic'), text="Rent Agreement Ristration Form",bd=4, 
				fg='black', justify=CENTER)
			self.lblNewRegistration_Title.pack(side=TOP,fill=X)

			self.NewRegistration_EntryFrame = Frame(self.OldDriver_Entry_Frame, width=460, height=650,bg='gainsboro', bd=15, pady=4)
			self.NewRegistration_EntryFrame.pack(side=TOP, fill=BOTH, expand=1)


			self.NewRegistration_Buttonframe = Frame(self.OldDriver_Entry_Frame, bg='gainsboro', bd=10, pady=4,relief=SUNKEN)
			self.NewRegistration_Buttonframe.pack(side=BOTTOM)

			self.NewRegistration_Buttonframe1 = Frame(self.OldDriver_Entry_Frame, bg='gainsboro', bd=3)
			self.NewRegistration_Buttonframe1.pack(side=TOP)

			############################ Entry boxex for left frame

			self.lblEmptylbl = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="", bg='gainsboro', fg='black')
			self.lblEmptylbl.grid(row=10,column=0,sticky=W)
			self.lblDriver_ID = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Driver ID ", bg='gainsboro', fg='black')
			self.lblDriver_ID.grid(row=1,column=0,sticky=W)
			self.txtDriver_ID= Entry(self.NewRegistration_EntryFrame, font=('arial',12,'bold'), textvariable=self.E_Driver_ID ,bd=7,bg="white", insertwidth=2, justify='right')
			self.txtDriver_ID.grid(row=1,column=1,padx=4,pady=6,sticky=W)

			self.lblCar_Millage = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Car Millage ", bg='gainsboro', fg='black')
			self.lblCar_Millage.grid(row=2,column=0,sticky=W)
			self.txtCar_Millage= Entry(self.NewRegistration_EntryFrame, font=('arial',12,'bold'), textvariable=self.E_Car_Millage ,bd=7,bg="white", insertwidth=2, justify='right')
			self.txtCar_Millage.grid(row=2,column=1,padx=4,pady=6,sticky=W)

			self.lblTaxi_Registration = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Taxi Registration", bg='gainsboro', fg='black')
			self.lblTaxi_Registration.grid(row=3,column=0,sticky=W)
			#self.txtTaxi_Registration= Entry(self.NewRegistration_EntryFrame, font=('arial',12,'bold'), textvariable=self.E_Taxi_Registration ,state=DISABLED, bd=7, bg="white", insertwidth=2, justify='right')
			#self.txtTaxi_Registration.grid(row=2,column=1,padx=4,pady=2,sticky=W)

			self.E_Taxi_Registration = ttk.Combobox(self.NewRegistration_EntryFrame,width=20, font=('arial', 12, 'bold'),height=10,value=["Please Select","abc1111", "abc2222", "abc3333","abc4444", "abc5555","abc6666","abc7777","abc8888","abc9999","abc1010"])
			self.E_Taxi_Registration .current(0)
			self.E_Taxi_Registration .grid(row=3, column = 1, pady=4)

			self.lblCar_Colour = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Car Colour ", bg='gainsboro', fg='black')
			self.lblCar_Colour.grid(row=4,column=0,sticky=W)
			#self.txtPay_Date= Entry(self.NewRegistration_EntryFrame, font=('arial',12,'bold'), bd=7, bg="white" , textvariable=self.E_Pay_Date , state=DISABLED,insertwidth=2, justify='right')
			#self.txtPay_Date.grid(row=3,column=1,padx=4,pady=2,sticky=W)

			self.E_Car_Colour = ttk.Combobox(self.NewRegistration_EntryFrame,width=20, font=('arial', 12, 'bold'),value=["Please Select","White", "Blue","Silver","Grey","Black","Red","Green","OfWhite"])
			self.E_Car_Colour.current(0)
			self.E_Car_Colour.grid(row=4, column = 1, pady=6)	

			self.lblCar_Manufacturer = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Car Manufacturer ", bg='gainsboro', fg='black')
			self.lblCar_Manufacturer.grid(row=5,column=0,sticky=W)
			#self.txtPay_Day= Entry(self.NewRegistration_EntryFrame, font=('arial',12,'bold'), textvariable=self.E_Pay_Day, bd=7, bg="white", insertwidth=2,state=DISABLED, justify='right')
			#self.txtPay_Day.grid(row=4,column=1,padx=4,pady=2,sticky=W)

			self.E_Car_Manufacturer = ttk.Combobox(self.NewRegistration_EntryFrame,width=20, font=('arial', 12, 'bold'),value=["Please Select", "Toyota","Ford","Passate", "Vaxuhall","BMW","UDI","Mercedese"])
			self.E_Car_Manufacturer.current(0)
			self.E_Car_Manufacturer.grid(row=5, column = 1, pady=6)	

			self.lblCar_Made_IN = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Car Made IN ", bg='gainsboro', fg='black')
			self.lblCar_Made_IN .grid(row=6,column=0,sticky=W)
			#self.txtWeekly_Access= Entry(self.NewRegistration_EntryFrame, font=('arial',12,'bold'), textvariable=self.E_Weekly_Access, state=DISABLED,bd=7, bg="white", insertwidth=2, justify='right')
			#self.txtWeekly_Access.grid(row=5,column=1,padx=4,pady=2,sticky=W)

			self.E_Car_Made_IN  = ttk.Combobox(self.NewRegistration_EntryFrame,width=20, font=('arial', 12, 'bold'),value=["Please Select","UK", "Germeny","France","Japan","US","Others"])
			self.E_Car_Made_IN.current(0)
			self.E_Car_Made_IN .grid(row=6, column = 1, pady=6)		

			self.E_Transmission = ttk.Combobox(self.NewRegistration_EntryFrame,width=20, font=('arial', 12, 'bold'),value=["Please Select", "Automatic","Manual","Semi_Auto","Other"])
			self.E_Transmission.current(0)
			self.E_Transmission.grid(row=7, column = 1, pady=6)

			self.lblTransmission = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Transmission ", bg='gainsboro', fg='black')
			self.lblTransmission.grid(row=7,column=0,sticky=W)

			self.E_Engine_Size = ttk.Combobox(self.NewRegistration_EntryFrame,width=20, font=('arial', 12, 'bold'),value=["Please Select", "Up to 999cc","1,000 - 1,999cc","2,000 - 2,999cc","Other"])
			self.E_Engine_Size.current(0)
			self.E_Engine_Size.grid(row=8, column = 1, pady=6)

			self.lblEngine_Size = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Engine Size ", bg='gainsboro', fg='black')
			self.lblEngine_Size.grid(row=8,column=0,sticky=W)

			self.E_Fuel_Type = ttk.Combobox(self.NewRegistration_EntryFrame,width=20, font=('arial', 12, 'bold'),value=["Please Select", "Diesel","Petrol","Gas","Hybrid Electric","Petrol/Gas","Other"])
			self.E_Fuel_Type.current(0)
			self.E_Fuel_Type.grid(row=9, column = 1, pady=6)

			self.lblFuel_Type = Label(self.NewRegistration_EntryFrame,font=('apple chancery', 14, 'bold'), text="Fuel Type ", bg='gainsboro', fg='black')
			self.lblFuel_Type.grid(row=9,column=0,sticky=W)
			#self.txtRent_per_Week= Entry(self.NewRegistration_EntryFrame, font=('arial',12,'bold'), bd=7, textvariable=self.E_Rent_per_Week,state=DISABLED, bg="white", insertwidth=2, justify='right')
			#self.txtRent_per_Week.grid(row=6,column=1,padx=4,pady=2,sticky=W)
		
		
		
			############################################### Registration frame Button #############################################################
			btnComplete_Registration = Button(self.NewRegistration_Buttonframe, text="Submit Registration Form",height=2,font=('arial', 14,'bold'),command= AddRegistration)
			btnComplete_Registration.grid(row=0, column=3,padx=2)
			self.btnPay_The_Rent = Label(self.NewRegistration_Buttonframe1, text="",bg='gainsboro', width=20,font=('arial', 14,'bold'))
			self.btnPay_The_Rent.grid(row=1, column=3,padx=2)

		if (self.message == "Pay_The_Rent"):
			self.master.geometry('1450x760+0+0')


			self.Master_Frame= Frame(self.master, bg='gainsboro', bd=10, width=1450, height=700, relie= SUNKEN)
			self.Master_Frame.pack(side=LEFT,fill=Y)

			self.Titel_Frame = Frame(self.Master_Frame, bg='gainsboro', bd=8, relief=SUNKEN)
			self.Titel_Frame.pack(fill=X)

			self.lblTitle = Label(self.Titel_Frame, text="Taxi Pay Point",bg='gainsboro',font=('apple chancery', 30, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblTitle.pack()

			self.Holder_Frame = Frame(self.Master_Frame, bg='gainsboro', bd=8, width=1380, height=500, relief=SUNKEN)
			self.Holder_Frame.pack(side=LEFT,fill=BOTH,expand=1)


			self.Search_Components_Frame = Frame(self.Holder_Frame, bg='gainsboro', bd=4, relief=SUNKEN)
			self.Search_Components_Frame.pack(side=TOP)

			self.RecordsFrame = Frame(self.Holder_Frame, width= 500, bg='gainsboro', bd=4, relief=SUNKEN)
			self.RecordsFrame.pack(side=LEFT, fill= BOTH, expand=1) #grid(row=0,column=0)

			#Entry box for search to customer
			search_box=Entry(self.Search_Components_Frame)
			search_box.grid(row=0, column=1, pady=10, padx=10)
			#entry box label
			search_box_label=Label(self.Search_Components_Frame, text="Search..",bg='gainsboro',font=("Ariel", 12, 'bold'))
			search_box_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
			#drop down box
			drop = ttk.Combobox(self.Search_Components_Frame, value=["search by...", "Driver FullName", "Driver ID", "Driver Mobile"],font=("Ariel", 12, 'bold'))
			drop.current(0)
			drop.grid(row=0, column = 2)

			#labels for searched records columns

			self.lblDriver_ID = Label(self.RecordsFrame,font=('apple chancery', 14, 'bold'), width=22, text="Driver ID ", bg='gainsboro', fg='black')
			self.lblDriver_ID.grid(row=0,column=0,sticky=W,columnspan=2,padx=40)
			self.txtDriver_ID= Entry(self.RecordsFrame, font=('arial',12,'bold'), bd=7, bg="white", insertwidth=2, justify='right',width=22, textvariable=self.E_Driver_ID)
			self.txtDriver_ID.grid(row=0,column=3,padx=2,pady=14,sticky=E) 

			self.lblFull_Name = Label(self.RecordsFrame,font=('apple chancery', 14, 'bold'), width=22, text="Full Name ", bg='gainsboro', fg='black')
			self.lblFull_Name.grid(row=1,column=0,sticky=W,columnspan=2,padx=40)
			self.txtFullname= Entry(self.RecordsFrame, font=('arial',12,'bold'), bd=7, bg="white", insertwidth=2, justify='right',width=22, textvariable=self.E_Full_Name)
			self.txtFullname.grid(row=1,column=3,padx=2,pady=14,sticky=E)

			self.lblpay_date = Label(self.RecordsFrame,font=('apple chancery', 14, 'bold'), width=22, text="Pay Date", bg='gainsboro', fg='black')
			self.lblpay_date.grid(row=2,column=0,sticky=W,columnspan=2,padx=40)
			self.txtPay_Date= Entry(self.RecordsFrame, font=('arial',12,'bold'), bd=7, bg="white", insertwidth=2, justify='right',width=22, textvariable=self.E_Pay_Date)
			self.txtPay_Date.grid(row=2,column=3,padx=2,pady=14,sticky=E)

			#self.E_Status= StringVar()
			self.E_W_A = StringVar()
			self.E_W_R = StringVar()
			self.E_P_D = StringVar()

			self.lbl_p_day = Label(self.RecordsFrame,font=('apple chancery', 14, 'bold'), width=22, text="Pay Day ", bg='gainsboro', fg='black')
			self.lbl_p_day.grid(row=3,column=0,sticky=W,columnspan=2,padx=40)
			self.txtpday= Entry(self.RecordsFrame, font=("arial", 12, "bold"),  textvariable=self.E_P_D , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txtpday.grid(row=3,column=3,padx=2,pady=14,sticky=E)

			self.lblweekly_access = Label(self.RecordsFrame,font=('apple chancery', 14, 'bold'), width=22, text="Weekly Access ", bg='gainsboro', fg='black')
			self.lblweekly_access.grid(row=4,column=0,sticky=W,columnspan=2,padx=40)
			self.txtWeekly_Access= Entry(self.RecordsFrame, font=("arial", 12, "bold"),  textvariable=self.E_W_A , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txtWeekly_Access.grid(row=4,column=3,padx=2,pady=14,sticky=E)

			self.lblweekly_rent = Label(self.RecordsFrame,font=('apple chancery', 14, 'bold'), width=22, text="Weekly Rent ", bg='gainsboro', fg='black')
			self.lblweekly_rent.grid(row=5,column=0,sticky=W,columnspan=2,padx=40)
			self.txt_weekly_Rent= Entry(self.RecordsFrame, font=("arial", 12, "bold"),  textvariable=self.E_W_R , bd=7, bg="white",width=22, insertwidth=2, justify= RIGHT)
			self.txt_weekly_Rent.grid(row=5,column=3,padx=2,pady=14,sticky=E)

			def Search_Record(): # Called from line 1524

				selected = drop.get()
				sql = ""
				if selected == "search by...":
					tkinter.messagebox.showwarning("Warning !", "Please choose correct options.")

				if selected == "Driver FullName":
					sql = "SELECT * FROM Drivers WHERE Full_Name = %s"
					

				if selected == "Driver ID":
					sql = "SELECT * FROM Drivers WHERE Driver_ID = %s"

				if selected == "Driver Mobile":
					sql = "SELECT * FROM Drivers WHERE Mobile = %s"

				searched = search_box.get()
				name = (searched,)    # i will investigate the brakets
				result = my_cursor.execute(sql, name)
				result = my_cursor.fetchall()
				
				if not result:

					result="Sorry No Record has been found for this " + str(drop.get())+ ". Try other option or check in all Driver List Tabel"
					tkinter.messagebox.showwarning("Warning",result)

					
				else:


					for index, x in enumerate(result): 
						if result[index][9]=="DeActive":
							tkinter.messagebox.showwarning("Alert !!","This Drive is no longer active !!")
						else:
							self.E_Driver_ID.set(result[index][12])
							self.E_Full_Name.set(result[index][0])
							self.E_Pay_Date.set(self.today)
							self.E_P_D.set(result[index][8])
							self.E_W_A.set(result[index][11])
							self.E_W_R.set(result[index][10])
							#self.E_Status.current(1)
							#self.E_Weekly_Rent.current(result[index][9])
							#self.E_Weekly_Access.current(result[index][10])
							#print(self.E_Driver_ID.get())


			def Payment_Submitted():
				
				if (str(self.E_Driver_ID.get())!='' and str(self.E_Full_Name.get())!='' and str(self.E_Pay_Date.get())!='' and str(self.E_P_D.get()) !='' and str(self.E_W_R.get()) !=''and str(self.E_W_A.get())!=''):
		
					sql_command = " INSERT INTO Taxi_Rent (Driver_ID, Pay_Date, Pay_Day, Weekly_Access, Weekly_Rent) VALUES (%s, %s, %s, %s, %s)"
					values = (str(self.E_Driver_ID.get()),str(self.E_Pay_Date.get()), str(self.E_P_D.get()),str(self.E_W_A.get()), str(self.E_W_R.get()))
					my_cursor.execute(sql_command, values)
					mydb.commit()

					self.E_Driver_ID.set("")
					self.E_Full_Name.set("")
					self.E_Pay_Date.set("")
					self.E_W_R.set("")
					self.E_W_A.set("")
					self.E_P_D.set("")
					#search_box.set("")
					tkinter.messagebox.showwarning("Thanks !! ", "Paymen has been Submitted Successfully!!")

					#SQL = "SELECT  Drivers.Driver_ID,Taxi_Rent.Rent_ID,Drivers.Full_Name,Taxi_Rent.Weekly_Rent, Taxi_Rent.Weekly_Access, Taxi_Rent.Pay_Date, Drivers.Mobile,Drivers.City FROM Taxi_Rent  INNER JOIN Drivers ON  Taxi_Rent.Driver_ID =Drivers.Driver_ID; " 
					#result = my_cursor.execute(SQL)
					#result = my_cursor.fetchall()
					SQL = "SELECT  Drivers.Driver_ID,Taxi_Rent.Rent_ID,Drivers.Full_Name,Taxi_Rent.Weekly_Rent, Taxi_Rent.Weekly_Access, Taxi_Rent.Pay_Date, Drivers.Mobile, Drivers.P_D FROM Drivers  INNER JOIN Taxi_Rent ON Drivers.Driver_ID = Taxi_Rent.Driver_ID;"
					
					#a = "SELECT  Drivers.Driver_ID, Taxi_Rent.Weekly_Rent, Drivers.Full_Name from Drivers INNER join  Taxi_Rent on Taxi_Rent.Driver_ID = Drivers.Driver_ID;"
					#.Driver_ID, Taxi_Rent.Rent_ID, Drivers.Full_Name,Taxi_Rent.Weekly_Rent, Taxi_Rent.Weekly_Access, Taxi_Rent.Pay_Date,  Drivers.Mobile, Drivers.City  FROM Drivers  INNER JOIN Taxi_Rent ON Drivers.Driver_ID = Taxi_Rent.Driver_ID;"
					result = my_cursor.execute(SQL)
					result = my_cursor.fetchall()
					#for row in result:
						#print (row)
					textbox.delete("1.0","end")
					#print()
					textbox.insert('end',"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
					textbox.insert('end',"DriverID\tRent_ID\tFull Name\t\tWeekly Payment\t\t Weekly Access\t\t Payment Date\t\t Mobile\t\t Pay Day\n\n ")
					textbox.insert('end',"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
					for index, x in enumerate(result): 
						textbox.insert('end', str(result[index][0])+ "\t" + str(result[index][1]) + "\t" + str(result[index][2])  + "\t\t" + "£" + str(result[index][3]) 
							+ "\t\t" + "£" + str(result[index][4]) +  "\t\t" + str(result[index][5])+"\t\t" + str(result[index][6])+ "\t\t"+  str(result[index][7]) + "\n ")
						
				else:
					tkinter.messagebox.showwarning("Warning !! ", "Please Check, Full Records have not been Entered!!")		

			Payment_button=Button(self.RecordsFrame, text="Submit Payment",font=("Ariel", 18, 'bold'),fg="black", bd=30, command= Payment_Submitted)
			Payment_button.grid(row = 6, column=0, padx=2, pady=50,sticky=W)
			Search_Payment_button=Button(self.Search_Components_Frame, text="Search Driver",font=("Ariel", 18, 'bold'),fg="black", bd=30, command= Search_Record)
			Search_Payment_button.grid(row = 1, column=0, padx=10, pady=15,sticky=W)

			#######################################################################################################################################################################
			############################################################## Filling right side no
			self.Master_Right_Frame= Frame(self.master, bg='gainsboro', bd=10, width=850, height=700, relief=SUNKEN)
			self.Master_Right_Frame.pack(side=RIGHT, fill=Y)
			self.Master_Right_Mosttop_Frame= Frame(self.Master_Right_Frame, bg='gainsboro', bd=10, width=850, height=80, relief=SUNKEN)
			self.Master_Right_Mosttop_Frame.pack(side=TOP,fill=X)
			self.lblTitle = Label(self.Master_Right_Mosttop_Frame, text="Drivers Payments Profile",bg='gainsboro',font=('apple chancery', 30, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblTitle.pack()
			self.Master_Right_Center_Frame= Frame(self.Master_Right_Frame, bg='gainsboro', bd=10, width=850, height=140, relief=SUNKEN)
			self.Master_Right_Center_Frame.pack(side=TOP,fill=X)

			self.Master_Right_top_Frame= Frame(self.Master_Right_Frame, bg='gainsboro', bd=10, width=850, height=520, relief=SUNKEN)
			self.Master_Right_top_Frame.pack(side=TOP, fill=BOTH, expand=1)

			search_box1=Entry(self.Master_Right_Center_Frame)
			search_box1.grid(row=0, column=1, pady=10, padx=10)
			#entry box label
			search_box_label1=Label(self.Master_Right_Center_Frame, text="Search Payment By...",bg="gainsboro",font=("Ariel", 12, 'bold'))
			search_box_label1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
			#drop down box
			drop1 = ttk.Combobox(self.Master_Right_Center_Frame, value=["search by...", "Driver FullName", "Driver ID", "Driver Mobile"],font=("Ariel", 12, 'bold'))
			drop1.current(0)
			drop1.grid(row=0, column = 2)
			Payment_search_button=Button(self.Master_Right_Center_Frame, text="Singel Driver Payments",font=("Ariel", 16, 'bold'),fg="black", bd=30)#, command= Drivers_Payments)
			Payment_search_button.grid(row = 1, column=0, padx=10, pady=15)
			####################################### Creatd cursor and TextBox

			scroll = Scrollbar(self.Master_Right_top_Frame)
			scroll.pack(side=RIGHT, fill=Y)

			textbox=Text(self.Master_Right_top_Frame,bg='azure', yscrollcommand=scroll.set,font=('arial', 11, 'bold'),width=210,height=44)
			textbox.pack(side=LEFT)

			scroll.config(command=textbox.yview)
			

			SQL = "SELECT  Drivers.Driver_ID,Taxi_Rent.Rent_ID,Drivers.Full_Name,Taxi_Rent.Weekly_Rent, Taxi_Rent.Weekly_Access, Taxi_Rent.Pay_Date, Drivers.Mobile, Taxi_Rent.Pay_Day FROM Drivers  INNER JOIN Taxi_Rent ON Drivers.Driver_ID = Taxi_Rent.Driver_ID;"
			result = my_cursor.execute(SQL)
			result = my_cursor.fetchall()
			#print(result)
			textbox.delete("1.0","end")
			textbox.insert('end',"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			textbox.insert('end',"DriverID\tRent_ID\tFull Name\t\tWeekly Payment\t\t Weekly Access\t\t Payment Date\t\t Mobile\t\t Pay Day\n\n ")
			textbox.insert('end',"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			for index, x in enumerate(result): 
				textbox.insert('end', str(result[index][0])+ "\t" + str(result[index][1]) + "\t" + str(result[index][2])  + "\t\t" + "£" + str(result[index][3]) 
						+ "\t\t" + "£" + str(result[index][4]) +  "\t\t" + str(result[index][5])+"\t\t" + str(result[index][6]) + "\t\t"+  str(result[index][7]) + "\n ")


			def Drivers_Payments():
				print(" i got here")
				textbox.delete("1.0","end")
				textbox.insert('end',"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
				textbox.insert('end',"DriverID\tRent_ID\tFull Name\t\tWeekly Payment\t\t Weekly Access\t\t Payment Date\t\t Mobile\t\t Pay Day\n \n")
				textbox.insert('end',"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
				SQL = "SELECT  Drivers.Driver_ID,Taxi_Rent.Rent_ID,Drivers.Full_Name,Taxi_Rent.Weekly_Rent, Taxi_Rent.Weekly_Access, Taxi_Rent.Pay_Date, Drivers.Mobile,Drivers.City , Taxi_Rent.Pay_Day FROM Drivers  INNER JOIN Taxi_Rent ON Drivers.Driver_ID = Taxi_Rent.Driver_ID 	WHERE Taxi_Rent.Driver_ID = " + search_box1.get()
				result = my_cursor.execute(SQL)
				result = my_cursor.fetchall()

				for index, x in enumerate(result): 
					textbox.insert('end', str(result[index][0])+ "\t" + str(result[index][1]) + "\t" + str(result[index][2])  + "\t\t" + "£" + str(result[index][3]) 
						+ "\t\t" + "£" + str(result[index][4]) +  "\t\t" + str(result[index][5])+"\t\t" + str(result[index][6])+ "\t\t"+  str(result[index][7]) + "\n ")

			Payment_search_button=Button(self.Master_Right_Center_Frame, text="Singel Driver Payments",font=("Ariel", 16, 'bold'),fg="black", bd=30, command= Drivers_Payments)
			Payment_search_button.grid(row = 1, column=0, padx=10, pady=15)

		if (self.message == "ALL TAXI DRIVERS"):
			print("All taxi Drivers")
			self.master.geometry('1050x900+150+100')
			self.Master_Frame= Frame(self.master, bg='gainsboro', bd=10, width=850, height=900, relief=SUNKEN)
			self.Master_Frame.pack(side=TOP,fill=BOTH, expand=1)

			self.Master_Title_Frame= Frame(self.Master_Frame, bg='gainsboro', bd=10, width=850, height=80, relief=SUNKEN)
			self.Master_Title_Frame.pack(side=TOP,fill=X)
			self.lblTitle = Label(self.Master_Title_Frame, text="Active Drivers Profile",bg='gainsboro',font=('apple chancery', 30, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblTitle.pack()

			self.Master_Center_Frame= Frame(self.Master_Frame, bg='gainsboro', bd=10, width=850, height=140, relief=SUNKEN)
			self.Master_Center_Frame.pack(side=TOP,fill=X)

			self.Master_txtbox_Frame= Frame(self.Master_Frame, bg='gainsboro', bd=10, width=850, height=220, relief=SUNKEN)
			self.Master_txtbox_Frame.pack(side=TOP)

			self.Master_Bottom_Frame= Frame(self.Master_Frame, bg='gainsboro', bd=10, width=850, height=220, relief=SUNKEN)
			self.Master_Bottom_Frame.pack(side=TOP,fill=BOTH, expand=1)

			
			self.Taxi_Replacement_Frame= Frame(self.Master_Bottom_Frame, bg='gainsboro', bd=10, width=500, height=90, relief=SUNKEN)
			self.Taxi_Replacement_Frame.pack(side=TOP,fill=X)
			self.lblTitle = Label(self.Taxi_Replacement_Frame, text="Replace Taxi Registration",bg='gainsboro',font=('apple chancery', 30, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblTitle.pack( fill=X)

			def Change_Registration():
				selected = drop1.get()
				sql = ""
				if selected == "search by...":
					tkinter.messagebox.showwarning("Warning !", "Please choose correct options.")

				if selected == "Driver ID":
					sql = "SELECT * FROM Taxi_Registration WHERE Driver_ID = %s"

				searched = search_box1.get()

				print(searched)
				name = (searched,)    # i will investigate the brakets
				result = my_cursor.execute(sql, name)
				result = my_cursor.fetchall()
				#print(result)
				
				if not result:

					result="Sorry No Record has been found for this " + str(drop1.get())+ ". Try other option or check in all Driver List Tabel"
					tkinter.messagebox.showwarning("Warning",result)
				else:

					for index, x in enumerate(result): #for enumerate watch video 31
						self.E_Driver_ID.set(result[index][0])
					self.E_Car_Millage.set("")


			def Update_New_Registration():
				print("update new reg")


				if (str(self.E_Car_Millage.get())!="" and str(self.E_Taxi_Registration.get())!='Please Select' and str(self.E_Car_Colour.get())!='Please Select' and str(self.E_Car_Manufacturer.get()) !='Please Select' and str(self.E_Car_Made_IN.get()) !='Please Select'and str(self.E_Transmission.get())!='Please Select'and str(self.E_Engine_Size.get())!='Please Select' and str(self.E_Fuel_Type.get())!='Please Select'):

					seq_command = """ UPDATE Taxi_Registration SET Driver_ID= %s, Car_Millage= %s, Registration_No= %s, Car_Colour= %s, Car_Manufacturer= %s, Car_Made_In= %s, Transmission= %s, Engine_Size= %s, Fuel_Type= %s WHERE Driver_ID = %s"""

					driver_Id  = search_box1.get()
					#inputs = (str(self.E_Full_Name1.get()),str(self.E_DOB1.get()),str(self.E_Mobile1.get()),str(self.E_Address1.get()), str(self.E_PostCode1.get()),str(self.E_City1.get()),str(self.E_State1.get()),str(self.E_Registration_Date1.get()),str(self.E_P_D.get()),str(self.E_Status.get()),str(self.E_W_R.get()),str(self.E_W_A.get()),str(driver_Id) )
					inputs = (str(self.E_Driver_ID.get()),str(self.E_Car_Millage.get()),str(self.E_Taxi_Registration.get()),str(self.E_Car_Colour.get()), str(self.E_Car_Manufacturer.get()), str(self.E_Car_Made_IN.get()) ,str(self.E_Transmission.get()),str(self.E_Engine_Size.get()),str(self.E_Fuel_Type.get()),str(driver_Id))
					my_cursor.execute(seq_command, inputs)
					mydb.commit()

					self.E_Driver_ID.set("")
					self.E_Taxi_Registration.set("Please Select")
					self.E_Car_Millage.set("")
					self.E_Car_Colour.set("Please Select")
					self.E_Car_Manufacturer.set("Please Select")
					self.E_Car_Made_IN.set("Please Select")
					self.E_Transmission.set("Please Select")
					self.E_Engine_Size.set("Please Select")
					self.E_Fuel_Type.set("Please Select")

					#self.E_Driver_ID.configure(state=NORMAL)
					self.E_Taxi_Registration.configure(state=DISABLED)
					#self.E_Car_Millage.configure(state=DISABLED)
					self.E_Car_Colour.configure(state=DISABLED)
					self.E_Car_Manufacturer.configure(state=DISABLED)
					self.E_Car_Made_IN.configure(state=DISABLED)
					self.E_Transmission.configure(state=DISABLED)
					self.E_Engine_Size.configure(state=DISABLED)
					self.E_Fuel_Type.configure(state=DISABLED)

					Update_Registration_button.configure(state=DISABLED)
					tkinter.messagebox.showwarning("Thanks !! ", "Driver Details Successfully Updated!!")
			
				else:
					tkinter.messagebox.showwarning("Warning !! ", "Please Check, Full Records have not been Entered!!")



				
			search_box1=Entry(self.Master_Center_Frame)
			search_box1.grid(row=0, column=1, pady=10, padx=10)
			#entry box label
			search_box_label1=Label(self.Master_Center_Frame, text="Search By...",bg="cornsilk",font=("Ariel", 12, 'bold'))
			search_box_label1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
			#drop down box
			drop1 = ttk.Combobox(self.Master_Center_Frame, value=["search by...", "Driver ID"],font=("Ariel", 12, 'bold'))
			drop1.current(0)
			drop1.grid(row=0, column = 2)
			Change_Registration_button=Button(self.Master_Center_Frame, text="Replace Taxi Registration",font=("Ariel", 16, 'bold'),fg="black", bd=30, command= Change_Registration)
			Change_Registration_button.grid(row = 1, column=0, padx=10, pady=15)
			####################################### Creatd cursor and TextBox

			scroll = Scrollbar(self.Master_txtbox_Frame)
			scroll.pack(side=RIGHT, fill=Y)

			textbox=Text(self.Master_txtbox_Frame,bg='azure', yscrollcommand=scroll.set,font=('verdana', 10, 'bold'),width=210,height=15)
			textbox.pack(side=LEFT)

			scroll.config(command=textbox.yview)
			
			SQL = "SELECT  Drivers.Driver_ID,\
			Drivers.Full_Name, Drivers.Address,Drivers.City,\
			Drivers.State, Drivers.Mobile,Taxi_Registration.Registration_No,\
			Drivers.Status FROM Drivers  INNER JOIN Taxi_Registration ON Drivers.Driver_ID = Taxi_Registration.Driver_ID;"
			result = my_cursor.execute(SQL)
			result = my_cursor.fetchall()
			#print(result)
			textbox.delete("1.0","end")
			textbox.insert('end',"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			textbox.insert('end',"\tDriverID\tFull Name\t\t\tAddress\t\t\t City\t\t state\t\t Mobile\t\t Registration_No\t\tStatus\n\n ")
			textbox.insert('end',"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			for index, x in enumerate(result): 
				textbox.insert('end', "\t"+ str(result[index][0])+ "\t" + str(result[index][1]) + "\t\t\t" + str(result[index][2])  + "\t\t\t" + str(result[index][3]) 
						+ "\t\t"  + str(result[index][4]) +  "\t\t" + str(result[index][5])+"\t\t" + str(result[index][6]) + "\t\t"+  str(result[index][7]) + "\n ")

			self.Driver_EntryFrame = Frame(self.Master_Bottom_Frame,bg='gainsboro', bd=15, pady=4)
			self.Driver_EntryFrame.pack(side=TOP,fill=BOTH, expand=1)
			
			self.E_Driver_ID = IntVar()
			self.E_Car_Millage = StringVar()
			self.E_Taxi_Registration  = StringVar()
			self.E_Car_Colour = StringVar()
			self.E_Car_Manufacturer = StringVar()
			self.E_Car_Made_IN = StringVar()
			self.E_Transmission = StringVar()
			self.E_Engine_Size = StringVar()
			self.E_Fuel_Type = StringVar()

			self.lblDriver_ID = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Driver ID ", bg='gainsboro', fg='black')
			self.lblDriver_ID.grid(row=0,column=0,sticky=W,padx=12)
			self.txtDriver_ID= Entry(self.Driver_EntryFrame, font=('arial',12,'bold'), textvariable=self.E_Driver_ID ,bd=7,bg="white", insertwidth=2, justify='left')
			self.txtDriver_ID.grid(row=0,column=1,pady=6,sticky=W)

			self.lblCar_Millage = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Car Millage ", bg='gainsboro', fg='black')
			self.lblCar_Millage.grid(row=0,column=2,sticky=W,padx=12)
			self.txtCar_Millage= Entry(self.Driver_EntryFrame, font=('arial',12,'bold'), textvariable=self.E_Car_Millage ,bd=7,bg="white", insertwidth=2, justify='right')
			self.txtCar_Millage.grid(row=0,column=3,pady=6,sticky=W)

			self.lblTaxi_Registration = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Taxi Registration", bg='gainsboro', fg='black')
			self.lblTaxi_Registration.grid(row=0,column=4,sticky=W,padx=12)
			self.E_Taxi_Registration = ttk.Combobox(self.Driver_EntryFrame,width=18, font=('arial', 12, 'bold'),height=10,value=["Please Select","abc1111", "abc2222", "abc3333","abc4444", "abc5555","abc6666","abc7777","abc8888","abc9999","abc1010"])
			self.E_Taxi_Registration .current(0)
			self.E_Taxi_Registration .grid(row=0, column = 5, pady=4)

			self.lblCar_Colour = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Car Colour ", bg='gainsboro', fg='black')
			self.lblCar_Colour.grid(row=1,column=0,sticky=W,padx=12)
			self.E_Car_Colour = ttk.Combobox(self.Driver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select","White", "Blue","Silver","Grey","Black","Red","Green","OfWhite"])
			self.E_Car_Colour.current(0)
			self.E_Car_Colour.grid(row=1, column = 1, pady=6)	

			self.lblCar_Manufacturer = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Car Manufacturer ", bg='gainsboro', fg='black')
			self.lblCar_Manufacturer.grid(row=1,column=2,sticky=W,padx=12)
			self.E_Car_Manufacturer = ttk.Combobox(self.Driver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select", "Toyota","Ford","Passate", "Vaxuhall","BMW","UDI","Mercedese"])
			self.E_Car_Manufacturer.current(0)
			self.E_Car_Manufacturer.grid(row=1, column = 3, pady=6)	

			self.lblCar_Made_IN = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Car Made IN ", bg='gainsboro', fg='black')
			self.lblCar_Made_IN .grid(row=1,column=4,sticky=W,padx=12)
			self.E_Car_Made_IN  = ttk.Combobox(self.Driver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select","UK", "Germeny","France","Japan","US","Others"])
			self.E_Car_Made_IN.current(0)
			self.E_Car_Made_IN .grid(row=1, column = 5, pady=6)		

			self.E_Transmission = ttk.Combobox(self.Driver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select", "Automatic","Manual","Semi_Auto","Other"])
			self.E_Transmission.current(0)
			self.E_Transmission.grid(row=2, column = 1, pady=6)
			self.lblTransmission = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Transmission ", bg='gainsboro', fg='black')
			self.lblTransmission.grid(row=2,column=0,sticky=W,padx=12)

			self.E_Engine_Size = ttk.Combobox(self.Driver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select", "Up to 999cc","1,000 - 1,999cc","2,000 - 2,999cc","Other"])
			self.E_Engine_Size.current(0)
			self.E_Engine_Size.grid(row=2, column = 3, pady=6)
			self.lblEngine_Size = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Engine Size ", bg='gainsboro', fg='black')
			self.lblEngine_Size.grid(row=2,column=2,sticky=W,padx=12)

			self.E_Fuel_Type = ttk.Combobox(self.Driver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select", "Diesel","Petrol","Gas","Hybrid Electric","Petrol/Gas","Other"])
			self.E_Fuel_Type.current(0)
			self.E_Fuel_Type.grid(row=2, column = 5, pady=6)
			self.lblFuel_Type = Label(self.Driver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Fuel Type ", bg='gainsboro', fg='black')
			self.lblFuel_Type.grid(row=2,column=4,sticky=W,padx=12)

			Update_Registration_button=Button(self.Driver_EntryFrame, text="Update Driver Details",font=("Ariel", 16, 'bold'),fg="black", bd=30, command= Update_New_Registration)
			Update_Registration_button.grid(row = 3, column=0, padx=10, pady=30)




		if (self.message == "TAXI DRIVERS Agreement"):
			print("All taxi Drivers")
			self.master.geometry('1250x850+150+100')
			self.Master_Right_Frame= Frame(self.master, bg='gainsboro', bd=10, width=650, height=800, relief=SUNKEN)
			self.Master_Right_Frame.pack(side=RIGHT,fill=BOTH,expand=1)
			self.Master_Right_Mosttop_Frame= Frame(self.Master_Right_Frame, bg='gainsboro', bd=10, width=850, height=80, relief=SUNKEN)
			self.Master_Right_Mosttop_Frame.pack(side=TOP,fill=X)
			self.lblTitle = Label(self.Master_Right_Mosttop_Frame, text="Update Drivers Agreement Form",bg='gainsboro',font=('apple chancery', 30, 'bold','italic'),
				fg ='black', justify=CENTER )
			self.lblTitle.pack()
			self.Master_Right_Center_Frame= Frame(self.Master_Right_Frame, bg='gainsboro', bd=10, width=850, height=140, relief=SUNKEN)
			self.Master_Right_Center_Frame.pack(side=TOP,fill=X)

			self.Master_Right_top_Frame= Frame(self.Master_Right_Frame, bg='gainsboro', bd=10, width=850, height=200, relief=SUNKEN)
			self.Master_Right_top_Frame.pack(side=TOP)
			self.Master_Right_top_Frame1= Frame(self.Master_Right_Frame, bg='gainsboro', bd=10, width=850, height=320, relief=SUNKEN)
			self.Master_Right_top_Frame1.pack(side=TOP,fill=BOTH, expand=1)

			self.E_Full_Name1 = StringVar()
			self.E_DOB1 = StringVar()
			self.E_Mobile1 = StringVar()
			self.E_Address1 = StringVar()
			self.E_City1 = StringVar()
			self.E_State1 = StringVar()
			self.E_PostCode1 = StringVar()
			self.E_Registration_Date1 = StringVar()

			self.E_Status= StringVar()
			self.E_W_A = StringVar()
			self.E_W_R = StringVar()
			self.E_P_D = StringVar()

			def Change_Drivers_Status():
				print(" I will change the Status")
				selected = drop1.get()
				sql = ""
				if selected == "search by...":
					tkinter.messagebox.showwarning("Warning !", "Please choose correct options.")

				if selected == "Driver FullName":
					sql = "SELECT * FROM Drivers WHERE Full_Name = %s"
					

				if selected == "Driver ID":
					sql = "SELECT * FROM Drivers WHERE Driver_ID = %s"

				if selected == "Driver Mobile":
					sql = "SELECT * FROM Drivers WHERE Mobile = %s"

				searched = search_box1.get()
				name = (searched,)    # i will investigate the brakets
				result = my_cursor.execute(sql, name)
				result = my_cursor.fetchall()
				#print(result)
				
				if not result:

					result="Sorry No Record has been found for this " + str(drop1.get())+ ". Try other option or check in all Driver List Tabel"
					tkinter.messagebox.showwarning("Warning",result)
				else:

					for index, x in enumerate(result): #for enumerate watch video 31
						self.E_Full_Name1.set(result[index][0])
						self.E_DOB1.set(result[index][1])
						self.E_Mobile1.set(result[index][2])
						self.E_Address1.set(result[index][3])
						self.E_PostCode1.set(result[index][4])
						self.E_City1.set(result[index][5])
						self.E_State1.set(result[index][6])
						self.E_Registration_Date1.set(result[index][7])
						self.E_P_D.set(result[index][8])
						self.E_Status.current(2)
						self.E_W_R.set("0")
						self.E_W_A.set("0")

			def Update_Agreement():
				print("i am in update")
				print(search_box1.get())
				#Drivers (Full_Name, DOB, Mobile, Address, PostCode, City, State, Registration_Date , P_D, Status, Week_R, Week_A)
				seq_command = """ UPDATE Drivers SET Full_Name = %s, DOB = %s, Mobile = %s, Address = %s, PostCode = %s, City = %s, State = %s, Registration_Date = %s, P_D = %s, Status =%s , Week_R = %s, Week_A =%s WHERE Driver_ID = %s"""
				

				self.E_Full_Name1.get()
				self.E_DOB1.get()
				self.E_Mobile1.get()
				self.E_Address1.get()
				self.E_PostCode1.get()
				self.E_City1.get()
				self.E_State1.get()
				self.E_Registration_Date1.get()
				self.E_P_D.get()
				self.E_Status.get()
				self.E_W_R.get()
				self.E_W_A.get()

				driver_Id  = search_box1.get()

				print(self.E_W_A.get())
				print(self.E_State1.get())
				print(self.E_W_A.get())
				print("")
				print("")
				print("")
				print("")

				inputs = (str(self.E_Full_Name1.get()),str(self.E_DOB1.get()),str(self.E_Mobile1.get()),str(self.E_Address1.get()), str(self.E_PostCode1.get()),str(self.E_City1.get()),str(self.E_State1.get()),str(self.E_Registration_Date1.get()),str(self.E_P_D.get()),str(self.E_Status.get()),str(self.E_W_R.get()),str(self.E_W_A.get()),str(driver_Id) )
				my_cursor.execute(seq_command, inputs)
				mydb.commit()

				self.E_Full_Name1.set("")
				self.E_DOB1.set("")
				self.E_Mobile1.set("")
				self.E_Address1.set("")
				self.E_PostCode1.set("")
				self.E_City1.set("")
				self.E_State1.set("")
				self.E_Registration_Date1.set("")
				self.E_P_D.current(0)
				self.E_Status.current(0)
				self.E_W_R.current(0)
				self.E_W_A.current(0)
				print("Updated Successfully")
				#txtFullname.delete(0, END)
				

			search_box1=Entry(self.Master_Right_Center_Frame)
			search_box1.grid(row=0, column=1, pady=10, padx=10)
			#entry box label
			search_box_label1=Label(self.Master_Right_Center_Frame, text="Search...",bg="gainsboro",font=("Ariel", 12, 'bold'))
			search_box_label1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
			#drop down box
			drop1 = ttk.Combobox(self.Master_Right_Center_Frame, value=["search by...", "Driver FullName", "Driver ID", "Driver Mobile"],font=("Ariel", 12, 'bold'))
			drop1.current(0)
			drop1.grid(row=0, column = 2)
			Payment_search_button=Button(self.Master_Right_Center_Frame, text="End Taxi Agreement",font=("Ariel", 16, 'bold'),fg="black", bd=30, command= Change_Drivers_Status)
			Payment_search_button.grid(row = 1, column=0, padx=10, pady=15)
			####################################### Creatd cursor and TextBox

			scroll = Scrollbar(self.Master_Right_top_Frame)
			scroll.pack(side=RIGHT, fill=Y)

			textbox=Text(self.Master_Right_top_Frame,bg='azure', yscrollcommand=scroll.set,font=('arial', 11, 'bold'),width=210,height=20)
			textbox.pack(side=LEFT, fill=BOTH, expand=1)

			scroll.config(command=textbox.yview)
			
			SQL = "SELECT  Drivers.Driver_ID,\
			Drivers.Full_Name, Drivers.Address,Drivers.City,\
			Drivers.State, Drivers.Mobile,Taxi_Registration.Registration_No,\
			Drivers.Status FROM Drivers  INNER JOIN Taxi_Registration ON Drivers.Driver_ID = Taxi_Registration.Driver_ID;"
			result = my_cursor.execute(SQL)
			result = my_cursor.fetchall()
			for r in result:
				print (r)
			textbox.delete("1.0","end")
			textbox.insert('end',"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			textbox.insert('end',"\tDriverID\tFull Name\t\t\tAddress\t\t\t City\t\t state\t\t Mobile\t\t Registration_No\t\tStatus\n\n ")
			textbox.insert('end',"--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
			for index, x in enumerate(result): 
				textbox.insert('end', "\t"+ str(result[index][0])+ "\t" + str(result[index][1]) + "\t\t\t" + str(result[index][2])  + "\t\t\t" + str(result[index][3]) 
						+ "\t\t"  + str(result[index][4]) +  "\t\t" + str(result[index][5])+"\t\t" + str(result[index][6]) + "\t\t"+  str(result[index][7]) + "\n ")

			self.NewDriver_Titleframe= Frame(self.Master_Right_top_Frame1, bg='grey',bd=10,width=400, height=90,relief=SUNKEN) ###### relief ridge check later
			self.NewDriver_Titleframe.pack(side=TOP,fill=X)
			self.lblCustomerTitle= Label(self.NewDriver_Titleframe, bg='gainsboro',font=('apple chancery', 16, 'bold','italic'), text="End The Taxi Agreement",bd=3, 
				fg='black', justify=CENTER)
			self.lblCustomerTitle.pack(fill=X)

			self.NewDriver_EntryFrame = Frame(self.Master_Right_top_Frame1,bg='gainsboro', bd=15, pady=4)
			self.NewDriver_EntryFrame.pack(side=TOP,fill=BOTH, expand=1)



			self.lblFull_Name = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Full Name ", bg='gainsboro', fg='black')
			self.lblFull_Name.grid(row=0,column=0,sticky=W)
			self.txtFullname= Entry(self.NewDriver_EntryFrame, font=('arial',12,'bold'), bd=7, bg="white", insertwidth=2, justify='right',width=18, textvariable=self.E_Full_Name1)
			self.txtFullname.grid(row=0,column=1,padx=20,pady=4,sticky=W)
		
			self.lbl_DOB = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Date of Birth  ", bg='gainsboro', fg='black')
			self.lbl_DOB.grid(row=0,column=2,sticky=W)  
			self.txt_DOB= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"), textvariable=self.E_DOB1 , bd=7, bg="white", insertwidth=2,width=18, justify= RIGHT)
			self.txt_DOB.grid(row=0,column=3,padx=20,pady=4,sticky=W)

			self.lblMobile = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Mobile ", bg='gainsboro', fg='black')
			self.lblMobile.grid(row=0,column=4,sticky=W)
			self.txtMobile= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_Mobile1 , bd=7, bg="white", insertwidth=2,width=18, justify= RIGHT)
			self.txtMobile.grid(row=0,column=5,padx=20,pady=4,sticky=W)

			self.lblAddress = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Address ", bg='gainsboro', fg='black')
			self.lblAddress.grid(row=0,column=6,sticky=W)
			self.txtAddress= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_Address1 , bd=7, bg="white",width=18, insertwidth=2, justify= RIGHT)
			self.txtAddress.grid(row=0,column=7,padx=20,pady=4,sticky=W)

			self.lblPostCode = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="PostCode", bg='gainsboro', fg='black')
			self.lblPostCode.grid(row=1,column=0,sticky=W)
			self.txtPostCode= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_PostCode1 , bd=7, bg="white",width=18, insertwidth=2, justify= RIGHT)
			self.txtPostCode.grid(row=1,column=1,padx=20,pady=4,sticky=W)

			self.lblCity = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="City ", bg='gainsboro', fg='black')
			self.lblCity.grid(row=1,column=2,sticky=W)
			self.txtCity= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_City1 , bd=7, bg="white",width=18, insertwidth=2, justify= RIGHT)
			self.txtCity.grid(row=1,column=3,padx=20,pady=4,sticky=W)

			self.lblState = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="State ", bg='gainsboro', fg='black')
			self.lblState.grid(row=1,column=4,sticky=W)
			self.txtState= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"),  textvariable=self.E_State1 , bd=7, bg="white",width=18, insertwidth=2, justify= RIGHT)
			self.txtState.grid(row=1,column=5,padx=20,pady=4,sticky=W)

			self.lblDate = Label(self.NewDriver_EntryFrame,font=('apple chancery', 14, 'bold'), text="Registration Date  ", bg='gainsboro', fg='black')
			self.lblDate.grid(row=1,column=6,sticky=W)  
			self.txtDate= Entry(self.NewDriver_EntryFrame, font=("arial", 12, "bold"), textvariable=self.E_Registration_Date1 , bd=7, bg="white",width=18, insertwidth=2, justify= RIGHT)
			self.txtDate.grid(row=1,column=7,padx=20,pady=4,sticky=W) 

			self.E_P_D = ttk.Combobox(self.NewDriver_EntryFrame,width=18, font=('arial', 12, 'bold'),value= ["Please Select","Monday", "Tuesday", "Wednesday","Thursday", "Friday","Saturday","Sunday"])
			self.E_P_D.current(0)
			self.E_P_D.grid(row=2, column = 1, pady=6, padx=10)

			self.lblP_D = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Pay Day ", bg='gainsboro', fg='black')
			self.lblP_D.grid(row=2,column=0,sticky=W)

			self.E_Status = ttk.Combobox(self.NewDriver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select", "Active","DeActive"])
			self.E_Status.current(0)
			self.E_Status.grid(row=2, column = 3, pady=6, padx=10)

			self.lblstatus = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Status ", bg='gainsboro', fg='black')
			self.lblstatus.grid(row=2,column=2,sticky=W)


			self.E_W_R = ttk.Combobox(self.NewDriver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select", "150","160","170", "175","180","185","190"])
			self.E_W_R.current(0)
			self.E_W_R.grid(row=2, column = 5, pady=6, padx=10)

			self.lblw_r = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Weekly Rent ", bg='gainsboro', fg='black')
			self.lblw_r.grid(row=2,column=4,sticky=W)

			self.E_W_A = ttk.Combobox(self.NewDriver_EntryFrame,width=18, font=('arial', 12, 'bold'),value=["Please Select","0", "10","15","20", "30","40","50","100"])
			self.E_W_A.current(0)
			self.E_W_A.grid(row=2, column = 7, pady=6, padx=10)

			self.lblw_a = Label(self.NewDriver_EntryFrame,font=('apple chancery', 12, 'bold'), text="Weekly Access ", bg='gainsboro', fg='black')
			self.lblw_a.grid(row=2,column=6,sticky=W)
			Payment_search_button=Button(self.NewDriver_EntryFrame, text="Update Agreement",font=("Ariel", 16, 'bold'),fg="black", bd=30, command= Update_Agreement)
			Payment_search_button.grid(row = 3, column=0, padx=2, pady=15)


			


			
			

			







if __name__ == '__main__':
	root = Tk()
	

	
	application = LoginWindow(root)

	root.mainloop()
