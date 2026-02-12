from tkinter import *

window = Tk()
icon = PhotoImage(file='./not_code_files/git_with_glasses.png')
button_icon = PhotoImage(file='./not_code_files/button.png')
button = Button(window, text='click on me')
label = Label(window, text='hello world')
button_icon = button_icon.subsample(12, 12)

def click():
    print('clicked')

window.title("search git commands")
window.geometry("1020x650")
window.iconphoto(True, icon)
window.config(background="#3c3a56")

button.config(activebackground="#191d27")
button.config(padx=8)
button.config(activeforeground="#2846a9")
button.config(command=click)
button.config(image=button_icon, state='active')
button.config(compound="left")
button.config(width=300, height=65)
button.config(font=("Arial", 35, 'bold'))
button.config(bg='#689a9d')
button.config(fg='#ffffff')
button.pack()

label.config(bg='#586137')
label.config(compound='top')
label.config(font=("Arial", 36, 'bold'))
label.config(width=24)
label.pack()

window.mainloop()