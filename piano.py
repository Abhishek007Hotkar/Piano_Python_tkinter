#48 keys in the keyboard

from tkinter import *
import keyboard
from playsound import playsound
import pygame
from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init() 
pygame.init()

#<---------------For refering to the black note names for displaying on the keys--------------->

IndexBlackNoteNames = { 0: 'Db3',1: 'Eb3',2: 'Gb3',3: 'Ab3',4: 'Bb3',5: 'Db4',6: 'Eb4',7: 'Gb4'
,8: 'Ab4',9: 'Bb4',10: 'Db5',11: 'Eb5',12: 'Gb5',13: 'Ab5',14: 'Bb5',15: 'Db6',16: 'Eb6',17: 'Gb6',18: 'Ab6',
19: 'Bb6'}

#<---------------For refering to the white note names for displaying on the keys--------------->

IndexWhiteNoteNames = { 0: 'C3',1: 'D3',2: 'E3',3: 'F3',4: 'G3',5: 'A3',6: 'B3',7: 'C4'
,8: 'D4',9: 'E4',10: 'F4',11: 'G4',12: 'A4',13: 'B4',14: 'C5',15: 'D5',16: 'E5',17: 'F5',18: 'G5',
19: 'A5',20: 'B5',21: 'C6',22: 'D6',23: 'E6',24: 'F6',25: 'G6',26: 'A6',27: 'B6',28: 'C7'}

#<-------------------------------Draw white keys---------------------------------->
def MakeWhiteKeys():
	white_key_array = [0]*29
	rectx_white = 50
	key_width_white = 35
	rectx_2_white = rectx_white+key_width_white
	for i in range(29):
			rectx_white=rectx_white+key_width_white
			rectx_2_white=rectx_white+2*key_width_white
			if(i == 28):	
				white_key_array[i] = canvas.create_rectangle(rectx_white,50,rectx_2_white-35,300,fill="white")
				canvas.create_text((rectx_white+15,280),text = IndexWhiteNoteNames.get(i),fill = "black",font = "'Oxanium 10 italic bold")

			else:
				white_key_array[i] = canvas.create_rectangle(rectx_white,50,rectx_2_white,300,fill="white")
				canvas.create_text((rectx_white+15,280),text = IndexWhiteNoteNames.get(i),fill = "black",font = "'Oxanium 10 italic bold")

		
	return white_key_array

#<-------------------------------Draw black keys---------------------------------->

def MakeBlackKeys():
	black_key_array = [0]*20
	rectx_black = 110
	key_width_black = 20 
	rectx_2_black = rectx_black+key_width_black
	for i in range(20):
		rectx_2_black = rectx_black+key_width_black
		black_key_array[i] = canvas.create_rectangle(rectx_black,50,rectx_2_black,230,fill="black")
		canvas.create_text((rectx_black+10,210),text = IndexBlackNoteNames.get(i),fill = "white",font = "'Oxanium 7 italic bold")
		if(i==1 or i==4 or i==6 or i==9 or i==11 or i==14 or i==16 or i==19):
			rectx_black = rectx_black+70
		else:
			rectx_black = rectx_black+35

		rectx_2_black = rectx_2_black+key_width_black	
	
	return black_key_array


#<-------------------------------Play notes---------------------------------->

def Playmusic(key,note_name,fileName):
		canvas.itemconfig(key, fill= "blue")
		canvas.itemconfig(key_text, text = note_name)
		#playsound(fileName)
		pygame.mixer.music.load(fileName)
		pygame.mixer.music.play(1)
		if key in white_key_objects:
			canvas.itemconfig(key,fill= "white")
		else:
			canvas.itemconfig(key,fill= "black")
		
		

window = Tk()
window.title("PIANO")
canvas = Canvas(window,width = 1400,height = 600)
white_key_objects = MakeWhiteKeys()
black_key_objects = MakeBlackKeys()
canvas.create_rectangle(1150,70,1250,140,fill = 'yellow')
key_text = canvas.create_text((1200,100) ,text = '',fill="darkblue",font="Times 20 italic bold")

#--------------Hotkeys for playing white keys ----------------------------------------#

