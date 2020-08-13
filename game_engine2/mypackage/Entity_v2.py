from ursina import *
class Entity(Entity):
    def copy(self):
        return self.__copy__()

    def __copy__(self):
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        return newone

class Entity_List():
    def __init__(self, max = 128):
        self.entities = {}
        self.max = max


    def _Generate_new_id(self, id):
        new_id = id
        i = 0
        while not self._Check_ID_is_free(new_id):
            new_id = id + "_" + str(i)
            i+=1
        return new_id

    def _Check_ID_is_free(self, id):
        if id != None:
            try:
                type(self.entities[id])
            except KeyError:
                return True
        return False

    def _Check_ID(self, id):
        if self._Check_ID_is_free(id):
            return id
        if id == None:
            id = ""
        return self._Generate_new_id(id)

    def Add_New(self, id=None, **kwargs):
        if(len(self.entities) < self.max):
            entity = Entity(**kwargs)
            return self.Add_Exist(entity, id)
        return None

    def Add_Exist(self, entity:Entity, id=None):
        id = self._Check_ID(id)
        if(len(self.entities) < self.max):
            self.entities.update({id : entity})
            return {"id":id, "entity":self.Get(id)}
        return None

    def GetInTable(self):
        dictlist = []
        for key, value in self.entities.items():
            temp = value
            dictlist.append(temp)
        return dictlist

    def Count(self):
        return len(self.entities)

    def update(self):
        return self.GetInTable()

    def __repr__(self):
        return 'Entity_List(max=%s, entities=%s)' % (self.max, self.entities)

    def Get(self, id): 
        
        try:
            return self.entities[id]
        except KeyError:
            pass
        return None

    def __call__(self, id=None): 
        if id == None:
            return self.entities
        return self.Get(id)

# player = Entity(
#     model = 'cube' ,           # finds a 3d model by name
#     color = color.orange,
#     scale_y = 2
#     )
# def genEntities(count):
#     entities = []
#     for i in range(count):
#         entity = Entity(
#             model = 'cube' ,           # finds a 3d model by name
#             color = color.orange,
#             scale = 0.1,
#             world_x= (random()*10-5),
#             world_y= (random()*10-5)
#         )
#         entities.append(entity)

#     return entities

# ent = genEntities(2000)

# def move(entities):
#     for ent in entities:
#         ent.x += (randrange(-1, 2)) * .1
#         ent.y += (randrange(-1, 2)) * .1