from typing import List

def export_palette_scss(hex_codes: List[str], filename: str = "palette.scss") -> None:
    with open(filename, "w") as f:
        for i, hex_code in enumerate(hex_codes):
            f.write(f"$color-{i+1}: {hex_code};\n")
        if hex_codes:
            f.write(f"$primary-color: {hex_codes[0]};\n") 