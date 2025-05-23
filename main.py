# by the crow
# do not use my code without my permission

import subprocess
import sys
from yt_dlp import *
from tkinter import *

'''
Basic Syntax Overview:

variables are defined just by `VARNAME = VALUE',
but can be further defined by [TODO]

functions are defined by `def FUNCTIONNAME():',
then the indented code after that.

'''

#functions
def downloadvideo(linktovideo): # download youtube video
    if "https://" in linktovideo:
        print("starting download")
        YoutubeDL().download(linktovideo)
    else:
        print("invalid text input")

def installpip(package): # install pip packages
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def listpip():
    subprocess.check_call([sys.executable, "-m", "pip", "list"])
    subprocess.check_output([sys.executable, "-m", "pip", "list"])

#window logic and creation
tk = Tk()

btn1 = Button(tk, text=">", width=4, command=lambda: downloadvideo(txtfield.get()),background="cyan")
btn2 = Button(tk, text="\/", width=4, command=lambda: listpip(),background="red")
txtfield = Entry(tk,width=45,borderwidth=2)

btn1.pack()
btn2.pack()
txtfield.pack(pady=10)

tk.title("crow-downloader")
tk.configure(background="gray")
tk.minsize(200, 100)
tk.maxsize(500, 250)
tk.geometry("300x150+50+50")

tk.mainloop()