keyboard.add_hotkey('q', lambda:Playmusic(white_key_objects[0],'C3','D:\\PythonProjects\\PianoProg\\note_sounds\\C3.mp3'))
keyboard.add_hotkey('w', lambda:Playmusic(white_key_objects[1],'D3','D:\\PythonProjects\\PianoProg\\note_sounds\\D3.mp3'))
keyboard.add_hotkey('e', lambda:Playmusic(white_key_objects[2],'E3','D:\\PythonProjects\\PianoProg\\note_sounds\\E3.mp3'))
keyboard.add_hotkey('r', lambda:Playmusic(white_key_objects[3],'F3','D:\\PythonProjects\\PianoProg\\note_sounds\\F3.mp3'))
keyboard.add_hotkey('t', lambda:Playmusic(white_key_objects[4],'G3','D:\\PythonProjects\\PianoProg\\note_sounds\\G3.mp3'))
keyboard.add_hotkey('y', lambda:Playmusic(white_key_objects[5],'A3','D:\\PythonProjects\\PianoProg\\note_sounds\\A3.mp3'))
keyboard.add_hotkey('u', lambda:Playmusic(white_key_objects[6],'B3','D:\\PythonProjects\\PianoProg\\note_sounds\\B3.mp3'))
keyboard.add_hotkey('i', lambda:Playmusic(white_key_objects[7],'C4','D:\\PythonProjects\\PianoProg\\note_sounds\\C4.mp3'))
keyboard.add_hotkey('o', lambda:Playmusic(white_key_objects[8],'D4','D:\\PythonProjects\\PianoProg\\note_sounds\\D4.mp3'))
keyboard.add_hotkey('p', lambda:Playmusic(white_key_objects[9],'E4','D:\\PythonProjects\\PianoProg\\note_sounds\\E4.mp3'))
keyboard.add_hotkey('a', lambda:Playmusic(white_key_objects[10],'F4','D:\\PythonProjects\\PianoProg\\note_sounds\\F4.mp3'))
keyboard.add_hotkey('s', lambda:Playmusic(white_key_objects[11],'G4','D:\\PythonProjects\\PianoProg\\note_sounds\\G4.mp3'))
keyboard.add_hotkey('d', lambda:Playmusic(white_key_objects[12],'A4','D:\\PythonProjects\\PianoProg\\note_sounds\\A4.mp3'))
keyboard.add_hotkey('f', lambda:Playmusic(white_key_objects[13],'B4','D:\\PythonProjects\\PianoProg\\note_sounds\\B4.mp3'))
keyboard.add_hotkey('g', lambda:Playmusic(white_key_objects[14],'C5','D:\\PythonProjects\\PianoProg\\note_sounds\\C5.mp3'))
keyboard.add_hotkey('h', lambda:Playmusic(white_key_objects[15],'D5','D:\\PythonProjects\\PianoProg\\note_sounds\\D5.mp3'))
keyboard.add_hotkey('j', lambda:Playmusic(white_key_objects[16],'E5','D:\\PythonProjects\\PianoProg\\note_sounds\\E5.mp3'))
keyboard.add_hotkey('k', lambda:Playmusic(white_key_objects[17],'F5','D:\\PythonProjects\\PianoProg\\note_sounds\\F5.mp3'))
keyboard.add_hotkey('l', lambda:Playmusic(white_key_objects[18],'G5','D:\\PythonProjects\\PianoProg\\note_sounds\\G5.mp3'))
keyboard.add_hotkey('z', lambda:Playmusic(white_key_objects[19],'A5','D:\\PythonProjects\\PianoProg\\note_sounds\\A5.mp3'))
keyboard.add_hotkey('x', lambda:Playmusic(white_key_objects[20],'B5','D:\\PythonProjects\\PianoProg\\note_sounds\\B5.mp3'))
keyboard.add_hotkey('c', lambda:Playmusic(white_key_objects[21],'C6','D:\\PythonProjects\\PianoProg\\note_sounds\\C6.mp3'))
keyboard.add_hotkey('v', lambda:Playmusic(white_key_objects[22],'D6','D:\\PythonProjects\\PianoProg\\note_sounds\\D6.mp3'))
keyboard.add_hotkey('b', lambda:Playmusic(white_key_objects[23],'E6','D:\\PythonProjects\\PianoProg\\note_sounds\\E6.mp3'))
keyboard.add_hotkey('n', lambda:Playmusic(white_key_objects[24],'F6','D:\\PythonProjects\\PianoProg\\note_sounds\\F6.mp3'))
keyboard.add_hotkey('m', lambda:Playmusic(white_key_objects[25],'G6','D:\\PythonProjects\\PianoProg\\note_sounds\\G6.mp3'))
keyboard.add_hotkey(',', lambda:Playmusic(white_key_objects[26],'A6','D:\\PythonProjects\\PianoProg\\note_sounds\\A6.mp3'))
keyboard.add_hotkey('.', lambda:Playmusic(white_key_objects[27],'B6','D:\\PythonProjects\\PianoProg\\note_sounds\\B6.mp3'))
keyboard.add_hotkey('/', lambda:Playmusic(white_key_objects[28],'C7','D:\\PythonProjects\\PianoProg\\note_sounds\\C7.mp3'))


