def get_UV_map():
    # setting up uv's
    dirt_uvs = [(0,0.5), (0.5,0.5), (0,1), (0.5,1)]
    grass_uvs_top = [(0,1), (0.5,1), (0,1.5), (0.5,1.5)]
    grass_uvs_side = [(0.5,0.5), (1,0.5), (0.5,1), (1,1)]
    stone_uvs = [(0.5,1), (1,1), (0.5,1.5), (1,1.5)]

    # creating a table of faces for block's
    dirt    = {
        "front":dirt_uvs,       "back":dirt_uvs,
        "top":dirt_uvs,         "bottom":dirt_uvs,
        "right":dirt_uvs,       "left":dirt_uvs
        }

    grass   = {
        "front":grass_uvs_side, "back":grass_uvs_side,
        "top":grass_uvs_top,    "bottom":dirt_uvs,
        "right":grass_uvs_side, "left":grass_uvs_side
        }
        
    stone   = {
        "front":stone_uvs,      "back":stone_uvs,       
        "top":stone_uvs,        "bottom":stone_uvs,     
        "right":stone_uvs,      "left":stone_uvs
        }
    
    return {1:dirt, 2:grass, 3:stone}

UV_MAP = get_UV_map()