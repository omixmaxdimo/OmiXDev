from openai import OpenAI

class OmixChatPro:
    chat_history = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"default": "", "multiline": False}),
                "user_message": ("STRING", {"default": "Hello!", "multiline": True}),
                "model": (["gpt-4.1-mini","gpt-4.1","gpt-4o-mini"], {"default":"gpt-4.1-mini"}),
            },
            "optional": {
                "reset": ("BOOLEAN", {"default": False}),
                "send_history": ("BOOLEAN", {"default": True})
            }
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("last_reply","chat_history")
    FUNCTION = "chat"
    CATEGORY = "👾 OmiXDev/Chat"

    def chat(self, api_key, user_message, model, reset=False, send_history=True):
        if reset:
            self.chat_history.clear()
            return ("[History cleared]", "")
        if not user_message.strip() or not api_key:
            return ("❌ Enter valid message and API key", "\n".join(self.chat_history))
        try:
            client = OpenAI(api_key=api_key)
            messages = [{"role":"user","content":user_message}]
            resp = client.chat.completions.create(model=model,messages=messages)
            reply = resp.choices[0].message.content.strip()
        except Exception as e:
            reply = f"❌ Error: {e}"

        self.chat_history.append(f"👤 {user_message}")
        self.chat_history.append(f"🤖 {reply}")
        return (reply, "\n".join(self.chat_history))

NODE_CLASS_MAPPINGS = {"OmixChatPro": OmixChatPro}
NODE_DISPLAY_NAME_MAPPINGS = {"OmixChatPro":"👾 OpenAI Chat API 🔑"}
