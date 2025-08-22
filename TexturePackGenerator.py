import yaml
import json

from fontTools.t1Lib import write
from numpy.ma.core import append
from pyparsing import Empty

cube_model_blocks = [
    "stone", "dirt", "grass_block", "oak_planks", "spruce_planks", "birch_planks", "jungle_planks",
    "acacia_planks", "dark_oak_planks", "mangrove_planks", "bamboo_planks", "cherry_planks",
    "crimson_planks", "warped_planks", "clay", "snow_block",
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
    "mud_bricks", "packed_mud", "terracotta", "white_terracotta", "orange_terracotta",
    "magenta_terracotta", "light_blue_terracotta", "yellow_terracotta", "lime_terracotta",
    "pink_terracotta", "gray_terracotta", "light_gray_terracotta", "cyan_terracotta",
    "purple_terracotta", "blue_terracotta", "brown_terracotta", "green_terracotta",
    "red_terracotta", "black_terracotta", "white_concrete", "orange_concrete",
    "magenta_concrete", "light_blue_concrete", "yellow_concrete", "lime_concrete", "pink_concrete",
    "gray_concrete", "light_gray_concrete", "cyan_concrete", "purple_concrete", "blue_concrete",
    "brown_concrete", "green_concrete", "red_concrete", "black_concrete", "hay_block", "bookshelf",
    "cobblestone", "mossy_cobblestone","granite", "polished_granite",
    "diorite", "polished_diorite","andesite", "polished_andesite","smooth_stone",
    "quartz_block","smooth_quartz","chiseled_quartz_block",
    "sandstone", "cut_sandstone", "smooth_sandstone", "chiseled_sandstone", "red_sandstone",
    "cut_red_sandstone", "smooth_red_sandstone", "chiseled_red_sandstone",
    "end_stone_bricks","prismarine_bricks", "coarse_dirt", "podzol",
    "mycelium", "rooted_dirt", "moss_block",
    "warped_nylium", "crimson_nylium", "oak_log", "spruce_log", "birch_log", "jungle_log",
    "acacia_log", "dark_oak_log", "mangrove_log", "cherry_log", "bamboo_block",
    "crimson_stem", "warped_stem",
    "oak_wood", "spruce_wood", "birch_wood", "jungle_wood",
    "acacia_wood", "dark_oak_wood", "mangrove_wood", "cherry_wood",
    "crimson_hyphae", "warped_hyphae",
    "stripped_oak_log", "stripped_spruce_log", "stripped_birch_log", "stripped_jungle_log",
    "stripped_acacia_log", "stripped_dark_oak_log", "stripped_mangrove_log", "stripped_cherry_log",
    "stripped_bamboo_block", "stripped_crimson_stem", "stripped_warped_stem",
    "stripped_oak_wood", "stripped_spruce_wood", "stripped_birch_wood", "stripped_jungle_wood",
    "stripped_acacia_wood", "stripped_dark_oak_wood", "stripped_mangrove_wood", "stripped_cherry_wood",
    "stripped_crimson_hyphae", "stripped_warped_hyphae",
    "crafting_table", "smithing_table", "fletching_table", "cartography_table", "loom",
    "note_block", "jukebox", "target", "beacon","dried_kelp_block",
    "melon", "pumpkin", "carved_pumpkin", "jack_o_lantern","red_mushroom_block", "brown_mushroom_block", "mushroom_stem"
]


###define funcs earlier here
def writeToJsonModel(name, layer, index, x, y):
    json_file = open(f"resources/assets/minecraft/models/block/{cube_model_blocks[index]}.json", 'w')
    json_data = {
        "parent": f"minecraft:block/{layer}",
        "textures": {
            "texture": f"tiles:{name}/{name}_{x}_{y}",
            "particle": f"tiles:{name}/{name}_{x}_{y}"
        }
    }
    json.dump(json_data, json_file)

def writeToJsonBlockstate(json_data, index):
    json_file = open(f"resources/assets/minecraft/blockstates/{cube_model_blocks[index]}.json", 'w')
    json.dump(json_data, json_file)

##########################
input("check block index before running!")
tileset = input("tileset name: ") + ".yaml"
tileset_yaml = yaml.safe_load(open(f"tileset_configs/{tileset}"))

#################### BINDEX
block_index = 57 #CHANGE AS REQUIRED
#####################################
start_block_index = block_index #SAVE FOR LATER
variants_json_list = []

for tiles in tileset_yaml['tiletypes']:
    tiles['block-ids'].clear()
    variants_json_list.clear()
    if tiles['auto-tile']:
        print("auto-tiling enabled")
        (x_start,y_start) = tiles['start-position']
        for y in range(0,3):
            for x in range(0,8):
                x_off = x_start + x
                y_off = y_start + y
                tiles['block-ids'].append(cube_model_blocks[block_index])
                writeToJsonModel(tileset_yaml['name'],tiles['layer'],block_index, x_off, y_off)
                json_data = {
                    "variants": {
                        "": {
                            "model": f"minecraft:block/{cube_model_blocks[block_index]}"
                        }
                    }
                }
                writeToJsonBlockstate(json_data, block_index)
                block_index += 1
    tiles['block-ids'].append(cube_model_blocks[block_index])
    for x in range (0,tiles['variants']): # Give variants cool mc files
        (x_start, y_start) = tiles['start-position']
        if tiles['auto-tile']:
            y_off = y_start + 3
        else:
            y_off = y_start
        x_off = x_start + x
        variants_json_list.append({
            "model": f"minecraft:block/{cube_model_blocks[block_index]}",
            "weight": tiles['weights'][x]
            })
        writeToJsonModel(tileset_yaml['name'], tiles['layer'], block_index, x_off, y_off)
        block_index += 1

    json_data = {
        "variants": {
            "": variants_json_list
        }
    }
    writeToJsonBlockstate(json_data, block_index - tiles['variants'])

end_block_index = block_index - 1
tileset_yaml['blockidsused'] = [start_block_index, end_block_index]
with open(f"tileset_configs/{tileset}", "w") as file_write:
    yaml.dump(tileset_yaml, file_write)



