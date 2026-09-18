# =========================================================
# Node: ColorPicker(beta version- Under Develop)
# Description: Select color from dropdown (with emoji) or enter HEX manually
# Author: OmiX
# Category: Tools
# =========================================================

class ColorPicker:
    """
    Select a color from preset list or enter HEX manually.

    Outputs:
        color_name - selected color name (STRING)
        hex_code   - hex color string (STRING)
        r          - red channel (INT)
        g          - green channel (INT)
        b          - blue channel (INT)
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset_color": (
                    [
                        "⚫ black",
                        "⚪ white",
                        "🔴 red",
                        "🟢 green",
                        "🔵 blue",
                        "🟡 yellow",
                        "🟠 orange",
                        "🟣 magenta",
                        "🟤 brown",
                        "🟦 cyan",
                        "⚙ gray",
                    ],
                    {"default": "⚪ white"}
                ),
                "hex_input": (
                    "STRING",
                    {"default": ""}
                ),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "INT", "INT", "INT")
    RETURN_NAMES = ("color_name", "hex_code", "r", "g", "b")

    FUNCTION = "select_color"
    CATEGORY = "👾 OmiXDev/Tools"

    def select_color(self, preset_color, hex_input):

        preset_map = {
            "⚫ black": ("black", "#000000"),
            "⚪ white": ("white", "#FFFFFF"),
            "🔴 red": ("red", "#FF0000"),
            "🟢 green": ("green", "#00FF00"),
            "🔵 blue": ("blue", "#0000FF"),
            "🟡 yellow": ("yellow", "#FFFF00"),
            "🟠 orange": ("orange", "#FFA500"),
            "🟣 magenta": ("magenta", "#FF00FF"),
            "🟤 brown": ("brown", "#8B4513"),
            "🟦 cyan": ("cyan", "#00FFFF"),
            "⚙ gray": ("gray", "#808080"),
        }

        if hex_input.strip() != "":
            hex_code = hex_input.strip()
            color_name = "custom"
        else:
            color_name, hex_code = preset_map[preset_color]

        if not hex_code.startswith("#"):
            hex_code = "#" + hex_code

        hex_clean = hex_code.lstrip("#")
        r = int(hex_clean[0:2], 16)
        g = int(hex_clean[2:4], 16)
        b = int(hex_clean[4:6], 16)

        return (color_name, hex_code.upper(), r, g, b)


NODE_CLASS_MAPPINGS = {
    "ColorPicker": ColorPicker
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ColorPicker": "👾 Color Picker 🎨"
}

