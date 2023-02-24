from tkinter import *
from tkinter import messagebox
import pickle

HEIGHT = 550
WIDTH = 550

def singup():
    label_error = None

    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')

    label = Label(frame, text='Sing Up', font='16')
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text='Login: ')
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_reg = Entry(frame)
    login_reg.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)

    pass_label1 = Label(frame, text='Passworg:')
    pass_label1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show='*')
    password1.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)

    pass_label2 = Label(frame, text='Confim Passworg:')
    pass_label2.place(rely=0.6, relwidth=0.35, relheight=0.1)

    password2 = Entry(frame, show='*')
    password2.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.55)

    button = Button(frame, text='Sing Up', command=lambda: reg())
    button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)

    def reg():
        nonlocal label_error
        error = ''
        if label_error:
            label_error.destroy()
        if len(login_reg.get()) == 0:
            error = 'Login error'
        elif len(password1.get()) <6:
            error = 'May be least 6 character'
        elif not password1.get() == password2.get():
            error = 'Password error'
        else:
            save()
        label_error = Label(frame, text=error, fg = 'red')
        label_error.place(rely=0.7)
    def save():
        data = dict()
        data[login_reg.get()] = password1.get()
        file = open('login.txt', 'wb')
        pickle.dump(data, file)
        file.close()
        singin()

def singin():
    label_error = None

    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')

    label = Label(frame, text='Sing In', font='16')
    label.place(relwidth=1, relheight=0.1)

    label_login = Label(frame, text='Login: ')
    label_login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    login_reg = Entry(frame)
    login_reg.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)

    pass_label1 = Label(frame, text='Passworg:')
    pass_label1.place(rely=0.4, relwidth=0.35, relheight=0.1)

    password1 = Entry(frame, show='*')
    password1.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)

    button = Button(frame, text='Sing In', command=lambda: qwe())
    button.place(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.5)

    def qwe():
        nonlocal label_error
        error = ''
        if label_error:
            label_error.destroy()
        if len(login_reg.get()) == 0:
            error = 'Login error'
        elif len(password1.get()) < 6:
            error = 'May be least 6 character'
        elif not password1.get() == password1.get():
            error = 'Password error'
        else:
            save()
        label_error = Label(frame, text=error, fg='red')
        label_error.place(rely=0.7)

    def save():
        data = dict()
        data[login_reg.get()] = password1.get()
        file = open('login.txt', 'wb')
        pickle.dump(data, file)
        file.close()
        singup()


root = Tk()
root.title('Form')
root.geometry('%dx%d'%(WIDTH, HEIGHT))
root.resizable(False, False)


root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'green')

img = PhotoImage(file='Image/bg2.gif')
background_label = Label(root, image=img)
background_label.place(relheight=1, relwidth=1)

button_up = Button(root, text='Sing Up', bg='#39c488', command=singup)
button_up.place(relx=0.2, rely=0.1, relwidth=0.3)

button_in = Button(root, text='Sing In', bg='#39c488', command=singin)
button_in.place(relx=0.5, rely=0.1, relwidth=0.3)

root.mainloop()