# 👾 OmiXDev/Math Math Nodes for ComfyUI
# Includes all custom Math nodes

# Import Resulation_Presets node
from .Resulation_Presets import NODE_CLASS_MAPPINGS as RES_PRESETS_NODES, NODE_DISPLAY_NAME_MAPPINGS as RES_PRESETS_DISPLAY

# Initialize unified dictionaries for ComfyUI
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Add Resulation_Presets nodes
NODE_CLASS_MAPPINGS.update(RES_PRESETS_NODES)
NODE_DISPLAY_NAME_MAPPINGS.update(RES_PRESETS_DISPLAY)
