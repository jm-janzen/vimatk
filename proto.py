import random
import sys

tiles = ['f', 'o', 'o', ' ']

prev = 0, ''
for i in range(25):
    sys.stdout.write(f"{i}:\t")
    for j in range(80):
        tile      = tiles[random.randint(0, len(tiles)-1)]
        prev_cnt  = prev[0]
        prev_tile = prev[1]

        # TODO Check if this is Nth in sequence,
        # and reshuffle if so
        if prev_tile == tile:
            prev_cnt += 1
        else:
            prev_tile = tile
            prev_cnt  = 1
        prev = prev_cnt, prev_tile

        sys.stdout.write(tile)
    sys.stdout.write(f"\t {prev}\n")



