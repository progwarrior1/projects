from tkinter import *
root = Tk()
root.title('Домашнее заание')
root.geometry('600x1000')
canvas = Canvas(root, width = 500, height = 500, bg = 'white')
canvas.pack()
def roof():
    canvas.itemconfig(a, fill = 'purple')
def wall():
    canvas.itemconfig(r, fill = 'black')
def sun():
    canvas.itemconfig(ov, fill = 'purple')
a = canvas.create_polygon(100, 300, 200, 50, 300, 300, fill = 'brown')
r = canvas.create_rectangle(100, 300, 300, 500, fill = 'blue')
ov = canvas.create_oval(500, 10, 400, 100, fill = 'yellow')
b1 = Button(root, height = 5, width = 30, text = 'крыша', command = roof).pack()
b2 = Button(root, height = 5, width = 30, text = 'стена', command = wall).pack()
b3 = Button(root, height = 5, width = 30, text = 'солнце', command = sun).pack()
root.mainloop()

