# USAGE
# tkinter_test.py

# import the necessary packages
from tkinter import *
from experiment import Measure
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
import numpy as np
root = Tk()

a = Measure()


global path

# Read image.
def select_image():
# grab a reference to the image panels

	global panelA, panelB, path, dest,image_name
	dest=False

# open a file chooser dialog and allow the user to select an input
	# image

	path = filedialog.askopenfilename()
	select_image.path=path


# ensure a file path was selected
	if len(path) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
                dest = True
                image = cv2.imread(path)
                edged=a.start(path,crop_flag=True)[1]
                resized_img=cv2.resize(image, (650,1400))
                resized_edged=cv2.resize(edged, (650,1400))
                y=270
                x=0
                h=750
                w=5000
                image1 = resized_img[y:y+h, x:x+w]
                image2 = resized_edged[y:y+h, x:x+w]
		
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
                image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                edged= cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

		# convert the images to PIL format...
                image = Image.fromarray(image)

                edged = Image.fromarray(edged)

		# ...and then to ImageTk format
                image = ImageTk.PhotoImage(image)
                edged = ImageTk.PhotoImage(edged)

		# if the panels are None, initialize them
                if panelA is None or panelB is None:
			# the first panel will store our original image
                        panelA = Label(image=image)
                        panelA.image = image
                        panelA.pack(side="left")
			# panelA.grid()

			# while the second panel will store the edge map
                        panelB = Label(image=edged)
                        panelB.image = edged
                        panelB.pack(side="right")
			# panelB.grid(row=0,column=1)

		# otherwise, update the image panels
                else:
			# update the pannels
                        panelA.configure(image=image)
                        panelB.configure(image=edged)
                        panelA.image = image
                        panelB.image = edged

# initialize the window toolkit along with the two image panels
def result():
	root2=Tk()
	dict = a.start(path,crop_flag=True)[0]
	frame2 = Frame(root2, width=100, height=100)
	row = 0
	col = 0
	for key, value in dict.items():
		tk.Label(root2,
				 text=str(key)).grid(row=row, column=col)
		tk.Label(root2,
				 text=str( 2*value)).grid(row=row, column=1)
		row+=1

panelA = None
panelB = None
#image_name=select_image.path.split(r'/')[-1].split('.')[0]

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI

btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom",  expand="yes", padx="2", pady="2")
btn1 = Button(root, text="Results", command=result)
btn1.pack(side="bottom",  expand="yes", padx="2", pady="2")

# kick off the GUI
root.mainloop()
