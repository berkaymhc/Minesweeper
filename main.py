from tkinter import *


root = Tk()
# Override the setttings of the window
root.configure(bg="gray")
root.geometry('600x600')
root.title("Minesweeper Game")
# root.resizable(False,False)

top_frame = Frame(
    root,
    bg='red', # Change later to black
    width=600,
    height=100
)
top_frame.place(x=0,y=0)



# Run the window
root.mainloop()