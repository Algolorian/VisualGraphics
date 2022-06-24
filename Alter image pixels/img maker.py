import numpy as np
from PIL import Image
from random import randint

file = open('test.py', 'r')
text = file.read()
file.close()


x = 1000
y = 1000

data = []
for _ in range(0, y):
    data.append([])
for i in range(0, y):
    print('Building image:', 100 * i/y, '%')
    for _ in range(0, x):
        data[i].append([randint(0, 255), randint(0, 255), randint(0, 255)])


print('Converting to array')
data = np.array(data)
print('Converting to uint8 codec')
im = Image.fromarray(data.astype(np.uint8))
print('Saving File')
im.save('img.png')
