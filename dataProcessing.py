import numpy as np
from array import array

# data = '[1070, 9, array([21, 39, 43], dtype=uint8)]'
# 
# data = '[102, 0, array([ 35, 137, 164], dtype=uint8)]'

def process_data(data):
  """
  This takes RGB data from writePng in the following shape
  
  data = '[1070, 9, array([21, 39, 43], dtype=uint8)]'
  
  and returns an array containing the values
  xPos
  yPos
  and the three 'R' 'G' 'B' values. 
  """
  # print data
  datac = []
  for word in str(data).split():
    datac.append(word)
  datac[0] = int(datac[0][1:-1])
  datac[1] = int(datac[1][0:-1])
  # print datac[2]
  if str(datac[2]) == "array([":
    datac.remove(datac[2])
    datac[2] = int(datac[2][:-1])
  else:
    datac[2] = int(datac[2][7:-1])
  datac[3] = int(datac[3][:-1])
  datac[4] = int(datac[4][:-2])
  datac.remove(datac[5])
  # datac.sort()
  return datac

# uncomment this and data in line 4 to test
# usabledata = process_data(data)
# print usabledata
