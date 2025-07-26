import os
import sys
from PIL import Image
import yaml
#row_1

tile_patterns = [
    (2, 0, 2,
     0, 1, 1,
     2, 1, 1),
    (2, 0, 2,
     1, 1, 1,
     2, 1, 2),
    (2, 0, 2,
     1, 1, 0,
     1, 1, 2),
    (2, 0, 2,
     0, 1, 1,
     2, 0, 2),
    (2, 0, 2,
     1, 1, 1,
     2, 0, 2),
    (2, 0, 2,
     1, 1, 0,
     2, 0, 2),
    (2, 0, 2,
     0, 1, 0,
     2, 1, 2),
    (-1,),
    #row2
    (2, 1, 2,
     0, 1, 1,
     2, 1, 2),
    (2, 0, 2,
     0, 1, 0,
     2, 0, 2),
    (2, 1, 2,
     1, 1, 0,
     2, 1, 2),
    (1, 1, 2,
     1, 1, 1,
     2, 1, 0),
    (2, 1, 1,
     1, 1, 1,
     0, 1, 2),
    (-1,),
    (2, 1, 2,
     0, 1, 0,
     2, 1, 2),
    (-1,),
    #row3
    (2, 1, 2,
     0, 1, 1,
     2, 0, 2),
    (2, 1, 2,
     1, 1, 1,
     2, 0, 2),
    (2, 1, 2,
     1, 1, 0,
     2, 0, 2),
    (2, 1, 0,
     1, 1, 1,
     1, 1, 2),
    (0, 1, 2,
     1, 1, 1,
     2, 1, 1),
    (-1,),
    (2, 1, 2,
     0, 1, 0,
     2, 0, 2),
    (-1,)
]
def substitute_wildcards(pattern, neighbors):
    return tuple(
        neighbors[i] if val == 2 else val
        for i, val in enumerate(pattern)
    )

def assignTileVariant(image, tile_pos,tile_colour):
    pixelNeighbours = []
    matchFound = False
    for x in range (-1,2):
        for y in range (-1,2):
            x_pos = tile_pos[0] + x
            y_pos = tile_pos[1] + y
            if 0 <= x_pos < image.width and 0 <= y_pos < image.height:
                pixel = image.getpixel((x_pos, y_pos))
                pixelNeighbours.append(1 if pixel == tile_colour else 0)
            else:
                pixelNeighbours.append(1)
    for pattern_id in range(len(tile_patterns)):
        checkedPattern = substitute_wildcards(tile_patterns[pattern_id],pixelNeighbours)
        if checkedPattern == pixelNeighbours:
            print(pattern_id)
            return (pattern_id)
    print(24)
    return 24

def checkTile(colour):
    for i in range(len(tilesetyaml['tiletypes'])):
        if colour == tuple(tilesetyaml['tiletypes'][i].get('colour', None)):
            return i
    print("Error: tile colour not matched!")
    sys.exit(1)

LevelName = input("Please enter the name of the level you would like to create: ")
tileset = input("assign tileset: ") + ".yaml"
with open(tileset, 'r') as f:
    tilesetyaml = yaml.safe_load(f)
LevelImage = Image.open(LevelName +".png")
functionList = []

for x in range(0,LevelImage.width):
    for y in range(0,LevelImage.height):
        print(LevelImage.getpixel((x,y)))
        TileTypeID = checkTile(LevelImage.getpixel((x,y)))
        if tilesetyaml['tiletypes'][TileTypeID].get('auto-tile'):
            variantID = assignTileVariant(LevelImage, (x, y), tilesetyaml['tiletypes'][TileTypeID].get('colour', None))
        else:
            variantID = 0;

        if tilesetyaml['tiletypes'][TileTypeID].get('layer') == 'bg':
            functionList.append(f"setblock {x} 0 {y} {tilesetyaml['tiletypes'][TileTypeID].get('block-ids')[variantID]}")
        else:
            functionList.append(f"setblock {x} 1 {y} {tilesetyaml['tiletypes'][TileTypeID].get('block-ids')[variantID]}")

for command in functionList:
    print(command)
