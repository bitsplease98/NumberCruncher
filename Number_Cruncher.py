from tkinter import *
from tkinter import messagebox

mainwindow = Tk()
mainwindow.title('Number Cruncher')

def makeframe(root):
    a = Frame(root)
    a.pack(fill='both', expand='yes')
    return a


displayvar = StringVar()
t1 = Entry(makeframe(mainwindow), font=('arial 55 bold'), fg="gray7",
           justify="right", relief="sunken", bd=3, textvariable=displayvar)
t1.pack(fill='both', expand="yes", side="top")


def buttonpressed(text):
    s = displayvar.get()
    if (text == 'C'):
        displayvar.set(s[:-1])
    elif (text == 'CE'):
        displayvar.set('')
    elif (text == '='):
        try:
            displayvar.set(eval(s))
        except:
            displayvar.set('')
            messagebox.showerror('ERROR', 'Do not type alphabets')
    else:
        displayvar.set(s + text)

    return

def makebutton(root, text):
    button = Button(root, text=text, bg="bisque", relief="raised",
                    font=('arial 15 bold'),
                    width=10, height=2,
                    command=lambda: buttonpressed(text))
    button.pack(side='left', fill='both', expand='yes')
    button['command'] = lambda: buttonpressed(text)
    return button


button_data = [('C'),
               (['CE']),
               ('7', '8', '9', '(', ')'),
               ('4', '5', '6', '*', '**'),
               ('1', '2', '3', '/', '%'),
               ('.', '0', '=', '+', '-')]

keypad = makeframe(mainwindow)
for i in button_data:
    a = makeframe(keypad)
    for j in i:
        makebutton(a, j)

mainwindow.mainloop()

