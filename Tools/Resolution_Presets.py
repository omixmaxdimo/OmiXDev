# =========================================================
# ComfyUI Costume Node 
# Node: ResolutionPresets
# Description: Select common resolution presets from dropdown
# Author: OmiXDev
# Category: Tools
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
                "preset": (
                    [
                        "720 x 540 SD - 4:3",
                        "1280x720 HD - 16:9",
                        "720x1280 HD - 9:16",
                        "640x360 Half HD - 16:9",
                        "360x640 Half HD - 9:16",
                        "1920x1080 Full HD - 16:9",
                        "250x1440 2K - 16:9",
                        "3840x2160 4K - 16:9",
                        "512x512 Square",
                        "1024x1024 Square",
                    ],
                    {"default": "640x360 Half HD - 16:9"}
                ),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "get_resolution"
    CATEGORY = "👾 OmiXDev/Tools"

    def get_resolution(self, preset):

        presets = {
            "720x540 SD - 4:3": (720, 540),
            "1280x720 HD - 16:9": (1280, 720),
            "720x1200 HD - 9:16": (720, 1280),
            "640x360 Half HD - 16:9": (640, 360),
            "360x640 Half HD - 9:16": (360, 640),
            "1920x1080 Full HD - 16:9": (1920, 1080),
            "2560x1440 2K - 16:9": (2560, 1440),
            "3840x2160 4K - 16:9": (3840, 2160),
            "512x512 Square": (512, 512),
            "1024x1024 Square": (1024, 1024),
        }

        return presets[preset]


# Register node (needed because Tools/__init__.py imports mappings)
NODE_CLASS_MAPPINGS = {
    "ResolutionPresets": ResolutionPresets
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionPresets": "👾 Resolution Presets 🖼"
}