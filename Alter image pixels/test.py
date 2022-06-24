import numpy as np
from PIL import Image

data = [[[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]]

p = np.array(data)

print(p)
im = Image.fromarray((p).astype(np.uint8))
im.save('fig2_modified.png')
