import tkinter.ttk
from tkinter import *

import googletrans
from PIL import Image,ImageTk
from googletrans import Translator

#Tạo khung app
root = Tk()
root.title('Google Translate')
root.geometry("1000x640")
root.iconbitmap('logo.ico')
root.resizable(0,0)

#Tải ảnh nền và vị trí ảnh
load = Image.open('assets/Global.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.place(x = 0, y = 0)

#Đặt tên
name = Label(root, text = 'Translate', fg = 'white', bd = 0, bg = '#719DCC')
name.config(font = ('assets/Lato-Regular',30))
name.pack(pady = 10)

#chọn ngôn ngữ đầu vào và đầu ra
label_input = Label(root, text = 'Choose input language', fg = 'white', bg = '#6392C8')
label_input.place(x = 80, y = 60)
lan_input = tkinter.ttk.Combobox(root, value = list(googletrans.LANGUAGES.values()))
lan_input.place(x = 220, y = 60)
label_input = Label(root, text = 'Choose output language', fg = 'white', bg = '#7CA2D1')
label_input.place(x = 80, y = 340)
lan_output = tkinter.ttk.Combobox(root, value = list(googletrans.LANGUAGES.values()))
lan_output.place(x = 220, y = 340)

#Textbox để nhập ngôn ngữ cần dịch
box_input = Text(root, width = 70, height = 8, font = ("ROBOTO",16))
box_input.pack(pady = 20)

#khung button
button_frame = Frame(root).pack(side = BOTTOM)

# Hàm dịch
def translate():
    input = box_input.get(1.0, END)
    box_output.delete(1.0, END)
    print(input)
    t = Translator()
    output = t.translate(input, src=lan_input.get(), dest=lan_output.get())
    result = output.text
    box_output.insert(END, result)

#Hàm xoá chữ
def clear():
    box_input.delete(1.0,END)
    box_output.delete(1.0,END)

#Tạo nút translate và đặt vị trí
button_translate = Button(button_frame, text = 'Translate', font = (('Arial'),10,'bold'), bg = '#4E647B', fg = 'white', command = translate)
button_translate.place(x = 350, y = 300)

#Tạo nút clear và đặt vị trí
button_clear = Button(button_frame, text = 'Clear text', font = (('Arial'),10,'bold'), bg = '#4E647B', fg = 'white', command = clear)
button_clear.place(x = 600, y = 300)

#Textbox hiện kết quả sau khi dịch
box_output = Text(root, width = 70, height = 8, font = ("ROBOTO",16))
box_output.pack(pady = 60)

root.mainloop()