from ursina import window, Texture

# window settings
#window.fullscreen = True
window.borderless = False
window.exit_button.visible = False  # additional exit button
window.cog_button.enabled = False   # ursina additional gamedev options
window.center_on_screen() 

CHUNK_SIZE  =   8  # count of block per chunk ^3
CHUNK_COUNT =   1   # count of chunks to load ^2
TEXTURE = Texture('textures/cube_textures.png')
TEXTURE.filtering = False
ENTITY_MODE = 'triangle'
GENERATOR_MODE = 'random' # values: 'simple'; 'random'
COLLISION = True