from tkinter import * 
from tkinter import ttk
import random

root = Tk()

root.title('Sorting Algo Visualizer')
root.geometry('900x600+200+80')
root.config(bg='#077A49')

# CREATING DIFFERENT LABELS, BUTTONS AND SPEED OF ALGO

mainLabel = Label(root, text="Choose Algorithm", font=("ariel", 13, "bold italic"),
                   bg="#05897a",width=15, fg="black",relief=GROOVE,bd=5)
mainLabel.place(x=0,y=0)



root.mainloop()