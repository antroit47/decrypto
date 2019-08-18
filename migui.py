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
    caesar1_btn = Button(window, text="  Caesar - encrypt  ", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn, caesar_click))
    caesar1_btn.grid(column=0, row=0)
    caesarD_btn = Button(window, text="  Caesar - decrypt  ", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn, caesarD_click))
    caesarD_btn.grid(column=1, row=0)
    vigenere_btn = Button(window, text="Vigenere - encrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn, vigenere_click))
    vigenere_btn.grid(column=0, row=1)
    vigenereD_btn = Button(window, text="Vigenere - decrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn, vigenereD_click))
    vigenereD_btn.grid(column=1, row=1)


def new_window(window, button, btn2, btn3, btn4, function):
    button.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    function(window)


def caesar_click(window):
    lbl = Label(window, text="message:")
    lbl.grid(column=0, row=0)

    msg_entry = Entry(window,width=30)
    msg_entry.grid(column=1, row=0)

    lbl2 = Label(window, text="step:")
    lbl2.grid(column=2, row=0)

    step_entry = Entry(window,width=5)
    step_entry.grid(column=3, row=0)

    lbl3 = Label(window, text="result: ")
    lbl3.grid(column=0, row=2)

    result_entry = Entry(window,width=30)
    result_entry.grid(column=1, row=2)
    
    encrypt_btn = Button(window, text="encrypt", command=lambda: caesar_encrypt(msg_entry.get(), step_entry.get(),result_entry))
    encrypt_btn.grid(column=0, row=1)

    exit_btn = Button(window, text="exit", command=lambda: exit_caesar_encrypt(window, lbl, msg_entry, lbl2, step_entry, lbl3, encrypt_btn, exit_btn, result_entry))
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
        label.delete(0,END)
        label.insert(0,caesar.encrypt(msg, int(step)))


def caesarD_click(window):
    lbl = Label(window, text="encrypted message:")
    lbl.grid(column=0, row=0)
    
    msg_entry = Entry(window,width=22)
    msg_entry.grid(column=1, row=0)

    lbl2 = Label(window, text="step:")
    lbl2.grid(column=2, row=0)

    step_entry = Entry(window,width=5)
    step_entry.grid(column=3, row=0)
    
    lbl3 = Label(window, text="original message: ")
    lbl3.grid(column=0, row=2)

    result_entry = Entry(window,width=22)
    result_entry.grid(column=1, row=2)

    decrypt_btn = Button(window, text="decrypt", command=lambda: caesar_decrypt(msg_entry.get(), step_entry.get(),result_entry))
    decrypt_btn.grid(column=0, row=1)

    exit_btn = Button(window, text="exit", command=lambda: exit_caesar_encrypt(window, lbl, msg_entry, lbl2, step_entry, lbl3, decrypt_btn, exit_btn, result_entry))
    exit_btn.grid(column=0, row=6)


def caesar_decrypt(msg, step, label):
    if msg == "":
        print("[message] is empty")
        messagebox.showinfo('Error','[message] is empty')
        return
    elif step == "":
        print("step was not specified - decrypting without step")
        label.delete(0,END)
        label.insert(0,caesar.select_best(caesar.decrypt_smart(msg)))
    elif not step.isdigit():
        print("step parameter has to be digit")
        messagebox.showinfo('Error','step parameter has to be a digit')
    else:
        label.delete(0,END)
        label.insert(0,caesar.decrypt(msg, int(step)))


def vigenere_click(window):
    lbl = Label(window, text="message:")
    lbl.grid(column=0, row=0)
    
    msg_entry = Entry(window,width=40)
    msg_entry.grid(column=1, row=0)

    lbl2 = Label(window, text="key:")
    lbl2.grid(column=0, row=1)

    key_entry = Entry(window,width=40)
    key_entry.grid(column=1, row=1)
    
    lbl3 = Label(window, text="result: ")
    lbl3.grid(column=0, row=3)

    result_entry = Entry(window,width=40)
    result_entry.grid(column=1, row=3)

    encrypt_btn = Button(window, text="encrypt", command=lambda: vigenere_encrypt(msg_entry.get(), key_entry.get(),result_entry))
    encrypt_btn.grid(column=0, row=2)

    exit_btn = Button(window, text="exit", command=lambda: exit_caesar_encrypt(window, lbl, msg_entry, lbl2, key_entry, lbl3, encrypt_btn, exit_btn, result_entry))
    exit_btn.grid(column=0, row=6)


def vigenere_encrypt(msg, key, label):
    if msg == "" or key == "":
        print("one of the following [message/key] is empty")
        messagebox.showinfo('Error','one of the following [message/key] is empty')
        return
    else:
        for char in key:
            if char.isdigit():
                print("invalid key - containing digits")
                messagebox.showinfo('Error','invalid key - containing digits')
                return
        label.delete(0,END)
        label.insert(0,vigenere.encrypt(msg, key))


def vigenereD_click(window):
    lbl = Label(window, text="encrypted message:")
    lbl.grid(column=0, row=0)
    
    msg_entry = Entry(window,width=30)
    msg_entry.grid(column=1, row=0)

    lbl2 = Label(window, text="key:")
    lbl2.grid(column=0, row=1)

    key_entry = Entry(window,width=30)
    key_entry.grid(column=1, row=1)
    
    lbl3 = Label(window, text="decrypted message: ")
    lbl3.grid(column=0, row=3)

    result_entry = Entry(window,width=40)
    result_entry.grid(column=1, row=3)

    encrypt_btn = Button(window, text="decrypt", command=lambda: vigenere_decrypt(msg_entry.get(), key_entry.get(),result_entry))
    encrypt_btn.grid(column=0, row=2)

    exit_btn = Button(window, text="exit", command=lambda: exit_caesar_encrypt(window, lbl, msg_entry, lbl2, key_entry, lbl3, encrypt_btn, exit_btn, result_entry))
    exit_btn.grid(column=0, row=6)


def vigenere_decrypt(msg, key, label):
    if msg == "" or key == "":
        print("one of the following [message/key] is empty")
        messagebox.showinfo('Error','one of the following [message/key] is empty')
        return
    else:
        for char in key:
            if char.isdigit():
                print("invalid key - containing digits")
                messagebox.showinfo('Error','invalid key - containing digits')
                return
        label.delete(0,END)
        label.insert(0,vigenere.decrypt(msg, key))


def exit_caesar_encrypt(window, s1,s2,s3,s4,s5,s6,s7,s8):
    s1.destroy()
    s2.destroy()
    s3.destroy()
    s4.destroy()
    s5.destroy()
    s6.destroy()
    s7.destroy()
    s8.destroy()
    init(window)
