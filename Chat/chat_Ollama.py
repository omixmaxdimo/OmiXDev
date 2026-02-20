import ollama

class OmixChatOllama:
    chat_history = []

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_message": ("STRING", {"default": "Hello!", "multiline": True}),
                "model": ("STRING", {"default": "Qwen3:4b"}),
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

    def chat(self, user_message, model, reset=False, send_history=True):
        if reset:
            self.chat_history.clear()
            return ("[History cleared]", "")

        if not user_message.strip():
            return ("❌ Enter valid message", "\n".join(self.chat_history))

        try:
            messages = []

            if send_history and self.chat_history:
                for line in self.chat_history:
                    if line.startswith("👤"):
                        messages.append({"role": "user", "content": line[2:].strip()})
                    elif line.startswith("🤖"):
                        messages.append({"role": "assistant", "content": line[2:].strip()})

            messages.append({"role": "user", "content": user_message})

            response = ollama.chat(
                model=model,
                messages=messages
            )

            reply = response["message"]["content"].strip()

        except Exception as e:
            reply = f"❌ Error: {e}"

        self.chat_history.append(f"👤 {user_message}")
        self.chat_history.append(f"🤖 {reply}")

        return (reply, "\n".join(self.chat_history))


NODE_CLASS_MAPPINGS = {"OmixChatOllama": OmixChatOllama}
NODE_DISPLAY_NAME_MAPPINGS = {"OmixChatOllama":"👾 Ollama Local Chat 🦙"}