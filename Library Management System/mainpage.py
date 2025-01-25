import customtkinter as ctk

from addbooks import add_books
from borrowbooks import borrow_books
from returnbooks import return_books
from delete import delete_books
from viewbooks import view_books
from viewlog import view_log
 
def main():
    window1 = ctk.CTk()
    window1.title("Library Management System-- main")
    window1.geometry("1548x900+0+0")
    window1.configure(fg_color ="#8770C9")

    #heading
    headingframe1 = ctk.CTkFrame(window1, fg_color="#D3D3D3", height= 110, width= 1548)
    headingframe1.place(x=0,y=0)

    headinglabel1 = ctk.CTkLabel(headingframe1, text= "LIBRARY MANAGEMENT SYSTEM",
                                 text_color="black",
                           font=("Helvetica", 50,"bold"),
                           fg_color="#D3D3D3")
    headinglabel1.place(x=370,y=30)


    #main frame
    frame = ctk.CTkFrame(window1,
                     fg_color= "#D3D3D3",
                       height=520,
                       width= 660, 
                     corner_radius=50)
    frame.place(x=450, y=200)


    #options

    add_btn = ctk.CTkButton(frame, text="ADD BOOKS",
                            height=42,
                            width=430,
                            text_color="white",
                            fg_color="black",
                            bg_color="#D3D3D3",
                            corner_radius=20,
                            hover_color="brown",
                            font=("Helvetica", 30),
                            command=add_books
                            )
    add_btn.place(x=120,y=80)

    borrow_btn = ctk.CTkButton(frame, text="BORROW BOOKS",
                            height=42,
                            width=430,
                            text_color="white",
                            fg_color="black",
                            bg_color="#D3D3D3",
                            corner_radius=20,
                            hover_color="brown",
                            font=("Helvetica", 30),
                            command= borrow_books
                            )
    borrow_btn.place(x=120,y=160)

    return_btn = ctk.CTkButton(frame, text="RETURN BOOKS",
                            height=42,
                            width=430,
                            text_color="white",
                            fg_color="black",
                            bg_color="#D3D3D3",
                            corner_radius=20,
                            hover_color="brown",
                            font=("Helvetica", 30),
                            command= return_books)
    return_btn.place(x=120,y=240)

    delete_btn = ctk.CTkButton(frame, text="DELETE BOOKS",
                            height=42,
                            width=430,
                            text_color="white",
                            fg_color="black",
                            bg_color="#D3D3D3",
                            corner_radius=20,
                            hover_color="brown",
                            font=("Helvetica", 30),
                            command= delete_books
                            )
    delete_btn.place(x=120,y=320)

    view_book_btn = ctk.CTkButton(frame, text="VIEW BOOKS",
                            height=42,
                            width=190,
                            text_color="white",
                            fg_color="black",
                            bg_color="#D3D3D3",
                            corner_radius=20,
                            hover_color="brown",
                            font=("Helvetica", 25),
                            command= view_books)
    view_book_btn.place(x=120,y=400)

    view_log_btn = ctk.CTkButton(frame, text="VIEW LOG",
                            height=42,
                            width=190,
                            text_color="white",
                            fg_color="black",
                            bg_color="#D3D3D3",
                            corner_radius=20,
                            hover_color="brown",
                            font=("Helvetica", 25),
                            command= view_log)
    view_log_btn.place(x=360,y=400)

    window1.mainloop()
