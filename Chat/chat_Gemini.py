import google.generativeai as genai

class OmixGeminiPro:
    """
    ComfyUI Node for chatting with Google Gemini models (Gemini 1.5 Pro, 1.5 Flash, etc.)
    Supports chat history, model selection, and reset control.
    """

    chat_history = []  # Static chat history for persistence

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"multiline": False, "default": "🔑 AIzaSy..."}),
                "user_message": ("STRING", {"multiline": True, "default": "Hello Gemini 👋"}),
                "model": (
                    ["gemini-2.5-flash-lite", "gemini-exp-1206"],
                    {"default": "gemini-2.5-flash-lite"},
                ),
            },
            "optional": {
                "reset": ("BOOLEAN", {"default": False}),
                "send_history": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("last_reply", "chat_history")
    FUNCTION = "chat"
    CATEGORY = "👾 OmiXDev/Chat"

    def chat(self, api_key, user_message, model, reset=False, send_history=True):
        """
        Chat with Gemini API using GenerativeModel interface.
        Maintains a conversation if send_history=True.
        """
        # --- 1. Reset history if needed ---
        if reset:
            self.chat_history.clear()
            return ("🧹 Chat history cleared.", "")

        # --- 2. Validate API key ---
        if not api_key or not api_key.startswith("AI"):
            reply = "❌ Invalid or missing Gemini API Key."
            return reply, "\n".join(self.chat_history)

        # --- 3. Skip if message empty ---
        if not user_message.strip():
            return ("", "\n".join(self.chat_history))

        try:
            # --- 4. Configure Gemini ---
            genai.configure(api_key=api_key)
            model_instance = genai.GenerativeModel(model)

            # --- 5. Prepare chat session ---
            if send_history and self.chat_history:
                history = []
                for line in self.chat_history:
                    if line.startswith("👤"):
                        history.append({"role": "user", "parts": [line[2:].strip()]})
                    elif line.startswith("🤖"):
                        history.append({"role": "model", "parts": [line[2:].strip()]})
                chat = model_instance.start_chat(history=history)
            else:
                chat = model_instance.start_chat(history=[])

            # --- 6. Send message ---
            response = chat.send_message(user_message)
            reply = response.text.strip()

        except Exception as e:
            reply = f"❌ Error: {e}"

        # --- 7. Update history ---
        self.chat_history.append(f"👤 {user_message}")
        self.chat_history.append(f"🤖 {reply}")

        return reply, "\n".join(self.chat_history)


# ✅ Register node
NODE_CLASS_MAPPINGS = {"OmixGeminiPro": OmixGeminiPro}
NODE_DISPLAY_NAME_MAPPINGS = {"OmixGeminiPro": "👾 Gemini Chat API 🔑"}
