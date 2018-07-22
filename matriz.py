import matplotlib.pyplot as plt
import numpy as np
import cv2

Y = []

for x in range(3):
   for y in range(30):
       Y.append([[255,0,0],[0,255,0],[0,0,255]])

YYY = np.array(Y)
YY = YYY.reshape(-1,30,3)

plt.imshow(YY)
plt.show()
