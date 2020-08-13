
from mypackage.Entity_v2 import *
from mypackage import time
from random import randrange,random, randint

def move(entities):
    for key, ent in entities.items():
        if "paricles" in key: 
            ent.x += (randrange(-1, 2)) * .1
            ent.y += (randrange(-1, 2)) * .1


entites = Entity_List(max = 0)
def generate_entities(args):
    try:
        max_e = int(args[0]) if args[0] != None and type(int(args[0])) == int else 64
    except:
        max_e = 64
    ent = Entity_List(max = max_e)
    ent.Add_New(
        "player",
        model = 'cube' ,
        color = color.orange,
        scale_y = 2,
    )
    while not ent.Add_New(
            "paricles",
            model = 'cube',
            color = color.random_color(),
            scale = 0.1
        ) == None:
        pass
    return ent

tick_counter = time.Tick(100)
dt1 = time.Deltatime()
dt2 = time.Deltatime()

def update_example():
    try:
        entites("player").x += held_keys['d'] * .1
        entites("player").x -= held_keys['a'] * .1
        entites("player").y -= held_keys['w'] * .1
        entites("player").y += held_keys['s'] * .1
    except AttributeError:
        pass
    if tick_counter():
        move(entites())
        print("dt1:", dt1.Get())
        print("dt2:", dt2.Get())
        dt2()

    dt1()


if __name__ == "__main__":
    entites = generate_entities(sys.argv[1:])
    app = Ursina()

    def update():
        update_example()

    app.run()