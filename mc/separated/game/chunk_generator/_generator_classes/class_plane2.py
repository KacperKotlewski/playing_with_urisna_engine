from ursina import Plane
from ursina import Vec3
from math import cos, sin

class Plane2(Plane):
    def __init__(self, subdivisions=(1,1), mode='triangle', pos:Vec3=(0,0,0), rot:Vec3=(0,0,0), uvs=None, **kwargs):
        super().__init__(subdivisions=(1,1), mode='triangle', **kwargs)
        # override Plane class to give possibility to pass UV coordinates
        self._UpdateUv(uvs)
        #self._MoveVertices(pos, rot)

    def _UpdateUv(self, uvs):
        if type(uvs) == type(list()):
            self.uvs = uvs

    def _rotate_x(self, v, q):
        x = v.x
        y = v.y
        z = v.z
        v.x = x
        v.y = y*cos(q) - z*sin(q)
        v.z = y*sin(q) + z*cos(q)
        return v
    def _rotate_y(self, v, q):
        x = v.x
        y = v.y
        z = v.z
        v.x = z*sin(q) + x*cos(q)
        v.y = y
        v.z = z*cos(q) - x*sin(q)
        return v
    def _rotate_z(self, v, q):
        x = v.x
        y = v.y
        z = v.z
        v.x = x*cos(q) - y*sin(q)
        v.y = x*sin(q) + y*cos(q)
        v.z = z
        return v

    def _rotate(self, vector, rotation):
        v = self._rotate_x(vector, (rotation.x))
        v = self._rotate_y(vector, (rotation.y))
        v = self._rotate_z(vector, (rotation.z))
        return v

    def _MoveVertices(self, pos, rot):
        newVerticles = list()
        for v in self.vertices:
            v = self._rotate(v, rot)
            
            newVerticles.append(v)

            v += pos
        return newVerticles