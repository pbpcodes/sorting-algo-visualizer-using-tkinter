from tkinter import * 
from tkinter import ttk
import random
from tkinter import font
from tkinter.font import Font

root = Tk()

root.title('Sorting Algo Visualizer')
root.geometry('900x600+200+80')
root.config(bg='#077A49')

# All functions

def drawData(data):
    visualizerCanvasHeight = 450
    visualizerCanvasWidth = 870
    xWidth = visualizerCanvasWidth / (len(data)+1)
    offset = 10
    spacing = 10
    normalizedData = [i/max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i*xWidth + offset + spacing
        y0 = visualizerCanvasHeight - height * 400

        x1 = (i+1) * xWidth
        y1 = visualizerCanvasHeight

        visualizerCanvas.create_rectangle(x0,y0,x1,y1, fill="#A90042")
        visualizerCanvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]), font=("new roman", 15, "bold italic"), 
                                        fill="orange")

def Generate():
    print("Selected Algorithm: " + selectedAlgo.get())
    data = [1,5,6,8,7,9,1,3,4,5]
    drawData(data)

selectedAlgo = StringVar()

# CREATING DIFFERENT LABELS, BUTTONS AND SPEED OF ALGO

mainLabel = Label(root, text="Choose Algorithm", font=("ariel", 13, "bold italic"),
                   bg="#05897a",width=15, fg="black",relief=GROOVE,bd=5)
mainLabel.place(x=0,y=0)

algos = ttk.Combobox(root, width=14, font=("ariel", 17, "bold italic"),
                    textvariable=selectedAlgo,
                    values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Selection Sort'])

algos.place(x=200,y=0)
algos.current(0) #This keeps the default set to algos[0] i.e. Bubble Sort

# Creating random array 

randomArr = Button(root, text="Generate", bg="#2DAE9A", font=("ariel",12, "bold italic"), relief=SUNKEN,
                   activebackground="#05945B", activeforeground="white", bd=5, width=10, command=Generate)

randomArr.place(x=750, y=60)

# Size of array to be created

sizeChangerLabel = Label(root, text="Size: ", font=("new roman", 12, "bold italic"), bg="#0E6DA5",
                       width=10, fg="black", height=2, relief=GROOVE, bd=5)
sizeChangerLabel.place(x=0,y=60)

sizeValue = Scale(root, from_=0, to=30, resolution=1, orient=HORIZONTAL,font=("new roman", 14, "bold italic"),
                   relief=GROOVE, bd=2, width=10)
sizeValue.place(x=125, y=60)

# Minimum value

minimumChangerLabel = Label(root, text="Min Value: ", font=("new roman", 12, "bold italic"), bg="#0E6DA5",
                       width=10, fg="black", height=2, relief=GROOVE, bd=5)
minimumChangerLabel.place(x=260,y=60)

minimumValue = Scale(root, from_=0, to=10, resolution=1, orient=HORIZONTAL,font=("new roman", 14, "bold italic"),
                   relief=GROOVE, bd=2, width=10)
minimumValue.place(x=385, y=60)


# Maximum Value 

maximumChangerLabel = Label(root, text="Max Value: ", font=("new roman", 12, "bold italic"), bg="#0E6DA5",
                       width=10, fg="black", height=2, relief=GROOVE, bd=5)
maximumChangerLabel.place(x=500,y=60)

maximumValue = Scale(root, from_=0, to=100, resolution=1, orient=HORIZONTAL,font=("new roman", 14, "bold italic"),
                   relief=GROOVE, bd=2, width=10)
maximumValue.place(x=625, y=60)


# Start the visualization

start = Button(root, text="Start!", bg="#C45B09", font=("ariel",12, "bold italic"), relief=SUNKEN,
                   activebackground="#05945B", activeforeground="white", bd=5, width=10)

start.place(x=750, y=0)

speedLabel = Label(root, text="Speed: ", font=("new roman", 12, "bold italic"), bg="#0E6DA5",
                       width=10, fg="black", relief=GROOVE, bd=5, height=1)
speedLabel.place(x=445,y=0)

speedScale = Scale(root, from_=0.1, to=5.0, resolution=1, orient=HORIZONTAL,font=("new roman", 14, "bold italic"),
                   relief=GROOVE, bd=2, width=10)
speedScale.place(x=570, y=0)


# The canvas where the sorting is visualized

visualizerCanvas = Canvas(root, bg="black", width=870, height=450)
visualizerCanvas.place(x=10, y=130)


root.mainloop()