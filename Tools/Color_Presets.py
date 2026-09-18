# =========================================================
# Node: Color Presets
# Description: Select color from dropdown or enter HEX manually (Strict HSB Hidden)
# Author: OmiX.IR
# Category: Tools
# =========================================================

class OmiX_HexSelector:
    """
    Select a color from preset list or enter HEX manually.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset_selection": (
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
                    ],
                    {"default": "⚪ white"}
                ),
                "manual_hex_code": (
                    "STRING",
                    {"default": "", "multiline": False}
                ),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("name_out", "code_out")

    FUNCTION = "execute_selection"
    CATEGORY = "👾 OmiXDev/Tools"

    def execute_selection(self, preset_selection, manual_hex_code):

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
        }

        clean_input = manual_hex_code.strip()

        if clean_input != "":
            hex_code = clean_input
            color_name = "custom"
        else:
            color_name, hex_code = preset_map[preset_selection]

        if not hex_code.startswith("#"):
            hex_code = "#" + hex_code

        return (color_name, hex_code.upper())


NODE_CLASS_MAPPINGS = {
    "OmiX_HexSelector": OmiX_HexSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OmiX_HexSelector": "👾 Color Presets 🎨"
}