from unittest import TestCase

import numpy as np
from PIL import Image
from matplotlib import image as mpimg, pyplot as plt
import cv2 as cv

from config import images_path
from main import otsu_main


class VVTest(TestCase):
    def test_collator(self):
        image_path = images_path + 'vladimir_vladimirovich_img.jpeg'

        img = mpimg.imread(image_path)
        res = otsu_main(img)
        res_np = np.array(res, dtype=np.uint8) * 255

        img_cv = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        ret, thresh1 = cv.threshold(img_cv, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

        fig, ax = plt.subplots(1, 3, figsize=(10, 5))
        image = Image.fromarray(res_np, mode='L')
        image_lib = Image.fromarray(thresh1, mode='L')

        ax[0].imshow(img)
        ax[0].set_title('Original Image')
        ax[0].axis('off')

        ax[1].imshow(image, cmap='gray')
        ax[1].set_title('Otsu Method')
        ax[1].axis('off')

        ax[2].imshow(image_lib, cmap='gray')
        ax[2].set_title('OpenCV Otsu')
        ax[2].axis('off')
        plt.show()
        s = res_np == thresh1
        true_count = np.sum(s)
        false_count = s.size - true_count

        # Check that result algorithm works similar to library
        self.assertTrue((false_count / (false_count + true_count)) < 0.01)
