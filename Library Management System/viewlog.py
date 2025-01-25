import customtkinter as ctk
import mysql.connector as myc
from tkinter import messagebox
from tkinter import ttk
 
conn = myc.connect(host = "localhost",
                     user= "root", 
                     password= "",
                     database = "")

def view_log():
    window7 = ctk.CTk()
    window7.geometry("1548x900+1+1")
    window7.title("Library Mangement System-- View Log")
    window7.configure(fg_color ="#8770C9")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    def search_logic(event = None):
        drop = dropdown.get()
        search = search_entry.get() + "%"
        mycur = conn.cursor()

        if drop =="All":
            query = "SELECT * FROM transaction WHERE book_id LIKE %s OR book_name LIKE %s OR student_id LIKE %s OR librarian_id LIKE %s"
            data = (search,search,search,search)
            mycur.execute(query, data)
        elif drop == "Book ID":
            query = "SELECT * FROM transaction WHERE book_id LIKE %s"
            data= (search,)
            mycur.execute(query, data)
        elif drop == "Book Name":
            query = "SELECT * FROM transaction WHERE book_name LIKE %s"
            data = (search,)
            mycur.execute(query, data)
        elif drop == "Student Id":
            query = "SELECT * FROM transaction WHERE student_id LIKE %s"
            data = (search,)
            mycur.execute(query, data)
        else:
            messagebox.showinfo("Error", "Invalid Request")


        tree.delete(*tree.get_children())

        rows = mycur.fetchall()
        for row in rows:
            tree.insert("", 'end', values=row)

        mycur.close()
    
    #heading
    headingframe1 = ctk.CTkFrame(window7, fg_color="#D3D3D3", height= 110, width= 1548)
    headingframe1.place(x=0,y=0)

    headinglabel1 = ctk.CTkLabel(headingframe1, text= "LIBRARY MANAGEMENT SYSTEM",
                                 text_color="black",
                           font=("Helvetica", 50,"bold"),
                           fg_color="#D3D3D3")
    headinglabel1.place(x=360,y=30)

    #main frame
    frame = ctk.CTkFrame(window7,
                     fg_color= "#D3D3D3",
                       height=560,
                       width= 1200, 
                     corner_radius=50)
    frame.place(x=170, y=160)

    #frame contents
    label1 = ctk.CTkLabel(frame, text="*VIEW LOG*",
                          fg_color="#D3D3D3",
                      text_color="black",
                      
                      font=("Helvetica", 30))
    label1.place(x=510,y=20)

    searchBY_label = ctk.CTkLabel(frame,text="SEARCH BY: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    searchBY_label.place(x=40,y=100)

    options = ["All","Book ID", "Book Name",  "Student Id"]
    dropdown = ctk.CTkOptionMenu(frame, values=options,width=150,corner_radius=10 ,height=25, fg_color= "#2B2B2B",bg_color="#D3D3D3")
    dropdown.place(x= 200, y=100)
    dropdown.set("All")


    search_label = ctk.CTkLabel(frame,text="SEARCH QUERY: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    search_label.place(x=400,y=100)

    search_entry = ctk.CTkEntry(frame,
                            placeholder_text="Enter elements to search",
                            width=200,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",)
    search_entry.place(x=600, y=100)

    search_entry.bind("<KeyRelease>", search_logic)

    btn = ctk.CTkButton(frame,text="SEARCH",
                    height=20,
                    width=100,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= search_logic
                    )

    btn.place(x=830, y=100)



    #Tree view

    tree = ttk.Treeview(frame, show= "headings", height=15)
    tree['columns'] = ("book_id", "book_name", "student_id","librarian_id" ,"issued_date","due_date","return_date","status")

    
    tree.column("book_id", width=50)
    tree.column("book_name", width=150)
    tree.column("student_id", width=150)
    tree.column("librarian_id", width=150)
    tree.column("issued_date", width=150)
    tree.column("due_date", width=150)
    tree.column("return_date", width=150)
    tree.column("status", width=100)

#heading

    
    tree.heading("book_id",text="Book ID")
    tree.heading("book_name", text="Book Name")
    tree.heading("student_id", text="Student ID")
    tree.heading("librarian_id", text="Librarian ID")
    tree.heading("issued_date", text="Issued Date")
    tree.heading("due_date", text="Due Date")
    tree.heading("return_date", text="Return Date")
    tree.heading("status", text="Status")

    tree.place(x= 225, y= 250)

    tree.delete(*tree.get_children())
    mycur = conn.cursor()
    mycur.execute("SELECT * FROM transaction;")  # Update table name and query as needed
    rows = mycur.fetchall()
    for row in rows:
        tree.insert("", 'end', values=row)
    conn.commit()    
    mycur.close()

    window7.mainloop()

