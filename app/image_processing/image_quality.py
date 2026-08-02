import cv2
import numpy as np


class ImageQuality:

    def __init__(self, image):
        self.image = image

    def get_dimensions(self):
        """
        Returns image height and width.
        """
        height, width = self.image.shape[:2]
        return width, height

    def get_brightness(self):
        """
        Calculate average brightness.
        """
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)
        return brightness

    def is_low_resolution(self):
        """
        Checks if image resolution is too low.
        """
        width, height = self.get_dimensions()

        if width < 800 or height < 600:
            return True

        return False
