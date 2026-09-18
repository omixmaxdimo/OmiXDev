# =========================================================
# Tools/Cbeep.py
# ComfyUI OmixDev Custom node
# Node: CompletionBeepPro (Universal Type Fix)
# =========================================================
import sys
import winsound


class CompletionBeepPro:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # استفاده از ستاره برای ورودی
                "trigger": ("*",),
                "sound_type": (
                    ["Default", "Hand", "Question", "Exclamation", "Asterisk"],
                    {"default": "Default"}
                ),
            }
        }

    # جادوی اصلی: ستاره به عنوان خروجی که خودش رو با نود بعدی وفق می‌ده
    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("output",)
    FUNCTION = "execute"
    CATEGORY = "👾 OmiXDev/Tools"

    # این تابع باعث میشه ComfyUI بیخیال چک کردن سخت‌گیرانه تایپ بشه
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def execute(self, trigger, sound_type):
        winsound.MessageBeep()
        print("************* triger ************** ")
        try:
            if sys.platform.startswith("win"):
                sound_map = {
                    "Default": -1,
                    "Hand": 0x00000010,
                    "Question": 0x00000020,
                    "Exclamation": 0x00000030,
                    "Asterisk": 0x00000040
                }
                winsound.MessageBeep(sound_map.get(sound_type, -1))
            else:
                print("\a", end="", flush=True)

            print(f"[CompletionBeepPro] Sound Triggered: {sound_type}")
        except Exception as e:
            print(f"[CompletionBeepPro] Sound error: {e}")

        # بازگرداندن داده ورودی بدون هیچ تغییر در ساختار
        return (trigger,)


NODE_CLASS_MAPPINGS = {"CompletionBeepPro": CompletionBeepPro}
NODE_DISPLAY_NAME_MAPPINGS = {"CompletionBeepPro": "👾 Completion Beep 🔊"}