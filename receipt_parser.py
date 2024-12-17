from openai import OpenAI
from config import OPENAI_API_KEY

class ReceiptParser:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def parse_receipt(self, text):
        """
        Parse the OCR text into structured JSON using OpenAI API.
        """
        prompt = f"""
        Convert the following receipt text into a structured JSON object.
        Include fields for store_name, date, items (with name, quantity, and price),
        subtotal, tax, and total.
        
        Receipt text:
        {text}
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a receipt parsing assistant. Convert receipt text to JSON format."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content 