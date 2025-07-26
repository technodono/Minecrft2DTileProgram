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

def assignTileVariant(image, tile_pos,tile_colour):
    pixelNeighbours = []
    for y_neb in (-1, 0, 1):
        for x_neb in (-1, 0, 1):
            x_pos = tile_pos[0] + x_neb
            y_pos = tile_pos[1] + y_neb
            if 0 <= x_pos < image.width and 0 <= y_pos < image.height:
                pixel = image.getpixel((x_pos, y_pos))
                pixelNeighbours.append(1 if pixel == tuple(tile_colour) else 0)
            else:
                pixelNeighbours.append(1)
    for pattern_id in range(len(tile_patterns)):
        #print(f"Checking pattern {pixelNeighbours} against known listed pattern {tile_patterns[pattern_id]}")
        match = True
        for i, val in enumerate(tile_patterns[pattern_id]):
            if val == 2:
                continue  # 2 = wildcard, ignore this position
            if val != pixelNeighbours[i]:
                match = False
                break
        if match:
            print(f"Match found with ID: {pattern_id}")
            return pattern_id
    print("No tile matched, default to 24")
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
functionList = [f"fill 0 0 0 {LevelImage.width} 1 {LevelImage.height} air"]

for x in range(0,LevelImage.width):
    for y in range(0,LevelImage.height):
        SelectedTileRGBAColour = LevelImage.getpixel((x,y))
        TileTypeID = checkTile(SelectedTileRGBAColour)
        if tilesetyaml['tiletypes'][TileTypeID].get('auto-tile'):
            print(f"auto-tile found with ID: {TileTypeID}")
            variantID = assignTileVariant(LevelImage, (x, y), tilesetyaml['tiletypes'][TileTypeID].get('colour', None))
        else:
            variantID = 0;
        if tilesetyaml['tiletypes'][TileTypeID].get('layer') == 'bg':
            functionList.append(f"setblock {x} 0 {y} {tilesetyaml['tiletypes'][TileTypeID].get('block-ids')[variantID]}")
        else:
            functionList.append(f"setblock {x} 1 {y} {tilesetyaml['tiletypes'][TileTypeID].get('block-ids')[variantID]}")

for command in functionList:
    print(command)