#--------------Hotkeys for playing black keys ----------------------------------------#


keyboard.add_hotkey('shift+q', lambda:Playmusic(black_key_objects[0],'Db3','D:\\PythonProjects\\PianoProg\\note_sounds\\Db3.mp3'))
keyboard.add_hotkey('shift+w', lambda:Playmusic(black_key_objects[1],'Eb3','D:\\PythonProjects\\PianoProg\\note_sounds\\Eb3.mp3'))
keyboard.add_hotkey('shift+e', lambda:Playmusic(black_key_objects[2],'Gb3','D:\\PythonProjects\\PianoProg\\note_sounds\\Gb3.mp3'))
keyboard.add_hotkey('shift+r', lambda:Playmusic(black_key_objects[3],'Ab3','D:\\PythonProjects\\PianoProg\\note_sounds\\Ab3.mp3'))
keyboard.add_hotkey('shift+t', lambda:Playmusic(black_key_objects[4],'Bb3','D:\\PythonProjects\\PianoProg\\note_sounds\\Bb3.mp3'))
keyboard.add_hotkey('shift+y', lambda:Playmusic(black_key_objects[5],'Db4','D:\\PythonProjects\\PianoProg\\note_sounds\\Db4.mp3'))
keyboard.add_hotkey('shift+u', lambda:Playmusic(black_key_objects[6],'Eb4','D:\\PythonProjects\\PianoProg\\note_sounds\\Eb4.mp3'))
keyboard.add_hotkey('shift+i', lambda:Playmusic(black_key_objects[7],'Gb4','D:\\PythonProjects\\PianoProg\\note_sounds\\Gb4.mp3'))
keyboard.add_hotkey('shift+o', lambda:Playmusic(black_key_objects[8],'Ab4','D:\\PythonProjects\\PianoProg\\note_sounds\\Ab4.mp3'))
keyboard.add_hotkey('shift+p', lambda:Playmusic(black_key_objects[9],'Bb4','D:\\PythonProjects\\PianoProg\\note_sounds\\Bb4.mp3'))
keyboard.add_hotkey('shift+a', lambda:Playmusic(black_key_objects[10],'Db5','D:\\PythonProjects\\PianoProg\\note_sounds\\Db5.mp3'))
keyboard.add_hotkey('shift+s', lambda:Playmusic(black_key_objects[11],'Eb5','D:\\PythonProjects\\PianoProg\\note_sounds\\Eb5.mp3'))
keyboard.add_hotkey('shift+d', lambda:Playmusic(black_key_objects[12],'Gb5','D:\\PythonProjects\\PianoProg\\note_sounds\\Gb5.mp3'))
keyboard.add_hotkey('shift+f', lambda:Playmusic(black_key_objects[13],'Ab5','D:\\PythonProjects\\PianoProg\\note_sounds\\Ab5.mp3'))
keyboard.add_hotkey('shift+g', lambda:Playmusic(black_key_objects[14],'Bb5','D:\\PythonProjects\\PianoProg\\note_sounds\\Bb5.mp3'))
keyboard.add_hotkey('shift+h', lambda:Playmusic(black_key_objects[15],'Db6','D:\\PythonProjects\\PianoProg\\note_sounds\\Db6.mp3'))
keyboard.add_hotkey('shift+j', lambda:Playmusic(black_key_objects[16],'Eb6','D:\\PythonProjects\\PianoProg\\note_sounds\\Eb6.mp3'))
keyboard.add_hotkey('shift+k', lambda:Playmusic(black_key_objects[17],'Gb6','D:\\PythonProjects\\PianoProg\\note_sounds\\Gb6.mp3'))
keyboard.add_hotkey('shift+l', lambda:Playmusic(black_key_objects[18],'Ab6','D:\\PythonProjects\\PianoProg\\note_sounds\\Ab6.mp3'))
keyboard.add_hotkey('shift+z', lambda:Playmusic(black_key_objects[19],'Bb6','D:\\PythonProjects\\PianoProg\\note_sounds\\Bb6.mp3'))


canvas.pack()
window.mainloop()
