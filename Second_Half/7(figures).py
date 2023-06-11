# from tkinter import *

# class Square():
#     pass
# class Circle():
from tkinter import *
from math import pi
#from random import choice

class Circle():
    def __init__(self, r) -> None:
        self.r = r
    def __repr__(self) -> str:
        return int(pi*self.r**2)
    def __str__(self) -> str:
        return str(self.__repr__())
class Square():
    def __init__(self,a) -> None:
        self.a = a
    def __repr__(self) -> str:
        return self.a**2
    def __str__(self) -> str:
        return str(self.__repr__())
class Triangle():
    def __init__(self, a) -> None:
        self.a = a
    def __repr__(self) -> str:
        return self.a**2//2
    def __str__(self) -> str:
        return str(self.__repr__())
        

class DrawFigWindow():
    def __init__(self, master:'Tk', figtype) -> None:
        self.master = master
        master.title('Figures')
        self.figtype = figtype
        self.entered_number = 0
        vcmd = self.master.register(self.validate)
        self.entry = Entry(master,validate='key',validatecommand=(vcmd, '%P'))
        
        self.info = Label(master,text='Введите сторону/радиус фигуры')
        self.area = ''
        self.area_tk = StringVar(master)
        
        self.area_tk.set(self.area)
        self.area_label = Label(master,textvariable=self.area_tk)
        self.button = Button(master,text='Построить', command=lambda: self.draw())
        

        self.canv = Canvas(master, width=600, height=600)


        self.info.grid(row=1,column=1)
        self.entry.grid(row=2,column=1)
        self.button.grid(row=3,column=1)
        self.area_label.grid(row=4,column=1,sticky=N)
        self.canv.grid(row=5,column=1)
        pass

    def draw(self):
        self.canv.create_rectangle(
                0,0,6000,6000,fill='white'
                )
        var = self.entered_number
        area = self.figtype(var)
        self.area = str(area)
        self.area_tk.set(f'Площадь фигуры = {area}')
        if isinstance(area,Circle):
            self.canv.create_oval(
                300-self.entered_number,300-self.entered_number,300+self.entered_number,300+self.entered_number,outline='black',fill='black'
                )
        elif isinstance(area,Square):
            self.canv.create_rectangle(
                300-self.entered_number,300-self.entered_number,300+self.entered_number,300+self.entered_number,outline='black',fill='black'
                )
            pass
        elif isinstance(area,Triangle):
            self.canv.create_polygon(
                300-self.entered_number,300-self.entered_number,300+self.entered_number,300-self.entered_number,300+self.entered_number,300+self.entered_number,outline='black',fill='black'
                )

    def validate(self, new_text: str):
        if not new_text:
            self.entered_number = 0
            return True
        try:
            if int(new_text)<=0:
                return False
            self.entered_number = int(new_text)
            return True 
        except ValueError:
            return False


class ChoiseWin():
    def __init__(self,master:'Tk') -> None:
        self.master =  master
        master.title('Figures')
        self.circle_button = Button(master,text='Circle', command=lambda:self.new_window('circle'))
        self.square_button = Button(master,text='Square', command=lambda:self.new_window('square'))
        self.triangle_button = Button(master,text='Triangle', command=lambda:self.new_window('triangle') )
        self.circle_button.grid(row=1,column=1)
        self.square_button.grid(row=1,column=2)
        self.triangle_button.grid(row=1,column=3)
    
    def new_window(self, fig):
        tk = Tk()
        #print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111')
        if fig == 'circle':
            a = DrawFigWindow(tk,Circle)
        elif fig == 'square':
            a = DrawFigWindow(tk,Square)
        elif fig == 'triangle':
            a = DrawFigWindow(tk,Triangle)
        self.master.destroy()
        return tk.mainloop()
tk = Tk()
start = ChoiseWin(tk)
tk.mainloop()

# tk = Tk()
# answer = 'Try your guess'
# answer_label = StringVar()
# answer_label.set(answer)
# label = Label(tk,textvariable=answer_label)
# label.grid(row=0, column=0)
# c = Canvas(tk, bg="#c7aba9", width="4i", height=300, relief=SUNKEN)
# c.grid(row=3,column=0 )

# def change_ball(event): # tk.CURRENT Положение символа, ближайшего к указателю мыши. Эта константа равна строке 'current'.
#     c.coords(CURRENT, (event.x-R, event.y-R, event.x+R, event.y+R)) # Запрашивает или изменяет координаты, определяющие элемент. Первым аргументом всегда должен быть тег / id элемента холста.
#     c.itemconfigure(CURRENT, fill=choice(colors)) # Эта команда аналогична методу Widget.configure, за исключением того, что она изменяет опции, специфичные для элементов, заданных тегом tagOrId, вместо того, чтобы изменять опции для всего виджета canvas.

# oval = c.create_oval((100-R, 100-R, 100+R, 100+R), fill="Black") # Для отрисовки овала применяется метод create_oval(). В качестве обязательных параметров он принимает координаты прямоугольника, в который будет вписан овал. create_oval(__x0: float, __y0: float, __x1: float, __y1: float)
# c.tag_bind(oval, "<1>", change_ball) # Метод tag_bind позволяет привязать событие (например, щелчок кнопкой мыши) к определенной фигуре на Canvas.
# tk.mainloop()

