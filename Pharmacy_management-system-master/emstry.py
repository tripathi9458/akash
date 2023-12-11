from tkinter import *
from PIL import Image, ImageTk
from tkinter import Button
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import mysql.connector

class Pharmacy:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1350x800+0+0")
        self.root.resizable(False, False)
        self.root.iconbitmap(r"D:/linux/Pharmacy_management-system-master/image/doc.ico")

        ##### addemp VARIABLE ######
        self.emp_variable = StringVar()
        self.addemp_variable = StringVar()

        ########## EMPLOYEE DEPARTMENT VARIABLE #######
        self.empno_var = StringVar()
        self.companyname_var = StringVar()
        self.Type_of_employe_var = StringVar()
        self.Employee_var = StringVar()
        self.Phoneno_var = StringVar()
        self.Department_var = StringVar()
        self.Joining_var = StringVar()
        self.Email_Id_var = StringVar()
        self.Gender_var = StringVar()
        self.dob_var = StringVar()
        self.TLname_var = StringVar()
        self.Salary_var = StringVar()
        self.Address_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        ######## title animation #########
        self.txt = "EMPLOYEE MANAGEMENT SYSTEM"
        self.count = 0
        self.text = ""
        self.color = ["green"]
        self.heading = Label(self.root, text=self.txt, font=(
            "times new roman", 30, "bold"), bg='grey', fg="blue", bd=9, relief=RIDGE)
        self.heading.pack(side=TOP, fill=X)
        self.slider()
        self.heading_color()

        # lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=11,relief=RIDGE
                            # ,bg='#7FFFD4',fg='#0020C2',font=('times new roman',35,'bold'),padx=2,pady=4)
        # lbltitle.pack(side=TOP,fill=X)

        ######### employee logo label #######
        img1 = Image.open(r"D:/linux/Pharmacy_management-system-master/image/med.jpg")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0, bg='grey')
        b1.place(x=15, y=8)

        ###### Top Frame #####
        topframe = Frame(self.root, bg='grey', bd=10, relief=RIDGE, padx=20)
        topframe.place(x=0, y=62, width=1350, height=740)

        ########  down button frame #######
        down_buttonframe = Frame(
            self.root, bg='grey', bd=10, relief=RIDGE, padx=20)
        down_buttonframe.place(x=12, y=462, width=1330, height=60)

            ###### all buttons ######
        add_button = Button(down_buttonframe, text="Add Employee", command=self.addEmployee, font=(
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
        self.search_combo["values"] = ("Select Options", "Emp No.")
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
                                     padx=20, text="Employee Information", font=("arial", 13, "bold"), fg="white")
        left_smallframe.place(x=0, y=5, width=820, height=350)

           #### labeling & entry box #########

        # 1

        emp_label = Label(left_smallframe, text="Employee No. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        emp_label.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="akash9458", database="employee")
        my_cursor = conn.cursor()
        my_cursor.execute("Select Emp_No from emp")
        row_01 = my_cursor.fetchall()

        # Extract values from the list and create a tuple
        emp_numbers = [item[0] for item in row_01]
        values_for_combobox = ('Select', *emp_numbers)

        self.emp_combo = ttk.Combobox(left_smallframe, textvariable=self.empno_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.emp_combo["values"] = values_for_combobox
        self.emp_combo.grid(row=0, column=1)
        self.emp_combo.current(0)

        # 2

        company_label = Label(left_smallframe, text="ID Proof :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        company_label.grid(row=1, column=0)

        self.company_entry = Entry(left_smallframe, textvariable=self.companyname_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.company_entry.grid(row=1, column=1)

        # 3
        type_label = Label(left_smallframe, text="Company Name :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        type_label.grid(row=2, column=0, sticky=W)

        self.type_combo = ttk.Combobox(left_smallframe, textvariable=self.Type_of_employe_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.type_combo["values"] = (
            "Select"," Intern  ", "Contactor", "Employee", "Manager", "Manter")
        self.type_combo.grid(row=2, column=1)
        self.type_combo.current(0)

        # 4

        empname_label = Label(left_smallframe, text="Employee Name :", padx=2, pady=4, font=("times new roman", 13, "bold"), bg="grey")
        empname_label.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", user="root", password="akash9458", database="employee")
        my_cursor = conn.cursor()
        my_cursor.execute("Select Emp_name from emp")
        row_02 = my_cursor.fetchall()

        # Extract values from the list of tuples and create a tuple
        Employee_names = [item[0] for item in row_02]
        values_for_empname_combobox = ('Select', *Employee_names)

        self.empname_combo = ttk.Combobox(left_smallframe, textvariable=self.Employee_var, width=22, font=(
            "times new roman", 13, "bold"), state="readonly")
        self.empname_combo["values"] = values_for_empname_combobox
        self.empname_combo.grid(row=3, column=1)
        self.empname_combo.current(0)

        # 5

        Phone_label = Label(left_smallframe, text=" Phone_no. :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        Phone_label.grid(row=4, column=0)

        self.Phone_entry = Entry(left_smallframe, textvariable=self.Phoneno_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.Phone_entry.grid(row=4, column=1)

        # 6

        Department_label = Label(left_smallframe, text="Gender :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        Department_label.grid(row=5, column=0)

        self.Department_entry = Entry(left_smallframe, textvariable=self.Department_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.Department_entry.grid(row=5, column=1)

        # 7

        Joining_label = Label(left_smallframe, text="Department:", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        Joining_label.grid(row=6, column=0)

        self.Joining_entry = Entry(left_smallframe, textvariable=self.Joining_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.Joining_entry.grid(row=6, column=1)

        # 8

        use_label = Label(left_smallframe, text="Date of Birth :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        use_label.grid(row=7, column=0)

        self.use_entry = Entry(left_smallframe, textvariable=self.Email_Id_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.use_entry.grid(row=7, column=1)

        # 9

        Gender_label = Label(left_smallframe, text="Email ID :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        Gender_label.grid(row=8, column=0)

        self.Gender_entry = Entry(left_smallframe, textvariable=self.Gender_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.Gender_entry.grid(row=8, column=1)

        # 10

        warn_label = Label(left_smallframe, text="Date of Joining:", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        warn_label.grid(row=9, column=0)

        self.warn_entry = Entry(left_smallframe, textvariable=self.dob_var, width=24, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.warn_entry.grid(row=9, column=1)

        # 11

        TLname_label = Label(left_smallframe, text="TL Name :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        TLname_label.grid(row=0, column=2)

        self.TLname_entry = Entry(left_smallframe, textvariable=self.TLname_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.TLname_entry.grid(row=0, column=3)

        # 12

        Salary_label = Label(left_smallframe, text="Salary :", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        Salary_label.grid(row=1, column=2)

        self.Salary_entry = Entry(left_smallframe, textvariable=self.Salary_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.Salary_entry.grid(row=1, column=3)

        # 13

        qt_label = Label(left_smallframe, text="Address:", padx=2, pady=4, font=(
            "times new roman", 13, "bold"), bg="grey")
        qt_label.grid(row=2, column=2)

        self.qt_entry = Entry(left_smallframe, textvariable=self.Address_var, width=28, font=(
            "times new roman", 13, "bold"), fg="black", bg="white")
        self.qt_entry.grid(row=2, column=3)

            ######## image in left small frame #####
        # image 1
        # img1 = Image.open(r"D:/linux/employee_management-system-master/image/med.jpg")
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
                                 text="New Empolyee Add department", font=("arial", 13, "bold"), fg="white")
        right_frame.place(x=846, y=5, width=452, height=350)

          # image & label

        # image 1
        self.bg1 = ImageTk.PhotoImage(file=r"D:/linux/Pharmacy_management-system-master/image/co.jpg")
        lbl_bg1 = Label(right_frame, image=self.bg1)
        lbl_bg1.place(x=0, y=0, width=240, height=100)
        # image 2
        self.bg2 = ImageTk.PhotoImage(file=r"D:/linux/Pharmacy_management-system-master/image/inject.jpg")
        lbl_bg2 = Label(right_frame, image=self.bg2)
        lbl_bg2.place(x=242, y=0, width=180, height=170)

        #### label & entry in right frame ####
        # 1
        no_label = Label(right_frame, text="Empolyee No:", font=(
            "times new roman", 11, "bold"), bg="grey")
        no_label.place(x=0, y=105)

        self.no_entry = Entry(right_frame, textvariable=self.emp_variable, width=16, font=(
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
                            bd=3, command=self.addemp, relief=RIDGE, activebackground="black", activeforeground="white")
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
        self.Employee_table = ttk.Treeview(side_frame, column=(
            "empno", "empname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.pack(side=RIGHT, fill=Y)

        sc_x.config(command=self.Employee_table.xview)
        sc_y.config(command=self.Employee_table.yview)


        self.Employee_table.heading("empno", text="Emp No.")
        self.Employee_table.heading("empname", text="Employee Name")

        self.Employee_table["show"] = "headings"
        self.Employee_table.pack(fill=BOTH, expand=1)

        self.Employee_table.column("empno", width=100)
        self.Employee_table.column("empname", width=100)

        self.Employee_table.bind("<ButtonRelease-1>", self.medget_cursor)
        self.fetch_datamed()

        ######### down frame #######
        down_frame = Frame(self.root, bg='grey', bd=10, relief=RIDGE)
        down_frame.place(x=10, y=522, width=1330, height=270)

        ########## scrollbar in down frame ########
        scroll_frame = Frame(down_frame, bd=2, relief=RIDGE, bg="white")
        scroll_frame.place(x=0, y=0, width=1310, height=250)

        ##### scrollbar code #####
        scroll_x = ttk.Scrollbar(scroll_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(scroll_frame, orient=VERTICAL)
        self.emp_table = ttk.Treeview(scroll_frame, column=("emp no", "companyname", "Type_of_employee", "employee_name", "Phone_no", "Department", "Joining",
                                       "Email-Id", "Gender", "Date of Birth", "TLname", "Salary", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.emp_table.xview)
        scroll_y.config(command=self.emp_table.yview)

        self.emp_table.heading("emp no", text="Emp No.")
        self.emp_table.heading("companyname", text="Company Name")
        self.emp_table.heading("Type_of_employee", text="Type Of Employee")
        self.emp_table.heading("employee_name", text="Employee Name")
        self.emp_table.heading("Phone_no", text="Phone No.")
        self.emp_table.heading("Department", text="Department ")
        self.emp_table.heading("Joining", text="Joining")
        self.emp_table.heading("Email_Id", text="Email-Id")
        self.emp_table.heading("Gender", text="Gender")
        self.emp_table.heading("dob", text="dob")
        self.emp_table.heading("TLname", text="TLname")
        self.emp_table.heading("Salary", text=" Salary")
        self.emp_table.heading("Address", text="Address:")

        self.emp_table["show"] = "headings"
        self.emp_table.pack(fill=BOTH, expand=1)

        self.emp_table.column("emp no", width=100)
        self.emp_table.column("companyname", width=100)
        self.emp_table.column("Type_of_employee", width=100)
        self.emp_table.column("employee_name", width=100)
        self.emp_table.column("Phone_no", width=100)
        self.emp_table.column("Department", width=100)
        self.emp_table.column("Joining", width=100)
        self.emp_table.column("Email-Id", width=100)
        self.emp_table.column("Gender", width=100)
        self.emp_table.column("dob", width=100)
        self.emp_table.column("TLname", width=100)
        self.emp_table.column("Salary", width=100)
        self.emp_table.column("Address", width=100)

        self.emp_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_new()

    ####### Employee ADD FUNCTIONALITY  DECLARATION #######

    def addemp(self):

        if self.emp_variable.get() == "" or self.addemp_variable.get() == "":
            messagebox.showerror("Error", "All fields are required")

        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
            my_cursor = conn.cursor()
            my_cursor.execute("Insert into emp(Emp_No,Emp_name) values(%s,%s)", (
                                                                                    self.emp_variable.get(),
                                                                                    self.addemp_variable.get(),
                                                                                    ))

            conn.commit()
            self.fetch_datamed()
            conn.close()

            messagebox.showinfo("Success", "EMPLOYEE ADDED")

    def fetch_datamed(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from emp")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Employee_table.delete(*self.Employee_table.get_children())

            for i in rows:
                self.Employee_table.insert("", END, values=i)

            conn.commit()
            conn.close()

    ###### for show data on click #####

    def medget_cursor(self, event):
        row_id = self.EmployeeTable.focus()
        content = self.EmployeeTable.item(row_id)
        print(content)  # Add this line to check the content of the entire row
        row = content['values']
        self.emp_variable.set(row[0])

    def Update_med(self):
        
        if self.emp_variable.get() == "" or self.addemp_variable.get()=="":

            messagebox.showerror("Error", "Emp No. and med name is required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
                my_cursor = conn.cursor()

                my_cursor.execute("Update emp set Emp_name=%s where Emp_No=%s", (
                                                                                self.addemp_variable.get(),
                                                                                self.emp_variable.get(),
                                                                                ))

                conn.commit()
                messagebox.showinfo("Update", "Successfully Updated", parent=self.root)
                self.fetch_datamed()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)




    def Delete_med(self):
        if self.emp_variable.get()=="":
            messagebox.showerror("Error","Emp no is required",parent=self.root)
        else:

            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
                my_cursor=conn.cursor()
            
                my_cursor.execute("Delete from emp where Emp_No=%s ",(self.emp_variable.get(),))
                conn.commit()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
                self.fetch_datamed()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to:{str(e)}",parent=self.root)

        

    def clear_med(self):
        self.emp_variable.set("")
        self.addemp_variable.set("")
        
    

    

    ######## EMPLOYEE DEPARTMENT FUNCTIONALITY #######
    def addEmployee(self):
        if self.empno_var.get() == "" or self.Phoneno_var.get() == "" or self.Type_of_employe_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
            new_cursor=conn.cursor()
            new_cursor.execute("INSERT INTO employee (Emp_No, COMPANY_NAME, Type_of_employee, Emp_name, Phone_NO, Department, Joining, Email-Id, Gender, dob, TLname, Salary, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (
            self.empno_var.get(),
            self.companyname_var.get(),
            self.Type_of_employe_var.get(),
            self.Employee_var.get(),
            self.Phoneno_var.get(),
            self.Department_var.get(),
            self.Joining_var.get(),
            self.Email_Id_var.get(),
            self.Gender_var.get(),
            self.dob_var.get(),
            self.TLname_var.get(),
            self.Salary_var.get(),
            self.Address_var.get(),
            ))
            conn.commit()
            self.fetch_new()
            
            messagebox.showinfo("Success","Successfully added")

    def fetch_new(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
        new_cursor=conn.cursor()
        new_cursor.execute("select * from Information")
        row=new_cursor.fetchall()

        if len(row)!=0:
            self.emp_table.delete(*self.emp_table.get_children())

            for i in row:
                self.emp_table.insert("",END,values=i)

            conn.commit()
        
    
    def get_cursor(self,event=""):
        cursor_row=self.emp_table.focus()
        content=self.emp_table.item(cursor_row)
        row=content["values"]
        self.empno_var.set(row[0])
        self.companyname_var.set(row[1])
        self.Type_of_employe_var.set(row[2])
        self.Employee_var.set(row[3])
        self.Phoneno_var.set(row[4])
        self.Department_var.set(row[5])
        self.Joining_var.set(row[6])
        self.Email_Id_var.set(row[7])
        self.Gender_var.set(row[8])
        self.dob_var.set(row[9])
        self.TLname_var.set(row[10])
        self.Salary_var.set(row[11])
        self.Address_var.set(row[12])

    def update_new(self):
        
        if self.empno_var.get() == "" or self.Phoneno_var.get() == "" or self.Type_of_employe_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
            new_cursor=conn.cursor()
            new_cursor.execute("Update employee set COMPANY_NAME=%s,Type_of_employee=%s,EMPNAME=%s,Phone_NO=%s,Department=%s,Joining=%s,Email-Id=%s,Gender=%s,dob=%s,TLname=%s,Salary=%s,Address=%s where Emp_No=%s",(
                                                                                               
            self.companyname_var.get(),
            self.Type_of_employe_var.get(),
            self.Employee_var.get(),
            self.Phoneno_var.get(),
            self.Department_var.get(),
            self.Joining_var.get(),
            self.Email_Id_var.get(),
            self.Gender_var.get(),
            self.dob_var.get(),
            self.TLname_var.get(),
            self.Salary_var.get(),
            self.Address_var.get(),
            self.empno_var.get(),

            ))
            conn.commit()
            self.fetch_new()
            
            self.clear_new()
            messagebox.showinfo("Success","Successfully updated")

    def clear_new(self):
        self.empno_var.set("")
        self.companyname_var.set("")
        self.Type_of_employe_var.set("")
        self.Employee_var.set("")
        self.Phoneno_var.set("")
        self.Department_var.set("")
        self.Joining_var.set("")
        self.Email_Id_var.set("")
        self.Gender_var.set("")
        self.dob_var.set("")
        self.TLname_var.set("")
        self.Salary_var.set("")
        self.Address_var.set("")
    

    def search_data(self):

        conn=mysql.connector.connect(host="localhost",user="root",password="akash9458",database="employee")
        new_cursor=conn.cursor()
        selected = self.search_combo.get()
        if selected == "Select Options":
            messagebox.showerror("Error","You have to choose an option")

        else:
            new_cursor.execute("Select * from employee where Emp_No=%s",(self.search_txt.get(),))
            row=new_cursor.fetchone()

            if len(row)!=0:
                self.emp_table.delete(*self.emp_table.get_children())

                for i in row:
                    self.emp_table.insert("",END,values=i)

                conn.commit()


    def slider(self):
        if self.count>=len(self.txt):
            self.count=-1
            self.text=""
            self.heading.config(text=self.text)
        else:
            self.text=self.text+self.txt[self.count]
            self.heading.config(text=self.text)
        self.count+=1
        self.heading.after(200,self.slider)

    def heading_color(self):
        fg=random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(100,self.heading_color)

    # def bind2(self):
    #         self.root.destroy()
    #         import bind2

if __name__ == '__main__':

    root=Tk()
    obj=Pharmacy(root)
    root.mainloop()
