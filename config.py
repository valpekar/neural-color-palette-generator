import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "models/gemini-1.5-flash"
PALETTE_SIZE = 6  # Default number of colors in palette 