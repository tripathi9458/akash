from tkinter import *
from PIL import Image, ImageTk
from tkinter import Button
import random
from tkinter import ttk, messagebox
import mysql.connector

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1350x800+0+0")
        self.root.resizable(False, False)
        self.root.iconbitmap(r"D:/linux/Pharmacy_management-system-master/image/doc.ico")

        ##### ADDMED VARIABLE ######
        self.ref_variable = StringVar()
        self.addemp_variable = StringVar()

        ########## Employee DEPARTMENT VARIABLE #######
        self.Emp_var = StringVar()
        self.companyname_var = StringVar()
        self.Select_ID_Proof = StringVar()
        self.Employee_Name_var = StringVar()
        self.Phone_no = StringVar()
        self.Date_of_Join_var = StringVar()
        self.Type_of_Employee_var = StringVar()
        self.Gender_var = StringVar()
        self.TL_name_var = StringVar()
        self.Date_of_Birth_var = StringVar()
        self.Email_ID_var = StringVar()
        self.Salary_var = StringVar()
        self.Address_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        ######## title animation #########
        self.txt = "Employee MANAGEMENT SYSTEM"
        self.count = 0
        self.text = ""
        self.color = ["green"]
        self.heading = Label(self.root, text=self.txt, font=(
            "times new roman", 30, "bold"), bg='grey', fg="blue", bd=9, relief=RIDGE)
        self.heading.pack(side=TOP, fill=X)
        self.slider()
        self.heading_color()

        # lbltitle=Label(self.root,text=" Employee MANAGEMENT SYSTEM",bd=11,relief=RIDGE
                            # ,bg='#7FFFD4',fg='#0020C2',font=('times new roman',35,'bold'),padx=2,pady=4)
        # lbltitle.pack(side=TOP,fill=X)

        ######### Employee logo label #######
        img1 = Image.open(r"D:/linux/Pharmacy_management-system-master/image/med.jpg")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0, bg='grey')
        b1.place(x=15, y=8)

        ###### Top Frame #####
        topframe = Frame(self.root, bg='grey', bd=10, relief=RIDGE, padx=20)
        topframe.place(x=0, y=62, width=1350, height=400)

        ########  down button frame #######
        down_buttonframe = Frame(
            self.root, bg='grey', bd=10, relief=RIDGE, padx=20)
        down_buttonframe.place(x=0, y=462, width=1350, height=70)

            ###### all buttons ######
        add_button = Button(down_buttonframe, text="Add Employee", command=self.addemp, font=(
            "arial", 12, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.grid(row=0, column=0)

        update_button = Button(down_buttonframe, command=self.update_new, text="Update", font=(
            "arial", 13, "bold"), width=14, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        update_button.grid(row=0, column=1)

        delete_button = Button(down_buttonframe, text="Delete", font=("arial", 13, "bold"), width=13,
                               fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        delete_button.grid(row=0, column=2)

        reset_button = Button(down_buttonframe, text="Reset", command=self.clear_new, font=("arial", 13, "bold"), width=12,
                              fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        reset_button.grid(row=0, column=3)

        exit_button = Button(down_buttonframe, command=self.root.quit, text="Exit", font=(
            "arial", 13, "bold"), width=10, fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        exit_button.grid(row=0, column=4)

        search_by = Label(down_buttonframe, text="Search By", font=(
            "arial", 15, "bold"), fg="black", bg="grey", bd=3, padx=3)
        search_by.grid(row=0, column=5, sticky=W)

        self.search_combo = ttk.Combobox(down_buttonframe, width=12, font=(
            "arial", 13, "bold"), state="readonly", textvariable=self.search_by)
        self.search_combo["values"] = ("Select Options", "Employee No.")
        self.search_combo.grid(row=0, column=6)
        self.search_combo.current(0)

        entry_button = Entry(down_buttonframe, font=("arial", 15, "bold"), fg="black",
                             bg="grey", bd=3, width=12, relief=RIDGE, textvariable=self.search_txt)
        entry_button.grid(row=0, column=7)

        search_button = Button(down_buttonframe, text="Search", font=("arial", 13, "bold"), width=10, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.search_data)
        search_button.grid(row=0, column=8)

        show_button = Button(down_buttonframe, text="Show All", font=("arial", 13, "bold"), fg="white", bg="black",
                             width=10, bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.fetch_new)
        show_button.grid(row=0, column=9)

        ######## left small frame #######
        left_smallframe = LabelFrame(topframe, bg='grey', bd=10, relief=RIDGE,
                                     padx=20, text="Employee ", font=("arial", 13, "bold"), fg="white")
        left_smallframe.place(x=0, y=5, width=820, height=350)

           #### labeling & entry box #########

        # 1

        ref_label = Label(left_smallframe, text=" Employee ID. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        ref_label.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="akash9458", database="Employee")
        my_cursor = conn.cursor()
        my_cursor.execute("Select emp_no from")
        row_01 = my_cursor.fetchall()

        # Extract values from the list and create a tuple
        ref_numbers = [item[0] for item in row_01]
        values_for_combobox = ('Select', *ref_numbers)

        self.ref_combo = ttk.Combobox(left_smallframe, textvariable=self.Emp_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.ref_combo["values"] = values_for_combobox
        self.ref_combo.grid(row=0, column=1)
        self.ref_combo.current(0)

        # 2

        company_label = Label(left_smallframe, text="Company Name  :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        company_label.grid(row=1, column=0)

        self.company_entry = Entry(left_smallframe, textvariable=self.companyname_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.company_entry.grid(row=1, column=1)

        # 3
        # type_label = Label(left_smallframe, text="Select ID  :", padx=2, pady=4, font=(
        #     "times new roman", 13, "bold"), bg="grey")
        # type_label.grid(row=2, column=0, sticky=W)

        self.type_combo = ttk.Combobox(left_smallframe, text="Select ID Proof", width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.type_combo["values"] = (
            " Aadhaar Card  ", "Voter Id", "PAN Card", "Passport")

        # type_label = Label(left_smallframe, text="Select ID  :", padx=2, pady=4, font=(
        #     "times new roman", 13, "bold"), bg="grey")
        # type_label.grid(row=2, column=0, sticky=W)


        self.type_entry = Entry(left_smallframe, textvariable=self.Select_ID_Proof, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.type_entry.grid(row=4, column=1)

        # self.type_Lable = ttk.Combobox(left_smallframe, textvariable=self.Select_ID_Proof, width=22, font=(
        #     "times new roman", 13, "bold"), state="readonly")
        # self.type_Lable["values"] = (
        # self.type_Lable.grid(row=2, column=1)

        # 4

        empname_label = Label(left_smallframe, text="Employee Name :", padx=2, pady=4, font=("times new roman", 13, "bold"), bg="grey")
        empname_label.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="akash9458", database="Employee")
        my_cursor = conn.cursor()
        my_cursor.execute("Select emp_name from Employee")
        row_02 = my_cursor.fetchall()

        # Extract values from the list of tuples and create a tuple
        medicine_names = [item[0] for item in row_02]
        values_for_empname_combobox = ('Select', *medicine_names)

        self.empname_combo = ttk.Combobox(left_smallframe, textvariable=self.Employee_Name_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.empname_combo["values"] = values_for_empname_combobox
        self.empname_combo.grid(row=3, column=1)
        self.empname_combo.current(0)

        # 5

        lot_label = Label(left_smallframe, text=" Phone No. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        lot_label.grid(row=4, column=0)

        self.lot_entry = Entry(left_smallframe, textvariable=self.Phone_no, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.lot_entry.grid(row=4, column=1)

        # 6

        issue_label = Label(left_smallframe, text="Date of Join :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        issue_label.grid(row=5, column=0)

        self.issue_entry = Entry(left_smallframe, textvariable=self.Date_of_Join_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.issue_entry.grid(row=5, column=1)

        # 7

        exp_label = Label(left_smallframe, text="Type of Employee :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        exp_label.grid(row=6, column=0)

        self.exp_entry = Entry(left_smallframe, textvariable=self.Type_of_Employee_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.exp_entry.grid(row=6, column=1)

        # 8

        use_label = Label(left_smallframe, text=" Gender :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        use_label.grid(row=7, column=0)

        self.use_entry = Entry(left_smallframe, textvariable=self.Gender_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.use_entry.grid(row=7, column=1)

        # 9

        sideeffect_label = Label(left_smallframe, text=" TL Name :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        sideeffect_label.grid(row=8, column=0)

        self.sideeffect_entry = Entry(left_smallframe, textvariable=self.TL_name_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.sideeffect_entry.grid(row=8, column=1)

        # 10

        warn_label = Label(left_smallframe, text=" Date of Birth:", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        warn_label.grid(row=9, column=0)

        self.warn_entry = Entry(left_smallframe, textvariable=self.Date_of_Birth_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.warn_entry.grid(row=9, column=1)

        # 11

        Email_ID_label = Label(left_smallframe, text=" Email_ID :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        Email_ID_label.grid(row=0, column=2)

        self.Email_ID_entry = Entry(left_smallframe, textvariable=self.Email_ID_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.Email_ID_entry.grid(row=0, column=3)

        # 12

        price_label = Label(left_smallframe, text="Salary:", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        price_label.grid(row=1, column=2)

        self.price_entry = Entry(left_smallframe, textvariable=self.Salary_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.price_entry.grid(row=1, column=3)

        # 13

        qt_label = Label(left_smallframe, text=" Address :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        qt_label.grid(row=2, column=2)

        self.qt_entry = Entry(left_smallframe, textvariable=self.Address_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.qt_entry.grid(row=2, column=3)

            ######## image in left small frame #####
        # image 1
        # img1 = Image.open(r"D:/linux/Employee_management-system-master/image/med.jpg")
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        # b1 = Button(self.root, image=self.photoimg1, borderwidth=0, bg='grey')
        # b1.place(x=15, y=8)

        self.bg = ImageTk.PhotoImage(file=r"D:/linux/Pharmacy_management-system-master/image/med.jpg")
        lbl_bg = Label(left_smallframe, image=self.bg)
        lbl_bg.place(x=370, y=165, width=200, height=150)
        # image 2
        self.bgg = ImageTk.PhotoImage(file=r"D:/linux/Pharmacy_management-system-master/image/medi.jpg")
        lbl_bgg = Label(left_smallframe, image=self.bgg)
        lbl_bgg.place(x=570, y=165, width=200, height=150)

        # save life label
        save_bgg = Label(left_smallframe, text="----------- Stay Home Stay Safe -----------",
                         font=("arial", 13, "bold"), bg='grey', fg="white")
        save_bgg.place(x=370, y=120, width=400)

        ############ right frame #########
        right_frame = LabelFrame(topframe, bg='grey', bd=10, relief=RIDGE, padx=5,
                                 text="New Employee Add department", font=("arial", 13, "bold"), fg="white")
        right_frame.place(x=846, y=5, width=452, height=350)

          # image & label

        # image 1
        self.bg1 = ImageTk.PhotoImage(file=r"D:/linux/Pharmacy_management-system-master/image/co.jpg")
        lbl_bg1 = Label(right_frame, image=self.bg1)
        lbl_bg1.place(x=0, y=0, width=240, height=100)
        # image 2
        self.bg2 = ImageTk.PhotoImage(file=r"D:/linux/Pharmacy_management-system-master/image/inject.jpg")
        lbl_bg2 = Label(right_frame, image=self.bg2)
        lbl_bg2.place(x=242, y=0, width=180, height=150)

        #### label & entry in right frame ####
        # 1
        no_label = Label(right_frame, text="Employee ID:", font=(
            "times new roman", 11, "bold"), bg="grey")
        no_label.place(x=0, y=105)

        self.no_entry = Entry(right_frame, textvariable=self.ref_variable, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.no_entry.place(x=100, y=105)
        # 2
        med_label = Label(right_frame, text="Employee Name:", font=(
            "times new roman", 11, "bold"), bg="grey")
        med_label.place(x=0, y=130)

        self.med_entry = Entry(right_frame, textvariable=self.addemp_variable, width=16, font=(
            "times new roman", 11, "bold"), bg="white")
        self.med_entry.place(x=100, y=130)

        #### in right frame small frame #####

        newframe = Frame(right_frame, bg='darkgreen', bd=5, relief=RIDGE)
        newframe.place(x=256, y=160, width=150, height=150)

          ###### button in this frame ###
        add_button = Button(newframe, text="Add", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                            bd=3, command=self.AddMed, relief=RIDGE, activebackground="black", activeforeground="white")
        add_button.grid(row=0, column=0)

        updatenew_button = Button(newframe, text="Update", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                                  bd=3, command=self.Update_med, relief=RIDGE, activebackground="black", activeforeground="white")
        updatenew_button.grid(row=1, column=0)

        delnew_button = Button(newframe, text="Delete", font=("arial", 13, "bold"), width=13, fg="white", bg="black",
                               bd=3, relief=RIDGE, activebackground="black", activeforeground="white", command=self.Delete_med)
        delnew_button.grid(row=2, column=0)

        clr_button = Button(newframe, text="Clear", command=self.clear_med, font=("arial", 13, "bold"), width=13,
                            fg="white", bg="black", bd=3, relief=RIDGE, activebackground="black", activeforeground="white")
        clr_button.grid(row=3, column=0)

        ##### scrollbar frame in right frame ####
        side_frame = Frame(right_frame, bd=4, relief=RIDGE, bg="dark green")
        side_frame.place(x=0, y=160, width=250, height=150)

        ### scrollbar code ###

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        self.emp_table = ttk.Treeview(side_frame, column=(
            "empno", "empname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.pack(side=RIGHT, fill=Y)

        sc_x.config(command=self.emp_table.xview)
        sc_y.config(command=self.emp_table.yview)


        self.emp_table.heading("Employeeno", text="Employee No")
        self.emp_table.heading("empname", text="Employee Name")

        self.emp_table["show"] = "headings"
        self.emp_table.pack(fill=BOTH, expand=1)

        self.emp_table.column("Employee No", width=100)
        self.emp_table.column("Employeename", width=100)

        self.emp_table.bind("<ButtonRelease-1>", self.medget_cursor)
        self.fetch_dataemp()

        ######### down frame #######
        down_frame = Frame(self.root, bg='grey', bd=10, relief=RIDGE)
        down_frame.place(x=0, y=522, width=1350, height=212)

        ########## scrollbar in down frame ########
        scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="white")
        scroll_frame.place(x=0, y=0, width=1330, height=192)

        ##### scrollbar code #####
        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.info_table = ttk.Treeview(scroll_frame, column=("Employee no", "comp name", "type", "medi name", "lot no", "issue", "exp",
                                       "uses", "Date of Birth", "warning", "Email_ID", "price", "product"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.info_table.xview)
        scroll_y.config(command=self.info_table.yview)

        self.info_table.heading("Employee no", text="Employee No.")
        self.info_table.heading("comp name", text="Company Name")
        self.info_table.heading("idproof", text="Select ID Proof")
        self.info_table.heading("emp name", text="Employee Name")
        self.info_table.heading("Phone no", text="Phone No.")
        self.info_table.heading("Date of Join", text="Date of Join Date")
        self.info_table.heading("typemp", text=" Type of Employee")
        self.info_table.heading("Gender", text="Gender")
        self.info_table.heading("TL Name", text="TL Name ")
        self.info_table.heading("Date of Brith", text=" Date of Brith")
        self.info_table.heading("Email_ID", text="Email_ID")
        self.info_table.heading("Salray", text="Employeeloyee Salray")
        self.info_table.heading("Address", text="Address.")

        self.info_table["show"] = "headings"
        self.info_table.pack(fill=BOTH, expand=1)

        self.info_table.column("Employee no", width=100)
        self.info_table.column("comp name", width=100)
        self.info_table.column("Selectofproof", width=100)
        self.info_table.column("emp name", width=100)
        self.info_table.column("phone no", width=100)
        self.info_table.column("typeofemp", width=100)
        self.info_table.column("gender", width=100)
        self.info_table.column("gender", width=100)
        self.info_table.column("tlname", width=100)
        self.info_table.column("dob", width=100)
        self.info_table.column("Email_ID", width=100)
        self.info_table.column("salary", width=100)
        self.info_table.column("Address", width=100)

        self.info_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_new()

    ####### MEDICINE ADD FUNCTIONALITY  DECLARATION #######

    def Addemp(self):

        if self.emp_variable.get() == "" or self.addemp_variable.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
            my_cursor = conn.cursor()
            my_cursor.execute("Insert into employee(emp_no,Med_name) values(%s,%s)", (
                                                                                    self.addemp_variable.get(),
                                                                                    self.addemp_variable.get(),
                                                                                    ))

            conn.commit()
            self.fetch_dataemp()
            conn.close()

            messagebox.showinfo("Success", "Employee ADDED")

    def fetch_dataemp(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employee")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.emp_table.delete(*self.emp_table.get_children())

            for i in rows:
                self.emp_table.insert("", END, values=i)

            conn.commit()
            conn.close()

    ###### for show data on click #####

    def medget_cursor(self, event):
        row_id = self.medicineTable.focus()
        content = self.medicineTable.item(row_id)
        print(content)  # Add this line to check the content of the entire row
        row = content['values']
        self.emp_variable.set(row[0])

    def Update_med(self):
        
        if self.emp_variable.get() == "" or self.addemp_variable.get()=="":

            messagebox.showerror("Error", "employee No. and med name is required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
                my_cursor = conn.cursor()

                my_cursor.execute("Update employee set Med_name=%s where emp_no=%s", (
                                                                                self.addemp_variable.get(),
                                                                                self.emp_variable.get(),
                                                                                ))

                conn.commit()
                messagebox.showinfo("Update", "Successfully Updated", parent=self.root)
                self.fetch_dataemp()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)




    def Delete_med(self):
        if self.emp_variable.get()=="":
            messagebox.showerror("Error","employee no is required",parent=self.root)
        else:

            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
                my_cursor=conn.cursor()
            
                my_cursor.execute("Delete from employee where Ref_no=%s ",(self.emp_variable.get(),))
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                self.fetch_dataemp()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)

        

    def clear_med(self):
        self.ref_variable.set("")
        self.addemp_variable.set("")
        
    

    

    ######## Employee DEPARTMENT FUNCTIONALITY #######
    def addemp(self):
        if self.Emp_var.get() == "" or self.Phone_no.get() == "" or self.Select_ID_Proof.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
            new_cursor=conn.cursor()
            new_cursor.execute("INSERT INTO Employee (Emp No, COMPANY_NAME, Select_ID_Proof,Employe Name, Phone_no, Date_of_Join, Type_of_Employee, Gender,TL_name , Date_of_Birth, Email_ID,Salary_var , Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
            self.Emp_var.get(),
            self.companyname_var.get(),
            self.Select_ID_Proof.get(),
            self.Employee_Name_var.get(),
            self.Phone_no.get(),
            self.Date_of_Join_var.get(),
            self.Type_of_Employee_var.get(),
            self.Gender_var.get(),
            self.TL_name_var.get(),
            self.Date_of_Birth_var.get(),
            self.Email_ID_var.get(),
            self.Salary_var.get(),
            self.Address_var.get(),
            ))
            conn.commit()
            self.fetch_new()
            
            messagebox.showinfo("Success","Successfully added")

    def fetch_new(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
        new_cursor=conn.cursor()
        new_cursor.execute("select * from Employee")
        row=new_cursor.fetchall()

        if len(row)!=0:
            self.info_table.delete(*self.info_table.get_children())

            for i in row:
                self.info_table.insert("",END,values=i)

            conn.commit()
        
    
    def get_cursor(self,event=""):
        cursor_row=self.info_table.focus()
        content=self.info_table.item(cursor_row)
        row=content["values"]
        self.Emp_var.set(row[0])
        self.companyname_var.set(row[1])
        self.Select_ID_Proof.set(row[2])
        self.Employee_Name_var.set(row[3])
        self.Phone_no.set(row[4])
        self.Date_of_Join_var.set(row[5])
        self.Type_of_Employee_var.set(row[6])
        self.Gender_var.set(row[7])
        self.Date_of_Birth_var.set(row[8])
        self.Date_of_Birth_var.set(row[9])
        self.Email_ID_var.set(row[10])
        self.Salary_var.set(row[11])
        self.Address_var.set(row[12])

    def update_new(self):
        
        if self.Emp_var.get() == "" or self.Phone_no.get() == "" or self.Select_ID_Proof.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
            new_cursor=conn.cursor()
            new_cursor.execute("Update Employee set COMPANY_NAME=%s,idproof=%s,empname=%s,Phoneno=%s,doj=%s,typeofemp=%s,gender=%s,tlname=%s,dob=%s,email=%s,salary=%s,Address=%s, where Emp_NO=%s",(
                                                                                               
            self.companyname_var.get(),
            self.Select_ID_Proof.get(),
            self.Employee_Name_var.get(),
            self.Phone_no.get(),
            self.Date_of_Join_var.get(),
            self.Type_of_Employee_var.get(),
            self.Gender_var.get(),
            self.TL_name_var.get(),
            self.Date_of_Birth_var.get(),
            self.Email_ID_var.get(),
            self.Salary_var.get(),
            self.Address_var.get(),
            self.Emp_var.get(),

            ))
            conn.commit()
            self.fetch_new()
            
            self.clear_new()
            messagebox.showinfo("Success","Successfully updated")

    def clear_new(self):
        self.Emp_var.set("")
        self.companyname_var.set("")
        self.Select_ID_Proof.set("")
        self.Employee_Name_var.set("")
        self.Phone_no.set("")
        self.Date_of_Join_var.set("")
        self.Type_of_Employee_var.set("")
        self.Gender_var.set("")
        self.Date_of_Birth_var.set("")
        self.Date_of_Birth_var.set("")
        self.Email_ID_var.set("")
        self.Salary_var.set("")
        self.Address_var.set("")
    

    def search_data(self):

        conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="Employee")
        new_cursor=conn.cursor()
        selected = self.search_combo.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option")

        else:
            new_cursor.execute("Select * from Employee where Emp_NO=%s",(self.search_txt.get(),))
            row=new_cursor.fetchone()

            if len(row)!=0:
                self.info_table.delete(*self.info_table.get_children())

                for i in row:
                    self.info_table.insert("",END,values=i)

                conn.commit()


    def slider(self):
            if self.count >= len(self.txt):
                self.count = -1
                self.text = ""
                self.heading.config(text=self.text)
            else:
                self.text += self.txt[self.count]
                self.heading.config(text=self.text)
                self.count += 1
                self.heading.after(150, self.slider)
    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(100,self.heading_color)

    # def bind2(self):
    #         self.root.destroy()
    #         import bind2

if __name__ == '__main__':

    root=Tk()
    obj=Employee(root)
    root.mainloop()
