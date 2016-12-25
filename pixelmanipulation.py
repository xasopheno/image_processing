import cv2
import numpy as np
import png
import time
import os

img_file = 'londontokyo.png'
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

# print img[2, 2]
start = time.time()

# p = np.array([])
newImg = open('swatch.png', 'wb')
# f = open('rgbvalues.txt', 'w')
y = 0
# f.write('[')]
# colors = []
while y < 200:
  # print y
  # f.write('(')
  row = list()
  for pixel in range(1080):
    
    # print img[pixel, y]
    for value in img[pixel, y]:
      print value
      # l = list(row)
      row.append(str(value))
    # colors.append(row)  
  print y 
  y += 1
w = png.Writer(200, 3240) 
w.write(newImg, row)
      # row = tuple(l)
    # print colors
    # row = tuple(row)
    # for value in row
    #   colors.append(value)
    # colors.append(row)
  # print colors
      # f.write(str(value))
      # f.write(',')
    # f.write(' ')
  # f.seek(-2, os.SEEK_CUR)
  # f.write('),')

# newImg.close()

# print colors

# a = ('2',)
# items = ['o', 'k', 'd', 'o']

# l = list(a)

# for x in items:
#     l.append(x)

# print tuple(l)


# f.write(']')
# f.close

# data = tuple(open('rgbvalues.txt', 'r'))
# print data
# with open('rgbvalues.txt', 'r') as myfile:
#     data=myfile.read().replace('\n', '')
# f = open('rgbvalues.txt', 'r')
# print 'It took', time.time()-start, 'seconds.'

# with open('rgbvalues.txt') as my_file:
#   my_array = my_file.readlines()
#   # my_array = my_array[1:-1]
#   print my_array



# cv2.imshow('londontokyo.png', cv2.IMREAD_COLOR) 
