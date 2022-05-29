import sys
import os
from tkinter import *

window=Tk()

window.title("Face Recoginition system")
window.geometry('550x500')

def run():
    os.system('python C:/Users/anmol.r/PycharmProjects/FaceRecognition/face_recog.py')

btn = Button(window, text="Mark Attendance!", bg="green", fg="white",command=run)
exit_button = Button(window, text="Exit", bg="green", fg="white", command=window.destroy)
btn.grid(column=5, row=5)
exit_button.grid(column=6, row=6)

window.mainloop()