from PIL import Image
import cv2
import numpy as np
import png
import time
import os
import random

from dataProcessing import process_data

file = 'londontokyo.png'

def get_color_data(image_file):
    img_file = file
    img = cv2.imread(img_file, cv2.IMREAD_COLOR)           # rgb
    alpha_img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED) # rgba
    gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # grayscale

    print type(img)
    print 'RGB shape: ', img.shape        # Rows, cols, channels
    print 'ARGB shape:', alpha_img.shape
    print 'Gray shape:', gray_img.shape
    print 'img.dtype: ', img.dtype
    print 'img.size: ', img.size

    print '_____'

    start = time.time()
    newImg = open('output.png', 'wb')
    # f = open('colors.csv', 'w')
    y = 0

    colors = []
    while y < 2560:
      row = list()
      for x in range(1, 1600):
        
        rgb = img[x, y]
        l = list(row) 
        l.append(y)
        l.append(x)
        l.append(rgb)

        colors.append(l) 
      
      print y
      # print colors[1066]
      y += 1
    cleanData = []
    z = 0
    for color in colors:
        # print color
        cleanData.append(process_data(color))
        z += 1
        if z % 100 == True:
            print z
    print cleanData


get_color_data(file)

img = Image.new( 'RGB', (2560,1600), "black") # create a new black image
pixels = img.load() # create the pixel map

# print colors[102]
# testdata = cleanData  
def assign_color(data):
    x = 0
    for value in data:
    # for xPos in range(img.size[0]):    # for every pixel:
    #     for yPos in range(img.size[1]):
    # print  value
        xPos, yPos, rVal, gVal, bVal = value
            # print(value)
        rand = random.randint(1, 40) 
        if rand == 1:
            pixels[xPos,yPos] = (255, 255, 0)
        elif rand == 2:
            pixels[xPos,yPos] = (0, 191, 255)
        elif rand == 3:
            pixels[xPos,yPos] = (100, 0, 0)
        else:
            # pixels[xPos,yPos] = (0, 0, 0)
            pixels[xPos,yPos] = (bVal, gVal, rVal)
    # print x
    x += 1
        # print xPos, yPos, rVal, gVal, bVal

        # pixels[xPos,yPos] = (rVal, gVal, bVal) # set the colour accordingly


#             pixels[xPos,yPos] = (rVal, gVal, bVal) # set the colour accordingly

for image in range(1, 50):
    assign_color(cleanData)
    file_name = 'vidbmp/' + str('%03d') % image + '.bmp'
    print file_name
    img.save(file_name)

# my_raster_sort(my_image_data)

# img_data = img.load()
# for x, y, color in data:
#     img_data[x,y] = color

# print 'It took', time.time()-start, 'seconds.'
# 
