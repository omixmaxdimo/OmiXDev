from openai import OpenAI

class OmixChatPro:
    """
    Node برای چت با OpenAI (کلید API به عنوان ورودی + تاریخچه + انتخاب مدل)
    """

    chat_history = []  # ذخیره تاریخچه برای این نود

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"multiline": False, "default": "🔑 sk-proj-xxxxxxxxx"}),
                "user_message": ("STRING", {"multiline": True, "default": "شروع جت Start Chat "}),
                "model": (["gpt-4.1-mini", "gpt-4.1", "gpt-4o-mini", "gpt-4o"], {"default": "gpt-4.1-mini"}),
            },
            "optional": {
                "reset": ("BOOLEAN", {"default": False}),
                "send_history": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("last_reply", "chat_history")
    FUNCTION = "chat"
    CATEGORY = "👾 OmiX/Chat"

    def chat(self, api_key, user_message, model, reset=False, send_history=True):
        if reset:
            self.chat_history.clear()
            return ("[History cleared]", "")

        if not user_message.strip():
            return ("", "\n".join(self.chat_history))

        if not api_key or not api_key.startswith("sk-"):
            reply = "❌ لطفاً یک API Key معتبر وارد کنید."
            return reply, "\n".join(self.chat_history)

        try:
            client = OpenAI(api_key=api_key)

            # ساخت پیام‌ها
            if send_history and self.chat_history:
                messages = [{"role": "system", "content": "تو یک دستیار مفید هستی و فارسی جواب می‌دهی."}]
                for line in self.chat_history:
                    if line.startswith("👤"):
                        messages.append({"role": "user", "content": line[2:].strip()})
                    elif line.startswith("🤖"):
                        messages.append({"role": "assistant", "content": line[2:].strip()})
                messages.append({"role": "user", "content": user_message})
            else:
                messages = [
                    {"role": "system", "content": "تو یک دستیار مفید هستی و فارسی جواب می‌دهی."},
                    {"role": "user", "content": user_message},
                ]

            resp = client.chat.completions.create(
                model=model,
                messages=messages,
            )
            reply = resp.choices[0].message.content.strip()
        except Exception as e:
            reply = f"❌ خطا: {e}"

        # اضافه به تاریخچه
        self.chat_history.append(f"👤 {user_message}")
        self.chat_history.append(f"🤖 {reply}")

        return reply, "\n".join(self.chat_history)


NODE_CLASS_MAPPINGS = {
    "OmixChatPro": OmixChatPro
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OmixChatPro": "👾 OpenAI Chat OmiXDev"
}
