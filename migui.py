from PIL import Image
import caesar
import steganography
import support
import texttransfer
import vigenere
from tkinter import *


def rungui():
    print("starting gui")
    window = Tk()
    window.geometry('350x200')
    window.title("Decrypto")
    init(window)
    
    window.mainloop()



def init(window):      
    caesar1_btn = Button(window, text="Caesar - known key", command=lambda: new_window(window,caesar1_btn, caesar_click))
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


    lbl2 = Label(window, text="result: ")
    lbl2.grid(column=0, row=2)
    
    encrypt_btn = Button(window, text="encrypt", command=lambda: caesar_encrypt(msg_entry.get(), step_entry.get(),lbl2))
    encrypt_btn.grid(column=0, row=1)

    exit_btn = Button(window, text="exit", command=lambda: init(window))
    exit_btn.grid(column=0, row=6)


def caesar_encrypt(msg, step, label):
    label.configure(text= "result: " + caesar.encrypt(msg, int(step))) #breach with int

