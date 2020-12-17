from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
points = 0
id_points = canv.create_text(30, 30, text = points, font = '28')


class bomb():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10
        self.blown = False
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill='black'
            )

    def move(self):
        self.y += 5
        self.set_coords()
        if abs(self.y - g1.y) + abs(self.x - g1.x) < 20:
            canv.coords(self.id, -10, -10, -10, -10)
            self.blown = True

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

class ball():
    def __init__(self, x, y):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.type = choice(['circle', 'square'])
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        if self.type=='circle':
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        if self.type=='square':
            self.id = canv.create_rectangle(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
        if self.type == 'bomb':
            self.color = 'black'
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )

        self.live = 10

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y <= 550:
            self.vy -= 1.2
            self.y -= self.vy
            self.x += self.vx
            self.vx *= 0.995
            self.set_coords()
        else:
            if self.vx**2 + self.vy**2 > 10:
                self.vy = -self.vy/2
                self.vx = self.vx/2
                self.y = 449
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.vx =- self.vx/2
            self.x = 779

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if abs(obj.x - self.x) <= (self.r + obj.r) and abs(obj.y - self.y) <= (self.r + obj.r):
            return True
        else:
            return False


class gun():
    def __init__(self, x):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = x
        self.y = 450
        self.id = canv.create_line(x, 450, x+30, 420, width = 7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(self.x, self.y)
        new_ball.r += 5
        if self.y < event.y:
            event.y = self.y+1
        self.an = math.pi + math.atan((event.x-new_ball.x) / (event.y-new_ball.y))
        new_ball.vx = self.f2_power * math.sin(self.an)
        new_ball.vy = - self.f2_power * math.cos(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if self.y < event.y:
                event.y = self.y+1
            self.an = math.pi + math.atan((event.x-self.x) / (event.y-self.y))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.sin(self.an),
                    self.y + max(self.f2_power, 20) * math.cos(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move_left(self, event):
        if self.x > 0:
            self.x -= 3

    def move_right(self, event):
        if self.x < 780:
            self.x += 3



class target():
    def __init__(self):
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()
        self.b = None

    def new_target(self):
        """ Инициализация новой цели. """
        self.type = choice(['bomb', 'vert', 'hor'])
        if self.type == 'vert':
            self.vx = -10
            self.vy = rnd(-15, 15)
        if self.type == 'hor':
            self.vx = rnd(-15, 15)
            self.vy = 10
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)

        if self.type == 'bomb':
            self.vx = (g1.x - self.x)/50
            self.vy = (100 - self.y)/50
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, add_points=1):
        """Попадание шарика в цель."""
        global points, id_points

        canv.coords(self.id, -10, -10, -10, -10)
        points += add_points
        canv.itemconfig(id_points, text=points)

    def move(self):

        global points, id_points

        if self.type == 'bomb':
            self.vx = (g1.x - self.x)/100
            self.vy = (100 - self.y)/100
            if abs(self.x-g1.x)<10 and not self.b:
                self.b = bomb(self.x, self.y)

        if self.b:
            self.b.move()
            if self.b.y>550:
                self.b = None
            elif self.b.blown:
                print(self.b.x, self.b.y)
                points -= 2
                canv.itemconfig(id_points, text=points)
                self.b = None

        x = self.x = self.x + self.vx
        if self.x > 780:
            self.vx = -self.vx
            x = self.x = 779
        if self.x < 0:
            self.vx = -self.vx
            x = self.x = 1

        y = self.y = self.y + self.vy
        if self.y > 550:
            self.vy = -self.vy
            y = self.y = 549
        if self.y < 0:
            self.vy = -self.vy
            y = self.y = 1
        d = rnd(-2, 2)
        if self.type == 'hor':
            self.vx -= d
        if self.type == 'vert':
            self.vy += d
        canv.coords(self.id, x - self.r, y - self.r, x + self.r, y + self.r)


screen1 = canv.create_text(400, 300, text='', font='28')
t1 = target()
t2 = target()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.focus_set()
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind('<Left>', g1.move_left)
    canv.bind('<Right>', g1.move_right)

    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        for b in balls:
            b.move()
            if t1.live:
                t1.move()
            if t2.live:
                t2.move()
            if b.hittest(t1) and t1.live:
                t1.new_target()
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.hit()
                t2.new_target()
            if not (t1.live or t2.live):
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g2.targetting()
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

mainloop()
