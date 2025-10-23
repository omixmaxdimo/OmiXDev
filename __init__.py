# 👾 OmiXDev — Custom Nodes Package for ComfyUI
# This package provides advanced AI-related nodes (Chat, Tools, etc.)
# OmiXDev/ root __init__.py
# Registers all submodules for ComfyUI

# Import Chat nodes
from .Chat import (
    NODE_CLASS_MAPPINGS as CHAT_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as CHAT_NODE_DISPLAY_NAME_MAPPINGS,
)

# Import Math nodes
from .Math import (
    NODE_CLASS_MAPPINGS as MATH_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as MATH_NODE_DISPLAY_NAME_MAPPINGS,
)

# Register all nodes from submodules
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Add Chat nodes
NODE_CLASS_MAPPINGS.update(CHAT_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CHAT_NODE_DISPLAY_NAME_MAPPINGS)

# Add Math nodes
NODE_CLASS_MAPPINGS.update(MATH_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MATH_NODE_DISPLAY_NAME_MAPPINGS)


