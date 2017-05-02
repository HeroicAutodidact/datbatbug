from cv2 import *
import numpy as np
from image_manager import IM

class PreProcessor:

    def __init__(self):
        self.clahe = createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    def contrastEnhanceBW(self, imgpath):
        img = imread(imgpath, 0)
        return self.clahe.apply(img)

    def contrastEnhanceColor(self, img):
        """

        :param img:
        :return:
        """
        cimg = img.copy()
        for ch in range(3):
            cimg[:,:,ch] = self.clahe.apply(extractChannel(cimg, ch, cimg))
        return cimg

    def tenContrastedBW(self):
        for i, imgpath in enumerate(IM.get_image_paths(10)):
            img = imread(imgpath, 0)
            clahe = createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
            contrasted_img = clahe.apply(img)
            imwrite("out/%d.jpg" % i, contrasted_img)
            imwrite("out/orig_%d.jpg" % i, img)

    def tenContrastedColor(self):
        for i, img in enumerate(IM.get_images(40)):
            IM.write_n(i, self.contrastEnhanceColor(img))

PP = PreProcessor()

