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

# === How to add more Math nodes in the future ===
# 1. Create your new node file in this folder, e.g., MyNewMathNode.py
# 2. Import it like this:
#     from .MyNewMathNode import NODE_CLASS_MAPPINGS as NEW_NODE, NODE_DISPLAY_NAME_MAPPINGS as NEW_DISPLAY
# 3. Update the dictionaries:
#     NODE_CLASS_MAPPINGS.update(NEW_NODE)
#     NODE_DISPLAY_NAME_MAPPINGS.update(NEW_DISPLAY)
# 4. Done! ComfyUI will now see your new Math node automatically.

# This structure keeps all Math nodes organized and easy to extend
