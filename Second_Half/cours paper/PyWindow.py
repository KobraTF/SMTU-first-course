import pygame as p
#from abc import ABC,abstractmethod
from chess_module import Figure,Desk,Calculator

class PygameWindow():

    sidepannel = p.Surface((200,800))
    playfield = p.Surface((800,800))
    calc_button = p.Surface((150,60))
    cb_image = p.image.load('calc-button.png')
    calc_button.fill((40,40,40))
    calc_button.set_colorkey((40,40,40))
    calc_button.blit(cb_image,(0,0))
    calc_button_rect=calc_button.get_rect(topleft=(25,715))
    pf_rect=playfield.get_rect(topleft=(200,0))

    def __init__(self, desk:Desk,l:int):
        self.l = l
        self.launch(desk)
        self.desk = desk
        self.calc_flag = True
        self.ns_flag = False
        self.mainloop()
        
        
    # Первоначальная настройка окна
    def launch(self,desk:Desk) -> None:
        p.init()
        self.fps=p.time.Clock()
        self.pywindow = p.display.set_mode((1000,800))
        p.display.set_caption('Chess 2')
        image = p.image.load('sp-info.png')
        kurai = p.font.Font('kurai.ttf',18)
        n = desk.n # N - размер доски
        cs=800/n #cell_size - размер клетки
        n_text = kurai.render(str(n),True,(23,22,22))
        l_text = kurai.render(str(self.l),True,(23,22,22))
        wb = p.Surface((cs,cs)) # white_bllit - белая клетка доски
        bb = p.Surface((cs,cs)) # black_bllit - чёрная клетка доски
        bb.fill((30,30,30))
        wb.fill((210,200,200))
        

        for i in range(0,n,2):
            for j in range(0,n,2):
                
                self.playfield.blit(wb,(i*cs,(j+1)*cs))
                self.playfield.blit(wb,((i+1)*cs,j*cs))
                self.playfield.blit(bb,((i+1)*cs,(1+j)*cs))
                self.playfield.blit(bb,(i*cs,j*cs))

        self.sidepannel.fill((186,176,138))
        self.sidepannel.blit(image,(0,0))
        self.sidepannel.blit(n_text,(90,212))
        self.sidepannel.blit(l_text,(90,300))
        player_fig=p.Surface((cs,cs))
        player_fig.set_colorkey('black')
        p.draw.circle(player_fig,color=(91,223,122),radius=cs/2, center=(cs/2,cs/2))
        script_fig=p.Surface((cs,cs))
        script_fig.set_colorkey('black')
        p.draw.circle(script_fig,color=(90,222,222),radius=cs/2, center=(cs/2,cs/2))

        attack_surf=p.Surface((cs,cs))
        attack_surf.set_alpha(50)
        attack_surf.fill('red')
        
        self.wb = wb
        self.bb = bb
        self.cs = cs
        self.attack_surf = attack_surf
        self.player_fig = player_fig
        self.script_fig = script_fig
        self.sidepannel.blit(self.calc_button,(25,715))
        self.pywindow.blit(self.sidepannel,(0,0))
        self.pywindow.blit(self.playfield,(200,0))

    # Обновление окна, работа с действиями пользователя
    def mainloop(self):
        self.cooldown=0
        running = True

        while running:

            if self.cooldown>0:
                self.cooldown-=1

            self.check_set()
            self.check_remove()
            self.check_calc()
            if not self.ns_flag:
                self.update()
            p.display.update()
            

            # Проверяю не закрыл ли пользователь окно
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False
                    p.quit()
            self.fps.tick(45)
    
    # Проверяю, не пробует ли пользователь поставить фигуру, если он может и хочет, то фигура ставится на выбранную им клетку
    def check_set(self):
        if p.mouse.get_pressed()[0] and self.calc_flag and not self.cooldown and self.pf_rect.collidepoint(p.mouse.get_pos()):
            if self.desk.set(*self.get_cords(p.mouse.get_pos(),'d'),-1):
                
                self.cooldown=10
        pass

    # Проверяю, не пробует ли пользователь убрать фигуру, если он может и хочет, то фигура убирается с выбранной им клетки
    def check_remove(self):
        if p.mouse.get_pressed()[2] and self.calc_flag and not self.cooldown and self.pf_rect.collidepoint(p.mouse.get_pos()):
            if self.desk.remove(*self.get_cords(p.mouse.get_pos(),'d')):
                
                self.cooldown=10
        pass
    
    # Проверяю, не хочет ли пользователь проверить расстановку или вывести все возможные расстановки в файл, если хочет, удовлетворяю его желание
    def check_calc(self):
        if not self.calc_flag and p.mouse.get_pressed()[0] and not self.cooldown and self.calc_button_rect.collidepoint(p.mouse.get_pos()):
            self.desk.clear()
            with open('output.txt','w') as f:
                if not self.ns_flag:
                    self.calculator.recursion(f,self.l,0,self.desk)
                else:
                    f.write('No solution')
            self.cooldown=40
            return
        if p.mouse.get_pressed()[0] and not self.cooldown and self.calc_button_rect.collidepoint(p.mouse.get_pos()):
            try:
                self.calculator = Calculator(self.l,self.desk)                    
                self.cooldown=40
                self.calc_flag =False
                print(str(self.desk).count('-2'),str(self.desk))
                output_png = p.image.load('output-button.png')
                self.calc_button.blit(output_png,(0,0))
                self.sidepannel.blit(self.calc_button,(25,715))
                self.pywindow.blit(self.sidepannel,(0,0))
                if str(self.desk).count('-2')==0:
                    self.ns_flag = True
                    ns = p.image.load('ns.png')
                    self.pywindow.blit(ns,(0,0))

            except RuntimeError:
                pass
    
    # Обновляю игровое поле
    def update(self):
        b = (self.bb,self.wb)
        for pos in range(self.desk.n**2):
            if self.desk.storage[pos] == 0:
                self.playfield.blit(b[sum(self.get_cords(pos,'p'))%2],self.get_cords(pos,'o'))
            elif self.desk.storage[pos] == -1:
                self.playfield.blit(self.player_fig,self.get_cords(pos,'o'))
            elif self.desk.storage[pos] == -2:
                self.playfield.blit(self.script_fig,self.get_cords(pos,'o'))
            else:
                self.playfield.blit(self.attack_surf,self.get_cords(pos,'o'))
        
        self.pywindow.blit(self.playfield,(200,0))
        
    # Метод, форматирующий координаты для работы с ними
    def get_cords(self, data, mode:str):
        cs = self.cs
        n = self.desk.n
        if mode == 'm':
            return (int((data[0]-200)//cs*cs),int(data[1]//cs*cs))
        if mode =='d':
            return (int((data[0]-200)//cs),int(data[1]//cs))
        if mode == 'p':
            return(data%n,data//n)
        if mode == 'o':
            return(int(data%n*self.cs),int(data//n*self.cs))

            

if __name__ == "__main__":
    f = Figure()
    d=Desk(5,f)
    a = PygameWindow(d)
    pass

