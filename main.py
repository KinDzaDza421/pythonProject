
from tkinter import *
import time



root = Tk()
root.title('smesharik')
mx = 700
my = 700
c = Canvas(root, width=mx, height=my, bg='black')
c.pack()


c.create_line(0,0,700,700, fill = "blue")
c.create_line(700,0,0,700, fill = "blue")
c.create_line(350,0,350,700, fill = "blue")
c.create_line(700,350,0,350, fill = "blue")
c.create_line(525,0,175,700, fill = "red")
c.create_line(700,175,0,525, fill = "red")
c.create_line(0,175,700,525, fill = "red")
c.create_line(175,0,525,700, fill = "red")

ball = c.create_oval(325, 325, 375, 375, fill='grey')


rec = c.create_rectangle(100, 100, 90, 90, fill = "blue")
rec1 = c.create_rectangle(100, 100, 0, 150, fill = "red")
while True:
    for _ in range (100):
        c.move(rec1, 0, 5)
        root.update()
        time.sleep(0.0001)

    for _ in range (100):
        c.move(rec1, 5, 0)
        root.update()
        time.sleep(0.0001)

    for _ in range(100):
        c.move(rec1, 0, -5)
        root.update()
        time.sleep(0.0001)

    for _ in range(100):
        c.move(rec1, -5, 0)
        root.update()
        time.sleep(0.0001)

    for _ in range (100):
        c.move(rec, 5, 0)
        root.update()
        time.sleep(0.0001)

    for _ in range (100):
        c.move(rec, 0, 5)
        root.update()
        time.sleep(0.0001)

    for _ in range (100):
        c.move(rec, -5, 0)
        root.update()
        time.sleep(0.0001)

    for _ in range (100):
        c.move(rec, 0, -5)
        root.update()
        time.sleep(0.0001)

root.mainloop()

