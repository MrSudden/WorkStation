from PyQt5 import QtCore, QtGui, QtWidgets
import ETMS_Resources_rc
import sys,os,re
from Database import Admin_Data,Client_Data

class Ui_Form(QtWidgets.QMainWindow):
	Database = Admin_Data()
	C_Database = Client_Data()

	def __init__(self, parent = None):
		super(Ui_Form, self).__init__(parent)
		self.setupUi(self)
		self.BusPark = ""

		self.calendarWidget.setEnabled(True)
		self.L_Admin.clicked.connect(self.page_Admin_0)
		self.L_About.clicked.connect(self.page_About_1)
		self.A_Back.clicked.connect(self.page_begin)
		self.Admin_Login_Button.clicked.connect(self.page_Admin_1)
		self.Admin_ID_Entry.textEdited.connect(self.Admin_Log_Error.clear)
		self.Admin_Password_Entry.textEdited.connect(self.Admin_Log_Error.clear)

		self.Admin_Client.clicked.connect(self.Client_Log_1)
		self.Admin_Client_Log.clicked.connect(self.Client_Log_2)
		self.Admin_Book.clicked.connect(self.Client_Log_3)
		self.Admin_Others.clicked.connect(self.Client_Log_5)
		self.Admin_Pay.clicked.connect(self.Client_Log_4)

		self.lineEdit_21.textEdited.connect(self.checkMark)
		self.lineEdit_22.textEdited.connect(self.checkMark)

		self.Reg_Reg.clicked.connect(self.Client_Log)

		self.Gender_Select.currentIndexChanged['int'].connect(self.Reg_Error.clear)
		self.Client_Select.currentIndexChanged['int'].connect(self.Reg_Error.clear)
		self.lineEdit.textEdited.connect(self.Reg_Error.clear)
		self.lineEdit_18.textEdited.connect(self.Reg_Error.clear)
		self.lineEdit_20.textEdited.connect(self.Reg_Error.clear)
		self.lineEdit_21.textEdited.connect(self.Reg_Error.clear)
		self.lineEdit_22.textEdited.connect(self.Reg_Error.clear)

		self.Log_UserEdit.textEdited.connect(self.Log_Error.clear)
		self.Log_UserPass.textEdited.connect(self.Log_Error.clear)

		self.Log_button.clicked.connect(self.Client_Login_log)

		self.Client_Return.clicked.connect(self.Return)
		self.Client_Package_Purchase.clicked.connect(self.Purchase_P)
		self.Client_Share_Resources.clicked.connect(self.ShareIt)
		self.Package_List.clicked.connect(self.Client_Log_6)

		self.Driver_Submit_BP.clicked.connect(self.Driver_BP)
		self.Driver_Next_BP.clicked.connect(self.Driver_BP)
		self.Quantity.valueChanged.connect(self.Driver_BP)
		self.Passenger_Number.valueChanged.connect(self.Driver_BP)

		self.Package_Amount.valueChanged.connect(self.Calc_Package)
		self.pushButton_5.clicked.connect(self.Make_P)

		self.Recipient_ID.textEdited.connect(self.Share_Parameters)
		self.Package_Ticket_Amount.valueChanged['int'].connect(self.Share_Parameters_1)

		self.pushButton_6.clicked.connect(self.Transfer_Package)

		self.Book_Next.clicked.connect(self.booking)
		self.Book_confirm.clicked.connect(self.booking)
		self.pushButton_4.clicked.connect(self.booking)

		self.Book_ID.textEdited.connect(self.Book_Log.clear)
		self.Book_Package.textEdited.connect(self.Book_Log.clear)

		self.Check_In.clicked.connect(self.D_Loc_Check)
		self.Check_Out.clicked.connect(self.D_Loc_Check)
		self.Drivers_ID.textEdited.connect(self.CSS)

		self.Pay_Client_ID.textEdited.connect(self.Pay_Log.clear)
		self.Pay_cpnfirm.clicked.connect(self.IssuePayment)
		self.Clear_Pay.clicked.connect(self.IssuePayment)
		self.Pay_Button.clicked.connect(self.IssuePayment)

	def booking(self):
		Signal = self.sender()
		SenderName = str(Signal.objectName())

		field = self.Admin_ID_Entry.text()
		ID = self.Book_ID.text()
		IDP = self.Book_Package.text()
		main_Ad = self.Database.Admin_main_id(field)

		Pack_Name = self.Database._port_Name(field)

		if SenderName == "pushButton_4":
			Queue_D = self.C_Database.Q_SD(Pack_Name,main_Ad)
			self.DisableToolButton()

			if Queue_D is None:
				self.C_Database.Q_AP(main_Ad,ID,Pack_Name,"None","None")
				UCV = self.C_Database.Q_PCU(main_Ad,Pack_Name)
				self.Book_Log.setStyleSheet("font-size: 15pt;"
															"font-family: Comic Sans MS;"
															"color: blue;")
				self.Book_Log.setText("There are no available Vehicle in %s's bus park,\ntherefore you have been assign the unique Call_Up Value '%i'\nplease wait at our Passenger's waiting area.\nPlease ensure to be at our bus park premises in order to respond\nwhen your unique value is called\nIf your are not available when your unique value is called\nyou will be called up when the next vehicle arrives\nThank you for making use of our service" % (Pack_Name,UCV - 1))
				self.Book_Next.setEnabled(True)
				self.pushButton_4.setEnabled(False)

			else:
				LP = self.C_Database.Q_DCU(Pack_Name,main_Ad)
				BUS = LP[0]
				C_Num = LP[1]
				self.C_Database.Q_AP(main_Ad,ID,Pack_Name,BUS,C_Num)
				self.Book_Log.setStyleSheet("font-size: 15pt;"
															"font-family: Comic Sans MS;"
															"color: blue;")
				self.Book_Log.setText('There is a Vehicle with ID: "%s" available for you\nYour entry value is: "%i", Please Proceed to your to the vehicle assigned to you\nThank you for making use of our service' % (BUS,C_Num))
				self.Book_Next.setEnabled(True)
				self.pushButton_4.setEnabled(False)

		elif SenderName == "Book_confirm":
			check = self.C_Database.CP_book(ID,IDP,main_Ad)

			if check is True and len(ID) == 11 and len(IDP) == 12:
				self.pushButton_4.setEnabled(True)
				self.Book_confirm.setEnabled(False)
				self.Book_ID.setReadOnly(True)
				self.Book_Package.setReadOnly(True)
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: blue;")
				self.Book_Log.setText("Please Proceed to Book")

			elif check is False and len(ID) == 11 and len(IDP) == 12:
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: green;")
				#a message where one is alerted if his package is empty
				self.Book_Log.setText("Please enter another Package ID belonging to you\nYou can Purchase Package if you do not have any,\nin other to continue enjoying our service")
				print("\a")

			elif check == "Nothing":
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: red;")
				self.Book_Log.setText("The Client ID entered does not exist for any client\nPlease re_enter the Client ID")
				print("\a")

			elif check == "Not in database" and len(ID) == 11 and len(IDP) == 12:
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: red;")
				self.Book_Log.setText("The Client ID entered does not exist for any client\nPlease re_enter the Client ID")
				print("\a")

			elif len(ID) == 11 and len(IDP) <= 0 or len(ID) <= 0 and len(IDP) == 12:
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: red;")
				self.Book_Log.setText("All field Must be filled")
				print("\a")

			elif check is None:
				self.Book_Log.setStyleSheet("font-size: 17pt;"
															"font-family: Comic Sans MS;"
															"color: red;")
				self.Book_Log.setText("You cannot book at the same location twice\nIn other to book once more\nat this location you must cancel\nyour previous book before the your assigned bus leaves the park\nor Just simply board your vehicle and book\nat our other bus park")
				print("\a")

			elif  len(IDP) < 12 or len(ID) < 11:
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: red;")
				self.Book_Log.setText("Invalid Input, Please re_enter the details specified")
				print("\a")

			elif  len(IDP) == 0 or len(ID) == 0:
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: red;")
				self.Book_Log.setText("Invalid Input, Both field must be filled")
				print("\a")

			else:
				self.Book_Log.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: red;")
				self.Book_Log.setText("All fields must be filled")
				print("\a")

		elif SenderName == "Book_Next":
			self.EnableToolButton()
			self.Book_ID.clear()
			self.Book_ID.setReadOnly(False)
			self.Book_Log.clear()
			self.Book_Package.clear()
			self.Book_Package.setReadOnly(False)
			self.pushButton_4.setEnabled(False)
			self.Book_confirm.setEnabled(True)
			self.Book_Next.setEnabled(False)

		else:
			pass

	def Calc_Package(self):
		value = self.Package_Amount.value()
		Est_Cost = str(value * 1000)
		Ticket = str(value * 10)
		self.Package_Estimated_Price.setText("N" + Est_Cost)
		self.Package_Ticket.setText(Ticket)
		if value > 0:
			self.pushButton_5.setEnabled(True)
		else:
			self.pushButton_5.setEnabled(False)

	def Make_P(self):
		Id = self.Log_UserEdit.text()
		fname = self.lineEdit_18.text()
		gender = self.Gender_Select.currentText()
		phone = self.lineEdit.text()
		Email = self.lineEdit_20.text()
		client = self.Client_Select.currentText()
		Pass = self.lineEdit_21.text()
		main_Ad = self.Database.Admin_main_id(self.Admin_ID_Entry.text())

		value = self.Package_Amount.value()
		ticket = value * 10

		ID =self.C_Database.Driver_ID(fname.title(),gender,phone,Email,client,Pass,main_Ad)

		if ID != []:
			obsolete = self.C_Database.Package_Ref(ID,main_Ad)

			Value = obsolete[0] + value
			Ticket = obsolete[1] + ticket
			self.C_Database.Update_Passenger(ID,Value,Ticket,main_Ad)
			self.C_Database.Package_Cord(value,Ticket,ID,main_Ad)

		else:
			obsolete = self.C_Database.Package_Ref(Id,main_Ad)

			Value = obsolete[0] + value
			Ticket = obsolete[1] + ticket
			self.C_Database.Update_Passenger(Id,Value,Ticket,main_Ad)
			self.C_Database.Package_Cord(value,ticket,Id,main_Ad)

		self.Package_Amount.setValue(0)
		self.Third_Stack_Widget.setCurrentIndex(2)
		self.Package_Quantity.setStyleSheet("font-size: 20pt;"
											"font-family: Consolas;"
											"color: rgb(170, 0, 255);"
											)
		self.Package_Quantity.setText(str(Value))

		self.Ticket_Quantity.setStyleSheet("font-size: 20pt;"
									"font-family: Consolas;"
									"color: rgb(170, 0, 255);"
									)
		self.Ticket_Quantity.setText(str(Ticket))

		self.buttonGroup_4.setExclusive(False)
		self.Client_Package_Purchase.setChecked(False)
		self.buttonGroup_4.setExclusive(True)

	def ShareIt(self):
		self.Third_Stack_Widget.setCurrentIndex(1)

	def Purchase_P(self):
		self.Third_Stack_Widget.setCurrentIndex(0)
		self.Payment_Successful.setStyleSheet("font-size: 20pt;"
															"font-family: Comic Sans MS;"
															"color: blue;")
		self.Payment_Successful.setText("Online Payment coming Soon....")

	def Transfer_Package(self):
		Id = self.Log_UserEdit.text()
		fname = self.lineEdit_18.text()
		gender = self.Gender_Select.currentText()
		phone = self.lineEdit.text()
		Email = self.lineEdit_20.text()
		client = self.Client_Select.currentText()
		Pass = self.lineEdit_21.text()
		main_Ad = self.Database.Admin_main_id(self.Admin_ID_Entry.text())
		ID = self.C_Database.Driver_ID(fname.title(),gender,phone,Email,client,Pass,main_Ad)

		ID_TF = self.Recipient_ID.text()
		Amount = self.Package_Ticket_Amount.value()

		Checker_ID = ""
		Checker_Id = ""

		if ID !=[]:
			Checker_ID = self.C_Database.Package_ref(ID,main_Ad,Amount)
		else:
			Checker_Id = self.C_Database.Package_ref(Id,main_Ad,Amount)

		if Checker_ID is None or Checker_Id is None:
			Checker_Id = None
			Checker_ID = None
		else:
			Checker_ID = True
			Checker_Id = True

		if ID != [] and Checker_ID is True and ID_TF != ID:
			Checker = self.C_Database.Client_Info(ID_TF,main_Ad)
			if Checker is True and ID != ID_TF:
				self.C_Database.Share_Package(ID,main_Ad,Amount,ID_TF)

				Value = self.C_Database.Package_Ref(ID,main_Ad)
				self.Package_Ticket_Amount.setValue(0)
				self.Third_Stack_Widget.setCurrentIndex(2)
				self.Package_Quantity.setStyleSheet("font-size: 20pt;"
													"font-family: Consolas;"
													"color: rgb(170, 0, 255);"
													)
				self.Package_Quantity.setText(str(Value[0]))

				self.Ticket_Quantity.setStyleSheet("font-size: 20pt;"
											"font-family: Consolas;"
											"color: rgb(170, 0, 255);"
											)
				self.Ticket_Quantity.setText(str(Value[1]))

				self.buttonGroup_4.setExclusive(False)
				self.Client_Share_Resources.setChecked(False)
				self.buttonGroup_4.setExclusive(True)

			else:
				self.Recipient_ID.clear()
				self.Package_Ticket_Amount.setValue(0)
				print("\a")

		else:
			Checker = self.C_Database.Client_Info(ID_TF,main_Ad)
			if Checker is True and ID_TF != Id and Checker_Id is True:
				self.C_Database.Share_Package(Id,main_Ad,Amount,ID_TF)

				Value = self.C_Database.Package_Ref(Id,main_Ad)
				self.Package_Ticket_Amount.setValue(0)
				self.Third_Stack_Widget.setCurrentIndex(2)
				self.Package_Quantity.setStyleSheet("font-size: 20pt;"
													"font-family: Consolas;"
													"color: rgb(170, 0, 255);"
													)
				self.Package_Quantity.setText(str(Value[0]))

				self.Ticket_Quantity.setStyleSheet("font-size: 20pt;"
											"font-family: Consolas;"
											"color: rgb(170, 0, 255);"
											)
				self.Ticket_Quantity.setText(str(Value[1]))

				self.buttonGroup_4.setExclusive(False)
				self.Client_Share_Resources.setChecked(False)
				self.buttonGroup_4.setExclusive(True)

			else:
				self.Recipient_ID.clear()
				self.Package_Ticket_Amount.setValue(0)
				print("\a")

	def Check_O(self):
		return self.Admin_ID_Entry.text(), self.Admin_Password_Entry.text()

	def page_Admin_0(self):
		self.mainStackWidget.setCurrentIndex(3)

	def page_About_1(self):
		self.mainStackWidget.setCurrentIndex(1)

	def page_begin(self):
		self.mainStackWidget.setCurrentIndex(0)

	def Client_Log_1(self):
		self.Second_Stack.setCurrentIndex(0)

	def Client_Log_2(self):
		self.Second_Stack.setCurrentIndex(1)

	def Client_Log_3(self):
		self.Second_Stack.setCurrentIndex(2)

	def Client_Log_4(self):
		self.Second_Stack.setCurrentIndex(3)
		self.Pay_Log.clear()

	def Client_Log_5(self):
		self.Second_Stack.setCurrentIndex(4)

	def Client_Log_6(self):
		fname = self.lineEdit_18.text()
		gender = self.Gender_Select.currentText()
		phone = self.lineEdit.text()
		Email = self.lineEdit_20.text()
		client = self.Client_Select.currentText()
		Pass = self.lineEdit_21.text()

		Id = self.Log_UserEdit.text()
		main_Ad = self.Database.Admin_main_id(self.Admin_ID_Entry.text())
		ID =self.C_Database.Driver_ID(fname.title(),gender,phone,Email,client,Pass,main_Ad)

		if ID != []:
			Package = self.C_Database.Package_Alert(ID,main_Ad)
			LPackage = len(Package)
			if Package != []:
				self.label_11.setStyleSheet("font-size: 20pt;"
												"font-family: Comic Sans MS;"
												"color: rgb(3, 230, 255);"
												"background-color: white"
												)
				self.label_11.setText("Your total number of package available is: %i" % LPackage)
				for x in range(0,LPackage):
					__sortingEnabled = self.TREE.isSortingEnabled()
					self.TREE.setSortingEnabled(False)
					item_0 = QtWidgets.QTreeWidgetItem(self.TREE)
					font = QtGui.QFont()
					font.setPointSize(12)
					item_0.setFont(0, font)
					item_0.setFont(1, font)
					item_0.setFont(2, font)
					self.TREE.topLevelItem(x).setText(0,str(x+1))
					self.TREE.topLevelItem(x).setText(1,Package[x][0])
					self.TREE.topLevelItem(x).setText(2,str(Package[x][1]))
					self.TREE.setSortingEnabled(__sortingEnabled)

			else:
				self.label_11.setStyleSheet("font-size: 18pt;"
												"font-family: Comic Sans MS;"
												"color: red;"
												"background-color: white"
												)
				self.label_11.setText("You have no Package, kindly purchase some to make use of our services")
				print("\a")
		else:
			Package = self.C_Database.Package_Alert(Id,main_Ad)
			LPackage = len(Package)
			if Package != []:
				self.label_11.setStyleSheet("font-size: 20pt;"
												"font-family: Comic Sans MS;"
												"color: rgb(3, 230, 255);"
												"background-color: white"
												)
				self.label_11.setText("Your total number of package available is: %i" % LPackage)
				for x in range(0,LPackage):
					__sortingEnabled = self.TREE.isSortingEnabled()
					self.TREE.setSortingEnabled(False)
					item_0 = QtWidgets.QTreeWidgetItem(self.TREE)
					font = QtGui.QFont()
					font.setPointSize(12)
					item_0.setFont(0, font)
					item_0.setFont(1, font)
					item_0.setFont(2, font)
					self.TREE.topLevelItem(x).setText(0,str(x+1))
					self.TREE.topLevelItem(x).setText(1,Package[x][0])
					self.TREE.topLevelItem(x).setText(2,str(Package[x][1]))
					self.TREE.setSortingEnabled(__sortingEnabled)

			else:
				self.label_11.setStyleSheet("font-size: 18pt;"
												"font-family: Comic Sans MS;"
												"color: red;"
												"background-color: white"
												)
				self.label_11.setText("You have no Package, kindly purchase some to make use of our services")
				print("\a")

		self.Third_Stack_Widget.setCurrentIndex(4)

	def Share_Parameters(self):
		if self.Package_Ticket_Amount.value() > 0 and len(self.Recipient_ID.text()) > 0:
			self.pushButton_6.setEnabled(True)
		else:
			self.pushButton_6.setEnabled(False)

	def Share_Parameters_1(self):
		if len(self.Recipient_ID.text()) > 0 and self.Package_Ticket_Amount.value() > 0:
			self.pushButton_6.setEnabled(True)
		else:
			self.pushButton_6.setEnabled(False)

	def Return(self):
		self.Log_UserEdit.clear()
		self.Log_UserPass.clear()
		self.lineEdit_18.clear()
		self.Gender_Select.setCurrentIndex(-1)
		self.Client_Select.setCurrentIndex(-1)
		self.lineEdit.clear()
		self.lineEdit_20.clear()
		self.lineEdit_21.clear()
		self.lineEdit_22.clear()
		self.Book_ID.clear()
		self.Book_Package.clear()
		self.Pay_Client_ID.clear()
		self.mainStackWidget.setCurrentIndex(2)
		self.Second_Stack.setCurrentIndex(6)

		self.buttonGroup_3.setExclusive(False)
		self.Admin_Client.setChecked(False)
		self.Admin_Client_Log.setChecked(False)
		self.buttonGroup_3.setExclusive(True)

		self.Package_Quantity.clear()
		self.Ticket_Quantity.clear()

		self.buttonGroup_4.setExclusive(False)
		self.Client_Return.setChecked(False)
		self.buttonGroup_4.setExclusive(True)

		length_Db = self.C_Database.Client_No()

		self.label_23.setStyleSheet("font-size: 20pt;"
												"font-family: Comic Sans MS;"
												"color: blue;"
												)
		self.label_23.setText("CLIENT COUNT\n%i" % length_Db)

		self.TREE.clear()

	def checkMark(self):
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/images/alert.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon.addPixmap(QtGui.QPixmap(":/images/alert.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)

		icon_2 = QtGui.QIcon()
		icon_2.addPixmap(QtGui.QPixmap(":/images/check.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon_2.addPixmap(QtGui.QPixmap(":/images/check.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)

		icon_3 = QtGui.QIcon()
		icon_3.addPixmap(QtGui.QPixmap(":/images/White.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon_2.addPixmap(QtGui.QPixmap(":/images/White.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)

		field = self.lineEdit_21.text()
		field_1 = self.lineEdit_22.text()

		if field == field_1 and len(field) >= 6 and len(field_1) >= 6:
			self.Checker_1.setIcon(icon_2)
			self.Checker_2.setIcon(icon_2)

		elif field != field_1 and len(field) < 6 and len(field_1) < 6:
			self.Checker_1.setIcon(icon)
			self.Checker_2.setIcon(icon)

		elif field == field_1 and len(field) < 6 and len(field_1) < 6:
			self.Checker_1.setIcon(icon)
			self.Checker_2.setIcon(icon)

		elif field != field_1 and len(field) >= 6 and len(field_1) >= 6:
			self.Checker_1.setIcon(icon)
			self.Checker_2.setIcon(icon)

		elif len(field) == 0 and len(field_1) == 0:
			self.Checker_1.setIcon(icon_3)
			self.Checker_2.setIcon(icon_3)

		else:
			self.Checker_1.setIcon(icon_3)
			self.Checker_2.setIcon(icon_3)

	def checkPass(self):
		field = self.lineEdit_21.text()
		field_1 = self.lineEdit_22.text()

		if field == field_1 and len(field) >= 6 and len(field_1) >= 6:
			return field_1

		elif len(field) >= 1 and len(field_1) >= 1 and len(field) <= 6 and len(field_1) <= 6:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Password is less than 6 digits")
			print("\a")
			return None
		elif len(field) == 0 and len(field_1) == 0:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("All fields must be filled")
			print("\a")
			return None
		else:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Invalid input format")
			print("\a")
			return None

	def validateEmail(self):
		email = re.compile(r'\w+@\w+\.\w+', re.IGNORECASE)
		email = email.findall(self.lineEdit_20.text())

		if email is not None and len(email) > 0 and "." in self.lineEdit_20.text():
			return self.lineEdit_20.text()

		elif len(self.lineEdit_20.text()) == 0:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("All fields must be filled")
			print("\a")
			return None
		else:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Error in Email format")
			print("\a")
			return None

	def validateName(self):
		namecontent = re.compile(r'[1234567890!@#$%&*()"{}+=/<>]')
		name = namecontent.search(self.lineEdit_18.text())

		if len(self.lineEdit_18.text()) >= 1 and len(self.lineEdit_18.text()) < 4:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Fullname too short to be valid")
			print("\a")
			return None

		elif len(self.lineEdit_18.text()) == 0:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("All fields must be filled")
			print("\a")
			return None

		elif name is None and len(self.lineEdit_18.text()) >= 4 and " " in self.lineEdit_18.text():
			return self.lineEdit_18.text().title()

		else:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("invalid input format")
			print("\a")
			return None

	def validatePhone(self):
		if self.lineEdit.text().isdigit() == True and len(self.lineEdit.text()) >= 11 and int(self.lineEdit.text()) != 0:
			return self.lineEdit.text()

		elif self.lineEdit.text().isdigit() == True and len(self.lineEdit.text()) >= 1 and  len(self.lineEdit.text()) <= 11:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Phone number less than eleven digits")
			print("\a")
			return None
		elif len(self.lineEdit.text()) == 0:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("All fields must be filled")
			print("\a")
			return None
		else:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Phone number contains non numeric values")
			print("\a")
			return None

	def validateGender(self):
		if self.Gender_Select.currentIndex() == -1:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Please specify your gender")
			print("\a")
			return None
		else:
			return self.Gender_Select.currentText()

	def validateClient(self):
		if self.Client_Select.currentIndex() == -1:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("Please specify what client you are")
			print("\a")
			return None
		else:
			return self.Client_Select.currentText()

	def validateID(self,value):
		if value == 0:
			return self.C_Database.IDP_Generator()

		elif value == 1:
			return self.C_Database.IDD_Generator()

		else:
			return None

	def DisableToolButton(self):
		self.Admin_Client.setEnabled(False)
		self.Admin_Client_Log.setEnabled(False)
		self.Admin_Book.setEnabled(False)
		self.Admin_Others.setEnabled(False)
		self.Admin_Pay.setEnabled(False)

	def EnableToolButton(self):
		self.Admin_Client.setEnabled(True)
		self.Admin_Client_Log.setEnabled(True)
		self.Admin_Book.setEnabled(True)
		self.Admin_Others.setEnabled(True)
		self.Admin_Pay.setEnabled(True)

	def Client_Log(self):
		Fname = self.validateName()
		gender = self.validateGender()
		Phone = self.validatePhone()
		email = self.validateEmail()
		client = self.validateClient()
		Pass = self.checkPass()
		ID = self.validateID(self.Client_Select.currentIndex())
		verify_All = self.C_Database.Check_All()
		All = (Fname, gender, Phone, email,client)
		main_Ad = self.Database.Admin_main_id(self.Admin_ID_Entry.text())

		if Fname is not None  and gender is not None and Phone is not None and email is not None and client is not None and Pass is not None and All not in verify_All and ID is not None:
			#implement to database
			#id generation comes here
			self.C_Database.Input(Fname, gender, Phone, email, client, Pass,ID,main_Ad)

			if ID[0:3] == "ETP":
				self.C_Database.Client_Passenger(ID,main_Ad)
				self.mainStackWidget.setCurrentIndex(4)
				self.Third_Stack_Widget.setCurrentIndex(2)
				self.Click_Details.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: blue;"
											)
				self.Click_Details.setText("Welcome %s \nYour Client_ID is: %s" % (Fname,ID))

				self.Package_Quantity.setStyleSheet("font-size: 20pt;"
											"font-family: Consolas;"
											"color: rgb(170, 0, 255);"
											)
				self.Package_Quantity.setText("0")

				self.Ticket_Quantity.setStyleSheet("font-size: 20pt;"
											"font-family: Consolas;"
											"color: rgb(170, 0, 255);"
											)
				self.Ticket_Quantity.setText("0")

			elif ID[0:3] == "ETD":
				B_ID = self.C_Database.IDD_Generator()
				self.BUS_ID = B_ID
				self.C_Database.Driver_Init_Info(ID,main_Ad,B_ID)
				self.Second_Stack.setCurrentIndex(5)
				self.DisableToolButton()
				self.Description_details.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: blue;"
											)
				self.Description_details.setText("Welcome %s \nYour Client_ID is: %s.\nYou are to pay a sum of\nN10,000\nfor Registration Fee and a Subsequent Charge of\nN1,500 per Month\nPlease specify your Bus Details below" % (Fname,ID))
				self.Driver_Show.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: blue;"
											)
				self.Driver_Show.setText("Your Bus_ID is: %s" % B_ID)

		elif Fname is not None  and gender is not None and Phone is not None and email is not None and client is not None and Pass is not None and All in verify_All:
			self.Reg_Error.setStyleSheet("font-size: 13pt;"
										"font-family: Comic Sans MS;"
										"color: red;"
										)
			self.Reg_Error.setText("The details entered is already been used")
			print("\a")

		else:
			pass

	def Driver_BP(self):
		Signal = self.sender()
		SenderName = str(Signal.objectName())

		fname = self.lineEdit_18.text()
		gender = self.Gender_Select.currentText()
		phone = self.lineEdit.text()
		Email = self.lineEdit_20.text()
		client = self.Client_Select.currentText()
		Pass = self.lineEdit_21.text()
		main_Ad = self.Database.Admin_main_id(self.Admin_ID_Entry.text())

		ID =self.C_Database.Driver_ID(fname.title(),gender,phone,Email,client,Pass,main_Ad)

		B_ID = self.C_Database.Bus_iD(ID,main_Ad)

		if SenderName == "Driver_Submit_BP" and self.Quantity.value() != 0 and self.Passenger_Number.value() != 0:
			self.Quantity.setEnabled(False)
			self.Passenger_Number.setEnabled(False)
			self.Driver_Submit_BP.setEnabled(False)
			self.C_Database.Update_Driver(ID,self.Quantity.value(),self.Passenger_Number.value(),main_Ad,B_ID)
			self.Driver_Next_BP.setEnabled(True)
			pass

		elif SenderName == "Quantity" or SenderName == "Passenger_Number":
			self.Driver_Show.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color:blue;"
											)
			self.Driver_Show.setText("Your Bus_ID is: %s" % B_ID)
			pass

		elif SenderName == "Driver_Next_BP":
			self.Quantity.setEnabled(True)
			self.Quantity.setValue(0)
			self.Passenger_Number.setEnabled(True)
			self.Passenger_Number.setValue(0)
			self.Driver_Submit_BP.setEnabled(True)
			self.Driver_Next_BP.setEnabled(False)
			self.EnableToolButton()
			self.buttonGroup_3.setExclusive(False)
			self.Admin_Client_Log.setChecked(False)
			self.buttonGroup_3.setExclusive(True)
			self.Second_Stack.setCurrentIndex(6)

			self.lineEdit_18.clear()
			self.Gender_Select.setCurrentIndex(-1)
			self.Client_Select.setCurrentIndex(-1)
			self.lineEdit.clear()
			self.lineEdit_20.clear()
			self.lineEdit_21.clear()
			self.lineEdit_22.clear()

		else:
			self.Driver_Show.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: red;"
											)
			self.Driver_Show.setText("Vehicle cannot have zero sit\nPlease respecify your bus details")
			print("\a")

	def page_Admin_1(self):
		field = self.Admin_ID_Entry.text()
		field_1 = self.Admin_Password_Entry.text()
		Database_Msg = self.Database._format(field,field_1)

		if len(field_1) == 0 and len(field) != 0 or len(field_1) != 0 and len(field) == 0 or len(field) == 0 and len(field_1) == 0:
			self.Admin_Log_Error.setStyleSheet("font-size: 13pt;"
												"font-family: Comic Sans MS;"
												"color: red;"
												)
			self.Admin_Log_Error.setText("All Fields must be filled")
			print("\a")

		elif Database_Msg == "ABAG":
			self.Admin_Log_Error.setStyleSheet("font-size: 13pt;"
												"font-family: Comic Sans MS;"
												"color: green;"
												)
			self.Admin_Log_Error.setText("Coming Soon...")

		elif Database_Msg == "AAG":
			self.mainStackWidget.setCurrentIndex(2)
			length_Db = self.C_Database.Client_No()
			placeholder = self.Database._port_Name(field)
			self.BusPark = placeholder
			Ad_Name = self.Database.Ad_name(field)

			self.label_22.setStyleSheet("font-size: 20pt;"
												"font-family: Comic Sans MS;"
												"color: blue;"
												)
			self.label_22.setText("BUS_PARK\n%s" % placeholder)

			self.label_23.setStyleSheet("font-size: 20pt;"
												"font-family: Comic Sans MS;"
												"color: blue;"
												)
			self.label_23.setText("CLIENT COUNT\n%i" % length_Db)

			self.label_24.setStyleSheet("font-size: 20pt;"
												"font-family: Monaco;"
												"color: purple;"
												)
			self.label_24.setText("%s" %Ad_Name)

		elif Database_Msg == "FI":
			self.Admin_Log_Error.setStyleSheet("font-size: 13pt;"
												"font-family: Comic Sans MS;"
												"color: red;"
												)
			self.Admin_Log_Error.setText("User_Id or Password not found")
			print("\a")

		else:
			self.Admin_Log_Error.setStyleSheet("font-size: 13pt;"
												"font-family: Comic Sans MS;"
												"color: red;"
												)
			self.Admin_Log_Error.setText("User_Id or Password not found")
			print("\a")

	def Client_Login_log(self):
		field = self.Log_UserEdit.text()
		field_1 = self.Log_UserPass.text()
		Database_Msg = self.C_Database._format(field,field_1)

		if len(field_1) == 0 and len(field) != 0 or len(field_1) != 0 and len(field) == 0 or len(field) == 0 and len(field_1) == 0:
			self.Log_Error.setStyleSheet("font-size: 13pt;"
												"font-family: Comic Sans MS;"
												"color: red;"
												)
			self.Log_Error.setText("All Fields must be filled")
			print("\a")

		elif Database_Msg == "Passenger":
			Fname = self.C_Database.Client_Name(field)
			Bname = self.Database._port_Name_BA(self.Admin_ID_Entry.text(),self.C_Database.Client_AD(field))
			Aname = self.Database.Ad_name(self.Admin_ID_Entry.text())
			self.mainStackWidget.setCurrentIndex(4) #passenger
			self.Third_Stack_Widget.setCurrentIndex(2)
			self.Click_Details.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: blue;"
											)
			self.Click_Details.setText("Welcome %s\nYou are in %s's Bus Park \nof\n%s" % (Fname,Bname.title(),Aname))

			self.Package_Quantity.setStyleSheet("font-size: 20pt;"
											"font-family: Consolas;"
											"color: rgb(170, 0, 255);"
											)
			self.Package_Quantity.setText(str(self.C_Database.Package_Ref(self.Log_UserEdit.text(),self.C_Database.Client_AD(field))[0]))

			self.Ticket_Quantity.setStyleSheet("font-size: 20pt;"
										"font-family: Consolas;"
										"color: rgb(170, 0, 255);"
										)
			self.Ticket_Quantity.setText(str(self.C_Database.Package_Ref(self.Log_UserEdit.text(),self.C_Database.Client_AD(field))[1]))

		elif Database_Msg == "Driver":
			#Fname = self.C_Database.Client_Name(field)
			#Bname = self.Database._port_Name_BA(self.Admin_ID_Entry.text(),self.C_Database.Client_AD(field))
			#Aname = self.Database.Ad_name(self.Admin_ID_Entry.text())
			#self.Second_Stack.setCurrentIndex(5) #Driver
			#
			#self.Description_details.setStyleSheet("font-size: 18pt;"
			#								"font-family: Consolas;"
			#								"color: blue;"
			#								)
			#self.Description_details.setText("Welcome %s\nYou are in Bus Park %s\nof\n%s" % (Fname,Bname.title(),Aname))
			self.Log_Error.setStyleSheet("font-size: 13pt;"
									"font-family: Comic Sans MS;"
									"color: green;"
									)
			self.Log_Error.setText("Coming Soon!!!......")

		else:
			self.Log_Error.setStyleSheet("font-size: 13pt;"
									"font-family: Comic Sans MS;"
									"color: red;"
									)
			self.Log_Error.setText("User_Id or Password not found")
			print("\a")


