from tkinter import *

window = Tk()
icon = PhotoImage(file='./not_code_files/git_with_glasses.png')
button = Button(window, text='click on me')

def click():
    print('clicked')

window.title("search git commands")
window.geometry("1020x650")
window.iconphoto(True, icon)
window.config(background="#3c3a56")

button.config(command=click)
button.config(font=("Arial", 35, 'bold'))
button.config(bg='#689a9d')
button.config(fg='#ffffff')
button.pack()


window.mainloop()