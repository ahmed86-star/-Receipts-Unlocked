import sys
import os
import cv2

# Add the parent directory of 'src' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.image_processor import ImageProcessor

def test_preprocess_image():
    # Path to the test image (using a raw string to avoid escape character issues)
    image_path = r"C:\Users\progr\OneDrive\Desktop\SecLab\Receipt-vison\test_images\media_1cdf08dccb12d6bfe32e9ad12d04271a869fc40a2.png"

    # Check if the image file exists
    if not os.path.isfile(image_path):
        print(f"Image file not found: {image_path}")
        return  # Exit the function if the file does not exist

    # Call the preprocess_image method
    processed_image = ImageProcessor.preprocess_image(image_path)

    # Check if the processed image is not None
    if processed_image is not None:
        print("Image processed successfully.")
        # Optionally, display the image (requires a GUI environment)
        cv2.imshow("Processed Image", processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image processing failed.")

if __name__ == "__main__":
    test_preprocess_image() 