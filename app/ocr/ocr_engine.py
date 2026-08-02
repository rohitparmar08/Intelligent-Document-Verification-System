import easyocr


class OCREngine:
    """
    OCR Engine using EasyOCR
    """

    def __init__(self):

        self.reader = easyocr.Reader(["en"], gpu=False)

    def extract_text(self, image_path):

        result = self.reader.readtext(image_path, detail=0)

        return result
