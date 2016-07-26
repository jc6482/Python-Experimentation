#Juan Carlos Ramirez
#Drawing a dimension wise spiral

import sys
import argparse

parser = argparse.ArgumentParser(description = "Creates a spiral using a grid and '#'")
parser.add_argument("-width",help="define the width",type=int, default=5)

args = parser.parse_args()

printGrid = [[" " for x in range(args.width)] for y in range(args.width)]


def traverseGrid(grid,startCol,startRow,steps,direction):
        if steps == 1:
            if direction == "right":
                    grid[startRow][startCol + 1] = "#"
            elif direction == "down":
                    grid[startRow+1][startCol] = "#"
            elif direction == "left":
                    grid[startRow][startCol - steps] = "#"
            elif direction == "up":
                    grid[startRow - steps][startCol] = "#"
            return
       
        if direction == "right":
            for x in range(startCol,startCol + steps):
                grid[startRow][x] = "#"
            traverseGrid(grid,startCol + steps-1, startRow,steps-1,"down")
        elif direction == "down":
            for x in range(startRow,startRow + steps):
                grid[x][startCol] = "#"
            traverseGrid(grid,startCol,startRow + steps-1,steps-1,"left")
        elif direction == "left":
            for x in range(startCol - steps + 1 ,startCol):
                grid[startRow][x] = "#"
            traverseGrid(grid,startCol - steps + 1,startRow,steps-1,"up")
        elif direction == "up":
            for x in range(startRow - steps+1,startRow):
                grid[x][startCol] = "#"
            traverseGrid(grid,startCol,startRow - steps + 1,steps-1,"right")

if(not args.width <= 1):

    traverseGrid(printGrid,0,0,args.width,"right")
elif args.width == 1:
    printGrid[0][0] = "#"
else:
    print "Well NO spirals for you :/"
    

for x in range(args.width):
    for y in range(args.width):
        sys.stdout.write(printGrid[x][y])
    sys.stdout.write("\n")
        

