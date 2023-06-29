#Digital Clock using Python
#import Tk and Label from tkinter library
#Tk is used to create a window for the clock
from tkinter import Tk
#Label allows us to manipulate the data in the window
from tkinter import Label
#import time module to work with time in python
import time  


tree=Tk()    #create a window and name it
tree.title("Digital Clock")

#function to get time continuously
def get_time():
  Var = time.strftime("%I:%M:%S %p") #time format
  clock.config(text=Var)
  clock.after(200,get_time)  #fetches time every 200ms

Label(tree,font=("Calibri",20),text="Made with Python",fg="white",bg="black").pack()
clock=Label(tree,font=("Arial",80),fg="white",bg="purple")
clock.pack() #to center the clock in the window
get_time()

tree.mainloop()  #for clock to run always
