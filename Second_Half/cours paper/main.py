from chess_module import Figure,Desk
from ctk_window import Chess
from PyWindow import PygameWindow


if __name__ =="__main__":
    # Открываю окно ввода данных
    CTk=Chess()
    CTk.mainloop()
    # Инициализирую фигуру и шахматную доску
    f=Figure()
    d=Desk(CTk.n,f)
    # Визуализирую доску
    p=PygameWindow(d,CTk.l)
