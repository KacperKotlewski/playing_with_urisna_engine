
from mypackage.Entity_v2 import *
from mypackage import time
from random import randrange,random, randint
import threading
from queue import Queue

global SPAWN_IN_RANGE
SPAWN_IN_RANGE=2

def move(entities):
    for key, ent in entities.items():
        if "paricles" in key: 
            ent.x += (randrange(-1, 2)) * .1
            ent.y += (randrange(-1, 2)) * .1


entites = Entity_List(max = 0)
def generate_entities(queue):
    val = queue.get()
    count, entites_list = val["count"], val["entites"]
    ent = Entity_List(max = count)
    ent.Add_New(
        "player",
        model = 'cube' ,
        color = color.orange,
        scale_y = 2,
        position = Vec3(randrange(-2,2,1), randrange(-2,2,1), 0),
    )
    #ent("player").set_position((randrange(-2,2,1), randrange(-2,2,1), 0))
    
    for i in range(999999999):
        particles = Entity(
            model = 'cube' ,
            color = color.random_color(),
            scale = 0.1,
            position = Vec3(randrange(-SPAWN_IN_RANGE,SPAWN_IN_RANGE,1), randrange(-SPAWN_IN_RANGE,SPAWN_IN_RANGE,1), 0),
        )
        #particles.set_position((randrange(-50,50,1), randrange(-50,50,1), 0))
        entity_added = ent.Add_Exist(entity=particles, id="paricles")
        #print('{0} : {1}'.format(i, entity_added))
        if entity_added == None:
            break
    entites_list = ent
    queue.put({"entites":entites_list})
    print("Count", ent.Count())

tick_counter = time.Tick(100)

def update_example(queue):
    val = queue.get()
    entites = val["entites"]
    if tick_counter():
        move(entites)

def playerMove():
    try:
        entites("player").x += held_keys['d'] * .1
        entites("player").x -= held_keys['a'] * .1
        entites("player").y -= held_keys['w'] * .1
        entites("player").y += held_keys['s'] * .1
    except AttributeError:
        pass


threadLock = threading.Lock()
threads = []
queue = Queue()
class myThread (threading.Thread):
   def __init__(self, function, **kwargs):
      threading.Thread.__init__(self)
      self.function = function
      self.kwargs = kwargs
      
   def run(self):
      threadLock.acquire()
      self.function(self.kwargs)
      threadLock.release()

if __name__ == "__main__":
    queue.put({"count":int(sys.argv[1:][0]), "entites":entites})
    t = threading.Thread(target=generate_entities, kwargs={"queue":queue} )
    t.start()
    threads.append(t)

    for t in threads:
        t.join()
        threads.remove(t)
    if not queue.empty():
        val = queue.get()
        entites = val["entites"]

    print("Count", entites.Count())
    app = Ursina()

    t1 = threading.Thread(target=update_example, kwargs={"queue":queue} )
    def update():
        queue.put({"entites":entites})
        t1.start()
        threads.append(t1)
        
        playerMove()
        #update_example()
        for t in threads:
            t.join()

    app.run()