import os
from PIL import Image
ResourcePackScale = 16
ImageOutputDir = os.path.join("resources", "assets", "tiles", "textures", "tile","")
os.makedirs(ImageOutputDir, exist_ok=True)

TilesetName = input("Please enter the name of the tileset you would like to generate: ")
TilesetImage = Image.open(TilesetName +".png")
for x in range(0,TilesetImage.width,ResourcePackScale):
    for y in range(0,TilesetImage.height,ResourcePackScale):

        quadrant = (int(x/ResourcePackScale), int(y/ResourcePackScale))
        SplicedImage = TilesetImage.crop((x,y,x+ResourcePackScale,y+ResourcePackScale))
        SplicedImage.save(ImageOutputDir + TilesetName + "_" + str(quadrant[0]) + "_" + str(quadrant[1]) + ".png")

