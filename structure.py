from PIL import Image
import caesar
import steganography
import support
import texttransfer
import vigenere
import migui

def caesar_test(text, step):
    text01 = caesar.encrypt(text, step)
    print(text01)
    print(caesar.decrypt(text01, step))
    caesar.decrypt_smart(text01)


def stegano_1bit_test(message, filename):  # pic has to be .png
    #print(message)
    steganography.steg1bit_encrypt(message, filename)
    new_msg = steganography.steg1bit_decrypt("encrypted.png")
    #print(new_msg)
    if message == new_msg:
        print("SUCCESS")
    else:
        print("FAIL")


def stegano_2bit_test(message, image):
    #print(message)
    steganography.steg2bit_encrypt(message, image)
    new_msg = steganography.steg2bit_decrypt("encrypted.png")
    #print(new_msg)
    if message == new_msg:
        print("SUCCESS")
    else:
        print("FAIL")

def start():
    #caesar_test("kapybara je nejvetsi hlodavec everest", 5)
    #message = "10010"*240
    #steganography.analski_kowalzsis_text("image.png", message)
    #stegano_1bit_test(message, "image.png")
    #stegano_2bit_test(message, "image.png")

    #these work
 
    #1.image is source, second is secret
    #steganography.analski_kowalzsis_image("xsnacksalot.png", "xcat.png")

    #steganography.steg_encrypt_image("xsnacksalot.png", "xcat.png")
    #steganography.steg_decrypt_image("encrypted.png", 512, 508, 32)
    #steganography.same_images_test("image2.png", "secret_image.png")

    #it seems that 4th variable gets broken because the format of certain pictures is weird.
    #lets just use RGB(24 bit pictures)

    #ascii testing
    #print(texttransfer.bits_to_ascii(texttransfer.ascii_to_bits("android")))
    #print(texttransfer.bits_to_ascii("1100001011011100110010001110010011011110110100101100100"))
    #message = texttransfer.ascii_to_bits("android")
    #steganography.steg1bit_encrypt(message, "image.png")
    #new_msg = steganography.steg1bit_decrypt("encrypted.png")
    #print(texttransfer.bits_to_ascii(new_msg))

    #cipher = vigenere.encrypt("ATTACKATDAWN", "LEMON")
    #print(vigenere.decrypt(cipher, "LEMON"))
 
    #gui
    #migui.rungui()

    steganography.each_color_check("image.png")
    
    print(":)")
    
start()

