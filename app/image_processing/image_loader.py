import cv2
import os


class ImageLoader:
    """
    Responsible for loading an image from disk.
    """

    def __init__(self, image_path):
        self.image_path = image_path

    def load_image(self):
        """
        Load image using OpenCV.
        """

        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image not found: {self.image_path}")

        image = cv2.imread(self.image_path)

        if image is None:
            raise ValueError("Unable to read image.")

        return image
