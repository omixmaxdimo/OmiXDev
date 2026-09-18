# 👾 OmiXDev root __init__.py
# Registers all submodules for ComfyUI

# Import Chat nodes
print("""
   ██████╗ ███╗   ███╗██╗██╗  ██╗██████╗ ███████╗██╗   ██╗
  ██╔═══██╗████╗ ████║██║╚██╗██╔╝██╔══██╗██╔════╝██║   ██║
  ██║   ██║██╔████╔██║██║ ╚███╔╝ ██║  ██║█████╗  ██║   ██║
  ██║   ██║██║╚██╔╝██║██║ ██╔██╗ ██║  ██║██╔══╝  ╚██╗ ██╔╝
  ╚██████╔╝██║ ╚═╝ ██║██║██╔╝ ██╗██████╔╝███████╗ ╚████╔╝ 
   ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝  ╚═══╝  
               ╔══════════════════════════════╗
               ║        ⚡  OMIXDEV  ⚡         ║
               ║   AI • 3D • VFX • COMFYUI    ║
               ╚══════════════════════════════╝
""")
from .Chat import (
    NODE_CLASS_MAPPINGS as CHAT_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as CHAT_NODE_DISPLAY_NAME_MAPPINGS,
)

# Import Math nodes
from .Tools import (
    NODE_CLASS_MAPPINGS as MATH_NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS as MATH_NODE_DISPLAY_NAME_MAPPINGS,
)

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Add Chat nodes
NODE_CLASS_MAPPINGS.update(CHAT_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(CHAT_NODE_DISPLAY_NAME_MAPPINGS)

# Add Tools nodes
NODE_CLASS_MAPPINGS.update(MATH_NODE_CLASS_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(MATH_NODE_DISPLAY_NAME_MAPPINGS)

# Import Games nodes safely
try:
    from .Games import (
        NODE_CLASS_MAPPINGS as GAMES_NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS as GAMES_NODE_DISPLAY_NAME_MAPPINGS,
    )

    NODE_CLASS_MAPPINGS.update(GAMES_NODE_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(GAMES_NODE_DISPLAY_NAME_MAPPINGS)

except Exception as e:
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("OmiXDev Games module failed to load:", e)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    