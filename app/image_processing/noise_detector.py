import cv2
import numpy as np


class NoiseDetector:

    def __init__(self, image):
        self.image = image

    def noise_score(self):
        """
        Estimate image noise using Laplacian standard deviation.
        Higher value = More noise
        """

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        laplacian = cv2.Laplacian(gray, cv2.CV_64F)

        score = np.std(laplacian)

        return score

    def is_noisy(self, threshold=35):

        score = self.noise_score()

        if score > threshold:
            return True

        return False
