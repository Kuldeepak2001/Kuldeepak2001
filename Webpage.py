import sys
import os
from tkinter import *

window=Tk()

window.title("Face Recoginition system")
window.geometry('550x500')

def run():
    os.system('python C:/Users/anmol.r/PycharmProjects/FaceRecognition/face_recog.py')

btn = Button(window, text="Click Me", bg="green", fg="white",command=run)
btn.grid(column=0, row=0)

window.mainloop()