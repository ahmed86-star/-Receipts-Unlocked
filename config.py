import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OCR configuration
# WSL Ubuntu path for Tesseract
TESSERACT_CMD = r'/usr/bin/tesseract'

# Image processing configuration
MIN_CONFIDENCE = 80