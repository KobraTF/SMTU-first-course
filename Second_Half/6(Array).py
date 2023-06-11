from tkinter import *



class OperatingWindow():
    def __init__(self, master:'Tk',array:list, action:str) -> None:
        self.master = master
        master.title(action)
        self.array = array
        self.entrydata = []
        self.bf =False

        if action == 'create':
            self.create()
        elif action == 'add':
            self.add()
        elif action == 'find':
            self.find()
        elif action == 'del':
            self.delete()
        elif action == 'length':
            self.length()
        else:
            self.master.destroy()

    
    def create(self):
        self.info = Label(master=self.master,text='Введите элементы массива через запятую')
        self.entry = Entry(master=self.master)
        self.button = Button(master=self.master,text='Записать массив',command=lambda:self.getentry('create'))
        self.info.grid(row=1,column=2)
        self.entry.grid(row=2,column=1,columnspan=3)
        self.button.grid(row=3,column=2)
        if self.bf:
            self.bf = False
            self.array.extend(self.entrydata)
            self.master.destroy()

    def add(self):
        self.info = Label(master=self.master,text='Введите элемент массива')
        self.entry = Entry(master=self.master)
        self.button = Button(master=self.master,text='Добавить',command=lambda:self.getentry('add'))
        self.info.grid(row=1,column=2)
        self.entry.grid(row=2,column=1,columnspan=3)
        self.button.grid(row=3,column=2)
        if self.bf:
            self.bf = False
            self.array.append(self.entrydata[0])
            self.master.destroy()

    def find(self):
        if not self.bf:
            self.info = Label(master=self.master,text='Введите элемент массива')
            self.entry = Entry(master=self.master)
            self.button = Button(master=self.master,text='Найти',command=lambda:self.getentry('find'))
            self.info.grid(row=1,column=2)
            self.entry.grid(row=2,column=1,columnspan=3)
            self.button.grid(row=3,column=2)
        index = ''
        if self.bf:
            self.info.destroy()
            self.button.destroy()
            for elem in range(len(self.array)):
                if self.entrydata[0] == self.array[elem]:
                    index+=f'{elem} '
            if index:
                self.info = Label(master=self.master,text=f'Искомый элемент в массиве находится на позиции: {index}')
            else:
                self.info = Label(master=self.master,text='Такого элемента в массиве нет')
            self.button = Button(master=self.master,text='Ok',command=lambda:self.master.destroy())
            self.info.grid(row=1,column=1)
            self.button.grid(row=3,column=1,)

    def delete(self):
        self.info = Label(master=self.master,text='Введите элемент массива')
        self.entry = Entry(master=self.master)
        self.button = Button(master=self.master,text='Удалить',command=lambda:self.getentry('del'))
        self.info.grid(row=1,column=2)
        self.entry.grid(row=2,column=1,columnspan=3)
        self.button.grid(row=3,column=2)
        if self.bf:
            if self.entrydata[0] in self.array:
                self.array.remove(self.entrydata[0])
            self.master.destroy()

    def length(self):
        self.info = Label(master=self.master,text=f'{len(self.array)}')
        self.button = Button(master=self.master,text='Ok',command=lambda:self.master.destroy())
        self.info.grid(row=1,column=2)
        self.button.grid(row=2,column=2)

    def getentry(self,action:str):
        self.entrydata = [el.strip() for el in self.entry.get().split(',')]
        self.bf = True
        if action == 'create':
            self.create()
        elif action == 'add':
            self.add()
        elif action == 'find':
            self.find()
        elif action == 'del':
            self.delete()

class MainWindow():
    def __init__(self,master:'Tk') -> None:
        self.master = master
        master.title('Arrays')
        self.array = []
        self.button1 = Button(master,text='Create' ,command=lambda:self.action('create'))
        self.button2 = Button(master,text='To console' ,command=lambda:self.action('console'))
        self.button3 = Button(master,text='To file' ,command=lambda:self.action('file'))
        self.button4 = Button(master,text='Length' ,command=lambda:self.action('length'))
        self.button5 = Button(master,text='Add elem' ,command=lambda:self.action('add'))
        self.button6 = Button(master,text='Find elem' ,command=lambda:self.action('find'))
        self.button7 = Button(master,text='Delet elem' ,command=lambda:self.action('del'))
        self.button8 = Button(master,text='Exit' ,command=lambda:self.action('exit'))
        buttons =[
            self.button1,self.button2,self.button3,self.button4,
            self.button5,self.button6,self.button7,self.button8]
        for x in range(len(buttons)):
            buttons[x].grid(row=x//4,column=x%4)

    def action(self, command:str):
        if command == 'exit':
            self.master.destroy()
        elif command == 'console':
            print(self.array)
        elif command == 'file':
            with open('out.txt', 'w') as f:
                for elem in self.array:
                    f.write(f'{elem}\n')
        else:
            root = Tk()
            win = OperatingWindow(root,self.array,command)
            root.mainloop()

root= Tk()
window = MainWindow(root)
root.mainloop()