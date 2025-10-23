# =========================================================
# Node: ResolutionPresets
# Description: Select common resolution presets from dropdown
# Author: Omid Ameri & ChatGPT
# Category: Math
# =========================================================

class ResolutionPresets:
    """
    This node lets the user select common resolution presets from a dropdown.
    Outputs:
        width  - integer width of resolution
        height - integer height of resolution
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Dropdown menu for preset selection
                "preset": (
                    [
                        "SD - 4:3",
                        "HD - 16:9",
                        "HD - 9:16",
                        "Half HD - 16:9",
                        "Half HD - 9:16",
                        "Full HD - 16:9",
                        "2K - 16:9",
                        "4K - 16:9",
                        "Square 512x512",
                        "Square 1024x1024",
                    ],
                    {"default": "Half HD - 16:9"}
                ),
            }
        }

    # Two integer outputs for width and height
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "get_resolution"
    CATEGORY = "👾 OmiXDev/Math"

    def get_resolution(self, preset):
        """
        Returns width and height based on the selected preset.
        """
        presets = {
            "SD - 4:3": (720, 540),
            "HD - 16:9": (1280, 720),
            "HD - 9:16": (720, 1280),
            "Half HD - 16:9": (640, 360),
            "Half HD - 9:16": (360, 640),
            "Full HD - 16:9": (1920, 1080),
            "2K - 16:9": (2560, 1440),
            "4K - 16:9": (3840, 2160),
            "Square 512x512": (512, 512),
            "Square 1024x1024": (1024, 1024),
        }

        return presets[preset]

# Register node in ComfyUI
NODE_CLASS_MAPPINGS = {"ResolutionPresets": ResolutionPresets}
NODE_DISPLAY_NAME_MAPPINGS = {"ResolutionPresets": "👾 Resolution Presets"}
