from tkinter import *
import speech as srf
import speec

button_clicked = False

def clicked():
    button_clicked = True
    speec.speech()
    #srf.main()

def clicked1():
    button_clicked = True
    #speec.speech()
    srf.main()
    	
root = Tk()

frame = Frame(root, width = 200, height = 100)
frame.pack()

root.title('speech recognition')

label = Label(root, font = 3, text = "SPEAK SOMETHING..", bg = 'orange')
label.pack()

butto1 = Button(root, text = 'speak to open', font = 5, bg = 'blue', fg = 'white', command = clicked).pack()
butto2 = Button(root, text = 'click to speak', font = 5, bg = 'blue', fg = 'white', command = clicked1).pack()

root.mainloop()
#inp = input('Enter to exit')
