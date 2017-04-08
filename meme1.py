from PIL import ImageTk , Image
import PIL.Image
from Tkinter import *
import tkMessageBox
import tkinter
import random
import zlib
import os

root = tkinter.Tk()
root.minsize(width = 770 , height = 600)
root.maxsize(width = 770 , height = 600)
root.geometry("770x600")
root.title("ZUZEncrypt")
root.configure(background = "black")


canvas = tkinter.Canvas(root, width = 600, height = 125)
canvas.pack()

my_image = tkinter.PhotoImage(file = "Demon_Eyes.png")
canvas.create_image(125 , 125 , image = my_image)



#global variables:
pwd = os.getcwd()



# global functions:
#--------------------------------------#
def Kyke():
              if pwd != "/home":
                       tkMessageBox.showinfo("Notification","you are not in root directory, this program works best in root directory. i will change it")
                       os.chdir("/home")
                       g = os.getcwd()
                       print "-> new directory is %s \n" % g
                       
     


#--------------------------------------./


# widgets: 
#--------------------------------------#



# Labels:

zuz_label = tkinter.Label(root,text = "ZUZ", fg = "Red" , bg ="black" , command = Kyke(), height = 5, width = 15 )
zuz_label.pack()

pwd_label = tkinter.Label(root, text = ("You current directory is: %s" % pwd), fg = "Red", bg = "darkgrey")
pwd_label.pack()

choose_label = tkinter.Label(root, text = "Type path", height = 4, width = 13, fg = "red", bg = "grey", borderwidth = 3)
choose_label.pack(side = LEFT)

#entry:

Fileencrypt = tkinter.Entry(root, bd = 5, width = 50)
Fileencrypt.pack(side = LEFT)



#buttons:
#--------------------------------------#

#button functions:

def encrypt():
    
              shit = open(Fileencrypt.get(), "rb").read()
              fuck = zlib.compress(shit, 9)
              f = open("%s.txt"%Fileencrypt.get(), "wb")
              f.write(fuck)
              f.close()
              print ("new %s compressed file created.\n" % Fileencrypt.get())


def decrypt():
              
              shit = open(Fileencrypt.get(), "rb").read()
              fuck = zlib.decompress(shit)
              f = open("%sdecompressed"%Fileencrypt.get(), "wb")
              f.write(fuck)
              f.close()
              print ("new %s decompressed file created.\n" % Fileencrypt.get())


#-------------------------------------->

quit = tkinter.Button(root, text = "Quit", width = 20 , height = 4, bg ="grey", fg ="red")
quit.pack(side = BOTTOM)

compress_button = tkinter.Button(root, text = "Compress" , width = 13 , height = 4 , command = encrypt , fg = "Red", bg = "grey")
compress_button.pack(side = RIGHT)

decompress_button = tkinter.Button(root, text = "Decompress" , width = 13 , height = 4 , command = decrypt , fg = "Red", bg = "grey")
decompress_button.pack(side = RIGHT)


#-------------------------------------./

root.mainloop()

