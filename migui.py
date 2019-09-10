from PIL import Image
import caesar
import steganography
import support
import texttransfer
import vigenere
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def rungui():
    """
    default function to run the gui
    All the other functions here basically control the GUI and call functions
    from the rest of the code
    :return: nothing
    """
    print("starting gui")
    window = Tk()
    window.geometry('600x200')
    window.title("Decrypto")
    init(window)
    window.mainloop()


def init(window):
    caesar1_btn = Button(window, text="  Caesar - encrypt  ", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, caesar_click))
    caesar1_btn.grid(column=0, row=0)
    caesarD_btn = Button(window, text="  Caesar - decrypt  ", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, caesarD_click))
    caesarD_btn.grid(column=1, row=0)
    vigenere_btn = Button(window, text="Vigenere - encrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, vigenere_click))
    vigenere_btn.grid(column=0, row=1)
    vigenereD_btn = Button(window, text="Vigenere - decrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, vigenereD_click))
    vigenereD_btn.grid(column=1, row=1)
    steg1bitenc_btn = Button(window, text="Steg 1bit - encrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, steg1bitenc_click))
    steg1bitenc_btn.grid(column=0, row=2)
    steg1bitdec_btn = Button(window, text="Steg 1bit - decrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, steg1bitdec_click))
    steg1bitdec_btn.grid(column=1, row=2)
    steg_encrypt_image_btn = Button(window, text="Steg img - encrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, steg_encrypt_image_click))
    steg_encrypt_image_btn.grid(column=0, row=3)
    steg_decrypt_image_btn = Button(window, text="Steg img - decrypt", command=lambda: new_window(window,caesar1_btn, caesarD_btn, vigenere_btn, vigenereD_btn,steg1bitenc_btn, steg1bitdec_btn,steg_encrypt_image_btn,steg_decrypt_image_btn,exit_btn, steg_decrypt_image_click))
    steg_decrypt_image_btn.grid(column=1, row=3)
    exit_btn = Button(window, text="             exit             ", command=window.destroy)
    exit_btn.grid(column=0, row=4)


def new_window(window, button, btn2, btn3, btn4,btn5, btn6, btn7, btn8, btn9, function):
    button.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn6.destroy()
    btn7.destroy()
    btn8.destroy()
    btn9.destroy()
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


def steg1bitenc_click(window):
    lbl = Label(window, text="Select a picture:")
    lbl.grid(column=0, row=0)

    file_btn = Button(window, text="select", command=lambda: select_file(file_btn))
    file_btn.grid(column=1, row=0)

    lbl2 = Label(window, text="secret message:")
    lbl2.grid(column=0, row=1)

    msg_entry = Entry(window,width=30)
    msg_entry.grid(column=1, row=1)

    result_entry = Label(window, text="")
    result_entry.grid(column=1, row=2)
    
    encrypt_btn = Button(window, text="encrypt", command=lambda: steg1bit_enc(msg_entry.get(), file_btn['text'], result_entry))
    encrypt_btn.grid(column=0, row=2)

    exit_btn = Button(window, text="exit", command=lambda: exit_caesar_encrypt(window, file_btn,lbl,lbl2,result_entry,msg_entry,encrypt_btn,exit_btn,exit_btn)) #exit btn is twice there but it works somehow
    exit_btn.grid(column=0, row=3)


def select_file(btn):
    file = ""
    file = filedialog.askopenfilename(filetypes = (("png files","*.png"),("jpg files","*.jpg")))
    if file == "":
        return
    btn.config(text = file)    


def steg1bit_enc(msg, file, result_entry):
    if file == "select":
        result_entry.configure(text= "Operation failed - select a file")
        return
    if msg == "":
        result_entry.configure(text= "Operation failed - type in a message")
        return
    if not steganography.msg_1bit_kowalzsis(file, msg):
        result_entry.configure(text= "Operation failed - picture does not fit the message or has wrong bit depth")
        return
    
    steganography.steg1bit_encrypt(texttransfer.ascii_to_bits(msg), file)
    result_entry.configure(text= "encrypted.png was created")

    
def steg1bitdec_click(window):
    lbl = Label(window, text="Select a picture:")
    lbl.grid(column=0, row=0)

    file_btn = Button(window, text="select", command=lambda: select_file(file_btn))
    file_btn.grid(column=1, row=0)


    lbl2 = Label(window, text="decrypted: ")
    lbl2.grid(column=0, row=2)

    result_entry = Entry(window,width=40)
    result_entry.grid(column=1, row=2)

    decrypt_btn = Button(window, text="decrypt", command=lambda: steg1bit_dec(file_btn['text'], result_entry))
    decrypt_btn.grid(column=0, row=1)

    exit_btn = Button(window, text="exit", command=lambda: exit_steg1bit_dec(window, file_btn,lbl,lbl2,decrypt_btn,exit_btn,result_entry))
    exit_btn.grid(column=0, row=3)


def steg1bit_dec(file, result_entry):
    if file == "select":
        result_entry.delete(0,END)
        result_entry.insert(0,"Operation failed - select a file")
        return

    result_entry.delete(0,END)
    result_entry.insert(0,texttransfer.bits_to_ascii(steganography.steg1bit_decrypt(file)))
    

def exit_steg1bit_dec(window, s1,s2,s3,s4,s5,s6):
    s1.destroy()
    s2.destroy()
    s3.destroy()
    s4.destroy()
    s5.destroy()
    s6.destroy()
    init(window)


def steg_encrypt_image_click(window):
    lbl = Label(window, text="Select a base picture:")
    lbl.grid(column=0, row=0)

    file_btn = Button(window, text="select", command=lambda: select_file(file_btn))
    file_btn.grid(column=1, row=0)


    lbl2 = Label(window, text="Select a secret picture:")
    lbl2.grid(column=0, row=1)

    file_btn2 = Button(window, text="select", command=lambda: select_file(file_btn2))
    file_btn2.grid(column=1, row=1)

    result_entry = Label(window, text="")
    result_entry.grid(column=1, row=2)
    
    encrypt_btn = Button(window, text="encrypt", command=lambda: steg_encrypt_image(file_btn['text'], file_btn2['text'], result_entry))
    encrypt_btn.grid(column=0, row=2)

    exit_btn = Button(window, text="exit", command=lambda: exit_caesar_encrypt(window, file_btn,lbl,lbl2,result_entry,file_btn2,encrypt_btn,exit_btn, exit_btn)) #exit btn is twice there but it works somehow
    exit_btn.grid(column=0, row=3)


def steg_encrypt_image(basef, secretf, result_entry):
    if basef == "select":
        result_entry.configure(text= "Operation failed - select a base file")
        return
    if secretf == "select":
        result_entry.configure(text= "Operation failed - select a secret file")
        return
    
    if not steganography.image_2bit_kowalzsis(basef, secretf):
        result_entry.configure(text= "Operation failed - wrong bit depth or message does not fit")
        return
    
    steganography.steg_encrypt_image(basef, secretf)
    result_entry.configure(text= "encrypted.png was created")
    
    

def steg_decrypt_image_click(window):
    lbl = Label(window, text="Select a picture:")
    lbl.grid(column=0, row=0)

    file_btn = Button(window, text="select", command=lambda: select_file(file_btn))
    file_btn.grid(column=1, row=0)

    lbl2 = Label(window, text="secret dimensions:")
    lbl2.grid(column=0, row=1)

    msg_entry = Entry(window,width=10)
    msg_entry.grid(column=1, row=1)

    lbl3 = Label(window, text="x")
    lbl3.grid(column=2, row=1)

    msg_entry2 = Entry(window,width=10)
    msg_entry2.grid(column=3, row=1)

    result_entry = Label(window, text="")
    result_entry.grid(column=1, row=2)
    
    encrypt_btn = Button(window, text="derypt", command=lambda: steg_decrypt_image(file_btn['text'],msg_entry.get(),msg_entry2.get(), result_entry))
    encrypt_btn.grid(column=0, row=2)

    exit_btn = Button(window, text="exit", command=lambda: exit_image_decrypt(window, file_btn,lbl,lbl2,lbl3,result_entry,msg_entry, msg_entry2, encrypt_btn,exit_btn)) 
    exit_btn.grid(column=0, row=3)


def exit_image_decrypt(window, s1,s2,s3,s4,s5,s6,s7,s8, s9):
    s1.destroy()
    s2.destroy()
    s3.destroy()
    s4.destroy()
    s5.destroy()
    s6.destroy()
    s7.destroy()
    s8.destroy()
    s9.destroy()
    init(window)

def steg_decrypt_image(file, x, y, result_entry):
    if file == "select":
        result_entry.configure(text= "Operation failed - select a file")
        return

    if x == "" or y == "":
        result_entry.configure(text= "Operation failed - type in a resolution")
        return
    if  (not x.isdigit()) or (not y.isdigit()):
        result_entry.configure(text= "Operation failed - resolution has to be number")
        return
    
    if not steganography.image_inimage_kowalzsis(file, int(x)*int(y)):
        result_entry.configure(text= "Operation failed - wrong bit depth or wrong resolution")
        return
    
    steganography.steg_decrypt_image(file, int(x), int(y), 24)
    result_entry.configure(text= "secret_image.png was created")

  

