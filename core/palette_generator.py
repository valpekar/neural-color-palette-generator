from typing import List
import google.generativeai as genai  # type: ignore
from config import API_KEY, GEMINI_MODEL, PALETTE_SIZE

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set. Please set it in your .env file or environment variables.")

class PaletteGenerator:
    def __init__(self):
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)

    def generate_palette(self, prompt: str, palette_size: int = PALETTE_SIZE) -> List[str]:
        """
        Generate a color palette from a text prompt using Gemini.
        Returns a list of hex color codes.
        """
        system_prompt = (
            f"Generate a color palette of {palette_size} distinct colors for the theme: '{prompt}'. "
            "The color scheme should be modern and stylish, Pinterest worthy."
            "Return only a comma-separated list of hex color codes, no extra text."
        )
        response = self.model.generate_content(system_prompt)
        hex_codes = self._extract_hex_codes(response.text, palette_size)
        return hex_codes

    @staticmethod
    def _extract_hex_codes(text: str, palette_size: int) -> List[str]:
        import re
        hex_pattern = r"#(?:[0-9a-fA-F]{3}){1,2}"
        codes = re.findall(hex_pattern, text)
        return codes[:palette_size] 