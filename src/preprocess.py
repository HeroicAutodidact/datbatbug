from cv2 import *
import numpy as np
from image_manager import IM

for i, imgpath in enumerate(IM.get_image_paths(10)):
    img = imread(imgpath, 0)
    clahe = createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    contrasted_img = clahe.apply(img)
    imwrite("out/%d.jpg" % i, contrasted_img)
    imwrite("out/orig_%d.jpg" % i, img)

