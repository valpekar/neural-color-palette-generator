from typing import Tuple, cast

def hex_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    """Convert 6-digit hex color code to RGB tuple."""
    hex_code = hex_code.lstrip('#')
    if len(hex_code) == 6:
        rgb = tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))
        return cast(Tuple[int, int, int], rgb)
    raise ValueError("Only 6-digit hex codes are supported.")


def rgb_to_str(rgb: Tuple[int, int, int]) -> str:
    """Format RGB tuple as string."""
    return f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})" 