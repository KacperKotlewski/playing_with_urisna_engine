from . import *
from ursina import *
from random import random, randrange
from .Entity_v2 import Entity_List

def move(entities):
    for ent in entities:
        ent.x += (randrange(-1, 2)) * .1
        ent.y += (randrange(-1, 2)) * .1


entites = Entity_List()
def create_entities():
    entites.Add_New(
        parent="scene",
        "player",
        model = 'cube' ,
        color = color.orange,
        scale_y = 2,
        world_position= (120,0,0),
    )
    for i in range(200):
        particles = Entity(
            parent="scene",
            model = 'cube' ,
            color = color.orange,
            scale = 0.1,
        )
        particles.set_position(((randrange(-200,200,1)),((randrange(-200,200,1)),0)
        print(f'{i} : {0}'.format(entites.Add_Exist(particles, "paricles"+str(i))))
    print("Count", entites.Count())



def update():                  # update gets automatically called by the engine.
    try:
        entites("player").x += held_keys['d'] * .1
        entites("player").x -= held_keys['a'] * .1
        entites("player").y -= held_keys['w'] * .1
        entites("player").y += held_keys['s'] * .1
    except AttributeError:
        pass
    print(entites())
    print(entites("player"))


if __name__ == '__main__':
    app = Ursina()
    create_entities()
    app.run()

