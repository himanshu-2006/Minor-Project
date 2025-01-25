import customtkinter as ctk
import mysql.connector as myc
from tkinter import messagebox
from tkinter import ttk

from update import update_books
 
conn = myc.connect(host = "localhost",
                     user= "root", 
                     password= "",
                     database = "")

def view_books():
    window6 = ctk.CTk()
    window6.geometry("1548x900+0+0")
    window6.title("Library Mangement System-- View Books")
    window6.configure(fg_color ="#8770C9")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def searchS_logic(event = None):
        drop = dropdown.get()
        search = search_entry.get() + "%"
        mycur = conn.cursor()

        if drop =="All":
            query = "SELECT * FROM books WHERE book_id LIKE %s OR title LIKE %s OR author LIKE %s"
            data = (search, search, search)
            mycur.execute(query, data)
        elif drop == "Book ID":
            query = "SELECT * FROM books WHERE book_id LIKE %s"
            data= (search,)
            mycur.execute(query, data)
        elif drop == "Book Name":
            query = "SELECT * FROM books WHERE title LIKE %s"
            data = (search,)
            mycur.execute(query, data)
        elif drop == "Author":
            query = "SELECT * FROM books WHERE author LIKE %s"
            data = (search,)
            mycur.execute(query, data)
        else:
            messagebox.showinfo("Error", "Invalid Request")


        tree.delete(*tree.get_children())

    # Fetch results and insert into treeview
        rows = mycur.fetchall()
        for row in rows:
            tree.insert("", 'end', values=row)

        mycur.close()

    


    #heading
    headingframe1 = ctk.CTkFrame(window6, fg_color="#D3D3D3", height= 110, width= 1548)
    headingframe1.place(x=0,y=0)

    headinglabel1 = ctk.CTkLabel(headingframe1, text= "LIBRARY MANAGEMENT SYSTEM",
                                 text_color="black",
                           font=("Helvetica", 50,"bold"),
                           fg_color="#D3D3D3")
    headinglabel1.place(x=360,y=30)

    #main frame
    frame = ctk.CTkFrame(window6,
                     fg_color= "#D3D3D3",
                       height=560,
                       width= 1200, 
                     corner_radius=50)
    frame.place(x=170, y=160)

    #frame contents
    label1 = ctk.CTkLabel(frame, text="*VIEW BOOKS*",
                          fg_color="#D3D3D3",
                      text_color="black",
                      
                      font=("Helvetica", 30))
    label1.place(x=480,y=20)

    searchBY_label = ctk.CTkLabel(frame,text="SEARCH BY: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 15))
    searchBY_label.place(x=140,y=100)

    options = ["All","Book ID", "Book Name", "Author"]
    dropdown = ctk.CTkOptionMenu(frame, values=options,width=150,corner_radius=10 ,height=25, fg_color= "#2B2B2B",bg_color="#D3D3D3")
    dropdown.place(x= 250, y=100)
    dropdown.set("All")


    search_label = ctk.CTkLabel(frame,text="SEARCH QUERY: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 15))
    search_label.place(x=450,y=100)

    search_entry = ctk.CTkEntry(frame,
                            placeholder_text="Enter elements to search",
                            width=200,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",)
    search_entry.place(x=600, y=100)

    search_entry.bind("<KeyRelease>", searchS_logic)

    btn = ctk.CTkButton(frame,text="SEARCH",
                    height=20,
                    width=100,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= searchS_logic
                    )

    btn.place(x=830, y=100)


    btn2 = ctk.CTkButton(frame,text="UPDATE",
                    height=20,
                    width=100,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= update_books
                    )

    btn2.place(x=950, y=100)

    #Tree view

    style = ttk.Style()
    style.configure("Treeview", 
                bg_color="#D3D3D3",
                 fieldbackground= "#D3D3D3",
                 fg_color = "black",
                 rowheight=30)

    tree = ttk.Treeview(frame, show= "headings", height=10)
    tree['columns'] = ("book_id", "title", "author","total_quantity" ,"available_quantity")

    
    tree.column("book_id", width=150)
    tree.column("title", width=300)
    tree.column("author", width=300)
    tree.column("total_quantity", width=220)
    tree.column("available_quantity", width=220)
    

#heading

    
    tree.heading("book_id",text="Book ID")
    tree.heading("title", text="Book Name")
    tree.heading("author", text="Author")
    tree.heading("total_quantity", text="Total Quantity")
    tree.heading("available_quantity", text="Available Quantiy")

    tree.place(x= 150, y= 250)

    tree.delete(*tree.get_children())
    mycur = conn.cursor()
    mycur.execute("SELECT * FROM books;")  # Update table name and query as needed
    rows = mycur.fetchall()
    for row in rows:
        tree.insert("", 'end', values=row)
    conn.commit()    
    mycur.close()


    window6.mainloop()


