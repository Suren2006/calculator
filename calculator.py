from tkinter import *
import tkinter.font as font
import math

t = Tk()
t.title('Calculator by Suren')
t.geometry('320x500')
t['bg'] = '#212121'
t.wm_attributes('-alpha', 0.95)

def zero(event):
    if label1['text'] == 0:
        label1['text'] = btn['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = label1['text'] * 10

def one(event):
    if label1['text'] == 0:
        label1['text'] = btn1['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn1['text']


def two(event):
    if label1['text'] == 0:
        label1['text'] = btn2['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn2['text']

def three(event):
    if label1['text'] == 0:
        label1['text'] = btn3['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn3['text']


def four(event):
    if label1['text'] == 0:
        label1['text'] = btn4['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn4['text']

def five(event):
    if label1['text'] == 0:
        label1['text'] = btn5['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn5['text']


def six(event):
    if label1['text'] == 0:
        label1['text'] = btn6['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn6['text']

def seven(event):
    if label1['text'] == 0:
        label1['text'] = btn7['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn7['text']


def eight(event):
    if label1['text'] == 0:
        label1['text'] = btn8['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn8['text']

def nine(event):
    if label1['text'] == 0:
        label1['text'] = btn9['text']
    else:
        h = len(str(label1['text']))
        label1['text'] = (label1['text'] * 10) + btn9['text']



def devide(event):
    btn_baj['bg'] = 'black'
    btn_bazm['bg'] = '#212121'
    btn_hanum['bg'] = '#212121'
    btn_gumar['bg'] = '#212121'
    label2['text'] = label1['text']
    label1['text']= 0

def times(event):
    btn_bazm['bg'] = 'black'
    btn_baj['bg'] = '#212121'
    btn_hanum['bg'] = '#212121'
    btn_gumar['bg'] = '#212121'
    label2['text'] = label1['text']
    label1['text']= 0

def minus(event):
    btn_hanum['bg'] = 'black'
    btn_bazm['bg'] = '#212121'
    btn_baj['bg'] = '#212121'
    btn_gumar['bg'] = '#212121'
    label2['text'] = label1['text']
    label1['text']= 0

def plus(event):
    btn_gumar['bg'] = 'black'
    btn_bazm['bg'] = '#212121'
    btn_hanum['bg'] = '#212121'
    btn_baj['bg'] = '#212121'
    label2['text'] = label1['text']
    label1['text']= 0

def ce():
    label1['text'] = 0
    label2['text'] = ''
    btn_baj['bg'] = '#212121'
    btn_bazm['bg'] = '#212121'
    btn_hanum['bg'] = '#212121'
    btn_gumar['bg'] = '#212121'

def c():
    label1['text'] = 0

def backspace(event):
    label1['text'] = math.floor(label1['text'] / 10)

def havasar(event):
    if btn_baj['bg'] == 'black':
        label1['text'] = round(label2['text'] / label1['text'], 4)
    if btn_bazm['bg'] == 'black':
        label1['text'] = round(label2['text'] * label1['text'], 4)
    if btn_hanum['bg'] == 'black':
        label1['text'] = round(label2['text'] - label1['text'], 4)
    if btn_gumar['bg'] == 'black':
        label1['text'] = round(label2['text'] + label1['text'], 4)
    label2['text'] = ''
    btn_baj['bg'] = '#212121'
    btn_bazm['bg'] = '#212121'
    btn_hanum['bg'] = '#212121'
    btn_gumar['bg'] = '#212121'

    

t.bind('0', zero)
t.bind('1', one)
t.bind('2', two)
t.bind('3', three)
t.bind('4', four)
t.bind('5', five)
t.bind('6', six)
t.bind('7', seven)
t.bind('8', eight)
t.bind('9', nine)
t.bind('/', devide)
t.bind('*', times)
t.bind('-', minus)
t.bind('+', plus)
t.bind('<BackSpace>', backspace)
t.bind('<Return>', havasar)

canvas1 = Canvas(t, height=150, width=310, bg='#343434', border=10)
canvas1.place(relx=0.5, rely=0.16, anchor=CENTER)

label1 = Label(canvas1, bg='#343434', fg='#ffffff')
label1['text'] = 0 
label1['font'] = font.Font(size=48)
label1.place(relx=0.95, rely=0.9, anchor=SE)

label2 = Label(canvas1, bg='#343434', fg='grey')
label2['text'] = ''
label2['font'] = font.Font(size=32)
label2.place(relx=0.98, rely=0.02, anchor=NE)   


canvas2 = Canvas(t, height=300, width=310, bg='#ffffff', border=0)
canvas2.place(relx=0.5, rely=0.69, anchor=CENTER)

canvas3 = Canvas(canvas2, height=240, width=240, bg='#ffffff')
canvas3.place(relx=0, rely=1, anchor=SW)

btn = Button(canvas3, text=0 , bg='#212121', fg='#ffffff', command=zero)
btn['font'] = font.Font(size=20)
btn.place(relx=0.5, rely=0.99, relwidth=0.32, relheight=0.239, anchor=S)

btn1 = Button(canvas3, text= 1 , bg='#212121', fg='#ffffff', command=one)
btn1['font'] = font.Font(size=20)
btn1.place(relx=0.01, rely=0.621, relwidth=0.32, relheight=0.239, anchor=W)

btn2 = Button(canvas3, text= 2 , bg='#212121', fg='#ffffff', command=two)
btn2['font'] = font.Font(size=20)
btn2.place(relx=0.5, rely=0.621, relwidth=0.32, relheight=0.239, anchor=CENTER)

btn3 = Button(canvas3, text= 3 , bg='#212121', fg='#ffffff', command=three)
btn3['font'] = font.Font(size=20)
btn3.place(relx=0.99, rely=0.621, relwidth=0.32, relheight=0.239, anchor=E)

btn4 = Button(canvas3, text= 4 , bg='#212121', fg='#ffffff', command=four)
btn4['font'] = font.Font(size=20)
btn4.place(relx=0.01, rely=0.37, relwidth=0.32, relheight=0.239, anchor=W)

btn5 = Button(canvas3, text= 5 , bg='#212121', fg='#ffffff', command=five)
btn5['font'] = font.Font(size=20)
btn5.place(relx=0.5, rely=0.37, relwidth=0.32, relheight=0.239, anchor=CENTER)

btn6 = Button(canvas3, text= 6 , bg='#212121', fg='#ffffff', command=six)
btn6['font'] = font.Font(size=20)
btn6.place(relx=0.99, rely=0.37, relwidth=0.32, relheight=0.239, anchor=E)

btn7 = Button(canvas3, text= 7 , bg='#212121', fg='#ffffff', command=seven)
btn7['font'] = font.Font(size=20)
btn7.place(relx=0.01, rely=0.001, relwidth=0.32, relheight=0.239, anchor=NW)

btn8 = Button(canvas3, text= 8, bg='#212121', fg='#ffffff', command=eight)
btn8['font'] = font.Font(size=20)
btn8.place(relx=0.5, rely=0.001, relwidth=0.32, relheight=0.239, anchor=N)

btn9 = Button(canvas3, text= 9 , bg='#212121', fg='#ffffff', command=nine)
btn9['font'] = font.Font(size=20)
btn9.place(relx=0.99, rely=0.001, relwidth=0.32, relheight=0.239, anchor=NE)

btn10 = Button(canvas3, text=' ± ', bg='#212121', fg='#ffffff')
btn10['font'] = font.Font(size=20)
btn10.place(relx=0.01, rely=0.99, relwidth=0.32, relheight=0.239, anchor=SW)

btn11 = Button(canvas3, text=' , ', bg='#212121', fg='#ffffff')
btn11['font'] = font.Font(size=20)
btn11.place(relx=0.99, rely=0.99, relwidth=0.32, relheight=0.239, anchor=SE)

btn_backspace = Button(canvas2, text=' ⊠ ', bg='#212121', fg='#ffffff')
btn_backspace['font'] = font.Font(size=18)
btn_backspace.place(relx=0.523, rely=0.01, relwidth=0.248, relheight=0.185, anchor=NW)

btn_baj = Button(canvas2, text=' ÷ ', bg='#212121', fg='#ffffff', command=devide)
btn_baj['font'] = font.Font(size=18)
btn_baj.place(relx=0.99, rely=0.01, relwidth=0.21, relheight=0.185, anchor=NE)

btn_bazm = Button(canvas2, text=' × ', bg='#212121', fg='#ffffff', command=times)
btn_bazm['font'] = font.Font(size=18)
btn_bazm.place(relx=0.99, rely=0.199, relwidth=0.21, relheight=0.194, anchor=NE)

btn_hanum = Button(canvas2, text=' - ', bg='#212121', fg='#ffffff', command=minus)
btn_hanum['font'] = font.Font(size=18)
btn_hanum.place(relx=0.99, rely=0.398, relwidth=0.21, relheight=0.194, anchor=NE)

btn_gumar = Button(canvas2, text=' + ', bg='#212121', fg='#ffffff', command=plus)
btn_gumar['font'] = font.Font(size=18)
btn_gumar.place(relx=0.99, rely=0.601, relwidth=0.21, relheight=0.194, anchor=NE)

btn_havasar = Button(canvas2, text=' = ', bg='#212121', fg='#ffffff', command=havasar)
btn_havasar['font'] = font.Font(size=18)
btn_havasar.place(relx=0.99, rely=0.804, relwidth=0.21, relheight=0.194, anchor=NE)

btn_ce = Button(canvas2, text=' CE ', bg='#212121', fg='#ffffff', command=ce)
btn_ce['font'] = font.Font(size=18)
btn_ce.place(relx=0.01, rely=0.01, relwidth=0.248, relheight=0.185, anchor=NW)

btn_c = Button(canvas2, text=' C ', bg='#212121', fg='#ffffff', command=c)
btn_c['font'] = font.Font(size=18)
btn_c.place(relx=0.265, rely=0.01, relwidth=0.248, relheight=0.185, anchor=NW)

t.mainloop()
