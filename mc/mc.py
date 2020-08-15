from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Plane(Plane):
    def __init__(self, subdivisions=(1,1), mode='triangle', uvs=None, **kwargs):
        super().__init__(subdivisions=(1,1), mode='triangle', **kwargs)
        # override Plane class to give possibility to pass UV coordinates
        if type(uvs) == type(list()):
            self.uvs = uvs

class Voxel(Entity):
    def __init__(self, chunk_map=[[[1]]], uv_map=None, **kwargs):
        super().__init__(**kwargs)
        self.Create(chunk_map, uv_map)

    def _CheckIsNeighborBlockOn(self, chunk_map=[[[1]]], pos=(0,0,0)):
        # if position is less then 0 Then False
        for i in pos:
            if i < 0:
                return False
        try:
            # if on position is something else then air then True
            if chunk_map[pos[0]][pos[1]][pos[2]] != 0:
                return True
        except:
            pass
        # if on position is out of range then False
        return False

    def Create(self, chunk_map=[[[1]]], uv_map=None):
        # geting self (self entity)
        main_entity = self

        for X, tableX in enumerate(chunk_map):
            x_entity = Entity(parent=main_entity)
            for Y, tableY in enumerate(tableX):
                for Z, _id in enumerate(tableY):
                    # if not air then get uv map of block
                    if _id != 0 and _id in uv_map:
                        uv = uv_map[_id]

                        # if dont have a neighbor then create a face
                        if not self._CheckIsNeighborBlockOn(chunk_map=chunk_map, pos=(X,Y,Z-1)):
                            Entity(parent=x_entity, model=Plane(subdivisions=(1,1), uvs=uv["front"]),  x=X,    y=Y,    z=Z-.5, rotation_x=-90)

                        if not self._CheckIsNeighborBlockOn(chunk_map=chunk_map, pos=(X,Y,Z+1)):
                            Entity(parent=x_entity, model=Plane(subdivisions=(1,1), uvs=uv["back"]),   x=X,    y=Y,    z=Z+.5, rotation_x=-90, rotation_z=180)

                        if not self._CheckIsNeighborBlockOn(chunk_map=chunk_map, pos=(X,Y+1,Z)):
                            Entity(parent=x_entity, model=Plane(subdivisions=(1,1), uvs=uv["top"]),    x=X,    y=Y+.5, z=Z, rotation_x=0)

                        if not self._CheckIsNeighborBlockOn(chunk_map=chunk_map, pos=(X,Y-1,Z)):
                            Entity(parent=x_entity, model=Plane(subdivisions=(1,1), uvs=uv["bottom"]), x=X,    y=Y-.5, z=Z, rotation_x=-180)
                            
                        if not self._CheckIsNeighborBlockOn(chunk_map=chunk_map, pos=(X+1,Y,Z)):
                            Entity(parent=x_entity, model=Plane(subdivisions=(1,1), uvs=uv["right"]),  x=X+.5, y=Y,    z=Z, rotation_z=90, rotation_x=-90)
                            
                        if not self._CheckIsNeighborBlockOn(chunk_map=chunk_map, pos=(X-1,Y,Z)):
                            Entity(parent=x_entity, model=Plane(subdivisions=(1,1), uvs=uv["left"]),   x=X-.5, y=Y,    z=Z, rotation_z=-90, rotation_x=-90)
        # combine all entities that was created to one entity
        self = main_entity.combine()
        self.mode = 'triangle'
        self.generate()

def Generator(chunk_size):
    chunk = []
    for x in range(chunk_size):
        chunkX=[]
        for y in range(chunk_size):
            chunkY=[]
            for z in range(chunk_size):
                # 0 == None || air
                # 1 == dirt
                # 2 == grass
                # 3 == stone
                block = 1

                if y == chunk_size-1:
                    block = 2
                elif y <= int(chunk_size*0.8):
                    block = 3

                chunkY.append(block)
            chunkX.append(chunkY)
        chunk.append(chunkX)
    return chunk

def get_UV_map():
    # setting up uv's
    dirt_uvs = [(0,0.5), (0.5,0.5), (0,1), (0.5,1)]
    grass_uvs_top = [(0,1), (0.5,1), (0,1.5), (0.5,1.5)]
    grass_uvs_side = [(0.5,0.5), (1,0.5), (0.5,1), (1,1)]
    stone_uvs = [(0.5,1), (1,1), (0.5,1.5), (1,1.5)]

    # creating a table of faces for block's
    dirt    = {"front":dirt_uvs,        "back":dirt_uvs,        "top":dirt_uvs,         "bottom":dirt_uvs,      "right":dirt_uvs,       "left":dirt_uvs}
    grass   = {"front":grass_uvs_side,  "back":grass_uvs_side,  "top":grass_uvs_top,    "bottom":dirt_uvs,      "right":grass_uvs_side, "left":grass_uvs_side}
    stone   = {"front":stone_uvs,       "back":stone_uvs,       "top":stone_uvs,        "bottom":stone_uvs,     "right":stone_uvs,      "left":stone_uvs}
    
    # table of block uv's
    return {1:dirt, 2:grass, 3:stone}

if __name__ == '__main__':
    app = Ursina()
    
    # texture loading
    cube_text = Texture('cube_textures.png')
    cube_text.filtering = False

    # count of block per chunk ^3
    chunk_size = 16
    # generate chunk table
    chunk_map = Generator(chunk_size)
    # count of chunks to load ^2
    chunk_count=1
    for x in range(chunk_count):
        for z in range(chunk_count):
            # generating chunk
            chunk = Voxel(parent=scene, uv_map=get_UV_map(), chunk_map=chunk_map, x=x*chunk_size, z=z*chunk_size, texture=cube_text)

    # setting player up
    player = FirstPersonController(position=(0,chunk_size+1,0))
    app.run()

