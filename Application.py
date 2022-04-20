import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

array = []
tuplee = ()
f = 1
FileDir = ""

#Load all files from directory
File = os.listdir('imgs/')
#print(File)

if __name__ == "__main__":
    root = tk.Tk()

#setting up a tkinter frame and canvas
frame = ttk.Frame(root)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

canvas = tk.Canvas(frame, bd=1, width=950, height=600)
canvas.grid(row=0, column=0)

frame.pack(expand=1)

FileDir = 'imgs/' + File[0]
img = ImageTk.PhotoImage(Image.open(FileDir))
cimg = canvas.create_image(0,0,image=img,anchor="nw")
#canvas.config(scrollregion=canvas.bbox(ALL))

def load_image():
    global canvas, img, FileDir
    FileDir = 'frames/' + File[f]
    canvas.delete("all")
    #del img
    #del canvas
    #canvas = Canvas(frame, bd=1, width=950, height=600)
    #canvas.grid(row=0, column=0, sticky=N+S+E+W)
    img = ImageTk.PhotoImage(Image.open(FileDir))
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    #root.update_idletasks()
    #root.after(100,load_image)

#function to be called when mouse is clicked
def printcoords(event):
    global FileDir
    global f
    global array
    array.append(event.x)
    array.append(event.y)
    tuplee = tuple(array)
    print (tuplee)
    if len(tuplee)==4:
        print ("Cropping...")
        crop(FileDir, tuplee, 'cropped%d.jpg' % f)
        print ("Cropped")
        array = []
        f += 1
        load_image()                    #should load the next image

#mouseclick event
canvas.bind("<Button 1>",printcoords)



#function to crop a certain area using coordinates
def crop(image_path, coords, saved_location):
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    image_obj.close()


root.mainloop()