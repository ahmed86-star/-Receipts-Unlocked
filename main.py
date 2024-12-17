from image_processor import ImageProcessor
from ocr_handler import OCRHandler
from receipt_parser import ReceiptParser
import json

def process_receipt(image_path):
    """
    Main function to process a receipt image and return structured data.
    """
    try:
        # Initialize components
        ocr = OCRHandler()
        parser = ReceiptParser()

        # Process image
        processed_image = ImageProcessor.preprocess_image(image_path)

        # Extract text using OCR
        extracted_text = ocr.extract_text(processed_image)

        # Parse text into structured data
        parsed_data = parser.parse_receipt(extracted_text)

        # Convert string response to JSON
        structured_data = json.loads(parsed_data)

        return structured_data

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Example usage
    receipt_image_path = "path/to/your/receipt.jpg"
    result = process_receipt(receipt_image_path)
    print(json.dumps(result, indent=2)) 