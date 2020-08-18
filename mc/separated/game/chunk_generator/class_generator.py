from ..settings import CHUNK_SIZE, CHUNK_COUNT, TEXTURE, GENERATOR_MODE
from ..uv_map import UV_MAP
from ursina import scene
from ._generator_classes import Chunk
import random


class Generator():
    def __init__(self, generetor_mode=GENERATOR_MODE):
        self.generetor_mode = generetor_mode
        self.Generate()

    def Generate(self):
        chunk_map = self._Generate_chunk_3d_table()
        chunks=[]

        try:
        # generating chunk entity
            for x in range(CHUNK_COUNT):
                for z in range(CHUNK_COUNT):
                    chunks.append(
                        Chunk(
                            parent=scene, 
                            uv_map=UV_MAP,
                            chunk_map=chunk_map, 
                            x=x*CHUNK_SIZE, 
                            z=z*CHUNK_SIZE, 
                            texture=TEXTURE
                        )
                    )
        finally:
            return chunks


    def _Generate_chunk_3d_table(self):
        # generate table
        chunk = []
        for y in range(CHUNK_SIZE):

            chunkY=[]

            for x in range(CHUNK_SIZE):
                chunkX=[]
                for z in range(CHUNK_SIZE):
                    #choose method of generation
                    if self.generetor_mode == 'simple':
                        block = self._simple_chunk_gen(y)
                    if self.generetor_mode == 'random':
                        block = self._random_chunk_gen()

                    chunkX.append(block)

                chunkY.append(chunkX)

            chunk.append(chunkY)

        return chunk

    def _simple_chunk_gen(self,y):
        block = 1 # 1 == dirt

        if y == CHUNK_SIZE-1:
            block = 2 # 2 == grass
        elif y <= int(CHUNK_SIZE*0.5):
            block = 3 # 3 == stone
            
        return block

    def _random_chunk_gen(self):
        # generate random block (50/50 empty spaces)
        block = 0 if random.randint(0,1) <= 0 else random.randint(1,3)
            
        return block