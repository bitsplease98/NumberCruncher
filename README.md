# NumberCruncher
Calculator

## Technology Used:

1.Python Language

2.Tkinter Library

## Sample Code

1.Tkinter Window

```
mainwindow = Tk()
mainwindow.title('Number Cruncher')
```

2.Making Buttons

```
def makebutton(root, text):
    button = Button(root, text=text, bg="bisque", relief="raised",
                    font=('arial 15 bold'),
                    width=10, height=2,
                    command=lambda: buttonpressed(text))
    button.pack(side='left', fill='both', expand='yes')
    button['command'] = lambda: buttonpressed(text)
    return button
```

3.Actions on clicking buttons

```
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
```

## Screenshots

![img](https://github.com/bitsplease98/NumberCruncher/blob/master/numb1.PNG)

![img](https://github.com/bitsplease98/NumberCruncher/blob/master/numb2.PNG)


