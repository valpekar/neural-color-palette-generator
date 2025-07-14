from flask import Flask, request, jsonify
from core.palette_generator import PaletteGenerator
from config import API_KEY, GEMINI_MODEL
import google.generativeai as genai  # type: ignore

app = Flask(__name__)
generator = PaletteGenerator()

@app.route('/generate_palette', methods=['POST'])
def generate_palette():
    data = request.get_json(silent=True) or {}
    prompt = data.get('prompt', '')
    user_api_key = data.get('api_key')
    # Use user-provided API key if present, else default
    if user_api_key:
        genai.configure(api_key=user_api_key)  # type: ignore
        model = genai.GenerativeModel(GEMINI_MODEL)  # type: ignore
        hex_codes = model.generate_content(
            f"Generate a color palette of 6 distinct colors for the theme: '{prompt}'. Return only a comma-separated list of hex color codes, no extra text."
        )
        # Extract hex codes using the same logic as PaletteGenerator
        import re
        codes = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", hex_codes.text)
        hex_codes = codes[:6]
    else:
        hex_codes = generator.generate_palette(prompt)
    return jsonify({'palette': hex_codes})

if __name__ == '__main__':
    app.run(debug=True) 