# ###############################################################

	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.setWindowModality(QtCore.Qt.NonModal)
		Form.setEnabled(True)
		Form.resize(1106, 700)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
		Form.setSizePolicy(sizePolicy)
		Form.setMinimumSize(QtCore.QSize(1200, 700))
		Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
		font = QtGui.QFont()
		font.setPointSize(10)
		Form.setFont(font)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/images/wallet.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		Form.setWindowIcon(icon)
		Form.setStyleSheet("QWidget{\n"
															"background-color:  rgb(255, 255, 255);\n"
															"}\n"
															"\n"
															"#Check_Tree,#Book_Log,#Click_Details,#Click_Details_2, #Driver_Info, #Description_details,#Driver_Show,#label_11,#TREE{\n"
															"border-radius: 5px;\n"
															"border: 2px solid rgbrgb(3, 230, 255);\n"
															"}\n"
															"#Shell,#Shell_1,#Shell_2,#Shell_3,#Shell_4,#Shell_5{\n"
															"border-radius: 12px;\n"
															"background-color: rgb(248, 248, 248);\n"
															"}\n"
															"\n"
															"#Client_Packages,#Client_Package_Cost,#Client_Ticket_Count,#Package_Estimated_Price,#Package_Ticket, #Recipient_Client, #Ticket_Issued{\n"
															"background-color: rgb(248, 248, 248);\n"
															"}\n"
															"\n"
															"#label,#label_6,#label_7,#label_8,#label_9{\n"
															"color: rgb(170, 0, 255)\n"
															"}\n"
															"\n"
															"#Log_LogTitle{\n"
															"color: rgb(170, 0, 255);\n"
															"font-size: 16pt ;\n"
															"font-family: Comic Sans MS;\n"
															"}\n"
															"\n"
															"QCheckBox,#Label_User,#Label_Pass,#Label_FN,#Label_U,#Label_G,#Label_P,#Label_CP,#Label_E,#Label_AN,#Label_BN,#Label_An,#Label_DoP,#Admin_User,#Admin_Pass, #Label_ID ,#Label_Package, #Label_Phone,#Admin_LOGIN,#Admin_PASSWORD,#Client_Packages,#Client_Package_Cost,#Client_Ticket_Count,#Recipient_Client,#Ticket_Issued,#Label_Client_ID_Pay,#Label_Payment_ID_Pay, #Driver_Check_Info,#NoS,#MNoP,#label_4,#label_5,#label_10,#label_12,#label_13,#label_14,#label_15,#label_16,#label_17{\n"
															"color: rgb(170, 0, 255);\n"
															"font-family: Comic Sans MS;\n"
															"}\n"
															"\n"
															"#Checker_1,#Checker_2{\n"
															"border: none\n"
															"}\n"
															"\n"
															"QPushButton {\n"
															"background-color: rgb(60, 187, 255);\n"
															"border-radius: 10px;\n"
															"font-size: 13pt ;\n"
															"font-family: Comic Sans MS;\n"
															"}\n"
															"\n"
															"QPushButton::hover{\n"
															"background-color: rgb(85, 85, 255);\n"
															"color: rgb(244, 244, 244);\n"
															"}\n"
															"\n"
															"QTextBrowser{\n"
															"border: none\n"
															"}\n"
															"\n"
															"QLineEdit,QComboBox , #Package_Amount,#Package_Ticket_Amount, #Quantity, #Passenger_Number{\n"
															"border-radius: 5px;\n"
															"border: 3px solid rgb(207, 207, 207);\n"
															"height: 30px;\n"
															"font: 12pt Consolas;\n"
															"margin-left: 3px;\n"
															"padding-left: 5px;\n"
															"}\n"
															"\n"
															"QLineEdit:focus, QComboBox:focus,#Package_Amount:focus,#Package_Ticket_Amount:focus, #Quantity:focus, #Passenger_Number:focus{\n"
															"outline: 1px solid rgb(60, 185, 112);\n"
															"background: rgb(231, 225, 255);\n"
															"border: 2px solid rgb(170, 0, 255);\n"
															"height: 10px;\n"
															"}\n"
															"\n"
															"QTextEdit{\n"
															"font-family: Comic Sans MS;\n"
															"border: none\n"
															"}\n"
															"\n"
															"#Admin_Client, #Admin_Book, #Admin_Pay, #Admin_Others, #Admin_Client_Log,#Client_Package_Purchase,#Client_Share_Resources,#Client_Return,#Package_List{\n"
															"border-radius: 10px;\n"
															"border: 3px solid rgbrgb(3, 230, 255);\n"
															"font-size: 10pt;\n"
															"font-family: Comic Sans MS;\n"
															"}\n"
															"\n"
															"#Admin_Client:checked,#Admin_Client:pressed, #Admin_Book:checked,#Admin_Book:pressed, #Admin_Pay:checked,#Admin_Pay:pressed, #Admin_Others:checked,#Admin_Others:pressed, #Admin_Client_Log:checked,#Admin_Client_Log:pressed, #Client_Package_Purchase:checked,#Client_Package_Purchase:pressed, #Client_Share_Resources:checked,#Client_Share_Resources:pressed, #Client_Return:checked,#Client_Return:pressed,#Package_List:checked,#Package_List:pressed{\n"
															"background:rgb(0, 192, 235)\n"
															"}\n"
															"\n"
															"#Admin_Client:hover, #Admin_Book:hover, #Admin_Pay:hover, #Admin_Others:hover, #Admin_Client_Log:hover,#Client_Package_Purchase:hover,#Client_Share_Resources:hover,#Client_Return:hover,#Package_List:hover{\n"
															"background-color: rgb(231, 225, 255)\n"
															"}\n"
															"\n"
															"#Admin_Client:checked:hover, #Admin_Book:checked:hover, #Admin_Pay:checked:hover, #Admin_Others:checked:hover, #Admin_Client_Log:checked:hover, #Client_Package_Purchase:checked:hover, #Client_Share_Resources:checked:hover, #Client_Return:checked:hover, #Package_List:checked:hover{\n"
															"background:rgb(0, 192, 235)\n"
															"}\n"
															"\n"
															"#Fut{\n"
															"border: none;\n"
															"background-color: white\n"
															"}\n"
															"\n"
															"#page_5,#Ticket_Quantity,#Package_Quantity,#label_4,#label_5,#label_17,#label_11{\n"
															"background-color: rgb(249, 249, 249)\n"
															"}")
		Form.setIconSize(QtCore.QSize(64, 64))
		self.centralwidget = QtWidgets.QWidget(Form)
		self.centralwidget.setStyleSheet("")
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout_51.setObjectName("verticalLayout_51")
		self.mainStackWidget = QtWidgets.QStackedWidget(self.centralwidget)
		self.mainStackWidget.setEnabled(True)
		self.mainStackWidget.setMaximumSize(QtCore.QSize(1350, 700))
		self.mainStackWidget.setStyleSheet("")
		self.mainStackWidget.setObjectName("mainStackWidget")
		self.FirstPage = QtWidgets.QWidget()
		self.FirstPage.setObjectName("FirstPage")
		self.gridLayout_14 = QtWidgets.QGridLayout(self.FirstPage)
		self.gridLayout_14.setObjectName("gridLayout_14")
		self.verticalLayout_31 = QtWidgets.QVBoxLayout()
		self.verticalLayout_31.setObjectName("verticalLayout_31")
		self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_25.setObjectName("horizontalLayout_25")
		self.Fut = QtWidgets.QToolButton(self.FirstPage)
		self.Fut.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Fut.sizePolicy().hasHeightForWidth())
		self.Fut.setSizePolicy(sizePolicy)
		self.Fut.setMinimumSize(QtCore.QSize(60, 60))
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(":/images/fut.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
		icon1.addPixmap(QtGui.QPixmap(":/images/fut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Fut.setIcon(icon1)
		self.Fut.setIconSize(QtCore.QSize(128, 128))
		self.Fut.setObjectName("Fut")
		self.horizontalLayout_25.addWidget(self.Fut)
		self.label = QtWidgets.QLabel(self.FirstPage)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(24)
		self.label.setFont(font)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.horizontalLayout_25.addWidget(self.label)
		self.verticalLayout_31.addLayout(self.horizontalLayout_25)
		self.verticalLayout_30 = QtWidgets.QVBoxLayout()
		self.verticalLayout_30.setObjectName("verticalLayout_30")
		spacerItem = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
		self.verticalLayout_30.addItem(spacerItem)
		self.verticalLayout_29 = QtWidgets.QVBoxLayout()
		self.verticalLayout_29.setObjectName("verticalLayout_29")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout()
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.label_2 = QtWidgets.QLabel(self.FirstPage)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_2.setFont(font)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_4.addWidget(self.label_2)
		spacerItem1 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_4.addItem(spacerItem1)
		self.textBrowser = QtWidgets.QTextBrowser(self.FirstPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
		self.textBrowser.setSizePolicy(sizePolicy)
		self.textBrowser.setOverwriteMode(False)
		self.textBrowser.setObjectName("textBrowser")
		self.verticalLayout_4.addWidget(self.textBrowser)
		self.Label_Start = QtWidgets.QLabel(self.FirstPage)
		self.Label_Start.setMinimumSize(QtCore.QSize(0, 80))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.Label_Start.setFont(font)
		self.Label_Start.setAlignment(QtCore.Qt.AlignCenter)
		self.Label_Start.setObjectName("Label_Start")
		self.verticalLayout_4.addWidget(self.Label_Start)
		self.verticalLayout_29.addLayout(self.verticalLayout_4)
		self.verticalLayout_28 = QtWidgets.QVBoxLayout()
		self.verticalLayout_28.setObjectName("verticalLayout_28")
		self.line = QtWidgets.QFrame(self.FirstPage)
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.verticalLayout_28.addWidget(self.line)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
		self.horizontalLayout.setContentsMargins(-1, -1, -1, 21)
		self.horizontalLayout.setSpacing(10)
		self.horizontalLayout.setObjectName("horizontalLayout")
		spacerItem2 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem2)
		self.L_Admin = QtWidgets.QPushButton(self.FirstPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.L_Admin.sizePolicy().hasHeightForWidth())
		self.L_Admin.setSizePolicy(sizePolicy)
		self.L_Admin.setObjectName("L_Admin")
		self.horizontalLayout.addWidget(self.L_Admin)
		spacerItem3 = QtWidgets.QSpacerItem(400, 60, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem3)
		self.L_About = QtWidgets.QPushButton(self.FirstPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(10)
		sizePolicy.setHeightForWidth(self.L_About.sizePolicy().hasHeightForWidth())
		self.L_About.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(13)
		self.L_About.setFont(font)
		self.L_About.setStyleSheet("")
		self.L_About.setObjectName("L_About")
		self.horizontalLayout.addWidget(self.L_About)
		spacerItem4 = QtWidgets.QSpacerItem(30, 65, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem4)
		self.verticalLayout_28.addLayout(self.horizontalLayout)
		self.verticalLayout_29.addLayout(self.verticalLayout_28)
		self.verticalLayout_30.addLayout(self.verticalLayout_29)
		self.verticalLayout_31.addLayout(self.verticalLayout_30)
		self.gridLayout_14.addLayout(self.verticalLayout_31, 0, 0, 1, 1)
		self.mainStackWidget.addWidget(self.FirstPage)
		self.AboutPage = QtWidgets.QWidget()
		self.AboutPage.setObjectName("AboutPage")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.AboutPage)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.textEdit = QtWidgets.QTextEdit(self.AboutPage)
		self.textEdit.setObjectName("textEdit")
		self.gridLayout_2.addWidget(self.textEdit, 0, 1, 1, 3)
		self.line_3 = QtWidgets.QFrame(self.AboutPage)
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 5)
		spacerItem5 = QtWidgets.QSpacerItem(200, 70, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
		spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem6, 2, 3, 1, 1)
		self.A_Back = QtWidgets.QPushButton(self.AboutPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.A_Back.sizePolicy().hasHeightForWidth())
		self.A_Back.setSizePolicy(sizePolicy)
		self.A_Back.setObjectName("A_Back")
		self.gridLayout_2.addWidget(self.A_Back, 2, 2, 1, 1)
		self.mainStackWidget.addWidget(self.AboutPage)
		self.AdminPage = QtWidgets.QWidget()
		self.AdminPage.setObjectName("AdminPage")
		self.gridLayout_7 = QtWidgets.QGridLayout(self.AdminPage)
		self.gridLayout_7.setObjectName("gridLayout_7")
		self.verticalLayout_18 = QtWidgets.QVBoxLayout()
		self.verticalLayout_18.setObjectName("verticalLayout_18")
		self.label_6 = QtWidgets.QLabel(self.AdminPage)
		font = QtGui.QFont()
		font.setFamily("Monaco")
		font.setPointSize(27)
		self.label_6.setFont(font)
		self.label_6.setAlignment(QtCore.Qt.AlignCenter)
		self.label_6.setObjectName("label_6")
		self.verticalLayout_18.addWidget(self.label_6)
		self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_35.setObjectName("horizontalLayout_35")
		self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_34.setObjectName("horizontalLayout_34")
		self.verticalLayout_17 = QtWidgets.QVBoxLayout()
		self.verticalLayout_17.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
		self.verticalLayout_17.setObjectName("verticalLayout_17")
		spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_17.addItem(spacerItem7)
		self.Admin_Client = QtWidgets.QToolButton(self.AdminPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Admin_Client.sizePolicy().hasHeightForWidth())
		self.Admin_Client.setSizePolicy(sizePolicy)
		self.Admin_Client.setSizeIncrement(QtCore.QSize(0, 0))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Admin_Client.setFont(font)
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(":/images/user.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Admin_Client.setIcon(icon2)
		self.Admin_Client.setIconSize(QtCore.QSize(70, 70))
		self.Admin_Client.setCheckable(True)
		self.Admin_Client.setChecked(False)
		self.Admin_Client.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Admin_Client.setObjectName("Admin_Client")
		self.buttonGroup_3 = QtWidgets.QButtonGroup(Form)
		self.buttonGroup_3.setObjectName("buttonGroup_3")
		self.buttonGroup_3.addButton(self.Admin_Client)
		self.verticalLayout_17.addWidget(self.Admin_Client)
		self.Admin_Client_Log = QtWidgets.QToolButton(self.AdminPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Admin_Client_Log.sizePolicy().hasHeightForWidth())
		self.Admin_Client_Log.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Admin_Client_Log.setFont(font)
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(":/images/login.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Admin_Client_Log.setIcon(icon3)
		self.Admin_Client_Log.setIconSize(QtCore.QSize(70, 70))
		self.Admin_Client_Log.setCheckable(True)
		self.Admin_Client_Log.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Admin_Client_Log.setObjectName("Admin_Client_Log")
		self.buttonGroup_3.addButton(self.Admin_Client_Log)
		self.verticalLayout_17.addWidget(self.Admin_Client_Log)
		self.Admin_Book = QtWidgets.QToolButton(self.AdminPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Admin_Book.sizePolicy().hasHeightForWidth())
		self.Admin_Book.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Admin_Book.setFont(font)
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(":/images/booking.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Admin_Book.setIcon(icon4)
		self.Admin_Book.setIconSize(QtCore.QSize(70, 70))
		self.Admin_Book.setCheckable(True)
		self.Admin_Book.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Admin_Book.setObjectName("Admin_Book")
		self.buttonGroup_3.addButton(self.Admin_Book)
		self.verticalLayout_17.addWidget(self.Admin_Book)
		self.Admin_Others = QtWidgets.QToolButton(self.AdminPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Admin_Others.sizePolicy().hasHeightForWidth())
		self.Admin_Others.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Admin_Others.setFont(font)
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(":/images/warning.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Admin_Others.setIcon(icon5)
		self.Admin_Others.setIconSize(QtCore.QSize(70, 70))
		self.Admin_Others.setCheckable(True)
		self.Admin_Others.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Admin_Others.setObjectName("Admin_Others")
		self.buttonGroup_3.addButton(self.Admin_Others)
		self.verticalLayout_17.addWidget(self.Admin_Others)
		self.Admin_Pay = QtWidgets.QToolButton(self.AdminPage)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Admin_Pay.sizePolicy().hasHeightForWidth())
		self.Admin_Pay.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Admin_Pay.setFont(font)
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(":/images/money.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Admin_Pay.setIcon(icon6)
		self.Admin_Pay.setIconSize(QtCore.QSize(70, 70))
		self.Admin_Pay.setCheckable(True)
		self.Admin_Pay.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Admin_Pay.setObjectName("Admin_Pay")
		self.buttonGroup_3.addButton(self.Admin_Pay)
		self.verticalLayout_17.addWidget(self.Admin_Pay)
		spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_17.addItem(spacerItem8)
		self.horizontalLayout_34.addLayout(self.verticalLayout_17)
		self.line_5 = QtWidgets.QFrame(self.AdminPage)
		self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")
		self.horizontalLayout_34.addWidget(self.line_5)
		self.horizontalLayout_35.addLayout(self.horizontalLayout_34)
		self.Second_Stack = QtWidgets.QStackedWidget(self.AdminPage)
		self.Second_Stack.setEnabled(True)
		self.Second_Stack.setStyleSheet("QPushButton {\n"
									"background-color: rgb(60, 187, 255);\n"
									"border-radius: 10px;\n"
									"font-size: 13pt ;\n"
									"font-family: Comic Sans MS;\n"
									"}\n"
									"\n"
									"QPushButton::hover{\n"
									"background-color: rgb(85, 85, 255);\n"
									"color: rgb(244, 244, 244);\n"
									"}\n"
									"\n"
									"#Log_Error, #Reg_Error{\n"
									"color: rgb(255, 0, 0);\n"
									"font-family: Comic Sans MS;\n"
									"}")
		self.Second_Stack.setObjectName("Second_Stack")
		self.Admin_Register = QtWidgets.QWidget()
		self.Admin_Register.setObjectName("Admin_Register")
		self.gridLayout = QtWidgets.QGridLayout(self.Admin_Register)
		self.gridLayout.setObjectName("gridLayout")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout()
		self.verticalLayout_5.setContentsMargins(-1, 10, -1, -1)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		spacerItem9 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_5.addItem(spacerItem9)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.verticalLayout_23 = QtWidgets.QVBoxLayout()
		self.verticalLayout_23.setObjectName("verticalLayout_23")
		self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_36.setObjectName("horizontalLayout_36")
		spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_36.addItem(spacerItem10)
		self.Label_FN = QtWidgets.QLabel(self.Admin_Register)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(9)
		self.Label_FN.setFont(font)
		self.Label_FN.setObjectName("Label_FN")
		self.horizontalLayout_36.addWidget(self.Label_FN)
		spacerItem11 = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_36.addItem(spacerItem11)
		self.lineEdit_18 = QtWidgets.QLineEdit(self.Admin_Register)
		self.lineEdit_18.setObjectName("lineEdit_18")
		self.horizontalLayout_36.addWidget(self.lineEdit_18)
		spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_36.addItem(spacerItem12)
		self.verticalLayout_23.addLayout(self.horizontalLayout_36)
		self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_37.setObjectName("horizontalLayout_37")
		spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_37.addItem(spacerItem13)
		self.Label_G = QtWidgets.QLabel(self.Admin_Register)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(9)
		self.Label_G.setFont(font)
		self.Label_G.setObjectName("Label_G")
		self.horizontalLayout_37.addWidget(self.Label_G)
		spacerItem14 = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_37.addItem(spacerItem14)
		self.Gender_Select = QtWidgets.QComboBox(self.Admin_Register)
		self.Gender_Select.setMinimumSize(QtCore.QSize(200, 0))
		self.Gender_Select.setMaxVisibleItems(2)
		self.Gender_Select.setMaxCount(2)
		self.Gender_Select.setObjectName("Gender_Select")
		self.Gender_Select.addItem("")
		self.Gender_Select.addItem("")
		self.horizontalLayout_37.addWidget(self.Gender_Select)
		spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_37.addItem(spacerItem15)
		self.verticalLayout_23.addLayout(self.horizontalLayout_37)
		self.verticalLayout_2.addLayout(self.verticalLayout_23)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem16)
		self.Label_Phone = QtWidgets.QLabel(self.Admin_Register)
		self.Label_Phone.setObjectName("Label_Phone")
		self.horizontalLayout_3.addWidget(self.Label_Phone)
		spacerItem17 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem17)
		self.lineEdit = QtWidgets.QLineEdit(self.Admin_Register)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
		self.lineEdit.setSizePolicy(sizePolicy)
		self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
		self.lineEdit.setMaxLength(11)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_3.addWidget(self.lineEdit)
		spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem18)
		self.verticalLayout.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_39.setObjectName("horizontalLayout_39")
		spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_39.addItem(spacerItem19)
		self.Label_E = QtWidgets.QLabel(self.Admin_Register)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		self.Label_E.setFont(font)
		self.Label_E.setObjectName("Label_E")
		self.horizontalLayout_39.addWidget(self.Label_E)
		spacerItem20 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_39.addItem(spacerItem20)
		self.lineEdit_20 = QtWidgets.QLineEdit(self.Admin_Register)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_20.sizePolicy().hasHeightForWidth())
		self.lineEdit_20.setSizePolicy(sizePolicy)
		self.lineEdit_20.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
		self.lineEdit_20.setObjectName("lineEdit_20")
		self.horizontalLayout_39.addWidget(self.lineEdit_20)
		spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_39.addItem(spacerItem21)
		self.verticalLayout.addLayout(self.horizontalLayout_39)
		self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_42.setObjectName("horizontalLayout_42")
		spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_42.addItem(spacerItem22)
		self.Label_DoP = QtWidgets.QLabel(self.Admin_Register)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(9)
		self.Label_DoP.setFont(font)
		self.Label_DoP.setObjectName("Label_DoP")
		self.horizontalLayout_42.addWidget(self.Label_DoP)
		spacerItem23 = QtWidgets.QSpacerItem(121, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_42.addItem(spacerItem23)
		self.Client_Select = QtWidgets.QComboBox(self.Admin_Register)
		self.Client_Select.setMinimumSize(QtCore.QSize(200, 0))
		self.Client_Select.setObjectName("Client_Select")
		self.Client_Select.addItem("")
		self.Client_Select.addItem("")
		self.horizontalLayout_42.addWidget(self.Client_Select)
		spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_42.addItem(spacerItem24)
		self.verticalLayout.addLayout(self.horizontalLayout_42)
		self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_40.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
		self.horizontalLayout_40.setObjectName("horizontalLayout_40")
		spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_40.addItem(spacerItem25)
		self.Label_P = QtWidgets.QLabel(self.Admin_Register)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(9)
		self.Label_P.setFont(font)
		self.Label_P.setObjectName("Label_P")
		self.horizontalLayout_40.addWidget(self.Label_P)
		spacerItem26 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_40.addItem(spacerItem26)
		self.lineEdit_21 = QtWidgets.QLineEdit(self.Admin_Register)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_21.sizePolicy().hasHeightForWidth())
		self.lineEdit_21.setSizePolicy(sizePolicy)
		self.lineEdit_21.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit_21.setObjectName("lineEdit_21")
		self.horizontalLayout_40.addWidget(self.lineEdit_21)
		spacerItem27 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_40.addItem(spacerItem27)
		self.Checker_1 = QtWidgets.QToolButton(self.Admin_Register)
		self.Checker_1.setEnabled(False)
		self.Checker_1.setText("")
		self.Checker_1.setObjectName("Checker_1")
		self.horizontalLayout_40.addWidget(self.Checker_1)
		self.verticalLayout.addLayout(self.horizontalLayout_40)
		self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_41.setObjectName("horizontalLayout_41")
		spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_41.addItem(spacerItem28)
		self.Label_CP = QtWidgets.QLabel(self.Admin_Register)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(9)
		self.Label_CP.setFont(font)
		self.Label_CP.setObjectName("Label_CP")
		self.horizontalLayout_41.addWidget(self.Label_CP)
		spacerItem29 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_41.addItem(spacerItem29)
		self.lineEdit_22 = QtWidgets.QLineEdit(self.Admin_Register)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lineEdit_22.sizePolicy().hasHeightForWidth())
		self.lineEdit_22.setSizePolicy(sizePolicy)
		self.lineEdit_22.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit_22.setObjectName("lineEdit_22")
		self.horizontalLayout_41.addWidget(self.lineEdit_22)
		spacerItem30 = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_41.addItem(spacerItem30)
		self.Checker_2 = QtWidgets.QToolButton(self.Admin_Register)
		self.Checker_2.setEnabled(False)
		self.Checker_2.setText("")
		self.Checker_2.setObjectName("Checker_2")
		self.horizontalLayout_41.addWidget(self.Checker_2)
		self.verticalLayout.addLayout(self.horizontalLayout_41)
		self.verticalLayout_2.addLayout(self.verticalLayout)
		self.verticalLayout_25 = QtWidgets.QVBoxLayout()
		self.verticalLayout_25.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.verticalLayout_25.setObjectName("verticalLayout_25")
		self.verticalLayout_2.addLayout(self.verticalLayout_25)
		self.Reg_Error = QtWidgets.QLabel(self.Admin_Register)
		self.Reg_Error.setMinimumSize(QtCore.QSize(0, 50))
		self.Reg_Error.setText("")
		self.Reg_Error.setAlignment(QtCore.Qt.AlignCenter)
		self.Reg_Error.setObjectName("Reg_Error")
		self.verticalLayout_2.addWidget(self.Reg_Error)
		self.verticalLayout_5.addLayout(self.verticalLayout_2)
		self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_46.setContentsMargins(20, 10, 20, 70)
		self.horizontalLayout_46.setSpacing(100)
		self.horizontalLayout_46.setObjectName("horizontalLayout_46")
		spacerItem31 = QtWidgets.QSpacerItem(180, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_46.addItem(spacerItem31)
		self.Reg_Reg = QtWidgets.QPushButton(self.Admin_Register)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Reg_Reg.sizePolicy().hasHeightForWidth())
		self.Reg_Reg.setSizePolicy(sizePolicy)
		self.Reg_Reg.setMinimumSize(QtCore.QSize(10, 30))
		self.Reg_Reg.setMaximumSize(QtCore.QSize(200, 60))
		self.Reg_Reg.setObjectName("Reg_Reg")
		self.horizontalLayout_46.addWidget(self.Reg_Reg)
		spacerItem32 = QtWidgets.QSpacerItem(180, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_46.addItem(spacerItem32)
		self.verticalLayout_5.addLayout(self.horizontalLayout_46)
		self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 2, 2)
		self.Second_Stack.addWidget(self.Admin_Register)
		self.Admin_Client_Login = QtWidgets.QWidget()
		self.Admin_Client_Login.setObjectName("Admin_Client_Login")
		self.gridLayout_6 = QtWidgets.QGridLayout(self.Admin_Client_Login)
		self.gridLayout_6.setObjectName("gridLayout_6")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout()
		self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
		self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setContentsMargins(-1, 10, -1, 10)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem33)
		self.Label_User = QtWidgets.QLabel(self.Admin_Client_Login)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Label_User.sizePolicy().hasHeightForWidth())
		self.Label_User.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Label_User.setFont(font)
		self.Label_User.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.Label_User.setObjectName("Label_User")
		self.horizontalLayout_4.addWidget(self.Label_User)
		self.Log_UserEdit = QtWidgets.QLineEdit(self.Admin_Client_Login)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(3)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Log_UserEdit.sizePolicy().hasHeightForWidth())
		self.Log_UserEdit.setSizePolicy(sizePolicy)
		self.Log_UserEdit.setMaxLength(11)
		self.Log_UserEdit.setObjectName("Log_UserEdit")
		self.horizontalLayout_4.addWidget(self.Log_UserEdit)
		spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem34)
		self.verticalLayout_3.addLayout(self.horizontalLayout_4)
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_5.addItem(spacerItem35)
		self.Label_Pass = QtWidgets.QLabel(self.Admin_Client_Login)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Label_Pass.sizePolicy().hasHeightForWidth())
		self.Label_Pass.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Label_Pass.setFont(font)
		self.Label_Pass.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.Label_Pass.setObjectName("Label_Pass")
		self.horizontalLayout_5.addWidget(self.Label_Pass)
		self.Log_UserPass = QtWidgets.QLineEdit(self.Admin_Client_Login)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(3)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Log_UserPass.sizePolicy().hasHeightForWidth())
		self.Log_UserPass.setSizePolicy(sizePolicy)
		self.Log_UserPass.setMaxLength(100)
		self.Log_UserPass.setEchoMode(QtWidgets.QLineEdit.Password)
		self.Log_UserPass.setObjectName("Log_UserPass")
		self.horizontalLayout_5.addWidget(self.Log_UserPass)
		spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_5.addItem(spacerItem36)
		self.verticalLayout_3.addLayout(self.horizontalLayout_5)
		self.Log_Error = QtWidgets.QLabel(self.Admin_Client_Login)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Log_Error.sizePolicy().hasHeightForWidth())
		self.Log_Error.setSizePolicy(sizePolicy)
		self.Log_Error.setMinimumSize(QtCore.QSize(0, 50))
		self.Log_Error.setText("")
		self.Log_Error.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.Log_Error.setObjectName("Log_Error")
		self.verticalLayout_3.addWidget(self.Log_Error)
		self.verticalLayout_6.addLayout(self.verticalLayout_3)
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.Log_button = QtWidgets.QPushButton(self.Admin_Client_Login)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Log_button.sizePolicy().hasHeightForWidth())
		self.Log_button.setSizePolicy(sizePolicy)
		self.Log_button.setMaximumSize(QtCore.QSize(100, 50))
		self.Log_button.setObjectName("Log_button")
		self.horizontalLayout_6.addWidget(self.Log_button)
		self.verticalLayout_6.addLayout(self.horizontalLayout_6)
		spacerItem37 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_6.addItem(spacerItem37)
		self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
		self.Second_Stack.addWidget(self.Admin_Client_Login)
		self.Admin_CLient_Book = QtWidgets.QWidget()
		self.Admin_CLient_Book.setObjectName("Admin_CLient_Book")
		self.gridLayout_8 = QtWidgets.QGridLayout(self.Admin_CLient_Book)
		self.gridLayout_8.setObjectName("gridLayout_8")
		self.verticalLayout_49 = QtWidgets.QVBoxLayout()
		self.verticalLayout_49.setContentsMargins(5, 5, 5, 5)
		self.verticalLayout_49.setObjectName("verticalLayout_49")
		spacerItem38 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_49.addItem(spacerItem38)
		self.verticalLayout_7 = QtWidgets.QVBoxLayout()
		self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.Label_ID = QtWidgets.QLabel(self.Admin_CLient_Book)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Label_ID.setFont(font)
		self.Label_ID.setObjectName("Label_ID")
		self.horizontalLayout_2.addWidget(self.Label_ID)
		spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem39)
		self.Book_ID = QtWidgets.QLineEdit(self.Admin_CLient_Book)
		self.Book_ID.setMaxLength(11)
		self.Book_ID.setObjectName("Book_ID")
		self.horizontalLayout_2.addWidget(self.Book_ID)
		self.verticalLayout_7.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_7.setObjectName("horizontalLayout_7")
		self.Label_Package = QtWidgets.QLabel(self.Admin_CLient_Book)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Label_Package.setFont(font)
		self.Label_Package.setObjectName("Label_Package")
		self.horizontalLayout_7.addWidget(self.Label_Package)
		spacerItem40 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_7.addItem(spacerItem40)
		self.Book_Package = QtWidgets.QLineEdit(self.Admin_CLient_Book)
		self.Book_Package.setMaxLength(12)
		self.Book_Package.setObjectName("Book_Package")
		self.horizontalLayout_7.addWidget(self.Book_Package)
		self.verticalLayout_7.addLayout(self.horizontalLayout_7)
		self.verticalLayout_49.addLayout(self.verticalLayout_7)
		spacerItem41 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_49.addItem(spacerItem41)
		self.verticalLayout_8 = QtWidgets.QVBoxLayout()
		self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_55.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_55.setObjectName("horizontalLayout_55")
		self.Book_confirm = QtWidgets.QPushButton(self.Admin_CLient_Book)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Book_confirm.sizePolicy().hasHeightForWidth())
		self.Book_confirm.setSizePolicy(sizePolicy)
		self.Book_confirm.setMaximumSize(QtCore.QSize(200, 50))
		self.Book_confirm.setObjectName("Book_confirm")
		self.horizontalLayout_55.addWidget(self.Book_confirm)
		spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_55.addItem(spacerItem42)
		self.pushButton_4 = QtWidgets.QPushButton(self.Admin_CLient_Book)
		self.pushButton_4.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
		self.pushButton_4.setSizePolicy(sizePolicy)
		self.pushButton_4.setMaximumSize(QtCore.QSize(200, 50))
		self.pushButton_4.setObjectName("pushButton_4")
		self.horizontalLayout_55.addWidget(self.pushButton_4)
		self.verticalLayout_8.addLayout(self.horizontalLayout_55)
		self.Book_Log = QtWidgets.QLabel(self.Admin_CLient_Book)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Book_Log.sizePolicy().hasHeightForWidth())
		self.Book_Log.setSizePolicy(sizePolicy)
		self.Book_Log.setMinimumSize(QtCore.QSize(648, 200))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.Book_Log.setFont(font)
		self.Book_Log.setText("")
		self.Book_Log.setAlignment(QtCore.Qt.AlignCenter)
		self.Book_Log.setObjectName("Book_Log")
		self.verticalLayout_8.addWidget(self.Book_Log)
		self.horizontalLayout_60 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_60.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_60.setObjectName("horizontalLayout_60")
		spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_60.addItem(spacerItem43)
		self.Book_Next = QtWidgets.QPushButton(self.Admin_CLient_Book)
		self.Book_Next.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Book_Next.sizePolicy().hasHeightForWidth())
		self.Book_Next.setSizePolicy(sizePolicy)
		self.Book_Next.setMaximumSize(QtCore.QSize(200, 50))
		self.Book_Next.setObjectName("Book_Next")
		self.horizontalLayout_60.addWidget(self.Book_Next)
		spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_60.addItem(spacerItem44)
		self.verticalLayout_8.addLayout(self.horizontalLayout_60)
		self.verticalLayout_49.addLayout(self.verticalLayout_8)
		spacerItem45 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_49.addItem(spacerItem45)
		self.gridLayout_8.addLayout(self.verticalLayout_49, 0, 0, 1, 1)
		self.Second_Stack.addWidget(self.Admin_CLient_Book)

		# ########################################################################
		# ########################################################################
		# ########################################################################

		self.Admin_Client_payroll = QtWidgets.QWidget()
		self.Admin_Client_payroll.setObjectName("Admin_Client_payroll")
		self.gridLayout_4 = QtWidgets.QGridLayout(self.Admin_Client_payroll)
		self.gridLayout_4.setObjectName("gridLayout_4")
		self.verticalLayout_9 = QtWidgets.QVBoxLayout()
		self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
		self.verticalLayout_9.setObjectName("verticalLayout_9")
		spacerItem46 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_9.addItem(spacerItem46)
		self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.Label_Client_ID_Pay = QtWidgets.QLabel(self.Admin_Client_payroll)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Label_Client_ID_Pay.setFont(font)
		self.Label_Client_ID_Pay.setObjectName("Label_Client_ID_Pay")
		self.horizontalLayout_8.addWidget(self.Label_Client_ID_Pay)
		spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_8.addItem(spacerItem47)
		self.Pay_Client_ID = QtWidgets.QLineEdit(self.Admin_Client_payroll)
		self.Pay_Client_ID.setMaxLength(11)
		self.Pay_Client_ID.setObjectName("Pay_Client_ID")
		self.horizontalLayout_8.addWidget(self.Pay_Client_ID)
		self.verticalLayout_9.addLayout(self.horizontalLayout_8)
		self.horizontalLayout_62 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_62.setObjectName("horizontalLayout_62")
		self.Pay_cpnfirm = QtWidgets.QPushButton(self.Admin_Client_payroll)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Pay_cpnfirm.sizePolicy().hasHeightForWidth())
		self.Pay_cpnfirm.setSizePolicy(sizePolicy)
		self.Pay_cpnfirm.setMaximumSize(QtCore.QSize(150, 50))
		self.Pay_cpnfirm.setObjectName("Pay_cpnfirm")
		self.horizontalLayout_62.addWidget(self.Pay_cpnfirm)
		self.Clear_Pay = QtWidgets.QPushButton(self.Admin_Client_payroll)
		self.Clear_Pay.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Clear_Pay.sizePolicy().hasHeightForWidth())
		self.Clear_Pay.setSizePolicy(sizePolicy)
		self.Clear_Pay.setMaximumSize(QtCore.QSize(150, 50))
		self.Clear_Pay.setObjectName("Clear_Pay")
		self.horizontalLayout_62.addWidget(self.Clear_Pay)
		self.verticalLayout_9.addLayout(self.horizontalLayout_62)
		self.horizontalLayout_63 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_63.setObjectName("horizontalLayout_63")
		self.Pay_Log = QtWidgets.QLabel(self.Admin_Client_payroll)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Pay_Log.sizePolicy().hasHeightForWidth())
		self.Pay_Log.setSizePolicy(sizePolicy)
		self.Pay_Log.setMinimumSize(QtCore.QSize(800, 50))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(13)
		self.Pay_Log.setFont(font)
		self.Pay_Log.setStyleSheet("color: green")
		self.Pay_Log.setText("")
		self.Pay_Log.setAlignment(QtCore.Qt.AlignCenter)
		self.Pay_Log.setObjectName("Pay_Log")
		self.horizontalLayout_63.addWidget(self.Pay_Log)
		self.verticalLayout_9.addLayout(self.horizontalLayout_63)
		self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_9.setObjectName("horizontalLayout_9")
		self.Pay_Button = QtWidgets.QPushButton(self.Admin_Client_payroll)
		self.Pay_Button.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Pay_Button.sizePolicy().hasHeightForWidth())
		self.Pay_Button.setSizePolicy(sizePolicy)
		self.Pay_Button.setMaximumSize(QtCore.QSize(150, 50))
		self.Pay_Button.setObjectName("Pay_Button")
		self.horizontalLayout_9.addWidget(self.Pay_Button)
		self.verticalLayout_9.addLayout(self.horizontalLayout_9)
		spacerItem48 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_9.addItem(spacerItem48)
		self.gridLayout_4.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
		self.Second_Stack.addWidget(self.Admin_Client_payroll)


		# #################################################
		# #################################################
		# #################################################
		self.Driver_Check_In = QtWidgets.QWidget()
		self.Driver_Check_In.setObjectName("Driver_Check_In")
		self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.Driver_Check_In)
		self.verticalLayout_50.setObjectName("verticalLayout_50")
		self.verticalLayout_33 = QtWidgets.QVBoxLayout()
		self.verticalLayout_33.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_33.setObjectName("verticalLayout_33")
		spacerItem48 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_33.addItem(spacerItem48)
		self.verticalLayout_32 = QtWidgets.QVBoxLayout()
		self.verticalLayout_32.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_32.setObjectName("verticalLayout_32")
		self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_26.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_26.setObjectName("horizontalLayout_26")
		self.Driver_Check_Info = QtWidgets.QLabel(self.Driver_Check_In)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Driver_Check_Info.setFont(font)
		self.Driver_Check_Info.setObjectName("Driver_Check_Info")
		self.horizontalLayout_26.addWidget(self.Driver_Check_Info)
		self.Drivers_ID = QtWidgets.QLineEdit(self.Driver_Check_In)
		self.Drivers_ID.setMaxLength(11)
		self.Drivers_ID.setObjectName("Drivers_ID")
		self.horizontalLayout_26.addWidget(self.Drivers_ID)
		self.verticalLayout_32.addLayout(self.horizontalLayout_26)
		self.label_3 = QtWidgets.QLabel(self.Driver_Check_In)
		self.label_3.setMinimumSize(QtCore.QSize(0, 50))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(14)
		self.label_3.setFont(font)
		self.label_3.setText("")
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.verticalLayout_32.addWidget(self.label_3)
		self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_28.setObjectName("horizontalLayout_28")
		self.Check_In = QtWidgets.QPushButton(self.Driver_Check_In)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Check_In.sizePolicy().hasHeightForWidth())
		self.Check_In.setSizePolicy(sizePolicy)
		self.Check_In.setMinimumSize(QtCore.QSize(150, 50))
		self.Check_In.setObjectName("Check_In")
		self.horizontalLayout_28.addWidget(self.Check_In)
		self.verticalLayout_32.addLayout(self.horizontalLayout_28)
		self.verticalLayout_33.addLayout(self.verticalLayout_32)
		self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_61.setContentsMargins(5, 5, 5, 5)
		self.horizontalLayout_61.setObjectName("horizontalLayout_61")
		self.Click_Details_2 = QtWidgets.QLabel(self.Driver_Check_In)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Click_Details_2.sizePolicy().hasHeightForWidth())
		self.Click_Details_2.setSizePolicy(sizePolicy)
		self.Click_Details_2.setMinimumSize(QtCore.QSize(0, 250))
		self.Click_Details_2.setText("")
		self.Click_Details_2.setAlignment(QtCore.Qt.AlignCenter)
		self.Click_Details_2.setObjectName("Click_Details_2")
		self.horizontalLayout_61.addWidget(self.Click_Details_2)

