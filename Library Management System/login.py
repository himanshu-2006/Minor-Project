import customtkinter as ctk
import mysql.connector as myc
from tkinter import messagebox
 
from mainpage import main

conn = myc.connect(host = "localhost",
                     user= "root", 
                     password= "",
                     database = "")

window0 = ctk.CTk()
window0.title("Library Management System")
window0.geometry("1548x900+1+1")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
window0.configure(fg_color="#8770C9") 

a = [12,22,32] #Login Id 
b= [156,157,158] #Login password


'''logic'''
def LoginI():
    a = e.get()
    b = p.get()


    

    if a == "12" and b =="156":
        window0.destroy()
        mycur = conn.cursor()
        query = "INSERT INTO login_Info (User_ID, Date_time) VALUES (%s, CURRENT_TIMESTAMP)"
        dataS = (a,)
        mycur.execute(query, dataS)
        conn.commit()
        mycur.close()
        main()
       
    elif a == "22" and b == "157":
        window0.destroy()
        mycur = conn.cursor()
        query = "INSERT INTO login_Info (User_ID, Date_time) VALUES (%s, CURRENT_TIMESTAMP)"
        dataS = (a,)
        mycur.execute(query, dataS)
        conn.commit()
        mycur.close()
        main()

    elif a == "32" and b == "158":
        window0.destroy()
        messagebox.showinfo("Login Succesful", "Login Succesful")

        mycur = conn.cursor()
        query = "INSERT INTO login_Info (User_ID, Date_time) VALUES (%s, CURRENT_TIMESTAMP)"
        dataS = (a,)
        mycur.execute(query, dataS)
        conn.commit()
        mycur.close()
        main()

    else:

        failed = ctk.CTkLabel(frame,text="Login Failed",
                      text_color="red",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 15, "italic"))
        failed.place(x=290,y=330)
        frame.configure(border_color = "red",border_width=5)
        check.configure(checkmark_color="red",)
        btn.configure(fg_color = "brown", hover_color = "black")
        title.configure(text_color= "red")
        librarian_id_label.configure(text_color = "red")
        librarian_pass_label.configure(text_color = "red")
        e.configure(border_color="red")  
        p.configure(border_color="red") 
        messagebox.showerror("Login Failed", "Your id & password does not match")


    def reset_entry_styles():
        original_color = "#D3D3D3"  # Replace this with the original color of the borders
        e.configure(border_color=original_color)
        p.configure(border_color=original_color)
    
def showpass():
    if check.get()==1:
        p.configure(show="")
    else:
        p.configure(show="*")



   

#header
headinFrame = ctk.CTkFrame(window0,
                            fg_color="#D3D3D3",
                              height= 110, 
                               width= 1548)
headinFrame.place(x=0,y=0)
headinLabel = ctk.CTkLabel(headinFrame,
                           fg_color= "#D3D3D3", 
                           text="LIBRARY MANAGEMENT SYSTEM",
                           text_color="black",
                           font=("Helvetica", 50,"bold"))
headinLabel.place(x=370,y=30)


#main frame
frame = ctk.CTkFrame(window0,
                     fg_color= "#D3D3D3",
                       height=400,
                       width= 660, 
                     corner_radius=50)
frame.place(x=450, y=250)
title = ctk.CTkLabel(frame,
                     text="***LOG IN***",
                     text_color= "black",
                     font=("Helvetica", 30, "bold"))
title.place(x=250,y=20)

librarian_id_label = ctk.CTkLabel(frame,text="Librarian ID: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
librarian_id_label.place(x=100,y=150)

e = ctk.CTkEntry(frame,
                            placeholder_text="Librarian ID",
                            width=250,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3")
e.place(x=250,y=150)

librarian_pass_label = ctk.CTkLabel(frame,text="Password: ",
                      text_color="black",
                      bg_color="#D3D3D3",
                      font=("Helvetica", 20))
librarian_pass_label.place(x=100,y=200)

p = ctk.CTkEntry(frame,
                            placeholder_text="Password",
                            width=250,
                            height=25,
                            corner_radius=10,
                            bg_color="#D3D3D3",
                            show="*")
p.place(x=250,y=200)

check = ctk.CTkCheckBox(frame,text="Show Pass",
                        fg_color="#D3D3D3",
                        bg_color="#D3D3D3",
                        text_color="black",
                        hover_color="brown",
                        checkmark_color="black",
                        command= showpass
                        )
check.place(x=520,y=200)
btn = ctk.CTkButton(frame,text="Log In",
                    height=30,
                    width=220,
                    text_color="#D3D3D3",
                    fg_color= "black",
                    bg_color="#D3D3D3",
                    corner_radius=20,
                    hover_color="brown",
                    command= LoginI
                    )
btn.place(x=230,y=300)

window0.mainloop()