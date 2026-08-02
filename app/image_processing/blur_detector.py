import cv2


class BlurDetector:

    def __init__(self, image):
        self.image = image

    def blur_score(self):
        """
        Returns variance of Laplacian.
        Higher value = Sharp image
        Lower value = Blurry image
        """
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        score = cv2.Laplacian(gray, cv2.CV_64F).var()

        return score

    def is_blurry(self, threshold=100):

        score = self.blur_score()

        if score < threshold:
            return True

        return False
