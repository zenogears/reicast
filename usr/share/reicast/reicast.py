#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
import tkMessageBox
import os
import getpass

conf_dir_path = "/home/" + getpass.getuser() + "/.reicast"

def start():
  os.system('/usr/bin/reicast.elf')

def open_iso():
  if not os.path.exists(conf_dir_path):
    tkMessageBox.showinfo("Error", "Ошибочка, запустите сначала эмулятор для создания файлов.")
  else:
    fn = tkFileDialog.Open(root, filetypes = [('*.cdi files', '.cdi')]).show()
    if fn == '':
      return
    path_to_iso = fn
  

  
## GUI
root = Tk()
root.title("reicast")
frame = Frame(root)
frame.pack()

start_button = Button(frame, text = 'Запустить эмулятор', command=start, width=10)
start_button.grid(row=0, column=0)

open_button = Button(frame, text = 'Выбрать образ', width=10, command=open_iso)
open_button.grid(row=1, column=0)

exit_button = Button(frame, text = 'Выход', width=10, command="exit 0")
exit_button.grid(row=2, column=0)

root.mainloop()
## END GUI
