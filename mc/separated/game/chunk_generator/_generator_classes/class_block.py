from ursina import Mesh, Vec3
from .class_plane2 import Plane2

class Block(Mesh):
    def __init__(self, neighbor, uvs,**kwargs):
        super().__init__(**kwargs)
        self._UpdateUv(uvs)
        self._UpdateNeighbor(neighbor)
        self._Create()
    
    def _UpdateNeighbor(self, neighbor):
        self.neighbor = neighbor

    def _UpdateUv(self, uv):
        self.uv = uv

    def _Create(self):
        self

        X, Y, Z = 0,0,0
        # if dont have a neighbor then create a face
        if not self.neighbor["front"]:  #checking neighbor for front face
            self += Plane2(subdivisions=(1,1), uvs=self.uv["front"],  pos=Vec3(X, Y, Z-.5), rot=Vec3(-90,0,0))

        if not self.neighbor["back"]:   #checking neighbor for back face
            self += Plane2(subdivisions=(1,1), uvs=self.uv["back"],   pos=Vec3(X, Y, Z+.5), rot=Vec3(-90,180,0))

        if not self.neighbor["top"]:    #checking neighbor for top face
            self += Plane2(subdivisions=(1,1), uvs=self.uv["top"],    pos=Vec3(X, Y+.5, Z), rot=Vec3(0,0,0))

        if not self.neighbor["bottom"]: #checking neighbor for bottom face
            self += Plane2(subdivisions=(1,1), uvs=self.uv["bottom"], pos=Vec3(X, Y-.5, Z), rot=Vec3(0,0,-180))
            
        if not self.neighbor["right"]:  #checking neighbor for right face
            self += Plane2(subdivisions=(1,1), uvs=self.uv["right"],  pos=Vec3(X+.5, Y, Z), rot=Vec3(90,0,-90))
            
        if not self.neighbor["left"]:   #checking neighbor for left face
            self += Plane2(subdivisions=(1,1), uvs=self.uv["left"],   pos=Vec3(X-.5, Y, Z), rot=Vec3(-90,0,-90))
