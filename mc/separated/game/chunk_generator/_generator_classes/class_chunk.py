from ursina import Entity, Vec3
from .class_plane2 import Plane2
from ...settings import ENTITY_MODE, COLLISION
from concurrent.futures import ThreadPoolExecutor
import numpy
import os

class Chunk(Entity):
    def __init__(self, chunk_map, uv_map=None, **kwargs):
        super().__init__(**kwargs)
        self.collision = COLLISION
        self.collider = 'mesh'
        self.chunk_map = chunk_map
        self.uv_map = uv_map
        self._Create()



    def _CheckIsNeighborBlockOn(self, chunk_map, pos=Vec3(0,0,0)):
        for i in pos:
            if i < 0:
                return False # if position is less then 0 Then False
        try:
            if chunk_map[pos.y][pos.x][pos.z] != 0: 
                return True # if on position is something else then air then True
        except:
            pass
        return False # if on position is out of range then False

    def _CreateLoop(self, to_render, offset):
        for Y, tableY in enumerate(to_render):
            temp_entity = Entity(parent=self)

            for X, tableX in enumerate(tableY):
                for Z, _id in enumerate(tableX):

                    # if not air then get uv map of block
                    if _id != 0 and _id in self.uv_map:
                        uv = self.uv_map[_id]

                        x = X
                        y = Y +offset
                        z = Z

                        # if dont have a neighbor then create a face
                        if not self._CheckIsNeighborBlockOn(chunk_map=self.chunk_map, pos=Vec3(x,y,z-1)): #checking neighbor for front face
                            Entity(parent=temp_entity, model=Plane2(subdivisions=(1,1), uvs=uv["front"]),  x=x,    y=y,    z=z-.5, rotation_x=-90)

                        if not self._CheckIsNeighborBlockOn(chunk_map=self.chunk_map, pos=Vec3(x,y,z+1)): #checking neighbor for back face
                            Entity(parent=temp_entity, model=Plane2(subdivisions=(1,1), uvs=uv["back"]),   x=x,    y=y,    z=z+.5, rotation_x=-90, rotation_z=180)

                        if not self._CheckIsNeighborBlockOn(chunk_map=self.chunk_map, pos=Vec3(x,y+1,z)): #checking neighbor for top face
                            Entity(parent=temp_entity, model=Plane2(subdivisions=(1,1), uvs=uv["top"]),    x=x,    y=y+.5, z=z, rotation_x=0)

                        if not self._CheckIsNeighborBlockOn(chunk_map=self.chunk_map, pos=Vec3(x,y-1,z)): #checking neighbor for bottom face
                            Entity(parent=temp_entity, model=Plane2(subdivisions=(1,1), uvs=uv["bottom"]), x=x,    y=y-.5, z=z, rotation_x=-180)
                            
                        if not self._CheckIsNeighborBlockOn(chunk_map=self.chunk_map, pos=Vec3(x+1,y,z)): #checking neighbor for right face
                            Entity(parent=temp_entity, model=Plane2(subdivisions=(1,1), uvs=uv["right"]),  x=x+.5, y=y,    z=z, rotation_z=90, rotation_x=-90)
                            
                        if not self._CheckIsNeighborBlockOn(chunk_map=self.chunk_map, pos=Vec3(x-1,y,z)): #checking neighbor for left face
                            Entity(parent=temp_entity, model=Plane2(subdivisions=(1,1), uvs=uv["left"]),   x=x-.5, y=y,    z=z, rotation_z=-90, rotation_x=-90)


    def _Create(self):

        # split table and run as separated threads
        workers = min(4, os.cpu_count() + 4)
        with ThreadPoolExecutor(max_workers=workers) as exe:
            sections = numpy.array_split(self.chunk_map, workers)
            jobs = [exe.submit(self._CreateLoop, section, int((i*workers)/2)) for i, section in enumerate(sections)]
        # finalize threads work
        for job in jobs:
            job.result()
        
        # combine all entities that was created to one entity
        self = self.combine()
        self.mode = ENTITY_MODE
        self.generate()
        self.collision = COLLISION
        self.collider = 'mesh'
