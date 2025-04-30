from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.NameOfTablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NoOfTablet = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.BloodPressure = StringVar()
        self.Storage = StringVar()
        self.Medication = StringVar()
        self.PatientId = StringVar()
        self.NhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
        
        lbltitle = Label(self.root,bd=20,relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",fg="red", font=("times new roman", 50, "bold"), bg="white")
        lbltitle.pack(side=TOP, fill=X)
        
        #======================DataFrame==============================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)
        
        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, text="Patient Information", font=("times new roman", 12, "bold"))
        DataframeLeft.place(x=0, y=5, width=980, height=350)
        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, text="Prescription", font=("times new roman", 12, "bold"))
        DataframeRight.place(x=990, y=5, width=460, height=350)
        
        #=============Button Frame ================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)
        
        #=============Details frame ================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)
        
        #======================DataframeLeft==============================
        lblNameTablet = Label(DataframeLeft,text="Names OF Tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0 ,sticky=W)
        
        comNameTablet = ttk.Combobox(DataframeLeft, textvariable=self.NameOfTablets,state="readonly", font=("arival", 12, "bold"), width=33)
        
        comNameTablet['value'] = ("Nice","Corona Vacancie","Acetaminophen","Adderall","Amlodipine","Activan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)
        
        lblref = Label(DataframeLeft, text="Ref No.", font=("arial", 12, "bold"), padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)
        
        lblDose = Label(DataframeLeft, text="Dose", font=("arial", 12, "bold"), padx=2,pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)
        
        lblNoOfTablet = Label(DataframeLeft, text="No Of Tablet", font=("arial", 12, "bold"), padx=2,pady=6)
        lblNoOfTablet.grid(row=3, column=0, sticky=W)
        txtNoOfTablet = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtNoOfTablet.grid(row=3, column=1)
        
        lblLot = Label(DataframeLeft, text="Lot No.", font=("arial", 12, "bold"), padx=2,pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtLot.grid(row=4, column=1)
        
        lblissueDate = Label(DataframeLeft, text="Issue Date", font=("arial", 12, "bold"), padx=2,pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtissueDate.grid(row=5, column=1)
        
        lblExpDate = Label(DataframeLeft, text="Exp Date", font=("arial", 12, "bold"), padx=2,pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)
        
        lblDailyDose = Label(DataframeLeft, text="Daily Dose", font=("arial", 12, "bold"), padx=2,pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)
        
        lblSideEffect = Label(DataframeLeft, text="Side Effect", font=("arial", 12, "bold"), padx=2,pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 13, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)
        
        lblFurtherInfo = Label(DataframeLeft, text="Further Information", font=("arial", 12, "bold"), padx=2)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtFurtherInfo.grid(row=0, column=3)
        
        lblBloodPressure = Label(DataframeLeft, text="Blood Pressure", font=("arial", 12, "bold"), padx=2,pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)
        
        lblStorage = Label(DataframeLeft, text="Storage Advice:", font=("arial", 12, "bold"), padx=2,pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtStorage.grid(row=2, column=3)
        
        lblMedicine = Label(DataframeLeft, text="Medication", font=("arial", 12, "bold"), padx=2,pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtMedicine.grid(row=3, column=3,sticky=W)
        
        lblPatientId = Label(DataframeLeft, text="Patient Id", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)
        
        lblNhsNumber = Label(DataframeLeft, text="NHS Number", font=("arial", 12, "bold"), padx=2,pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtNhsNumber.grid(row=5, column=3)
        
        lblPatientname = Label(DataframeLeft, text="Patient Name", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtPatientname.grid(row=6, column=3)
        
        lblDateOfBirth = Label(DataframeLeft, text="Date Of Birth", font=("arial", 12, "bold"), padx=2,pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtDateOfBirth.grid(row=7, column=3)
        
        lblPatientAddress = Label(DataframeLeft, text="Patient Address", font=("arial", 12, "bold"), padx=2,pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("arial", 12, "bold"), width=35)
        txtPatientAddress.grid(row=8, column=3)
        
        
        
        
        
        
        #====================DataframeRight=========================
        
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=46, height=16,padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)
        
        #====================Button=========================
        btnPrescription = Button(Buttonframe, text="Prescription", font=("arial", 12, "bold"),padx=16, pady=10, width=23, bg="green", fg="white")
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", font=("arial", 12, "bold"),padx=16, pady=10, width=23, bg="green", fg="white")
        btnPrescriptionData.grid(row=0, column=1)
        
        btnUpdate = Button(Buttonframe, text="Update", font=("arial", 12, "bold"),padx=16, pady=10, width=23, bg="green", fg="white")
        btnUpdate.grid(row=0, column=2)
        
        btnDelete = Button(Buttonframe, text="Delete", font=("arial", 12, "bold"),padx=16, pady=10, width=23, bg="green", fg="white")
        btnDelete.grid(row=0, column=3)
        
        btnClear = Button(Buttonframe, text="Clear", font=("arial", 12, "bold"),padx=16, pady=10, width=23, bg="green", fg="white")
        btnClear.grid(row=0, column=4)
        
        btnExit = Button(Buttonframe, text="Exit", font=("arial", 12, "bold"),padx=16, pady=10, width=23, bg="green", fg="white")
        btnExit.grid(row=0, column=5)
        
        
        #====================Table=========================
        #====================Scrollbar=========================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameOftablets","ref",  "dose", "no_of_tablet", "lot", "issue_date", "exp_date", "daily_dose", "storage_advice",  "nhs_number", "patient_name", "date_of_birth", "patient_address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameOftablets", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Ref No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("no_of_tablet", text="No Of Tablet")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issue_date", text="Issue Date")
        self.hospital_table.heading("exp_date", text="Exp Date")
        self.hospital_table.heading("daily_dose", text="Daily Dose")
        self.hospital_table.heading("storage_advice", text="Storage")
        self.hospital_table.heading("nhs_number", text="NHS Number")
        self.hospital_table.heading("patient_name", text="Patient Name")
        self.hospital_table.heading("date_of_birth", text="Date Of Birth")
        self.hospital_table.heading("patient_address", text="Patient Address")
        self.hospital_table['show'] = 'headings'
        
        self.hospital_table.column("nameOftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("no_of_tablet", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issue_date", width=100)
        self.hospital_table.column("exp_date", width=100)
        self.hospital_table.column("daily_dose", width=100)
        self.hospital_table.column("storage_advice", width=100)
        self.hospital_table.column("nhs_number", width=100)
        self.hospital_table.column("patient_name", width=100)
        self.hospital_table.column("date_of_birth", width=100)
        self.hospital_table.column("patient_address", width=100)
        
        self.hospital_table.pack(fill=BOTH, expand=1)
        
        def iPrescriptionData(self):
          if self.NameOfTablets.get() == "" or self.Ref.get() == "":
             messagebox.showerror("Error", "All fields are required")
          else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Chamodi@2003", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.NameOfTablets.get(),
            self.Ref.get(),
            self.Dose.get(),
            self.NoOfTablet.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.Storage.get(),
            self.NhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get()
        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")


            
            

# ✅ This must be outside the class!
if __name__ == "__main__":
    root = Tk()
    ob = Hospital(root)
    root.mainloop()
