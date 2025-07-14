from typing import List
from rich.console import Console  # type: ignore
from rich.table import Table  # type: ignore
from core.color_utils import hex_to_rgb, rgb_to_str


def display_palette(hex_codes: List[str]) -> None:
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Swatch")
    table.add_column("Hex")
    table.add_column("RGB")
    for hex_code in hex_codes:
        rgb = hex_to_rgb(hex_code)
        rgb_str = rgb_to_str(rgb)
        table.add_row(f"[white on {hex_code}]     ", hex_code, rgb_str)
    console.print(table) 