from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import os


window = Tk()

window.title("HTML IDE")

window.minsize(650,650)
window.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))

save_img = ImageTk.PhotoImage(Image.open("save.png"))

exit_img = ImageTk.PhotoImage(Image.open("exit.png"))

name = ""
def open_file():
    global name 
    my_text_msg.delete(1.0,END)
    input_file_name.delete(0,END)

    text_file = filedialog.askopenfilename(title="Open Text File",filetypes=(("text files","*.txt"),))
    print(text_file)

    name = os.path.basename(text_file)
    formatted_name = name.split(".") [0]
    input_file_name.insert(END,formatted_name)
    window.title(formatted_name)
    
    text_file = open(name,'r')
    paragraph = text_file.read()
    my_text_msg.insert(END,paragraph)
    text_file.close()


label_file_name = Label(window,text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name = Entry(window)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text_msg = Text(window,height=35,width=80)
my_text_msg.place(relx=0.5,rely=0.5,anchor=CENTER)

my_text_msg.config(background="ivory4")

open_btn = Button(window,image=open_img,text="Open")
open_btn.place(relx=0.05,rely=0.03,anchor=CENTER)

save_btn = Button(window,image=save_img,text="Save")
save_btn.place(relx=0.11,rely=0.03,anchor=CENTER)

exit_btn = Button(window,image=exit_img,text="Exit")
exit_btn.place(relx=0.17,rely=0.03,anchor=CENTER)

window.mainloop()