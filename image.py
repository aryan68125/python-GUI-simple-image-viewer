from tkinter import *
#if the import of ImageTk does't work then 
#type in terminal :- for python3.5 and above--> sudo apt-get install python3-pil python3-pil.imagetk
#this module allows us to use png and jpg images in our program
from PIL import ImageTk,Image
#import message box to create a pop up window of information display type
from tkinter import messagebox

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
    #updating the status widget every time press the next button
    index=image_number+1
    status = Label(window,text="Image "+str(index)+" of "+str(len(imageList)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

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
    #updating the status widget every time press the back button
    index=image_number+1
    status = Label(window,text="Image "+str(index)+" of "+str(len(imageList)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    

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

#creating a status label that will tell us on which image we are on and the total no of images in app
#bd=1 will give the status widget a border of thinkess = 1
#relief=SUNKEN will sink the entire widget within the border inside the screen
#anchor=E allows us to achor our widget on a particular position in the application
# E = right in x axis :-> this means our widget will be anchored in the right side of the screen
status = Label(window,text="Image 1 of "+str(len(imageList)),bd=1,relief=SUNKEN,anchor=E)

#creating back and next button
button_back = Button(window,text='<<',command=lambda : back(0))
button_next = Button(window,text=">>",command=lambda : forward(1))
#exit button
Button_exit = Button(window, text="Exit Program", command=window.quit)

#puttin image on the screen in our application
my_lable = Label(image=image1)
my_lable.grid(row=0,column=0, columnspan=3)

#putting back button on the app screen
button_back.grid(row=1,column=0,pady=10)
Button_exit.grid(row=1,column=1,pady=10)
button_next.grid(row=1,column=2,pady=10)
#sticky=W+E will allow us to streach a widget along x axis
#sticky=N+S will allow us to streach a widget along y axis
#N = up along y axis, S=down along Y axis, E= right along X axis ,W= left along x axis
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

#creating a function for our pop up window
def dev():
    #create a message box showinfo will just show some kind of information on the pop up window it is not interactive
    #showinfo("the title bar that you want to show up", message that you want to show in your actual pop up window)
    messagebox.showinfo("developer info", "Name = Aditya Kumar \n class = B.tech 2nd year \n college = SITM \n Roll number = 1901230100001")

#now here we are going to create a button which when clicked will trigger a popup window
ButtonDev = Button(window,text="Developer information",command = dev).grid(row=3,column=0,columnspan=4, padx = 20, pady=20)


window.mainloop()