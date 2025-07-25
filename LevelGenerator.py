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
    (-1),
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
    (-1),
    (2, 1, 2,
     0, 1, 0,
     2, 1, 2),
    (-1),
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
    (-1),
    (2, 1, 2,
     0, 1, 0,
     2, 0, 2),
    (-1)
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
    for pattern_id in range(tile_patterns):
        checkedPattern = substitute_wildcards(tile_patterns[pattern_id],pixelNeighbours)
        if checkedPattern == pixelNeighbours:
            return (pattern_id)
    return 25

