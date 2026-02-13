from tkinter import *

window = Tk()
icon = PhotoImage(file='./not_code_files/git_with_glasses.png')
button_icon = PhotoImage(file='./not_code_files/button.png')
button = Button(window, text='click on me')
label = Label(window, text='hello world')
button_icon = button_icon.subsample(12, 12)
entry = Entry()

def click():
    username = entry.get()
    print(username)

window.title("search git commands")
window.geometry("1020x650")
window.iconphoto(True, icon)
window.config(background="#3c3a56")

entry.config(bg="#111111")
entry.config(fg="#00ff00")
entry.config(font=("Ink free", 35, 'bold'))
entry.config(width=20)
entry.pack(pady=(20, 10))

button.config(bg='#689a9d')
button.config(fg='#ffffff')
button.config(activebackground="#191d27")
button.config(activeforeground="#2846a9")
button.config(padx=8)
button.config(command=click)
button.config(image=button_icon, state='active')
button.config(compound="left")
button.config(width=300, height=65)
button.config(font=("Arial", 35, 'bold'))
button.pack()

window.mainloop()