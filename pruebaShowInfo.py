from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter.messagebox import askokcancel, showinfo, WARNING

app = []


def main():
    USER_INP = simpledialog.askstring(title="App Name",
                                      prompt="Insert the name of the app:")

    print(USER_INP)
    answer = askokcancel(
        title='DELETION',
        message='Are you sure?',
        icon=WARNING)

    if answer:
        print(answer)
        messagebox.showinfo("INFO", "User pressed yes")
        app.append(USER_INP)
    else:
        messagebox.showinfo("INFO", "User pressed cancel")


root = Tk()

myButton = Button(root, text='input', command=main)
myButton.pack()

root.mainloop()