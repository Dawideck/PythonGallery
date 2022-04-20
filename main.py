import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.createFrames()
        self.dispFirstPhoto()
        self.createButtons()
        self.createTxtFields()

        #vars for displaying photos
        self.currentFile = 1
        self.howManyFiles = len(os.listdir('imgs/'))
        self.currentFilePath = ""
        self.stringNo = None


    def createFrames(self):
        self.photoFrame = tk.Frame(width=645, height=485, highlightbackground="black", highlightthickness=0)
        self.photoFrame.grid(column=3, row=1)

        self.buttonFrame = tk.Frame(width=200, height=100, highlightbackground="black", highlightthickness=0)
        self.buttonFrame.grid(column=3, row=2)

        self.txtFrame = tk.Frame(height=100, width=100, highlightbackground="black", highlightthickness=0)
        self.txtFrame.grid(column=1, row=1)

        self.quitFrame = tk.Frame(height=100, width=100, highlightbackground="black", highlightthickness=0)
        self.quitFrame.grid(column=4, row=4)

    def createButtons(self):
        self.left = tk.Button(master=self.buttonFrame, text="<-", command=self.prevPhoto)
        self.left.grid(column=0, row=1)

        self.rotateRight = tk.Button(master=self.buttonFrame, text="180*", command=self.rotatePhoto)
        self.rotateRight.grid(column=1, row=1)

        self.right = tk.Button(master=self.buttonFrame, text="->", command=self.nextPhoto)
        self.right.grid(column=2, row=1)

        self.quit = tk.Button(master=self.quitFrame, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(column=1, row=2)



    def createTxtFields(self):
        self.nameLbl = ttk.Label(master=self.txtFrame, text="Filename: \nimg001.jpg\n\n")
        self.nameLbl.grid(column=1, row=1, sticky="w")

        self.dateLbl = ttk.Label(master=self.txtFrame, text="Date: \n2022-04-20\n\n")
        self.dateLbl.grid(column=1, row=2, sticky="w")

        self.timeLbl = ttk.Label(master=self.txtFrame, text="Time: \n12:38:00\n\n")
        self.timeLbl.grid(column=1, row=3, sticky="w")

    def dispFirstPhoto(self):
        self.photo = Image.open('imgs/img1.jpg')
        self.photo = ImageTk.PhotoImage(self.photo)

        self.photoLbl = tk.Label(master=self.photoFrame, image=self.photo)
        self.photoLbl.pack()


    def rotatePhoto(self):
        print("This will rotate photo 180*")

    def nextPhoto(self):

        self.currentFile += 1
        if self.currentFile > self.howManyFiles:
            self.currentFile = 1
        self.stringNo = str(self.currentFile)

        filename = 'imgs/img'+ self.stringNo+'.jpg'

        self.photoLbl.destroy()
        self.photo = Image.open(filename)
        self.photo = ImageTk.PhotoImage(self.photo)

        self.photoLbl = tk.Label(master=self.photoFrame, image=self.photo)
        self.photoLbl.pack()




        #print(os.path.getctime(filename))
        #c_time = os.path.getctime(filename)
        #loc_time = time.ctime(c_time)
        #print(loc_time)

    def prevPhoto(self):

        self.currentFile -= 1
        if self.currentFile < 1:
            self.currentFile = self.howManyFiles
        self.stringNo = str(self.currentFile)

        filename = 'imgs/img' +self.stringNo +'.jpg'

        self.photoLbl.destroy()
        self.photo = Image.open(filename)
        self.photo = ImageTk.PhotoImage(self.photo)

        self.photoLbl = tk.Label(master=self.photoFrame, image=self.photo)
        self.photoLbl.pack()

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)



app = Application(master=root)


app.mainloop()
