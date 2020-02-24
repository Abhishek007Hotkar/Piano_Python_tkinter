#48 keys in the keyboard

from tkinter import *
import keyboard


play_notes_when_key_pressed=[[]]




window = Tk()

window.title("PIANO")
canvas = Canvas(window,width = 1400,height = 300)
rectx = 50
rectx_2 = 90
key_width = 40
for i in range(29):
		rectx=rectx+key_width
		rectx_2=rectx+2*key_width
	
		canvas.create_rectangle(rectx,50,rectx_2,250,fill="white")
		
	


canvas.pack()
window.mainloop()