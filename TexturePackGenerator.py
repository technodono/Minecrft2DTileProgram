import yaml
import json

from fontTools.t1Lib import write
from numpy.ma.core import append
from pyparsing import Empty

cube_model_blocks = [
    "stone", "dirt", "grass_block", "oak_planks", "spruce_planks", "birch_planks", "jungle_planks",
    "acacia_planks", "dark_oak_planks", "mangrove_planks", "bamboo_planks", "cherry_planks",
    "crimson_planks", "warped_planks", "sand", "red_sand", "gravel", "clay", "snow_block",
    "ice", "packed_ice", "blue_ice", "coal_block", "iron_block", "gold_block", "diamond_block",
    "emerald_block", "netherite_block", "copper_block", "waxed_copper_block", "waxed_exposed_copper",
    "waxed_weathered_copper", "waxed_oxidized_copper", "cut_copper", "waxed_cut_copper",
    "redstone_block", "lapis_block", "amethyst_block", "calcite", "tuff", "dripstone_block",
    "deepslate", "polished_deepslate", "cobbled_deepslate", "blackstone", "polished_blackstone",
    "chiseled_polished_blackstone", "gilded_blackstone", "basalt", "smooth_basalt", "end_stone",
    "purpur_block", "purpur_pillar", "netherrack", "nether_bricks", "red_nether_bricks",
    "chiseled_nether_bricks", "magma_block", "soul_sand", "soul_soil", "glowstone", "shroomlight",
    "ancient_debris", "crying_obsidian", "obsidian", "prismarine", "dark_prismarine", "sea_lantern",
    "bricks", "stone_bricks", "mossy_stone_bricks", "cracked_stone_bricks", "chiseled_stone_bricks",
    "deepslate_bricks", "cracked_deepslate_bricks", "deepslate_tiles", "cracked_deepslate_tiles",
    "mud_bricks", "packed_mud", "mud", "terracotta", "white_terracotta", "orange_terracotta",
    "magenta_terracotta", "light_blue_terracotta", "yellow_terracotta", "lime_terracotta",
    "pink_terracotta", "gray_terracotta", "light_gray_terracotta", "cyan_terracotta",
    "purple_terracotta", "blue_terracotta", "brown_terracotta", "green_terracotta",
    "red_terracotta", "black_terracotta", "concrete", "white_concrete", "orange_concrete",
    "magenta_concrete", "light_blue_concrete", "yellow_concrete", "lime_concrete", "pink_concrete",
    "gray_concrete", "light_gray_concrete", "cyan_concrete", "purple_concrete", "blue_concrete",
    "brown_concrete", "green_concrete", "red_concrete", "black_concrete", "hay_block", "bookshelf"
]


###define funcs earlier here
def writetToJsonModel(name, layer, index, x, y, variant):
    json_file = open(f"resources/assets/minecraft/models/block/{cube_model_blocks[index]}.json", 'w')
    json_data = {
        "parent": f"minecraft:block/{layer}",
        "textures": {
            "all": f"tiles:{name}/{name}_{x}_{y}{variant}"
        }
    }
    json.dump(json_data, json_file)

def writeToJsonBlockstate(json_data, index):
    json_file = open(f"resources/assets/minecraft/blockstates/{cube_model_blocks[index]}.json", 'w')
    json.dump(json_data, json_file)

##########################x

tileset = input("tileset name: ") + ".yaml"
tilesetopened = open(tileset)
tileset_yaml = yaml.safe_load(tilesetopened)
block_index = 0

for tiles in tileset_yaml['tiletypes']:
    tiles['block-ids'].clear()
    if tiles['auto-tile']:
        print("auto-tiling enabled")
        (x_start,y_start) = tiles['start-position']
        for x in range(0,7):
            for y in range(0,2):
                x+= x_start
                y += y_start
                tiles['block-ids'].append(cube_model_blocks[block_index])
                writetToJsonModel(tileset_yaml['name'],tiles['layer'],block_index, x, y,"")
                block_index += 1

    variants_json_list = []
    block_index += 1 ## Advance block by only 1 for a block and it's states
    for x in range (0,tiles['variants']):
        (x_start, y_start) = tiles['start-position']
        if tiles['auto-tile']:
            y = y_start + 3
        else:
            y += y_start
        x += x_start
        variants_json_list[cube_model_blocks[block_index]] = {
            "model": cube_model_blocks[block_index],
            "weight": tiles['weights'][x]
            }
        tiles['block-ids'].append(cube_model_blocks[block_index])
        writetToJsonModel(tileset_yaml['name'], tiles['layer'], block_index, x, y)

    json_data = {
        "variants": variants_json_list
    }
    writeToJsonBlockstate(json_data, block_index)

with open(tileset, "w") as file_write:
    yaml.dump(tileset_yaml, file_write)



