#Juan Carlos Ramirez

import cImage as image

response = raw_input('Use Default Values (Y/N): ').lower()

while( not (response == "y" or response == "n")):
	response = raw_input('Use Default Values (Y/N): ').lower()

if response == 'n':
		
	cornerA = int(raw_input('Corner A (EG. 200): '))
	cornerB = int(raw_input('Corner B (EG. 200): '))
	side = int(raw_input('Side (EG. 20): '))

	width = int(raw_input('Width (EG. 200): '))
	height = int(raw_input('Height (EG. 200): '))
else:
	cornerA = 125
	cornerB = 369
	side = 544

	width = 300
	height = 300
	
newIm = image.EmptyImage(width,height)

for i in range(width):
	for j in range(height):
		x = cornerA + i * side/width
		y = cornerB + j * side/height
		c = int((x*x) + (y*y))
		#print("The Result(%r,%r): %r" % (cornerA + (i * (side/500)),cornerB + (j * (side/100)),c))
		if (c % 3) == 0:
			newIm.setPixel(i,j,image.Pixel(255,0,0))
		elif (c % 3) == 1:
			newIm.setPixel(i,j,image.Pixel(255,255,255))
		else:
			newIm.setPixel(i,j,image.Pixel(0,0,0))
			

win = image.ImageWin("Custom Wallpaper",width,height)
newIm.draw(win)
win.exitonclick()

response = raw_input('Save Image (Y/N): ').lower()

while( not (response == "y" or response == "n")):
	response = raw_input('Save Image (Y/N): ').lower()
	
if response == 'y':
	name = raw_input('Name it: ')
	newIm.savePIL(name)