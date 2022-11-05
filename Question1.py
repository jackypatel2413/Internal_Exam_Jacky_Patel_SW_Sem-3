from tkinter import *
import tkinter as tk

root=tk.Tk()
root.geometry("900x400")
root.title("Question 1")
root.config(bg="skyblue")

fn=Label(root , text="First Name :",width=10 ,font=('Arial', 10))
fn.place(x=10,y=20)

fn_var = tk.StringVar()
fn_entry = Entry(root, textvariable=fn_var,font=('Arial', 10, 'normal'),width=23)
fn_entry.place(x=100 ,y=20)

ln=Label(root , text="Last Name :" ,font=('Arial', 10),width=10)
ln.place(x=10,y=45)

ln_var = tk.StringVar()
ln_entry = Entry(root, textvariable=ln_var, width=23,font=('Arial', 10, 'normal'))
ln_entry.place(x=100 ,y=45)

gen=Label(root , text="Gender :" ,font=('Arial', 10),width=10)
gen.place(x=10,y=70)
var = tk.StringVar()
r1 = tk.Radiobutton(root, text='Male', variable=var,value='Male')
r1.place(x=100,y=70)
r2 = tk.Radiobutton(root, text='Female', variable=var,value='Female')
r2.place(x=150,y=70)

Lan=Label(root , text="Languages :" ,font=('Arial', 10),width=10)
Lan.place(x=10,y=100)
lan_var=tk.StringVar()
cb1=Checkbutton(root ,text="Telugu", variable=lan_var)
cb1.place(x=100 , y=100 )
cb2=Checkbutton(root ,text="English", variable=lan_var)
cb2.place(x=160 , y=100 )
cb3=Checkbutton(root ,text="Hindi", variable=lan_var)
cb3.place(x=220 , y=100 )

email=Label(root , text="Email :" ,font=('Arial', 10),width=10)
email.place(x=10,y=130)
em_var=tk.StringVar()
em_entry = Entry(root, textvariable=em_var,font=('Arial', 10, 'normal'),width=23)
em_entry.place(x=100 ,y=130)

add=Label(root , text="Address :" ,font=('Arial', 10),width=10)
add.place(x=10,y=160)
add_var=tk.StringVar()
add_entry=tk.Text(root , height=5 ,width=20 )
add_entry.place(x=100 ,y=160)

state=Label(root , text="State :" ,font=('Arial', 10),width=10)
state.place(x=10,y=250)
state_menu= StringVar() 
state_menu.set("Choose State")
drop= OptionMenu(root, state_menu,"Gujarat", "Maharastra","Delhi","Rajasthan")
drop.place(x=100,y=250)

zip_code = tk.Label(root, text="Zip", width=10, font=("arial", 10))
zip_code.place(x=10, y=290)
zip_var=tk.StringVar()
zip_entry = tk.Entry(root ,font=('Arial', 10, 'normal'),textvariable=zip_var,width=23)
zip_entry.place(x=100, y=290)

cc=Label(root , text="Credit Card :" ,font=('Arial', 10),width=10)
cc.place(x=10,y=330)
cc_menu= StringVar() 
cc_menu.set("Choose Credit Card")
drop= OptionMenu(root, cc_menu,"VISA", "Master")
drop.place(x=100,y=330)


def insert():

    firstname = fn_var.get()
    lastname = ln_var.get()
    gender_i = var.get()
    zipp = zip_var.get()

    inserted_fname = tk.Label(text="First Name : "+firstname)
    inserted_lname = tk.Label(text="Last Name : "+lastname)
    inserted_gen = tk.Label(text="Gender : "+gender_i)
    inserted_zip = tk.Label(text="Zip Code :"+zipp)
    inserted_fname.place(x=500, y=20)
    inserted_lname.place(x=500, y=50)
    inserted_gen.place(x=500, y=80)
    inserted_zip.place(x=500 , y=110)


insert_btn = tk.Button(root, text='Insert', command=insert , height=2,width=10)
insert_btn.place(x=350,y=100)

delete_btn = tk.Button(root, text='delete' , height=2,width=10)
delete_btn.place(x=350,y=170)

def theame():
    root.config(bg="green")

theame_btn = tk.Button(root , text="Theame" , command=theame ,height=2,width=10)
theame_btn.place(x=350,y=230)


root.mainloop()