# ################################################
		self.Check_Tree = QtWidgets.QTreeWidget(self.Driver_Check_In)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		self.Check_Tree.setStyleSheet("color: blue")
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
# ###################################################

		sizePolicy.setHeightForWidth(self.Check_Tree.sizePolicy().hasHeightForWidth())
		self.Check_Tree.setSizePolicy(sizePolicy)
		self.Check_Tree.setObjectName("Check_Tree")
		self.Check_Tree.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.Check_Tree.headerItem().setFont(0, font)
		item_0 = QtWidgets.QTreeWidgetItem(self.Check_Tree)

# ##################################################

		self.horizontalLayout_61.addWidget(self.Check_Tree)
		self.verticalLayout_33.addLayout(self.horizontalLayout_61)
		self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_33.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.horizontalLayout_33.setContentsMargins(-1, 0, -1, 0)
		self.horizontalLayout_33.setObjectName("horizontalLayout_33")
		self.Check_Out = QtWidgets.QPushButton(self.Driver_Check_In)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Check_Out.sizePolicy().hasHeightForWidth())
		self.Check_Out.setSizePolicy(sizePolicy)
		self.Check_Out.setMinimumSize(QtCore.QSize(150, 50))
		self.Check_Out.setObjectName("Check_Out")
		self.horizontalLayout_33.addWidget(self.Check_Out)
		self.verticalLayout_33.addLayout(self.horizontalLayout_33)
		spacerItem49 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_33.addItem(spacerItem49)
		self.verticalLayout_50.addLayout(self.verticalLayout_33)
		self.Second_Stack.addWidget(self.Driver_Check_In)
		self.page_3 = QtWidgets.QWidget()
		self.page_3.setObjectName("page_3")
		self.gridLayout_15 = QtWidgets.QGridLayout(self.page_3)
		self.gridLayout_15.setObjectName("gridLayout_15")
		self.verticalLayout_36 = QtWidgets.QVBoxLayout()
		self.verticalLayout_36.setObjectName("verticalLayout_36")
		self.label_9 = QtWidgets.QLabel(self.page_3)
		font = QtGui.QFont()
		font.setFamily("Monaco")
		font.setPointSize(27)
		self.label_9.setFont(font)
		self.label_9.setAlignment(QtCore.Qt.AlignCenter)
		self.label_9.setObjectName("label_9")
		self.verticalLayout_36.addWidget(self.label_9)
		self.verticalLayout_35 = QtWidgets.QVBoxLayout()
		self.verticalLayout_35.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_35.setObjectName("verticalLayout_35")
		self.Description_details = QtWidgets.QLabel(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Description_details.sizePolicy().hasHeightForWidth())
		self.Description_details.setSizePolicy(sizePolicy)
		self.Description_details.setMinimumSize(QtCore.QSize(0, 200))
		self.Description_details.setText("")
		self.Description_details.setAlignment(QtCore.Qt.AlignCenter)
		self.Description_details.setObjectName("Description_details")
		self.verticalLayout_35.addWidget(self.Description_details)
		self.verticalLayout_34 = QtWidgets.QVBoxLayout()
		self.verticalLayout_34.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_34.setObjectName("verticalLayout_34")
		self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_29.setObjectName("horizontalLayout_29")
		self.NoS = QtWidgets.QLabel(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.NoS.sizePolicy().hasHeightForWidth())
		self.NoS.setSizePolicy(sizePolicy)
		self.NoS.setMinimumSize(QtCore.QSize(300, 0))
		self.NoS.setMaximumSize(QtCore.QSize(300, 16777215))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(14)
		self.NoS.setFont(font)
		self.NoS.setObjectName("NoS")
		self.horizontalLayout_29.addWidget(self.NoS)
		self.Quantity = QtWidgets.QSpinBox(self.page_3)
		self.Quantity.setMinimumSize(QtCore.QSize(200, 0))
		self.Quantity.setMaximumSize(QtCore.QSize(200, 16777215))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.Quantity.setFont(font)
		self.Quantity.setMaximum(110)
		self.Quantity.setObjectName("Quantity")
		self.horizontalLayout_29.addWidget(self.Quantity)
		self.verticalLayout_34.addLayout(self.horizontalLayout_29)
		self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_30.setObjectName("horizontalLayout_30")
		self.MNoP = QtWidgets.QLabel(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.MNoP.sizePolicy().hasHeightForWidth())
		self.MNoP.setSizePolicy(sizePolicy)
		self.MNoP.setMinimumSize(QtCore.QSize(200, 0))
		self.MNoP.setMaximumSize(QtCore.QSize(300, 16777215))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(14)
		self.MNoP.setFont(font)
		self.MNoP.setObjectName("MNoP")
		self.horizontalLayout_30.addWidget(self.MNoP)
		self.Passenger_Number = QtWidgets.QSpinBox(self.page_3)
		self.Passenger_Number.setMinimumSize(QtCore.QSize(200, 0))
		self.Passenger_Number.setMaximumSize(QtCore.QSize(200, 16777215))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.Passenger_Number.setFont(font)
		self.Passenger_Number.setMaximum(130)
		self.Passenger_Number.setObjectName("Passenger_Number")
		self.horizontalLayout_30.addWidget(self.Passenger_Number)
		self.verticalLayout_34.addLayout(self.horizontalLayout_30)
		self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_31.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_31.setObjectName("horizontalLayout_31")
		self.Driver_Show = QtWidgets.QLabel(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Driver_Show.sizePolicy().hasHeightForWidth())
		self.Driver_Show.setSizePolicy(sizePolicy)
		self.Driver_Show.setMinimumSize(QtCore.QSize(0, 70))
		self.Driver_Show.setText("")
		self.Driver_Show.setAlignment(QtCore.Qt.AlignCenter)
		self.Driver_Show.setObjectName("Driver_Show")
		self.horizontalLayout_31.addWidget(self.Driver_Show)
		self.verticalLayout_34.addLayout(self.horizontalLayout_31)
		self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_32.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_32.setObjectName("horizontalLayout_32")
		self.Driver_Submit_BP = QtWidgets.QPushButton(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Driver_Submit_BP.sizePolicy().hasHeightForWidth())
		self.Driver_Submit_BP.setSizePolicy(sizePolicy)
		self.Driver_Submit_BP.setMinimumSize(QtCore.QSize(150, 50))
		self.Driver_Submit_BP.setMaximumSize(QtCore.QSize(150, 16777215))
		self.Driver_Submit_BP.setObjectName("Driver_Submit_BP")
		self.horizontalLayout_32.addWidget(self.Driver_Submit_BP)
		self.Driver_Next_BP = QtWidgets.QPushButton(self.page_3)
		self.Driver_Next_BP.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Driver_Next_BP.sizePolicy().hasHeightForWidth())
		self.Driver_Next_BP.setSizePolicy(sizePolicy)
		self.Driver_Next_BP.setMinimumSize(QtCore.QSize(150, 50))
		self.Driver_Next_BP.setMaximumSize(QtCore.QSize(150, 16777215))
		self.Driver_Next_BP.setObjectName("Driver_Next_BP")
		self.horizontalLayout_32.addWidget(self.Driver_Next_BP)
		self.verticalLayout_34.addLayout(self.horizontalLayout_32)
		self.verticalLayout_35.addLayout(self.verticalLayout_34)
		self.verticalLayout_36.addLayout(self.verticalLayout_35)
		self.gridLayout_15.addLayout(self.verticalLayout_36, 0, 0, 1, 1)
		self.Second_Stack.addWidget(self.page_3)
		self.page_4 = QtWidgets.QWidget()
		self.page_4.setObjectName("page_4")
		self.gridLayout_17 = QtWidgets.QGridLayout(self.page_4)
		self.gridLayout_17.setObjectName("gridLayout_17")
		self.verticalLayout_48 = QtWidgets.QVBoxLayout()
		self.verticalLayout_48.setContentsMargins(5, 5, 5, 5)
		self.verticalLayout_48.setObjectName("verticalLayout_48")
		self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_43.setContentsMargins(5, 5, 5, 5)
		self.horizontalLayout_43.setObjectName("horizontalLayout_43")
		self.verticalLayout_47 = QtWidgets.QVBoxLayout()
		self.verticalLayout_47.setContentsMargins(5, 5, 5, 5)
		self.verticalLayout_47.setObjectName("verticalLayout_47")
		spacerItem50 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_47.addItem(spacerItem50)
		self.label_22 = QtWidgets.QLabel(self.page_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
		self.label_22.setSizePolicy(sizePolicy)
		self.label_22.setMinimumSize(QtCore.QSize(350, 0))
		self.label_22.setText("")
		self.label_22.setAlignment(QtCore.Qt.AlignCenter)
		self.label_22.setObjectName("label_22")
		self.verticalLayout_47.addWidget(self.label_22)
		spacerItem51 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_47.addItem(spacerItem51)
		self.label_23 = QtWidgets.QLabel(self.page_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
		self.label_23.setSizePolicy(sizePolicy)
		self.label_23.setMinimumSize(QtCore.QSize(350, 0))
		self.label_23.setText("")
		self.label_23.setAlignment(QtCore.Qt.AlignCenter)
		self.label_23.setObjectName("label_23")
		self.verticalLayout_47.addWidget(self.label_23)
		spacerItem52 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_47.addItem(spacerItem52)
		self.horizontalLayout_43.addLayout(self.verticalLayout_47)
		self.frame = QtWidgets.QFrame(self.page_4)
		self.frame.setStyleSheet("background-color: rgb(79, 159, 239);\n"
									"border-radius: 10px")
		self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.frame.setObjectName("frame")
		self.gridLayout_16 = QtWidgets.QGridLayout(self.frame)
		self.gridLayout_16.setObjectName("gridLayout_16")
		self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
		font = QtGui.QFont()
		font.setPointSize(15)
		self.calendarWidget.setFont(font)
		self.calendarWidget.setStyleSheet("background-color:rgb(85, 170, 255);\n"
									"gridline-color: none;\n"
									"selection-background-color:rgb(85, 170, 255);\n"
									"selection-color: rgb(255, 255, 255);\n"
									"border: none;")
		self.calendarWidget.setDateEditEnabled(False)
		self.calendarWidget.setObjectName("calendarWidget")
		self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
		self.gridLayout_16.addWidget(self.calendarWidget, 0, 0, 1, 1)
		self.horizontalLayout_43.addWidget(self.frame)
		self.verticalLayout_48.addLayout(self.horizontalLayout_43)
		self.line_9 = QtWidgets.QFrame(self.page_4)
		self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_9.setObjectName("line_9")
		self.verticalLayout_48.addWidget(self.line_9)
		self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_44.setObjectName("horizontalLayout_44")
		spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_44.addItem(spacerItem53)
		self.label_24 = QtWidgets.QLabel(self.page_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
		self.label_24.setSizePolicy(sizePolicy)
		self.label_24.setMinimumSize(QtCore.QSize(600, 60))
		self.label_24.setText("")
		self.label_24.setAlignment(QtCore.Qt.AlignCenter)
		self.label_24.setObjectName("label_24")
		self.horizontalLayout_44.addWidget(self.label_24)
		spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_44.addItem(spacerItem54)
		self.verticalLayout_48.addLayout(self.horizontalLayout_44)
		self.gridLayout_17.addLayout(self.verticalLayout_48, 0, 0, 1, 1)
		self.Second_Stack.addWidget(self.page_4)
		self.horizontalLayout_35.addWidget(self.Second_Stack)
		self.verticalLayout_18.addLayout(self.horizontalLayout_35)
		self.gridLayout_7.addLayout(self.verticalLayout_18, 0, 1, 1, 1)
		spacerItem55 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_7.addItem(spacerItem55, 0, 0, 1, 1)
		spacerItem56 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_7.addItem(spacerItem56, 0, 2, 1, 1)
		self.mainStackWidget.addWidget(self.AdminPage)
		self.Admin_Login_Page = QtWidgets.QWidget()
		self.Admin_Login_Page.setObjectName("Admin_Login_Page")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.Admin_Login_Page)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.verticalLayout_12 = QtWidgets.QVBoxLayout()
		self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_12.setObjectName("verticalLayout_12")
		self.label_7 = QtWidgets.QLabel(self.Admin_Login_Page)
		self.label_7.setMaximumSize(QtCore.QSize(16777215, 100))
		font = QtGui.QFont()
		font.setFamily("Monaco")
		font.setPointSize(25)
		self.label_7.setFont(font)
		self.label_7.setAlignment(QtCore.Qt.AlignCenter)
		self.label_7.setObjectName("label_7")
		self.verticalLayout_12.addWidget(self.label_7)
		spacerItem57 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_12.addItem(spacerItem57)
		self.verticalLayout_11 = QtWidgets.QVBoxLayout()
		self.verticalLayout_11.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_11.setObjectName("verticalLayout_11")
		self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_10.setContentsMargins(10, -1, 10, -1)
		self.horizontalLayout_10.setObjectName("horizontalLayout_10")
		spacerItem58 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_10.addItem(spacerItem58)
		self.Admin_LOGIN = QtWidgets.QLabel(self.Admin_Login_Page)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Admin_LOGIN.sizePolicy().hasHeightForWidth())
		self.Admin_LOGIN.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(14)
		self.Admin_LOGIN.setFont(font)
		self.Admin_LOGIN.setObjectName("Admin_LOGIN")
		self.horizontalLayout_10.addWidget(self.Admin_LOGIN)
		spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_10.addItem(spacerItem59)
		self.Admin_ID_Entry = QtWidgets.QLineEdit(self.Admin_Login_Page)
		self.Admin_ID_Entry.setMaximumSize(QtCore.QSize(1000, 16777215))
		self.Admin_ID_Entry.setText("")
		self.Admin_ID_Entry.setMaxLength(12)
		self.Admin_ID_Entry.setObjectName("Admin_ID_Entry")
		self.horizontalLayout_10.addWidget(self.Admin_ID_Entry)
		spacerItem60 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_10.addItem(spacerItem60)
		self.verticalLayout_11.addLayout(self.horizontalLayout_10)
		spacerItem61 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_11.addItem(spacerItem61)
		self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_11.setContentsMargins(10, -1, 10, -1)
		self.horizontalLayout_11.setObjectName("horizontalLayout_11")
		spacerItem62 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_11.addItem(spacerItem62)
		self.Admin_PASSWORD = QtWidgets.QLabel(self.Admin_Login_Page)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(14)
		self.Admin_PASSWORD.setFont(font)
		self.Admin_PASSWORD.setObjectName("Admin_PASSWORD")
		self.horizontalLayout_11.addWidget(self.Admin_PASSWORD)
		spacerItem63 = QtWidgets.QSpacerItem(27, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_11.addItem(spacerItem63)
		self.Admin_Password_Entry = QtWidgets.QLineEdit(self.Admin_Login_Page)
		self.Admin_Password_Entry.setMaximumSize(QtCore.QSize(1000, 16777215))
		self.Admin_Password_Entry.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
		self.Admin_Password_Entry.setMaxLength(100)
		self.Admin_Password_Entry.setEchoMode(QtWidgets.QLineEdit.Password)
		self.Admin_Password_Entry.setObjectName("Admin_Password_Entry")
		self.horizontalLayout_11.addWidget(self.Admin_Password_Entry)
		spacerItem64 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_11.addItem(spacerItem64)
		self.verticalLayout_11.addLayout(self.horizontalLayout_11)
		self.Admin_Log_Error = QtWidgets.QLabel(self.Admin_Login_Page)
		self.Admin_Log_Error.setMinimumSize(QtCore.QSize(0, 50))
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(14)
		self.Admin_Log_Error.setFont(font)
		self.Admin_Log_Error.setStyleSheet("")
		self.Admin_Log_Error.setText("")
		self.Admin_Log_Error.setAlignment(QtCore.Qt.AlignCenter)
		self.Admin_Log_Error.setObjectName("Admin_Log_Error")
		self.verticalLayout_11.addWidget(self.Admin_Log_Error)
		spacerItem65 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_11.addItem(spacerItem65)
		self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
		self.horizontalLayout_12.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_12.setSpacing(10)
		self.horizontalLayout_12.setObjectName("horizontalLayout_12")
		self.Admin_Login_Button = QtWidgets.QPushButton(self.Admin_Login_Page)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Admin_Login_Button.sizePolicy().hasHeightForWidth())
		self.Admin_Login_Button.setSizePolicy(sizePolicy)
		self.Admin_Login_Button.setMinimumSize(QtCore.QSize(300, 50))
		self.Admin_Login_Button.setObjectName("Admin_Login_Button")
		self.horizontalLayout_12.addWidget(self.Admin_Login_Button)
		self.verticalLayout_11.addLayout(self.horizontalLayout_12)
		self.verticalLayout_12.addLayout(self.verticalLayout_11)
		spacerItem66 = QtWidgets.QSpacerItem(20, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_12.addItem(spacerItem66)
		self.gridLayout_3.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
		self.mainStackWidget.addWidget(self.Admin_Login_Page)
		self.Client_Log_Mainpage = QtWidgets.QWidget()
		self.Client_Log_Mainpage.setObjectName("Client_Log_Mainpage")
		self.gridLayout_13 = QtWidgets.QGridLayout(self.Client_Log_Mainpage)
		self.gridLayout_13.setObjectName("gridLayout_13")
		self.verticalLayout_15 = QtWidgets.QVBoxLayout()
		self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_15.setObjectName("verticalLayout_15")
		self.label_8 = QtWidgets.QLabel(self.Client_Log_Mainpage)
		self.label_8.setMaximumSize(QtCore.QSize(16777215, 100))
		font = QtGui.QFont()
		font.setFamily("Monaco")
		font.setPointSize(25)
		self.label_8.setFont(font)
		self.label_8.setAlignment(QtCore.Qt.AlignCenter)
		self.label_8.setObjectName("label_8")
		self.verticalLayout_15.addWidget(self.label_8)
		self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_13.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_13.setObjectName("horizontalLayout_13")
		self.Shell = QtWidgets.QWidget(self.Client_Log_Mainpage)
		self.Shell.setObjectName("Shell")
		self.gridLayout_12 = QtWidgets.QGridLayout(self.Shell)
		self.gridLayout_12.setObjectName("gridLayout_12")
		self.verticalLayout_13 = QtWidgets.QVBoxLayout()
		self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_13.setObjectName("verticalLayout_13")
		self.Client_Package_Purchase = QtWidgets.QToolButton(self.Shell)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Client_Package_Purchase.sizePolicy().hasHeightForWidth())
		self.Client_Package_Purchase.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Client_Package_Purchase.setFont(font)
		icon7 = QtGui.QIcon()
		icon7.addPixmap(QtGui.QPixmap(":/images/dollars.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Client_Package_Purchase.setIcon(icon7)
		self.Client_Package_Purchase.setIconSize(QtCore.QSize(100, 128))
		self.Client_Package_Purchase.setCheckable(True)
		self.Client_Package_Purchase.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Client_Package_Purchase.setObjectName("Client_Package_Purchase")
		self.buttonGroup_4 = QtWidgets.QButtonGroup(Form)
		self.buttonGroup_4.setObjectName("buttonGroup_4")
		self.buttonGroup_4.addButton(self.Client_Package_Purchase)
		self.verticalLayout_13.addWidget(self.Client_Package_Purchase)
		self.Package_List = QtWidgets.QToolButton(self.Shell)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Package_List.sizePolicy().hasHeightForWidth())
		self.Package_List.setSizePolicy(sizePolicy)
		self.Package_List.setIcon(icon)
		self.Package_List.setIconSize(QtCore.QSize(100, 128))
		self.Package_List.setCheckable(True)
		self.Package_List.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Package_List.setObjectName("Package_List")
		self.buttonGroup_4.addButton(self.Package_List)
		self.verticalLayout_13.addWidget(self.Package_List)
		self.Client_Share_Resources = QtWidgets.QToolButton(self.Shell)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Client_Share_Resources.sizePolicy().hasHeightForWidth())
		self.Client_Share_Resources.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Client_Share_Resources.setFont(font)
		icon8 = QtGui.QIcon()
		icon8.addPixmap(QtGui.QPixmap(":/images/share.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Client_Share_Resources.setIcon(icon8)
		self.Client_Share_Resources.setIconSize(QtCore.QSize(100, 128))
		self.Client_Share_Resources.setCheckable(True)
		self.Client_Share_Resources.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Client_Share_Resources.setObjectName("Client_Share_Resources")
		self.buttonGroup_4.addButton(self.Client_Share_Resources)
		self.verticalLayout_13.addWidget(self.Client_Share_Resources)
		self.Client_Return = QtWidgets.QToolButton(self.Shell)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Client_Return.sizePolicy().hasHeightForWidth())
		self.Client_Return.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(10)
		self.Client_Return.setFont(font)
		icon9 = QtGui.QIcon()
		icon9.addPixmap(QtGui.QPixmap(":/images/loading.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.Client_Return.setIcon(icon9)
		self.Client_Return.setIconSize(QtCore.QSize(100, 128))
		self.Client_Return.setCheckable(True)
		self.Client_Return.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.Client_Return.setObjectName("Client_Return")
		self.buttonGroup_4.addButton(self.Client_Return)
		self.verticalLayout_13.addWidget(self.Client_Return)
		self.gridLayout_12.addLayout(self.verticalLayout_13, 0, 0, 1, 1)
		self.horizontalLayout_13.addWidget(self.Shell)
		self.line_4 = QtWidgets.QFrame(self.Client_Log_Mainpage)
		self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.horizontalLayout_13.addWidget(self.line_4)
		self.verticalLayout_14 = QtWidgets.QVBoxLayout()
		self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_14.setObjectName("verticalLayout_14")
		self.Third_Stack_Widget = QtWidgets.QStackedWidget(self.Client_Log_Mainpage)
		self.Third_Stack_Widget.setObjectName("Third_Stack_Widget")
		self.page = QtWidgets.QWidget()
		self.page.setObjectName("page")
		self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.page)
		self.verticalLayout_21.setObjectName("verticalLayout_21")
		self.verticalLayout_19 = QtWidgets.QVBoxLayout()
		self.verticalLayout_19.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_19.setObjectName("verticalLayout_19")
		spacerItem67 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_19.addItem(spacerItem67)
		self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_20.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_20.setObjectName("horizontalLayout_20")
		spacerItem68 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_20.addItem(spacerItem68)
		self.verticalLayout_16 = QtWidgets.QVBoxLayout()
		self.verticalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_16.setObjectName("verticalLayout_16")
		self.Shell_1 = QtWidgets.QWidget(self.page)
		self.Shell_1.setObjectName("Shell_1")
		self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.Shell_1)
		self.verticalLayout_20.setObjectName("verticalLayout_20")
		self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_14.setObjectName("horizontalLayout_14")
		self.Client_Packages = QtWidgets.QLabel(self.Shell_1)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Client_Packages.sizePolicy().hasHeightForWidth())
		self.Client_Packages.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Client_Packages.setFont(font)
		self.Client_Packages.setObjectName("Client_Packages")
		self.horizontalLayout_14.addWidget(self.Client_Packages)
		spacerItem69 = QtWidgets.QSpacerItem(56, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_14.addItem(spacerItem69)
		self.Package_Amount = QtWidgets.QSpinBox(self.Shell_1)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Package_Amount.sizePolicy().hasHeightForWidth())
		self.Package_Amount.setSizePolicy(sizePolicy)
		self.Package_Amount.setMinimumSize(QtCore.QSize(0, 30))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.Package_Amount.setFont(font)
		self.Package_Amount.setMaximum(10)
		self.Package_Amount.setSingleStep(1)
		self.Package_Amount.setObjectName("Package_Amount")
		self.horizontalLayout_14.addWidget(self.Package_Amount)
		spacerItem70 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_14.addItem(spacerItem70)
		self.verticalLayout_20.addLayout(self.horizontalLayout_14)
		self.verticalLayout_16.addWidget(self.Shell_1)
		self.Shell_2 = QtWidgets.QWidget(self.page)
		self.Shell_2.setObjectName("Shell_2")
		self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.Shell_2)
		self.horizontalLayout_18.setObjectName("horizontalLayout_18")
		self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_15.setObjectName("horizontalLayout_15")
		self.Client_Package_Cost = QtWidgets.QLabel(self.Shell_2)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Client_Package_Cost.setFont(font)
		self.Client_Package_Cost.setObjectName("Client_Package_Cost")
		self.horizontalLayout_15.addWidget(self.Client_Package_Cost)
		spacerItem71 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_15.addItem(spacerItem71)
		self.Package_Estimated_Price = QtWidgets.QLabel(self.Shell_2)
		self.Package_Estimated_Price.setMinimumSize(QtCore.QSize(0, 50))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.Package_Estimated_Price.setFont(font)
		self.Package_Estimated_Price.setText("")
		self.Package_Estimated_Price.setOpenExternalLinks(False)
		self.Package_Estimated_Price.setObjectName("Package_Estimated_Price")
		self.horizontalLayout_15.addWidget(self.Package_Estimated_Price)
		spacerItem72 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_15.addItem(spacerItem72)
		self.horizontalLayout_18.addLayout(self.horizontalLayout_15)
		self.verticalLayout_16.addWidget(self.Shell_2)
		self.Shell_3 = QtWidgets.QWidget(self.page)
		self.Shell_3.setObjectName("Shell_3")
		self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.Shell_3)
		self.horizontalLayout_19.setObjectName("horizontalLayout_19")
		self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_16.setObjectName("horizontalLayout_16")
		self.Client_Ticket_Count = QtWidgets.QLabel(self.Shell_3)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Client_Ticket_Count.setFont(font)
		self.Client_Ticket_Count.setObjectName("Client_Ticket_Count")
		self.horizontalLayout_16.addWidget(self.Client_Ticket_Count)
		spacerItem73 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_16.addItem(spacerItem73)
		self.Package_Ticket = QtWidgets.QLabel(self.Shell_3)
		self.Package_Ticket.setMinimumSize(QtCore.QSize(0, 50))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.Package_Ticket.setFont(font)
		self.Package_Ticket.setText("")
		self.Package_Ticket.setObjectName("Package_Ticket")
		self.horizontalLayout_16.addWidget(self.Package_Ticket)
		spacerItem74 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_16.addItem(spacerItem74)
		self.horizontalLayout_19.addLayout(self.horizontalLayout_16)
		self.verticalLayout_16.addWidget(self.Shell_3)
		self.Payment_Successful = QtWidgets.QLabel(self.page)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Payment_Successful.sizePolicy().hasHeightForWidth())
		self.Payment_Successful.setSizePolicy(sizePolicy)
		self.Payment_Successful.setMinimumSize(QtCore.QSize(0, 70))
		self.Payment_Successful.setText("")
		self.Payment_Successful.setAlignment(QtCore.Qt.AlignCenter)
		self.Payment_Successful.setObjectName("Payment_Successful")
		self.verticalLayout_16.addWidget(self.Payment_Successful)
		self.horizontalLayout_20.addLayout(self.verticalLayout_16)
		spacerItem75 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_20.addItem(spacerItem75)
		self.verticalLayout_19.addLayout(self.horizontalLayout_20)
		self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_17.setObjectName("horizontalLayout_17")
		spacerItem76 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_17.addItem(spacerItem76)
		self.pushButton_5 = QtWidgets.QPushButton(self.page)
		self.pushButton_5.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
		self.pushButton_5.setSizePolicy(sizePolicy)
		self.pushButton_5.setMinimumSize(QtCore.QSize(150, 40))
		self.pushButton_5.setObjectName("pushButton_5")
		self.horizontalLayout_17.addWidget(self.pushButton_5)
		spacerItem77 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_17.addItem(spacerItem77)
		self.verticalLayout_19.addLayout(self.horizontalLayout_17)
		spacerItem78 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_19.addItem(spacerItem78)
		self.verticalLayout_21.addLayout(self.verticalLayout_19)
		self.Third_Stack_Widget.addWidget(self.page)
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setObjectName("page_2")
		self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.page_2)
		self.verticalLayout_27.setObjectName("verticalLayout_27")
		self.verticalLayout_22 = QtWidgets.QVBoxLayout()
		self.verticalLayout_22.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_22.setObjectName("verticalLayout_22")
		spacerItem79 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_22.addItem(spacerItem79)
		self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_21.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_21.setObjectName("horizontalLayout_21")
		spacerItem80 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_21.addItem(spacerItem80)
		self.verticalLayout_24 = QtWidgets.QVBoxLayout()
		self.verticalLayout_24.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
		self.verticalLayout_24.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_24.setObjectName("verticalLayout_24")
		self.Shell_4 = QtWidgets.QWidget(self.page_2)
		self.Shell_4.setObjectName("Shell_4")
		self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.Shell_4)
		self.verticalLayout_26.setObjectName("verticalLayout_26")
		self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_22.setObjectName("horizontalLayout_22")
		self.Recipient_Client = QtWidgets.QLabel(self.Shell_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Recipient_Client.sizePolicy().hasHeightForWidth())
		self.Recipient_Client.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Recipient_Client.setFont(font)
		self.Recipient_Client.setObjectName("Recipient_Client")
		self.horizontalLayout_22.addWidget(self.Recipient_Client)
		spacerItem81 = QtWidgets.QSpacerItem(66, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_22.addItem(spacerItem81)
		self.Recipient_ID = QtWidgets.QLineEdit(self.Shell_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Recipient_ID.sizePolicy().hasHeightForWidth())
		self.Recipient_ID.setSizePolicy(sizePolicy)
		self.Recipient_ID.setMaxLength(11)
		self.Recipient_ID.setObjectName("Recipient_ID")
		self.horizontalLayout_22.addWidget(self.Recipient_ID)
		self.verticalLayout_26.addLayout(self.horizontalLayout_22)
		self.verticalLayout_24.addWidget(self.Shell_4)
		self.Shell_5 = QtWidgets.QWidget(self.page_2)
		self.Shell_5.setObjectName("Shell_5")
		self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.Shell_5)
		self.horizontalLayout_23.setObjectName("horizontalLayout_23")
		self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_24.setObjectName("horizontalLayout_24")
		self.Ticket_Issued = QtWidgets.QLabel(self.Shell_5)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.Ticket_Issued.setFont(font)
		self.Ticket_Issued.setObjectName("Ticket_Issued")
		self.horizontalLayout_24.addWidget(self.Ticket_Issued)
		spacerItem82 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_24.addItem(spacerItem82)
		self.Package_Ticket_Amount = QtWidgets.QSpinBox(self.Shell_5)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.Package_Ticket_Amount.sizePolicy().hasHeightForWidth())
		self.Package_Ticket_Amount.setSizePolicy(sizePolicy)
		self.Package_Ticket_Amount.setMinimumSize(QtCore.QSize(100, 30))
		font = QtGui.QFont()
		font.setFamily("Consolas")
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(50)
		self.Package_Ticket_Amount.setFont(font)
		self.Package_Ticket_Amount.setMaximum(10)
		self.Package_Ticket_Amount.setSingleStep(2)
		self.Package_Ticket_Amount.setObjectName("Package_Ticket_Amount")
		self.horizontalLayout_24.addWidget(self.Package_Ticket_Amount)
		spacerItem83 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_24.addItem(spacerItem83)
		self.horizontalLayout_23.addLayout(self.horizontalLayout_24)
		self.verticalLayout_24.addWidget(self.Shell_5)
		spacerItem84 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.verticalLayout_24.addItem(spacerItem84)
		self.horizontalLayout_21.addLayout(self.verticalLayout_24)
		spacerItem85 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_21.addItem(spacerItem85)
		self.verticalLayout_22.addLayout(self.horizontalLayout_21)
		self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_27.setObjectName("horizontalLayout_27")
		spacerItem86 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_27.addItem(spacerItem86)
		self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
		self.pushButton_6.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
		self.pushButton_6.setSizePolicy(sizePolicy)
		self.pushButton_6.setMinimumSize(QtCore.QSize(150, 40))
		self.pushButton_6.setObjectName("pushButton_6")
		self.horizontalLayout_27.addWidget(self.pushButton_6)
		spacerItem87 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_27.addItem(spacerItem87)
		self.verticalLayout_22.addLayout(self.horizontalLayout_27)
		spacerItem88 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_22.addItem(spacerItem88)
		self.verticalLayout_27.addLayout(self.verticalLayout_22)
		self.Third_Stack_Widget.addWidget(self.page_2)
		self.page_5 = QtWidgets.QWidget()
		self.page_5.setObjectName("page_5")
		self.gridLayout_18 = QtWidgets.QGridLayout(self.page_5)
		self.gridLayout_18.setObjectName("gridLayout_18")
		spacerItem89 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_18.addItem(spacerItem89, 0, 0, 1, 1)
		self.verticalLayout_37 = QtWidgets.QVBoxLayout()
		self.verticalLayout_37.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_37.setObjectName("verticalLayout_37")
		self.Click_Details = QtWidgets.QLabel(self.page_5)
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setStyleStrategy(QtGui.QFont.PreferDefault)
		self.Click_Details.setFont(font)
		self.Click_Details.setTabletTracking(False)
		self.Click_Details.setAcceptDrops(False)
		self.Click_Details.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.Click_Details.setAutoFillBackground(False)
		self.Click_Details.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.Click_Details.setLineWidth(1)
		self.Click_Details.setMidLineWidth(0)
		self.Click_Details.setText("")
		self.Click_Details.setTextFormat(QtCore.Qt.AutoText)
		self.Click_Details.setScaledContents(True)
		self.Click_Details.setAlignment(QtCore.Qt.AlignCenter)
		self.Click_Details.setWordWrap(False)
		self.Click_Details.setIndent(3)
		self.Click_Details.setOpenExternalLinks(False)
		self.Click_Details.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
		self.Click_Details.setObjectName("Click_Details")
		self.verticalLayout_37.addWidget(self.Click_Details)
		self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_38.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_38.setObjectName("horizontalLayout_38")
		self.label_4 = QtWidgets.QLabel(self.page_5)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(19)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_38.addWidget(self.label_4)
		self.Package_Quantity = QtWidgets.QLabel(self.page_5)
		self.Package_Quantity.setEnabled(True)
		font = QtGui.QFont()
		font.setPointSize(40)
		self.Package_Quantity.setFont(font)
		self.Package_Quantity.setText("")
		self.Package_Quantity.setAlignment(QtCore.Qt.AlignCenter)
		self.Package_Quantity.setObjectName("Package_Quantity")
		self.horizontalLayout_38.addWidget(self.Package_Quantity)
		self.verticalLayout_37.addLayout(self.horizontalLayout_38)
		self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_47.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_47.setObjectName("horizontalLayout_47")
		self.label_5 = QtWidgets.QLabel(self.page_5)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(19)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout_47.addWidget(self.label_5)
		self.Ticket_Quantity = QtWidgets.QLabel(self.page_5)
		font = QtGui.QFont()
		font.setPointSize(40)
		self.Ticket_Quantity.setFont(font)
		self.Ticket_Quantity.setText("")
		self.Ticket_Quantity.setAlignment(QtCore.Qt.AlignCenter)
		self.Ticket_Quantity.setObjectName("Ticket_Quantity")
		self.horizontalLayout_47.addWidget(self.Ticket_Quantity)
		self.verticalLayout_37.addLayout(self.horizontalLayout_47)
		self.gridLayout_18.addLayout(self.verticalLayout_37, 0, 1, 1, 1)
		spacerItem90 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_18.addItem(spacerItem90, 0, 2, 1, 1)
		self.Third_Stack_Widget.addWidget(self.page_5)
		self.page_6 = QtWidgets.QWidget()
		self.page_6.setObjectName("page_6")
		self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.page_6)
		self.verticalLayout_44.setObjectName("verticalLayout_44")
		self.verticalLayout_43 = QtWidgets.QVBoxLayout()
		self.verticalLayout_43.setObjectName("verticalLayout_43")
		self.verticalLayout_42 = QtWidgets.QVBoxLayout()
		self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_42.setObjectName("verticalLayout_42")
		self.verticalLayout_41 = QtWidgets.QVBoxLayout()
		self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_41.setObjectName("verticalLayout_41")
		self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_56.setObjectName("horizontalLayout_56")
		spacerItem91 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_56.addItem(spacerItem91)
		self.label_10 = QtWidgets.QLabel(self.page_6)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.label_10.setFont(font)
		self.label_10.setObjectName("label_10")
		self.horizontalLayout_56.addWidget(self.label_10)
		self.lineEdit_2 = QtWidgets.QLineEdit(self.page_6)
		self.lineEdit_2.setMaxLength(16)
		self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.horizontalLayout_56.addWidget(self.lineEdit_2)
		spacerItem92 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_56.addItem(spacerItem92)
		self.verticalLayout_41.addLayout(self.horizontalLayout_56)
		self.verticalLayout_40 = QtWidgets.QVBoxLayout()
		self.verticalLayout_40.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_40.setObjectName("verticalLayout_40")
		self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_49.setObjectName("horizontalLayout_49")
		self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_50.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_50.setObjectName("horizontalLayout_50")
		self.label_15 = QtWidgets.QLabel(self.page_6)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.label_15.setFont(font)
		self.label_15.setObjectName("label_15")
		self.horizontalLayout_50.addWidget(self.label_15)
		self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_51.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_51.setObjectName("horizontalLayout_51")
		self.frame1 = QtWidgets.QFrame(self.page_6)
		self.frame1.setStyleSheet("background-color: rgb(244, 244, 244);\n"
										"border-radius: 10px\n"
										"")
		self.frame1.setObjectName("frame1")
		self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame1)
		self.verticalLayout_38.setObjectName("verticalLayout_38")
		self.label_12 = QtWidgets.QLabel(self.frame1)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(11)
		self.label_12.setFont(font)
		self.label_12.setStyleSheet("")
		self.label_12.setAlignment(QtCore.Qt.AlignCenter)
		self.label_12.setObjectName("label_12")
		self.verticalLayout_38.addWidget(self.label_12)
		self.spinBox = QtWidgets.QSpinBox(self.frame1)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
		self.spinBox.setSizePolicy(sizePolicy)
		self.spinBox.setMinimumSize(QtCore.QSize(50, 30))
		self.spinBox.setMaximum(12)
		self.spinBox.setObjectName("spinBox")
		self.verticalLayout_38.addWidget(self.spinBox)
		self.horizontalLayout_51.addWidget(self.frame1)
		self.line_6 = QtWidgets.QFrame(self.page_6)
		self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_6.setObjectName("line_6")
		self.horizontalLayout_51.addWidget(self.line_6)
		self.frame2 = QtWidgets.QFrame(self.page_6)
		self.frame2.setStyleSheet("background-color: rgb(244, 244, 244);\n"
										"border-radius: 10px")
		self.frame2.setObjectName("frame2")
		self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame2)
		self.verticalLayout_39.setObjectName("verticalLayout_39")
		self.label_14 = QtWidgets.QLabel(self.frame2)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(11)
		self.label_14.setFont(font)
		self.label_14.setAlignment(QtCore.Qt.AlignCenter)
		self.label_14.setObjectName("label_14")
		self.verticalLayout_39.addWidget(self.label_14)
		self.spinBox_2 = QtWidgets.QSpinBox(self.frame2)
		self.spinBox_2.setMinimumSize(QtCore.QSize(50, 30))
		self.spinBox_2.setMinimum(2018)
		self.spinBox_2.setMaximum(3091)
		self.spinBox_2.setObjectName("spinBox_2")
		self.verticalLayout_39.addWidget(self.spinBox_2)
		self.horizontalLayout_51.addWidget(self.frame2)
		self.horizontalLayout_50.addLayout(self.horizontalLayout_51)
		self.horizontalLayout_49.addLayout(self.horizontalLayout_50)
		spacerItem93 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_49.addItem(spacerItem93)
		self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_48.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_48.setObjectName("horizontalLayout_48")
		self.lineEdit_3 = QtWidgets.QLineEdit(self.page_6)
		self.lineEdit_3.setMaxLength(3)
		self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.horizontalLayout_48.addWidget(self.lineEdit_3)
		self.horizontalLayout_49.addLayout(self.horizontalLayout_48)
		self.verticalLayout_40.addLayout(self.horizontalLayout_49)
		self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_52.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_52.setObjectName("horizontalLayout_52")
		spacerItem94 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_52.addItem(spacerItem94)
		self.label_13 = QtWidgets.QLabel(self.page_6)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.label_13.setFont(font)
		self.label_13.setObjectName("label_13")
		self.horizontalLayout_52.addWidget(self.label_13)
		self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_53.setObjectName("horizontalLayout_53")
		self.lineEdit_5 = QtWidgets.QLineEdit(self.page_6)
		self.lineEdit_5.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhSensitiveData)
		self.lineEdit_5.setMaxLength(4)
		self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.horizontalLayout_53.addWidget(self.lineEdit_5)
		self.horizontalLayout_52.addLayout(self.horizontalLayout_53)
		spacerItem95 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_52.addItem(spacerItem95)
		self.verticalLayout_40.addLayout(self.horizontalLayout_52)
		self.line_2 = QtWidgets.QFrame(self.page_6)
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.verticalLayout_40.addWidget(self.line_2)
		self.verticalLayout_41.addLayout(self.verticalLayout_40)
		self.verticalLayout_42.addLayout(self.verticalLayout_41)
		self.verticalLayout_43.addLayout(self.verticalLayout_42)
		self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_59.setObjectName("horizontalLayout_59")
		self.pushButton_2 = QtWidgets.QPushButton(self.page_6)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
		self.pushButton_2.setSizePolicy(sizePolicy)
		self.pushButton_2.setMinimumSize(QtCore.QSize(200, 50))
		self.pushButton_2.setObjectName("pushButton_2")
		self.horizontalLayout_59.addWidget(self.pushButton_2)
		self.line_7 = QtWidgets.QFrame(self.page_6)
		self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_7.setObjectName("line_7")
		self.horizontalLayout_59.addWidget(self.line_7)
		self.pushButton = QtWidgets.QPushButton(self.page_6)
		self.pushButton.setEnabled(False)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
		self.pushButton.setSizePolicy(sizePolicy)
		self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_59.addWidget(self.pushButton)
		self.verticalLayout_43.addLayout(self.horizontalLayout_59)
		self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_57.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_57.setObjectName("horizontalLayout_57")
		spacerItem96 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_57.addItem(spacerItem96)
		self.label_16 = QtWidgets.QLabel(self.page_6)
		font = QtGui.QFont()
		font.setFamily("Comic Sans MS")
		font.setPointSize(12)
		self.label_16.setFont(font)
		self.label_16.setObjectName("label_16")
		self.horizontalLayout_57.addWidget(self.label_16)
		self.horizontalLayout_58 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_58.setObjectName("horizontalLayout_58")
		self.lineEdit_7 = QtWidgets.QLineEdit(self.page_6)
		self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
		self.lineEdit_7.setMaxLength(10)
		self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
		self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit_7.setObjectName("lineEdit_7")
		self.horizontalLayout_58.addWidget(self.lineEdit_7)
		self.horizontalLayout_57.addLayout(self.horizontalLayout_58)
		spacerItem97 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_57.addItem(spacerItem97)
		self.verticalLayout_43.addLayout(self.horizontalLayout_57)
		self.verticalLayout_44.addLayout(self.verticalLayout_43)
		self.Third_Stack_Widget.addWidget(self.page_6)
		self.page_7 = QtWidgets.QWidget()
		self.page_7.setObjectName("page_7")
		self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.page_7)
		self.verticalLayout_46.setObjectName("verticalLayout_46")
		self.verticalLayout_45 = QtWidgets.QVBoxLayout()
		self.verticalLayout_45.setContentsMargins(10, 10, 10, 10)
		self.verticalLayout_45.setObjectName("verticalLayout_45")
		self.label_11 = QtWidgets.QLabel(self.page_7)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
		self.label_11.setSizePolicy(sizePolicy)
		self.label_11.setMinimumSize(QtCore.QSize(0, 100))
		self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.label_11.setText("")
		self.label_11.setAlignment(QtCore.Qt.AlignCenter)
		self.label_11.setObjectName("label_11")
		self.verticalLayout_45.addWidget(self.label_11)
		self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_54.setContentsMargins(10, 10, 10, 10)
		self.horizontalLayout_54.setObjectName("horizontalLayout_54")
		spacerItem98 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_54.addItem(spacerItem98)
		self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_45.setObjectName("horizontalLayout_45")
		spacerItem99 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_45.addItem(spacerItem99)
		self.TREE = QtWidgets.QTreeWidget(self.page_7)
		self.TREE.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.TREE.sizePolicy().hasHeightForWidth())
		self.TREE.setSizePolicy(sizePolicy)
		self.TREE.setMaximumSize(QtCore.QSize(583, 391))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.TREE.setFont(font)
		self.TREE.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.TREE.setProperty("showDropIndicator", False)
		self.TREE.setTextElideMode(QtCore.Qt.ElideMiddle)
		self.TREE.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
		self.TREE.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
		self.TREE.setIndentation(10)
		self.TREE.setUniformRowHeights(False)
		self.TREE.setItemsExpandable(False)
		self.TREE.setAnimated(False)
		self.TREE.setAllColumnsShowFocus(False)
		self.TREE.setExpandsOnDoubleClick(False)
		self.TREE.setColumnCount(3)
		self.TREE.setObjectName("TREE")
		font = QtGui.QFont()
		font.setPointSize(14)
		self.TREE.headerItem().setFont(0, font)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.TREE.headerItem().setFont(1, font)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.TREE.headerItem().setFont(2, font)
		self.TREE.header().setVisible(True)
		self.TREE.header().setCascadingSectionResizes(True)
		self.TREE.header().setDefaultSectionSize(200)
		self.TREE.header().setHighlightSections(False)
		self.TREE.header().setMinimumSectionSize(50)
		self.TREE.header().setSortIndicatorShown(False)
		self.TREE.header().setStretchLastSection(True)
		self.horizontalLayout_45.addWidget(self.TREE)
		spacerItem100 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_45.addItem(spacerItem100)
		self.horizontalLayout_54.addLayout(self.horizontalLayout_45)
		spacerItem101 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_54.addItem(spacerItem101)
		self.verticalLayout_45.addLayout(self.horizontalLayout_54)
		self.verticalLayout_46.addLayout(self.verticalLayout_45)
		self.Third_Stack_Widget.addWidget(self.page_7)
		self.verticalLayout_14.addWidget(self.Third_Stack_Widget)
		self.horizontalLayout_13.addLayout(self.verticalLayout_14)
		self.verticalLayout_15.addLayout(self.horizontalLayout_13)
		self.gridLayout_13.addLayout(self.verticalLayout_15, 0, 0, 1, 1)
		self.mainStackWidget.addWidget(self.Client_Log_Mainpage)
		self.verticalLayout_51.addWidget(self.mainStackWidget)
		Form.setCentralWidget(self.centralwidget)

		self.retranslateUi(Form)
		self.mainStackWidget.setCurrentIndex(0)
		self.Second_Stack.setCurrentIndex(6)
		self.Gender_Select.setCurrentIndex(-1)
		self.Client_Select.setCurrentIndex(-1)
		self.Third_Stack_Widget.setCurrentIndex(2)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "E - TRANSPORT MANAGEMENT SYSTEM"))
		self.Fut.setText(_translate("Form", "..."))
		self.label.setText(_translate("Form", "E - TRANSPORT   MANAGEMENT SYSTEM"))
		self.label_2.setText(_translate("Form", "Welcome to the E - Transport Management Application"))
		self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
												"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
												"p, li { white-space: pre-wrap; }\n"
												"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
												"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
												"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
												"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">No more Bus_Park Queue challenges</span></p>\n"
												"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
												"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">No more currency denomination exchange convertion problem</span></p>\n"
												"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:12pt;\"><br /></p>\n"
												"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt;\">No more unnecessary delay at the Bus_Park</span></p></body></html>"))
		self.Label_Start.setText(_translate("Form", "Creating ease for both Passengers and Cab Drivers, Bus Drivers\n""\n""For details about the Software developers please click the Question mark button"))
		self.L_Admin.setText(_translate("Form", "Admin"))
		self.L_About.setText(_translate("Form", "?"))
		self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
												"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
												"p, li { white-space: pre-wrap; }\n"
												"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#aa00ff;\">E - TRANSPORTATION MANAGEMENT SYSTEM SOFTWARE</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#aa00ff;\">(ETMS)</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#55aaff;\">Developed by</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Software Engineering GROUP 2, 2018/2019</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#55aaff;\">Members of Group 2</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Joel Audu. 2014/1/49734CP</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Orbunde Terna. 2014/1/49769CP</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Babangida Idris. 2014/1/49787CP</span></p>\n"

												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Group 6 members</span></p>\n"
												"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">Qt Designer, Qt Documentation, Qt Development Environment and PyQt5</span></p></body></html>"))
		self.A_Back.setText(_translate("Form", "Back"))
		self.label_6.setText(_translate("Form", "       ADMIN CLIENT SERVICES"))
		self.Admin_Client.setText(_translate("Form", "Client registration"))
		self.Admin_Client_Log.setText(_translate("Form", "Client Log"))
		self.Admin_Book.setText(_translate("Form", "Client Booking"))
		self.Admin_Others.setText(_translate("Form", "Driver\'s_Check In"))
		self.Admin_Pay.setText(_translate("Form", "Driver\'s_Payroll"))
		self.Label_FN.setText(_translate("Form", "FULLNAME:"))
		self.lineEdit_18.setPlaceholderText(_translate("Form", " Full_Name e.g Name Surname"))
		self.Label_G.setText(_translate("Form", "GENDER:"))
		self.Gender_Select.setItemText(0, _translate("Form", "Male"))
		self.Gender_Select.setItemText(1, _translate("Form", "Female"))
		self.Label_Phone.setText(_translate("Form", "PHONE NUMBER:"))
		self.lineEdit.setPlaceholderText(_translate("Form", "Phone number"))
		self.Label_E.setText(_translate("Form", "EMAIL:"))
		self.lineEdit_20.setPlaceholderText(_translate("Form", "Email"))
		self.Label_DoP.setText(_translate("Form", "CLIENT:"))
		self.Client_Select.setItemText(0, _translate("Form", "Passenger"))
		self.Client_Select.setItemText(1, _translate("Form", "Driver"))
		self.Label_P.setText(_translate("Form", "PASSWORD:"))
		self.lineEdit_21.setPlaceholderText(_translate("Form", "Password"))
		self.Label_CP.setText(_translate("Form", "CONFIRM PASSWORD:"))
		self.lineEdit_22.setPlaceholderText(_translate("Form", "Password Confirmation"))
		self.Reg_Reg.setText(_translate("Form", "REGISTER"))
		self.Label_User.setText(_translate("Form", "CLIENT ID:"))
		self.Log_UserEdit.setPlaceholderText(_translate("Form", "ETP_####### for passsengers or ETD_####### for drivers"))
		self.Label_Pass.setText(_translate("Form", "PASSWORD:"))
		self.Log_UserPass.setPlaceholderText(_translate("Form", "Password"))
		self.Log_button.setText(_translate("Form", "Client Log"))
		self.Label_ID.setText(_translate("Form", "Client ID:"))
		self.Book_ID.setPlaceholderText(_translate("Form", "Client ID e.g ETP_#######"))
		self.Label_Package.setText(_translate("Form", "Package ID:"))
		self.Book_Package.setPlaceholderText(_translate("Form", "Package ID e.g ETPA_#######"))
		self.Book_confirm.setText(_translate("Form", "Confirm Package"))
		self.pushButton_4.setText(_translate("Form", "Book"))
		self.Book_Next.setText(_translate("Form", "Next"))
		self.Label_Client_ID_Pay.setText(_translate("Form", "Driver ID:"))
		self.Pay_Client_ID.setPlaceholderText(_translate("Form", "Client ID e.g ETD_#######"))

		self.Pay_cpnfirm.setText(_translate("Form", "Confirm Payment"))
		self.Clear_Pay.setText(_translate("Form", "Next"))
		self.Pay_Button.setText(_translate("Form", "Pay"))
		self.Driver_Check_Info.setText(_translate("Form", "Driver ID:"))
		self.Drivers_ID.setPlaceholderText(_translate("Form", "Client ID e.g ETD_#######"))
		self.Check_In.setText(_translate("Form", "Check In"))

		# ###################################

		self.Check_Tree.headerItem().setText(0, _translate("Form", "List of Callup Number Available For Current Checked in Drivers"))
		__sortingEnabled = self.Check_Tree.isSortingEnabled()
		self.Check_Tree.setSortingEnabled(False)
		self.Check_Tree.setSortingEnabled(__sortingEnabled)

		# ###################################

		self.Check_Out.setText(_translate("Form", "Check Out"))
		self.label_9.setText(_translate("Form", "BUS DESCRIPTION"))
		self.NoS.setText(_translate("Form", "Number of Seat:"))
		self.MNoP.setText(_translate("Form", "Maximum Number of Passenger:"))
		self.Driver_Submit_BP.setText(_translate("Form", "Submit"))
		self.Driver_Next_BP.setText(_translate("Form", "Next"))
		self.label_7.setText(_translate("Form", "ADMIN\'S LOG"))
		self.Admin_LOGIN.setText(_translate("Form", "ADMIN ID:"))
		self.Admin_ID_Entry.setPlaceholderText(_translate("Form", "Admin ID"))
		self.Admin_PASSWORD.setText(_translate("Form", "PASSWORD:"))
		self.Admin_Password_Entry.setPlaceholderText(_translate("Form", "Admin Password"))
		self.Admin_Login_Button.setText(_translate("Form", "Login"))
		self.label_8.setText(_translate("Form", "CLIENT\'S LOG"))
		self.Client_Package_Purchase.setText(_translate("Form", "Purchase Packages"))
		self.Package_List.setText(_translate("Form", "Package"))
		self.Client_Share_Resources.setText(_translate("Form", "Share Resources"))
		self.Client_Return.setText(_translate("Form", "Return to Admin"))
		self.Client_Packages.setText(_translate("Form", "Number of Package:"))
		self.Client_Package_Cost.setText(_translate("Form", "Estimated Cost of Package:"))
		self.Client_Ticket_Count.setText(_translate("Form", "Number of Ticket:"))
		self.pushButton_5.setText(_translate("Form", "Pay"))
		self.Recipient_Client.setText(_translate("Form", "Recipient Client ID:"))
		self.Recipient_ID.setPlaceholderText(_translate("Form", "Recipient ID e.g ETP_#######"))
		self.Ticket_Issued.setText(_translate("Form", "Amount of Tickets:"))
		self.pushButton_6.setText(_translate("Form", "Transfer"))
		self.label_4.setText(_translate("Form", "Packages Available:"))
		self.label_5.setText(_translate("Form", "Tickets Available:"))
		self.label_10.setText(_translate("Form", "Card Number:"))
		self.lineEdit_2.setPlaceholderText(_translate("Form", "XXXX - XXXX - XXXX -XXXX"))
		self.label_15.setText(_translate("Form", "Card Expiry Date:"))
		self.label_12.setText(_translate("Form", "Month"))
		self.label_14.setText(_translate("Form", "Year"))
		self.lineEdit_3.setPlaceholderText(_translate("Form", "CVC"))
		self.label_13.setText(_translate("Form", "PIN:"))
		self.lineEdit_5.setPlaceholderText(_translate("Form", "XXXX"))
		self.pushButton_2.setText(_translate("Form", "Click to generate OTP"))
		self.pushButton.setText(_translate("Form", "Pay"))
		self.label_16.setText(_translate("Form", "OTP:"))
		self.lineEdit_7.setPlaceholderText(_translate("Form", "XXX - XXX"))
		self.TREE.headerItem().setText(0, _translate("Form", "S/N"))
		self.TREE.headerItem().setText(1, _translate("Form", "Packages"))
		self.TREE.headerItem().setText(2, _translate("Form", "Amount of Tickets"))

	def D_Loc_Check(self):
		Signal = self.sender()
		SenderName = str(Signal.objectName())

		field = self.Admin_ID_Entry.text()
		main_Ad = self.Database.Admin_main_id(field)

		D_ID = self.Drivers_ID.text()

		Client = self.C_Database.Client_Info(D_ID,main_Ad)

		if SenderName == "Check_In":
			if len(D_ID) == 0:
				self.label_3.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: red;"
											)
				self.label_3.setText("Field present must be filled")
				print("\a")
			elif Client is False:
				self.label_3.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: red;"
											)
				self.label_3.setText("The ID entered does not exist")
				print("\a")

			else:

				Bus_Id = self.C_Database.BID(D_ID,main_Ad)
				Load_Val = self.C_Database.BusPick(self.BusPark,main_Ad,Bus_Id[0],Bus_Id[1])
				self.C_Database.C_Queue(main_Ad,D_ID,self.BusPark)
				status = self.C_Database.D_Status(D_ID,main_Ad)
				status = status[0]
				if status == self.BusPark:
					self.label_3.setStyleSheet("font-size: 18pt;"
												"font-family: Consolas;"
												"color: red;"
												)
					self.label_3.setText("You have already checked in at this Location")
					print("\a")

				elif status != self.BusPark and status != "None":
					self.label_3.setStyleSheet("font-size: 18pt;"
												"font-family: Consolas;"
												"color: red;"
												)
					self.label_3.setText("You did not Check out from the Bus park\nwhich you checked in last")
					print("\a")
				elif status == "None" and Bus_Id[2] == Bus_Id[1] and status[1] == self.BusPark:
					self.Click_Details_2.setStyleSheet("font-size: 15pt;"
																	"font-family: 	Consolas;"
																	"color: Green;"
																	)
					self.Click_Details_2.setText("The Bus with ID %s have been filled at this location" % Bus_Id[0])
				else:
					if Load_Val == 0:
						self.C_Database.SDL(self.BusPark,main_Ad,D_ID,SenderName,0)
						Drop = self.C_Database.ComTrac(main_Ad,Bus_Id[0],self.BusPark)
						if Drop == 0:
							self.Click_Details_2.setStyleSheet("font-size: 15pt;"
													"font-family: Consolas;"
													"color: Blue;"
													)
							self.Click_Details_2.setText("Please Stand by\nPassenger will be available\nSoon")
						else:
							self.C_Database.Spent(Bus_Id[0])
							self.Click_Details_2.setStyleSheet("font-size: 15pt;"
													"font-family: Consolas;"
													"color: Blue;"
													)
							self.Click_Details_2.setText("%i Passenger was dropped of at\n%s's Buspark by the bus with ID %s .\nPlease Stand by\nPassenger will be available\nSoon" % (Drop,self.BusPark,Bus_Id[0]))

					else:
						self.C_Database.SDL(self.BusPark,main_Ad,D_ID,SenderName,len(Load_Val))
						Drop = self.C_Database.ComTrac(main_Ad,Bus_Id[0],self.BusPark)

						if Drop == 0:
							self.Click_Details_2.setStyleSheet("font-size: 15pt;"
													"font-family: Consolas;"
													"color: Blue;"
													)
							self.Click_Details_2.setText("%i passenger is available\n and have been assigned to you\nPlease notify the passenger\nat the waiting center\nwith callup number from\nlist of Call Numbers Available to you\nPlease take a note of the Callup values" % len(Load_Val))
							for x in range(0,len(Load_Val)):
								item_0 = QtWidgets.QTreeWidgetItem(self.Check_Tree)
								font = QtGui.QFont()
								font.setPointSize(15)
								font.setBold(True)
								item_0.setFont(0, font)
								self.Check_Tree.topLevelItem(x).setTextAlignment(0, QtCore.Qt.AlignCenter)
								self.Check_Tree.topLevelItem(x).setText(0, str(Load_Val[x][1]))
						else:
							self.C_Database.Spent(Bus_Id[0])
							self.Click_Details_2.setStyleSheet("font-size: 15pt;"
													"font-family: Consolas;"
													"color: Blue;"
													)
							self.Click_Details_2.setText("%i Passenger was dropped of at\n%s's Buspark by the bus with ID %s .\n%i passenger is available\n and have been assigned to you\nPlease notify the passenger\nat the waiting center\nwith callup number from\nlist of Call Numbers Available to you\nPlease take a note of the Callup values" % (Drop,self.BusPark,Bus_Id[0],len(Load_Val)))
							# ######
							# ######
							for x in range(0,len(Load_Val)):
								item_0 = QtWidgets.QTreeWidgetItem(self.Check_Tree)
								font = QtGui.QFont()
								font.setPointSize(15)
								font.setBold(True)
								item_0.setFont(0, font)
								self.Check_Tree.topLevelItem(x).setTextAlignment(0, QtCore.Qt.AlignCenter)
								self.Check_Tree.topLevelItem(x).setText(0, str(Load_Val[x][1]))

		elif SenderName == "Check_Out":
			if len(D_ID) == 0:
				self.label_3.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: red;"
											)
				self.label_3.setText("Field present must be filled")
				print("\a")
			elif Client is False:
				self.label_3.setStyleSheet("font-size: 18pt;"
											"font-family: Consolas;"
											"color: red;"
											)
				self.label_3.setText("The ID entered does not exist")
				print("\a")
			else:
				status = self.C_Database.D_Status(D_ID,main_Ad)

				if status[0] != self.BusPark and status != "None":
					self.Click_Details_2.setStyleSheet("font-size: 15pt;"
											"font-family: Consolas;"
											"color: Blue;"
											)
					self.Click_Details_2.setText("You did not Check out from the Bus park\nwhich you checked in last.\nIn order to successfully\nbe able to Checkout\nfrom this location, you must first Checkout\nfrom the previous Buspark you where\nat then check in at this buspark")
				elif status[0] != "None" and status[1] != self.BusPark:
					self.Click_Details_2.setStyleSheet("font-size: 15pt;"
											"font-family: Consolas;"
											"color: Blue;"
											)
					self.Click_Details_2.setText("Please Check In at this current\nLocation")
				else:
					Leave = self.C_Database.BID(D_ID,main_Ad)
					Percentage = (80/100) * Leave[1]

					if Leave[2] >= Percentage:
						self.C_Database.SDL(self.BusPark,main_Ad,D_ID,SenderName,'')
						self.Click_Details_2.setStyleSheet("font-size: 15pt;"
												"font-family: Consolas;"
												"color: Blue;"
												)
						self.Click_Details_2.setText("You Have Checkedout from\n%s's BusPark with a total of %i Passenger" % (self.BusPark,Leave[2]))
					else:
						self.Click_Details_2.setStyleSheet("font-size: 15pt;"
												"font-family: Consolas;"
												"color: Blue;"
												)
						self.Click_Details_2.setText("You have less than 80% Passengers.\nPlease Standby Passengers will be available\nSoon")
						print("\a")

		else:
			pass

	def CSS(self):
		self.label_3.clear()
		self.Click_Details_2.clear()
		self.Check_Tree.clear()

	def IssuePayment(self):
		Signal = self.sender()
		SenderName = str(Signal.objectName())

		D_ID = self.Pay_Client_ID.text()
		field = self.Admin_ID_Entry.text()
		main_Ad = self.Database.Admin_main_id(field)
		Client = self.C_Database.Client_Info(D_ID,main_Ad)
		if SenderName == "Pay_cpnfirm":
			if len(D_ID) == 0:
				self.Pay_Log.setStyleSheet("font-size: 15pt;"
										"font-family: Consolas;"
										"color: red;"
										)
				self.Pay_Log.setText("Field present must be filled")
				print("\a")
			elif Client is False:
				self.Pay_Log.setStyleSheet("font-size: 15pt;"
										"font-family: Consolas;"
										"color: red;"
										)
				self.Pay_Log.setText("The ID entered does not exist")
				print("")
			else:
				B_ID = self.C_Database.BID(D_ID,main_Ad)
				B_ID = B_ID[0]
				self.Pay_Log.setStyleSheet("font-size: 15pt;"
										"font-family: Consolas;"
										"color: Blue;"
										)
				self.Pay_Log.setText("The ID entered is assign to %s" % B_ID)
				self.Pay_cpnfirm.setEnabled(False)
				self.Clear_Pay.setEnabled(True)
				self.Pay_Client_ID.setReadOnly(True)
				self.DisableToolButton()

		elif SenderName == "Clear_Pay":
			B_ID = self.C_Database.BID(D_ID,main_Ad)
			B_ID = B_ID[0]
			PaymentIssue = self.C_Database.Payment(main_Ad,B_ID)
			Payment = PaymentIssue * 100
			if Payment == 0:
				self.Pay_Log.setStyleSheet("font-size: 15pt;"
										"font-family: Consolas;"
										"color: Blue;"
										)
				self.Pay_Log.setText("Sorry you have Nothing to cash out")
				print("\a")
				self.EnableToolButton()
				self.Clear_Pay.setEnabled(False)
				self.Pay_Client_ID.setReadOnly(False)
				self.Pay_Client_ID.clear()
				self.Pay_cpnfirm.setEnabled(True)


			else:
				self.Pay_Log.setStyleSheet("font-size: 15pt;"
											"font-family: Consolas;"
											"color: Blue;"
											)
				self.Pay_Log.setText("Payment earn so far is N%i, Please Click 'Pay' to cash out" % (Payment))
				self.Pay_Button.setEnabled(True)
				self.Clear_Pay.setEnabled(False)

		elif SenderName == "Pay_Button":
			self.EnableToolButton()
			self.Pay_Client_ID.setReadOnly(False)
			self.Pay_Client_ID.clear()
			self.Pay_Button.setEnabled(False)
			self.Pay_cpnfirm.setEnabled(True)
			self.Pay_Log.clear()

		else:
			pass



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	Form = Ui_Form()
	Form.show()
	app.exec_()
	#this codes runs after the app is closed
	#x = Form.Check_O()
	#print(x)
	#print(Ui_Form.Database.Check_Admin(x)