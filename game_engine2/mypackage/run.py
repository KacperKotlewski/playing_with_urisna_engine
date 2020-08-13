from . import *
from ursina import *
from random import random, randrange
from .Entity_v2 import Entity_List

def move(entities):
    for ent in entities:
        ent.x += (randrange(-1, 2)) * .1
        ent.y += (randrange(-1, 2)) * .1



entites = Entity_List()
entites.Add_New(
    "player",
    model = 'cube' ,
    color = color.orange,
    scale_y = 2,
)
for i in range(200):
    particles = Entity(
        model = 'cube' ,
        color = color.orange,
        scale = 0.1,
        world_x= (random()*10-5),
        world_y= (random()*10-5)
    )
    entites.Add_Exist(particles, "paricles"+str(i))
print("Count", entites.Count())

app = Ursina()


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