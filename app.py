from flask import Flask, request, jsonify
from core.palette_generator import PaletteGenerator

app = Flask(__name__)
generator = PaletteGenerator()

@app.route('/generate_palette', methods=['POST'])
def generate_palette():
    data = request.get_json(silent=True) or {}
    prompt = data.get('prompt', '')
    hex_codes = generator.generate_palette(prompt)
    return jsonify({'palette': hex_codes})

if __name__ == '__main__':
    app.run(debug=True) 