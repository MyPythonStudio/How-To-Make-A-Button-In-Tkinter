from tkinter import * #Imports Tkinter (Imports All)
window = Tk() # Window Refers To Tk()
window.config(background='yellow')
button = Button(window, text='Click Me!', background='yellow', foreground='brown', font=('Microsoft YaHei UI Light', 26, 'bold'), command='click', activeforeground='brown', activebackground='yellow')
button.pack()

window.mainloop()