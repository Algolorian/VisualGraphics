import numpy as np
from PIL import Image

im = Image.open('fig2.png')
data = np.array(im)

for i in range(10, 200):
    for j in range(10, 400):
        data[i][j] = [0, 50, 200]

r1, g1, b1 = 255, 255, 255
for i in data:
    print(i)

im = Image.fromarray(data)
im.save('fig2_modified.png')
