import cv2
import numpy as np


class RotationDetector:
    """
    Detects document rotation angle.
    """

    def __init__(self, image):
        self.image = image

    def rotation_angle(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 50, 150)

        lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

        if lines is None:
            return 0.0

        angles = []

        for line in lines:

            rho, theta = line[0]

            angle = (theta * 180 / np.pi) - 90

            if -45 <= angle <= 45:
                angles.append(angle)

        if len(angles) == 0:
            return 0.0

        return float(np.median(angles))

    def is_rotated(self, threshold=2):

        angle = self.rotation_angle()

        return abs(angle) > threshold
