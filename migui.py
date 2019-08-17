from PIL import Image
import caesar
import steganography
import support
import texttransfer
import vigenere
from tkinter import *
from tkinter import messagebox



def rungui():
    print("starting gui")
    window = Tk()
    window.geometry('350x200')
    window.title("Decrypto")
    init(window)
    
    window.mainloop()



def init(window):      
    caesar1_btn = Button(window, text="Caesar - encrypt", command=lambda: new_window(window,caesar1_btn, caesar_click))
    caesar1_btn.grid(column=0, row=0)    


def new_window(window, button, function):
    button.destroy()
    function(window)


def caesar_click(window):
    lbl = Label(window, text="message:")
    lbl.grid(column=0, row=0)

    msg_entry = Entry(window,width=25)
    msg_entry.grid(column=1, row=0)


    lbl2 = Label(window, text="step:")
    lbl2.grid(column=2, row=0)

    step_entry = Entry(window,width=5)
    step_entry.grid(column=3, row=0)


    lbl3 = Label(window, text="result: ")
    lbl3.grid(column=0, row=2)
    
    encrypt_btn = Button(window, text="encrypt", command=lambda: caesar_encrypt(msg_entry.get(), step_entry.get(),lbl3))
    encrypt_btn.grid(column=0, row=1)

    exit_btn = Button(window, text="exit", command=lambda: exit_caesar(window, lbl, msg_entry, lbl2, step_entry, lbl3, encrypt_btn, exit_btn))
    exit_btn.grid(column=0, row=6)


def caesar_encrypt(msg, step, label):
    if msg == "" or step == "":
        print("one of the following [message, step] is empty")
        messagebox.showinfo('Error','one of the following [message, step] is empty')
        return
    elif not step.isdigit():
        print("step parameter has to be digit")
        messagebox.showinfo('Error','step parameter has to be a digit')
    else:
        label.configure(text= "result: " + caesar.encrypt(msg, int(step)))


def exit_caesar(window, s1,s2,s3,s4,s5,s6,s7):
    s1.destroy()
    s2.destroy()
    s3.destroy()
    s4.destroy()
    s5.destroy()
    s6.destroy()
    s7.destroy()
    init(window)
