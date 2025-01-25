import customtkinter as ctk
import mysql.connector as myc
from tkinter import messagebox
conn = myc.connect(host = "localhost",
                     user= "root", 
                     password= "",
                     database = "")
 
def add_books():
    window2 = ctk.CTk()
    window2.title("Library Management System-- Add Books")
    window2.geometry("1548x900+0+0")
    window2.configure(fg_color ="#8770C9")
    ctk.set_appearance_mode("dark")

    a = [12,22,32]

    '''logic'''

    def add_books_logic():
        from tkinter import messagebox
        l_id = librarian_id_entry.get() #Retriving the input 
        b_id = book_id_entry.get()
        b_name = book_name_entry.get()
        b_author = author_entry.get()
        b_total = total_quantity_entry.get()
        b_avail = available_quantity_entry.get()
        
        reset_entry_styles()
        error = False
        if not l_id.isdigit() or int(l_id) not in a:
            librarian_id_entry.configure(border_color="red", border_width=5)
            error = True
    
        if not b_id.isdigit():
            book_id_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_name:
            book_name_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_author:
            author_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_total.isdigit():
            total_quantity_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_avail.isdigit():
            available_quantity_entry.configure(border_color = "red",border_width=5)
            error = True

        if error:
            print("Warning", "Please correct the highlighted fields.")
        else:
            mycur = conn.cursor()
            query = """
            INSERT INTO books (book_id, title, author, total_quantity, available_quantity)
            VALUES (%s, %s, %s, %s, %s)
            """
            data = (b_id, b_name, b_author, b_total, b_avail)
            mycur.execute(query, data)
            conn.commit()
            mycur.close()

            messagebox.showinfo("Success", "Data has been inserted successfully.")

            # Clear the form fields
            book_id_entry.delete(0, 'end')
            book_name_entry.delete(0, 'end')
            author_entry.delete(0, 'end')
            total_quantity_entry.delete(0, 'end')
            available_quantity_entry.delete(0, 'end')

        
        
    def reset_entry_styles():
    
        original_color = "#D3D3D3"  # Replace this with the original color of the borders
        book_id_entry.configure(border_color = original_color)
        librarian_id_entry.configure(border_color = original_color)
        book_id_entry.configure(border_color=original_color)
        book_name_entry.configure(border_color=original_color)
        author_entry.configure(border_color=original_color)
        total_quantity_entry.configure(border_color=original_color)
        available_quantity_entry.configure(border_color=original_color)
    

    #heading
    headingframe1 = ctk.CTkFrame(window2, fg_color="#D3D3D3", height= 110, width= 1548)
    headingframe1.place(x=0,y=0)

    headinglabel1 = ctk.CTkLabel(headingframe1, text= "LIBRARY MANAGEMENT SYSTEM",
                                 text_color="black",
                           font=("Helvetica", 50,"bold"),
                           fg_color="#D3D3D3")
    headinglabel1.place(x=360,y=30)


    #main frame
    frame = ctk.CTkFrame(window2,
                     fg_color= "#D3D3D3",
                       height=580,
                       width= 660, 
                     corner_radius=50)
    frame.place(x=450, y=160)

    # frame content
    label1 = ctk.CTkLabel(frame, text="*ADD BOOKS*",
                          fg_color="#D3D3D3",
                      text_color="black",
                      
                      font=("Helvetica", 30))
    label1.place(x=240,y=20)

    librarian_id =  ctk.CTkLabel(frame,text="Librarian ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    librarian_id.place(x=80,y=100)

    
    librarian_id_entry = ctk.CTkEntry(frame,
                            placeholder_text="Librarian Id",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    librarian_id_entry.place(x=280,y=100)
    
    book_id =  ctk.CTkLabel(frame,text="Book ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_id.place(x=100,y=160)

    
    book_id_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book Id",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    book_id_entry.place(x=280,y=160)

    book_name =  ctk.CTkLabel(frame,text="Book Name: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_name.place(x=80,y=220)

    book_name_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book Name",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    book_name_entry.place(x=280,y=220)
    


    author =  ctk.CTkLabel(frame,text="Author Name: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    author.place(x=90,y=280)

    author_entry = ctk.CTkEntry(frame,
                            placeholder_text="Author Name",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    
    author_entry.place(x=280,y=280)


    total_quantity =  ctk.CTkLabel(frame,text="Total Quantity: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    total_quantity.place(x=80,y=340)

    total_quantity_entry = ctk.CTkEntry(frame,
                            placeholder_text="Total Number of copies",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    total_quantity_entry.place(x=280,y=340)

   

    available_quantity =  ctk.CTkLabel(frame,text="Available Quantity: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    available_quantity.place(x=70,y=400)

    available_quantity_entry = ctk.CTkEntry(frame,
                            placeholder_text="Available Number of copies",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    available_quantity_entry.place(x=280,y=400)
    
    
    
    btn = ctk.CTkButton(frame,text="SUBMIT",
                    height=30,
                    width=220,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= add_books_logic
                    )

    btn.place(x=240, y=500)

    window2.mainloop()

