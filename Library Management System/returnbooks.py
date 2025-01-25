import customtkinter as ctk
import mysql.connector as myc
from tkinter import messagebox
from datetime import datetime

conn = myc.connect(host = "localhost",
                     user= "root", 
                     password= "",
                     database = "")

def return_books():
    window4 = ctk.CTk()
    window4.geometry("1548x900+1+1")
    window4.title("Library Mangement System-- Return Books")
    window4.configure(fg_color ="#8770C9")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    a = [12,22,32]
    def check_registration_number(reg_number):
        try:
            mycur = conn.cursor()
            query = "SELECT * FROM students WHERE reg_number = %s"
            mycur.execute(query, (reg_number,))
            result = mycur.fetchone()
            mycur.close()

            if result:
                return True  # Registration number is valid
            else:
                return False  # Registration number is not valid
        except Exception as e:
            print("Error checking registration number:", e)
        return False
    
    #to check the book name
    def check_book_name(book_id, book_name):
        try:
            mycur = conn.cursor()
            query = "SELECT title FROM books WHERE book_id = %s"
            mycur.execute(query, (book_id,))
            result = mycur.fetchone()
            mycur.close()

            if result and result[0].lower() == book_name.lower():  # Match book name with book ID
                return True  
            else:
                return False  
        except Exception as e:
            print("Error checking book name:", e)
            return False
    #To check the book id
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
    def return_book_logic():
        l_id = librarian_id_entry.get()
        b_id = book_id_entry.get()
        b_name = book_name_entry.get()
        s_id = student_ID_entry.get()
        # r_date = Return_entry.get()
        sta_id = status_entry.get()

        # if not all([l_id,b_id,s_id,sta_id]):
        #         messagebox.showwarning("Warning", "Please fill in all fields.")
        #         return
        
        reset_entry_styles()
        error = False

        if not b_id.isdigit() or not check_book_id(b_id):
            book_id_entry.configure(border_color = "red",border_width=5)
            error = True
        if not b_name or not check_book_name(b_id, b_name):
            book_name_entry.configure(border_color = "red",border_width=5)
            error = True
        if not l_id.isdigit() or int(l_id) not in a:
            librarian_id_entry.configure(border_color = "red",border_width=5)
            error = True
        if not s_id.isdigit() or not check_registration_number(s_id):
            student_ID_entry.configure(border_color = "red",border_width=5)
            error = True

        
        if error:
            print("Warning", "Please correct the highlighted fields.")
        else:
            current_datetime = datetime.now()
            mycur = conn.cursor()
            query = "UPDATE transaction SET status = %s, return_date = %s WHERE book_id = %s AND student_id = %s AND book_name = %s"
            data = ( sta_id, current_datetime, b_id, s_id, b_name)
            s = "UPDATE books SET available_quantity= available_quantity+1 WHERE book_id = %s"
            datas = (b_id,)
            mycur.execute(query, data)
            mycur.execute(s,datas)
            conn.commit()
            mycur.close()
            messagebox.showinfo("Success", "Data has been inserted successfully.")
            
            librarian_id_entry.delete(0, 'end')
            book_id_entry.delete(0, 'end')
            book_name_entry.delete(0,'end')
            student_ID_entry.delete(0, 'end')

    def reset_entry_styles():
    
        original_color = "#D3D3D3"  # Replace this with the original color of the borders
        book_id_entry.configure(border_color=original_color)
        book_name_entry.configure(border_color=original_color)
        student_ID_entry.configure(border_color = original_color)
        librarian_id_entry.configure(border_color = original_color)
        

    #heading
    headingframe1 = ctk.CTkFrame(window4, fg_color="#D3D3D3", height= 110, width= 1548)
    headingframe1.place(x=0,y=0)

    headinglabel1 = ctk.CTkLabel(headingframe1, text= "LIBRARY MANAGEMENT SYSTEM",
                                 text_color="black",
                           font=("Helvetica", 50,"bold"),
                           fg_color="#D3D3D3")
    headinglabel1.place(x=360,y=30)


    #main frame
    frame = ctk.CTkFrame(window4,
                     fg_color= "#D3D3D3",
                       height=560,
                       width= 660, 
                     corner_radius=50)
    frame.place(x=450, y=160)

    #frame contents
    label1 = ctk.CTkLabel(frame, text="*RETURN BOOKS*",
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
                            bg_color="#D3D3D3",
                            )
    librarian_id_entry.place(x=280,y=100)

    book_id =  ctk.CTkLabel(frame,text="Book ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_id.place(x=110,y=180)

    book_id_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book ID",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    book_id_entry.place(x=280,y=180)
    


    book_name =  ctk.CTkLabel(frame,text="Book Name: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    book_name.place(x=100,y=260)

    book_name_entry = ctk.CTkEntry(frame,
                            placeholder_text="Book Name",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    
    book_name_entry.place(x=280,y=260)


    student_ID =  ctk.CTkLabel(frame,text="Student ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
    student_ID.place(x=110,y=340)

    student_ID_entry = ctk.CTkEntry(frame,
                            placeholder_text="Student ID",
                            width=300,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            )
    student_ID_entry.place(x=280,y=340)

   

    

    stat_label = ctk.CTkLabel(frame,text="Status: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20) )
    stat_label.place(x=120,y=420)
    options = ["returned"]
    status_entry = ctk.CTkOptionMenu(frame, values= options, width=300,corner_radius=10 ,height=25, fg_color= "#2B2B2B",bg_color="#D3D3D3")
    status_entry.place(x= 280, y= 420)
    status_entry.set("returned")
    
    
    
    
    btn = ctk.CTkButton(frame,text="SUBMIT",
                    height=30,
                    width=220,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= return_book_logic
                    )

    btn.place(x=240, y=500)
    window4.mainloop()
