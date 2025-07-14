from core.palette_generator import PaletteGenerator
from presentation.swatch_display import display_palette
from presentation.export_scss import export_palette_scss

def main():
    prompt = input("Enter a theme or description (e.g., 'autumn forest', 'melancholy neon'): ")
    generator = PaletteGenerator()
    hex_codes = generator.generate_palette(prompt)
    print("\nGenerated Palette:")
    display_palette(hex_codes)
    export_palette_scss(hex_codes)
    print("\nPalette exported to palette.scss")

if __name__ == "__main__":
    main()
