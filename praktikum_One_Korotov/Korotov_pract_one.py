#импортируем пакеты
import math
import tkinter

#задаём параметры экрана
root = tkinter.Tk()
c = tkinter.Canvas(root, width=700, height=700, bg="red")

c.pack()
#задаём цвета большому и маленькому шару
ball = c.create_oval(100, 100, 500, 500, fill='white')
dot = c.create_oval(485, 285, 515, 315, fill='blue')

#переменная со значением скорости и направления
speed = 0

#создаём функцию - 
def motion():

    global speed
    corner = 1 + speed
    #координаты орбиты полёта шарика по косинусу и синусу
    x = 300 + 200 * math.cos(corner)
    y = 300 + 200 * math.sin(corner)

    #рисунок шарика летающего по орбите, изменив одну координату, он станет овалом, а не шаром
    c.coords(dot, (x - 20, y - 20, x + 20, y + 20))

    #скорость полёта шара
    speed -= 0.028

    if corner == 0:
        speed = 0
    #я бы назвал это - фпс    
    root.after(12, motion)

#вызываем функцию montion
motion()
root.mainloop()