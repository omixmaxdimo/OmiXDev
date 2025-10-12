# 👾 OmiXDev — Custom Nodes Package for ComfyUI
# This package provides advanced AI-related nodes (Chat, Tools, etc.)

from .Chat import (
    NODE_CLASS_MAPPINGS as CHAT_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as CHAT_NODE_DISPLAY_NAME_MAPPINGS,
)

# Register all nodes from Chat submodule
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

NODE_CLASS_MAPPINGS.update(CHAT_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CHAT_NODE_DISPLAY_NAME_MAPPINGS)


