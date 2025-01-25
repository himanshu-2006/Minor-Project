import customtkinter as ctk
import mysql.connector as myc
from tkinter import messagebox
conn = myc.connect(host = "localhost",
                     user= "root", 
                     password= "",
                     database = "")

def update_books():
    window8 = ctk.CTk()
    window8.title("Library Management System-- Add Books")
    window8.geometry("1548x900+0+0")
    window8.configure(fg_color ="#8770C9")
    ctk.set_appearance_mode("dark")

    a = [12,22,32]
         
    #to check the book id
        
    def check_book_id(book_id):
        try:
            mycur = conn.cursor()
            query = "SELECT book_id FROM books WHERE book_id = %s"
            mycur.execute(query, (book_id,))
            result = mycur.fetchone()
            mycur.close()

            if result:  # If a record is found, the book ID exists
                return True
            else:
                return False  # Book ID doesn't exist
        except Exception as e:
            print("Error checking book ID:", e)
            return False

    def update_logic():
        l_id = librarian_id_entry.get()
        b_id = book_id_entry.get()
        b_name = book_name_entry.get()
        b_author = author_entry.get()
        t_quan = total_quantity_entry.get()
        a_quan = available_quantity_entry.get()
        # if not all([b_id,l_id ,b_name, b_author, t_quan, a_quan]):
        #     messagebox.showwarning("Warning", "Please fill in all fields.")
        #     return
        
        reset_style()

        error = False
        if not l_id.isdigit() or int(l_id) not in a:
            librarian_id_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_id.isdigit() or not check_book_id(b_id):
            book_id_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_name:
            book_name_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_author:
            author_entry.configure(border_color = "red",border_width=5)
            error = True
        if not t_quan.isdigit():
            total_quantity_entry.configure(border_color = "red",border_width=5)
            error = True
        if not a_quan.isdigit():
            available_quantity_entry.configure(border_color = "red",border_width=5)
            error = True
        

        if error:
            print("Warning", "Please correct the highlighted fields.")
        else:
            mycur = conn.cursor()

            query = "UPDATE books set title = %s, author = %s, total_quantity = %s, available_quantity = %s WHERE book_id = %s"
            data = (b_name, b_author, t_quan, a_quan, b_id)
            mycur.execute(query,data)
            conn.commit()
            mycur.close()
            messagebox.showinfo("Success", "Data has been updated successfully.")
            librarian_id_entry.delete(0, 'end')
            book_id_entry.delete(0, 'end')
            book_name_entry.delete(0,'end')
            author_entry.delete(0, 'end')
            total_quantity_entry.delete(0, 'end')
            available_quantity_entry.delete(0, 'end')

    def reset_style():
        original_color = "#D3D3D3"  # Replace this with the original color of the borders
        book_id_entry.configure(border_color=original_color)
        book_name_entry.configure(border_color=original_color)
        librarian_id_entry.configure(border_color = original_color)
        author_entry.configure(border_color = original_color)
        total_quantity_entry.configure(border_color = original_color)
        available_quantity_entry.configure(border_color = original_color)
        
    #heading
    headingframe1 = ctk.CTkFrame(window8, fg_color="#D3D3D3", height= 110, width= 1548)
    headingframe1.place(x=0,y=0)

    headinglabel1 = ctk.CTkLabel(headingframe1, text= "LIBRARY MANAGEMENT SYSTEM",
                                 text_color="black",
                           font=("Helvetica", 50,"bold"),
                           fg_color="#D3D3D3")
    headinglabel1.place(x=360,y=30)

    #main frame
    frame = ctk.CTkFrame(window8,
                     fg_color= "#D3D3D3",
                       height=560,
                       width= 660, 
                     corner_radius=50)
    frame.place(x=450, y=160)

    #frame contents
    label1 = ctk.CTkLabel(frame, text="*UPDATE BOOKS*",
                          fg_color="#D3D3D3",
                      text_color="black",
                      
                      font=("Helvetica", 30))
    label1.place(x=200,y=20)



    librarian_id =  ctk.CTkLabel(frame,text="Librarian ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    librarian_id.place(x=100,y=100)

    
    librarian_id_entry = ctk.CTkEntry(frame,
                            placeholder_text="User Id",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3", fg_color= "#2B2B2B"
                            )
    librarian_id_entry.place(x=280,y=100)

    book_id =  ctk.CTkLabel(frame,text="Book ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_id.place(x=120,y=160)

    book_id_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book ID",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3", fg_color= "#2B2B2B"
                            )
    book_id_entry.place(x=280,y=160)
    


    book_name =  ctk.CTkLabel(frame,text="Book Name: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_name.place(x=110,y=220)

    book_name_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book Name",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3"
                            , fg_color= "#2B2B2B"
                            )
    
    book_name_entry.place(x=280,y=220)


    author =  ctk.CTkLabel(frame,text="Author Name: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    author.place(x=100,y=280)

    author_entry = ctk.CTkEntry(frame,
                            placeholder_text="Author Name",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            fg_color= "#2B2B2B"
                            )
    author_entry.place(x=280,y=280)

   

    total_quantity =  ctk.CTkLabel(frame,text="Total Quantity: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    total_quantity.place(x=100,y=340)

    total_quantity_entry = ctk.CTkEntry(frame,
                            placeholder_text="Total Quantity of books",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            fg_color= "#2B2B2B"
                            )
    total_quantity_entry.place(x=280,y=340)
    


    available_quantity = ctk.CTkLabel(frame,text="Available Quantity: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20) )
    available_quantity.place(x=90,y=400)
    available_quantity_entry = ctk.CTkEntry(frame,
                            placeholder_text="Available Quantity of books",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            fg_color= "#2B2B2B"
                            )
    available_quantity_entry.place(x= 280, y= 400)
    
    btn = ctk.CTkButton(frame,text="SUBMIT",
                    height=30,
                    width=220,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= update_logic
                    
                    )

    btn.place(x=240, y=480)
    window8.mainloop()

