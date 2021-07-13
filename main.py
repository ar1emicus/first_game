import tkinter
import random

def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    if canvas.coords(obj)[0] == field_X:
        canvas.coords(obj, (0, canvas.coords(obj)[1]))
    if canvas.coords(obj)[1] == field_Y:
        canvas.coords(obj, (canvas.coords(obj)[0], 0))
    if canvas.coords(obj)[0] < 0:
        canvas.coords(obj, (field_X - step, canvas.coords(obj)[1]))
    if canvas.coords(obj)[1] < 0:
        canvas.coords(obj, (canvas.coords(obj)[0], field_Y - step))

def do_nothing(x):
    pass

def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text='Ты проиграл!')
            master.bind("<KeyPress>", do_nothing)
def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    if event.keysym == 'Down':
        move_wrap(player, (0, step))
    if event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    if event.keysym == 'Right':
        move_wrap(player, (step, 0))
    for enemy in enemies:
        direction = enemy[1]()
        move_wrap(enemy[0], direction)
    check_move()

def always_right():
    return (step, 0)

def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])

def prepare_and_start():
    global player, exit, fires, enemies
    canvas.delete('all')
    player_pos = (random.randint(0, N_X - 1) * step,
                  random.randint(0, N_Y - 1) * step)
    player = canvas.create_image(player_pos, image=player_pic, anchor='nw')
    exit_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)
    exit = canvas.create_image(exit_pos, image=exit_pic, anchor='nw')
    N_FIRES = 6
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
        fire = canvas.create_image(fire_pos, image=fire_pic, anchor='nw')
        fires.append(fire)
    N_ENEMIES = 4
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(1, N_X - 1) * step,
                     random.randint(1, N_Y - 1) * step)
        enemy = canvas.create_image(enemy_pos, image=enemy_pic, anchor='nw')
        enemies.append((enemy, random.choice([always_right, random_move])))
    label.config(text='Найди выход')
    master.bind("<KeyPress>", key_pressed)

step = 100
N_X = 12
N_Y = 6
field_X = N_X * step
field_Y = N_Y * step
master = tkinter.Tk()
player_pic = tkinter.PhotoImage(file="C:/Users/Пользователь/Documents/pycharm проекты/game/player.gif")
exit_pic = tkinter.PhotoImage(file="C:/Users/Пользователь/Documents/pycharm проекты/game/exit.gif")
fire_pic = tkinter.PhotoImage(file="C:/Users/Пользователь/Documents/pycharm проекты/game/fire.gif")
enemy_pic = tkinter.PhotoImage(file="C:/Users/Пользователь/Documents/pycharm проекты/game/enemy.gif")
label = tkinter.Label(master, text='Найди выход')
label.pack()
canvas = tkinter.Canvas(master, bg='black',
                        width= field_X, height= field_Y)
canvas.pack()
restart = tkinter.Button(master, text='Начать заново', command=prepare_and_start)
restart.pack()
prepare_and_start()
master.mainloop()
