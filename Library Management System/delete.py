import customtkinter as ctk
import mysql.connector as myc
from tkinter import messagebox

 
conn = myc.connect(host = "localhost",
                     user= "root", 
                     password= "",
                     database = "")


def delete_books():
    window5 = ctk.CTk()
    window5.geometry("1548x900+0+0")
    window5.title("Library Mangement System-- Delete Books")
    window5.configure(fg_color ="#8770C9")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    #logic
    a =[12,22,32]


    #to check the book name
    def check_book_name(book_id, book_name):
        try:
            mycur = conn.cursor()
            query = "SELECT title FROM books WHERE book_id = %s"
            mycur.execute(query, (book_id,))
            result = mycur.fetchone()
            mycur.close()

            if result and result[0].lower() == book_name.lower():  # Match book name with book ID
                return True  # Book ID and name match
            else:
                return False  # Book ID and name do not match
        except Exception as e:
            print("Error checking book name:", e)
            return False
        
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

    def delete_logic():
        l_id = librarian_id_entry.get()
        b_id = book_id_entry.get()
        b_name = book_title_entry.get()

        # if not all([b_id,l_id,b_name]):
        #         messagebox.showwarning("Warning", "Please fill in all fields.")
        #         return

        reset_entry_styles()
        error = False

        if not b_id.isdigit() or not check_book_id(b_id):
            book_id_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_name or not check_book_name(b_id, b_name):
            book_title_entry.configure(border_color = "red",border_width=5)
            error = True
        if not l_id.isdigit() or int(l_id) not in a:
            librarian_id_entry.configure(border_color = "red",border_width=5)
            error = True

        if error:
            print("Warning", "Please correct the highlighted fields.")

        else:
            mycur = conn.cursor()
            query ="DELETE FROM books WHERE book_id = %s AND title = %s" 
            data = (b_id,b_name)
            mycur.execute(query,data)
            conn.commit()
            mycur.close()
            messagebox.showinfo("Success", "Data has been updated successfully.")
            librarian_id_entry.delete(0, 'end')
            book_id_entry.delete(0, 'end')
            book_title_entry.delete(0, 'end')

    def reset_entry_styles():
    
        original_color = "#D3D3D3"  # Replace this with the original color of the borders
        librarian_id_entry.configure(border_color = original_color)
        book_id_entry.configure(border_color=original_color)
        book_title_entry.configure(border_color=original_color)

    #heading
    headingframe1 = ctk.CTkFrame(window5, fg_color="#D3D3D3", height= 110, width= 1548)
    headingframe1.place(x=0,y=0)

    headinglabel1 = ctk.CTkLabel(headingframe1, text= "LIBRARY MANAGEMENT SYSTEM",
                                 text_color="black",
                           font=("Helvetica", 50,"bold"),
                           fg_color="#D3D3D3")
    headinglabel1.place(x=360,y=30)


    #main frame
    frame = ctk.CTkFrame(window5,
                     fg_color= "#D3D3D3",
                       height=450,
                       width= 660, 
                     corner_radius=50)
    frame.place(x=450, y=200)
    label1 = ctk.CTkLabel(frame, text="*DELETE BOOKS*",
                          fg_color="#D3D3D3",
                      text_color="black",
                      
                      font=("Helvetica", 30))
    label1.place(x=215,y=30)

    librarian_id = ctk.CTkLabel(frame, text="Librarian ID:",
                                text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    librarian_id.place(x=100,y=130)

    librarian_id_entry = ctk.CTkEntry(frame,
                            placeholder_text="User Id",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    librarian_id_entry.place(x=260,y=130)

    book_id =  ctk.CTkLabel(frame,text="Book ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_id.place(x=110,y=210)

    book_id_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book ID",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3", fg_color= "#2B2B2B"
                            )
    book_id_entry.place(x=260,y=210)

    book_title =  ctk.CTkLabel(frame,text="Book Name: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_title.place(x=100,y=290)

    book_title_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book Name",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3"
                            , fg_color= "#2B2B2B"
                            )
    book_title_entry.place(x=260,y=290)

    btn = ctk.CTkButton(frame,text="SUBMIT",
                    height=30,
                    width=220,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= delete_logic
                    )

    btn.place(x=240, y=380)

    window5.mainloop()
