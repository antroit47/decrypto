# decrypto
This is a simple python tool for a  very simple encryption/decryption of data. Has a simple GUI (run structure.py), but can also be used as a library. 
# Caesar cipher
GUI: A bruteforce attack on caesar cipher can be enabled by not specifying the *step* value when decrypting. The result displayed is selected by counting the vowels and consonants in words.

Library: Use decrypt_smart in caesar.py for bruteforce attack. Returns an array of possible results sorted by their *vowels and consonants value*.

# Vigenere cipher
Library: For a bruteforce atack use decrypt_smart in vigenere.py, length of the key must be provided. Returns an array of possible results sorted by *their vowels and consonants value*.

# Steganography
GUI: Only able to hide into 1 least signifficant bit of an image. *Steg 1bit* works hides strings into images, *Steg img* hides images within images. 

Library (steganography.py): Also has 2 least signifficant bits hiding.

# Revealing hidden data within images
Library (steganography.py): each_color_check_blacknwhite - Used for looking for secret patterns of *more or less* the same color in an image. First reads an image in greyscale, then it creates 256 images for every shade of gray. The current shade is white, the rest is black. 

Library (steganography.py): top_pixels_color_check - Used for looking for secret patterns of exactly the same color in an image. Takes most common colors (the amount provided by parameter) in a picture and makes a set of pictures where all of these colors are represented by white, the rest is black.

Library (steganography.py): stegano_last1bit_diff - function to visualize any difference in 2 provided pictures of the same size. Any difference in pixels will be marked as white, the rest is black. Useful for recognising compression, steganographic alteration of some sorts, or hidden symbols / watermarks which differ by only one value

Library (steganography.py): stegano_last1bit_diff_EXP - function to visualize difference in 2 provided pictures of the same size. The lighter the color a resulting pixel, the more the difference there was on that pixel between the two original pictures. Useful for spotting more signifficant changes within images (spot the difference games, find out the photoshopped parts of an image).
