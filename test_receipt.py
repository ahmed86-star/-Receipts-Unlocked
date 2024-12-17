from src.main import process_receipt
import os

def test_receipt_processing():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a test directory if it doesn't exist
    test_dir = os.path.join(current_dir, 'test_images')
    os.makedirs(test_dir, exist_ok=True)
    
    # Path to test image
    test_image = os.path.join(test_dir, 'test_receipt.jpg')
    
    # Check if image exists
    if not os.path.exists(test_image):
        print(f"Please place a test receipt image at: {test_image}")
        return
    
    try:
        result = process_receipt(test_image)
        print("Processing successful!")
        print("Extracted data:")
        print(result)
    except Exception as e:
        print(f"Error processing receipt: {str(e)}")

if __name__ == "__main__":
    test_receipt_processing() 