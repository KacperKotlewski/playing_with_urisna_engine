from ursina.prefabs.first_person_controller import FirstPersonController 
from .settings import CHUNK_SIZE
from .chunk_generator import Generator

def init():
    Generator()
    player = FirstPersonController(position=(0,CHUNK_SIZE+1,0))