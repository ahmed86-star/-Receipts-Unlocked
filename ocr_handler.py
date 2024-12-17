import pytesseract
from config import TESSERACT_CMD

class OCRHandler:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

    def extract_text(self, image):
        """
        Extract text from the preprocessed image using Tesseract OCR.
        """
        try:
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            raise Exception(f"OCR processing failed: {str(e)}") 