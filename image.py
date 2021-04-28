from tkinter import *
#if the import of ImageTk does't work then 
#type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
#this module allows us to use png and jpg images in our program
from PIL import ImageTk,Image
window = Tk()
window.title("image viewer")

#functions that is going to handle the back and forward button's functionality
def forward(image_number):
	#global variables allow us to work with them outside the function
	#You can't modify a global variable without using the global statement inside the function in python
    global my_lable
    global button_forward
    global button_back 
    global imageIndex
    #deleting the old image from the application screen
    my_lable.grid_forget()
    #acessing images from the image list
    my_lable = Label(image=imageList[image_number])
    #updating image
    button_next = Button(window,text=">>",command=lambda : forward(image_number+1))
    button_back = Button(window,text='<<',command=lambda : back(image_number-1))
    #disabling forward button when reaching the end of the image list
    if image_number==5:
    	button_next = Button(window,text=">>",state=DISABLED)
    #putting the new image on the application screen
    my_lable.grid(row=0,column=0, columnspan=3)
    button_next.grid(row=1,column=2)
    button_back.grid(row=1,column=0)
    

def back(image_number):
    global my_lable
    global button_forward
    global button_back 
    global imageIndex
    #deleting the old image from the application screen
    my_lable.grid_forget()
    #acessing images from the image list
    my_lable = Label(image=imageList[image_number])
    #updating image
    button_next = Button(window,text=">>",command=lambda : forward(image_number+1))
    button_back = Button(window,text='<<',command=lambda : back(image_number-1))
    #disabling back button when reaching the end of the image list
    if image_number==0:
    	button_back = Button(window,text="<<",state=DISABLED)
    #putting the new image on the application screen
    my_lable.grid(row=0,column=0, columnspan=3)
    button_next.grid(row=1,column=2)
    button_back.grid(row=1,column=0)
    

#how to deal with images in tkinter
#importing images from the directoring to our application
image1 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux.png"))
image2 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux2.png"))
image3 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux3.png"))
image4 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux4.png"))
image5 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux5.png"))
image6 = ImageTk.PhotoImage(Image.open("/home/aditya/development/python/imageViewer/icons/linux6.png"))

#creating an image list so that we can scroll through the images in our application
imageList=[image1,image2,image3,image4,image5,image6]

#creating back and next button
button_back = Button(window,text='<<',command=lambda : back(0))
button_next = Button(window,text=">>",command=lambda : forward(1))
#exit button
Button_exit = Button(window, text="Exit Program", command=window.quit)

#puttin image on the screen in our application
my_lable = Label(image=image1)
my_lable.grid(row=0,column=0, columnspan=3)

#putting back button on the app screen
button_back.grid(row=1,column=0)
Button_exit.grid(row=1,column=1)
button_next.grid(row=1,column=2)
window.mainloop()