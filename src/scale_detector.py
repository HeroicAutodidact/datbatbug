import numpy as np
from cv2 import *
import imutils

class ScaleDetector:

    def __init__(self):
        self.penny_template = imread("penny_template.jpg")
        self.temp_height, self.temp_width = self.penny_template.shape[:2]

    def get_scale(self, img):
        scalesToTry = np.linspace(.7, 1.4, 20)
        best_val_so_far = 0
        best_loc_so_far = None
        for scale in scalesToTry:
            resized_penny = imutils.resize(self.penny_template, width=(scale * self.penny_template.shape[1]))
            match_space = matchTemplate(img, resized_penny, TM_SQDIFF)
            (_, max_val, _, max_loc) = minMaxLoc(match_space)
            if max_val > best_val_so_far:
                best_val_so_far = max_val
                best_scale_so_far = scale
                best_loc_so_far = max_loc
        r = best_scale_so_far
        loc = best_loc_so_far
        (startX, startY) = (int(loc[0] * r), int(loc[1] * r))
        (endX, endY) = (int((loc[0] + self.temp_height) * r), int((loc[1] + self.temp_height) * r))
        rectangle()

SD = ScaleDetector()
