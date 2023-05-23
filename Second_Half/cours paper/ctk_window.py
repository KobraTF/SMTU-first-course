import customtkinter as ct

# Ошибка для отрицательных N L
class NLError(BaseException):
    pass

# Класс, отвечающий за работу с окном ввода данных(N,L)
class Chess(ct.CTk):
    
    # Открываю окно при инициализации объекта класса 
    def __init__(self) -> None:
        super().__init__()

        # Создаю окно
        self.geometry('300x200+600+300')
        self.title('Chess 2')
        self.resizable(False,False)
        ct.set_appearance_mode("Dark")

        # Созал рабочую область
        self.main_frame= ct.CTkFrame(master=self,width=300)
        # Создал текстовые виджеты для обозначения полей ввода
        self.n_text = ct.CTkLabel(master=self.main_frame, text_color='grey', text='Введите размер поля(N): ')
        self.l_text = ct.CTkLabel(master=self.main_frame, text_color='grey', text='Введите количество фигур(L):  ')
        # Создал виджеты полей ввода
        self.n_entry = ct.CTkEntry(master=self.main_frame, width=60)
        self.l_entry = ct.CTkEntry(master=self.main_frame, width=60)
        # Создал кнопку для проверки правильности ввода, сохраниения данных, а также перехода в следующее окно
        self.button=ct.CTkButton(master=self.main_frame,width=100, text='Далее', command=self.get_data)

        # Разместил все виджеты в рабочей области
        self.button.place(relx=0.6, rely=0.8)
        self.n_entry.place(relx=0.75,rely=0.1)
        self.l_entry.place(relx=0.75,rely=0.3)
        self.n_text.place(relx=0.08,rely=0.1)
        self.l_text.place(relx=0.08,rely=0.3)

        # Отобразил виджеты
        self.main_frame.grid(row=0, column=0)

    # Метод для проверки правильности ввода данных и их сохранения в объекте    
    def get_data(self) -> None:
        # Проверяю правильно ли введены данные. Если да, сохраняю и перехожу в следующее окно
        try:
            n=int(self.n_entry.get())
            l=int(self.l_entry.get())
            if n<1:
                raise NLError()
            self.n = n
            self.l = l
            self.destroy()
        except ValueError:
            er=ErrorWindow('N,L должны быть целыми положительными числами!!!')
            er.mainloop()
        except NLError:
            er=ErrorWindow('N и L должны быть положительными!!!')
            er.mainloop()


        
# Класс отвечающий за окно с уведомлением об ошибке
class ErrorWindow(ct.CTk):
    def __init__(self,error:str) -> None:
        # Создаю окно, вывожу в окне текст ошибки
        super().__init__()
        self.geometry('400x50+600+300')
        self.title('Chess 2')
        self.resizable(False,False)
        ct.set_appearance_mode("Dark")
        self.main_frame= ct.CTkFrame(master=self,width=500)

        self.error_text = ct.CTkLabel(master=self.main_frame, text_color='grey', text=error)
        self.error_text.place(relx=0.0,rely=0.0)

        self.main_frame.grid(row=0, column=0)

if __name__=='__main__':
    chess_2 = Chess()
    chess_2.mainloop()
