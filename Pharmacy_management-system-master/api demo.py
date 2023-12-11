from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import ttk, messagebox
import mysql.connector

class Pharmacy:
    def __init__(self, root):
        self.root = root
        self.root.title("FormApi")
        self.root.geometry("1350x800+0+0")
        self.root.resizable(False, False)

        #####  VARIABLE ######
        self.Name_variable = StringVar()
        self.Mobile_variable = StringVar()
        self.addmed_variable=StringVar()
        self.email_variable=StringVar()

        # Create database and table
        #conn = mysql.connector.connect(host="localhost",user="root",password="Akash@9458",database="pharmacy")
        #my_cursor = conn.cursor()
        #my_cursor.execute("")
        #self.create_table()

        # Create GUI components
        self.label_name = ttk.Label(root, text="Name:")
        self.entry_name = ttk.Entry(root)

        self.label_mob = ttk.Label(root, text="Mobile:")
        self.entry_mob = ttk.Entry(root)

        self.label_email = ttk.Label(root, text="Email:")
        self.entry_email = ttk.Entry(root)
        
        self.label_add = ttk.Label(root, text="Address:")
        self.entry_add = ttk.Entry(root)

        self.submit_button = ttk.Button(root, text="Submit", command=self.submit_form)
        

  # Grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_name.grid(row=1, column=1, padx=10, pady=10)

        self.label_mob.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_mob.grid(row=2, column=1, padx=10, pady=10)

        self.label_mob.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_mob.grid(row=3, column=1, padx=10, pady=10)

        self.label_add.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_add.grid(row=4, column=1, padx=10, pady=10)

        self.label_add.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entry_add.grid(row=5, column=1, padx=10, pady=10)

        self.label_email.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_email.grid(row=6, column=1, padx=10, pady=10)

        
        self.label_email.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.entry_email.grid(row=7, column=1, padx=10, pady=10)

        self.submit_button.grid(row=8, column=0, columnspan=2, pady=10)
        

 


    """def create_table(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Akash@9458",database="pharmacy")
        cursor.execute("Insert into pharma(Name,Mobile,Address,email) values(%s,%s,%s,%s)", (self.Name_variable=StringVar(),
                                                                                    self.Mobile_variable = StringVar(),
                                                                                    self.addmed_variable=StringVar(),
                                                                                    self.email_variable=StringVar(),
                                                                                    ))
            
        self.conn.commit()
        conn.close()"""

    def submit_form(self):
        name = self.entry_name.get()
        Mobile=self.entry_mobile.get()
        Address=self.entry_address.get()
        email = self.entry_email.get()

        # Insert data into the database
        #cursor = self.conn.cursor()
        #cursor.execute("INSERT INTO forms (name, email) VALUES (?, ?)", (name, email))
        #self.conn.commit()

        # Clear the entry fields after submission
        self.entry_name.delete(0, "end")
        self.entry_mobile.delete(0,"end")
        self.entry_address.delete(0,"end")
        self.entry_email.delete(0, "end")







if __name__ == '__main__':
    root=Tk()
    obj=Pharmacy(root)
    root.mainloop()