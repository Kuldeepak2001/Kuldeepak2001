import os
from tkinter import *

window=Tk()

window.title("Face Recognition system")
window.geometry('550x300')
window.configure(bg='white')


def run():
    os.system('python C:/Users/anmol.r/PycharmProjects/FaceRecognition/face_recog.py')


l = Label(window, text = "Face Recoginition system", font="25px")

btn = Button(window, text="Mark Entry", bg="green", fg="white",font="15px", command=run)
sbtn = Button(window, text="Close Application", bg="red", fg="white", font="15px", command=window.destroy)

l.pack(pady=30)
btn.pack(pady=10)
sbtn.pack()

window.mainloop()