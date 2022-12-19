from tkinter import *
import pyautogui
root = Tk()
root.title("Screenshot App")
root.geometry('400x400')

frame = Frame(root)
frame.pack()

def takeSS():
    mySS = pyautogui.screenshot()

button = Button(frame, text="Screenshot" , command="takeSS")
button.pack()


root.mainloop()
