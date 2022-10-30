import imageio.v2 as imageio
from pathlib import Path
import sys
import os

currentdir = "C:\\Users\\user\\Documents\\manybodies\\"
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, currentdir)

image_path = Path(currentdir + 'd')
images = list(image_path.glob('*.png'))

image_list = []

for file_name in images:
    image_list.append(imageio.imread(file_name))
    print(file_name)


# creating the gif
print("ended")
imageio.mimwrite('galaxysimd.gif', image_list, fps=2, loop=True)
print("endend finnaly")