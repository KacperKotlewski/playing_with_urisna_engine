from ursina import *           # this will import everything we need from ursina with just one line.
from random import random, randrange

app = Ursina()

player = Entity(
    model = 'cube' ,           # finds a 3d model by name
    color = color.orange,
    scale_y = 2
    )
def genEntities(count):
    entities = []
    for i in range(count):
        entity = Entity(
            model = 'cube' ,           # finds a 3d model by name
            color = color.orange,
            scale = 0.1,
            world_x= (random()*10-5),
            world_y= (random()*10-5)
        )
        entities.append(entity)

    return entities

ent = genEntities(2000)

def move(entities):
    for ent in entities:
        ent.x += (randrange(-1, 2)) * .1
        ent.y += (randrange(-1, 2)) * .1

def update():                  # update gets automatically called by the engine.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1
    player.y -= held_keys['w'] * .1
    player.y += held_keys['s'] * .1
    # ent
    move(ent)


app.run()                     # opens a window and starts the game.