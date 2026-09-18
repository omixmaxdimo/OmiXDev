# Games/Comfy_Chess.py
# 👾 OmiXDev/Games  for ComfyUI
import os
import torch
import numpy as np
import chess
from PIL import Image, ImageDraw, ImageFont
import winsound


class ChessBoardNode:
    """"
    👾 OmiX Chess Board Renderer for ComfyUI
    Manages chess logic, renders board, and supports FEN Load/Save.
    """

    board = chess.Board()
    # ذخیره آخرین FEN لود شده برای جلوگیری از تداخل
    last_loaded_fen = ""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "move": ("STRING", {"multiline": False, "default": ""}),
                "fen_input": ("STRING", {"multiline": True, "default": chess.STARTING_FEN}),
                "reset": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("IMAGE", "CURRENT_FEN")
    FUNCTION = "render"
    CATEGORY = "👾 OmiXDev/Games"

    PIECE_CHARS = {
        chess.PAWN: "♟", chess.ROOK: "♜", chess.KNIGHT: "♞",
        chess.BISHOP: "♝", chess.QUEEN: "♛", chess.KING: "♚"
    }

    def render(self, move, fen_input, reset):
        winsound.Beep(1000, 500)  # صدای تیزتر

        # ۱. مدیریت ریست
        if reset:
            self.board.reset()
            self.last_loaded_fen = self.board.fen()

        # ۲. مدیریت لود کردن FEN (اگر کاربر دستی یک FEN جدید چسبانده باشد)
        fen_input = fen_input.strip()
        if fen_input and fen_input != self.last_loaded_fen and fen_input != self.board.fen():
            try:
                self.board = chess.Board(fen_input)
                self.last_loaded_fen = fen_input
            except Exception as e:
                winsound.MessageBeep()
                print(f"OmiX Error: Invalid FEN! {e}")

        # ۳. اعمال حرکت
        move = move.strip()
        if move:
            try:
                try:
                    self.board.push_san(move)
                except:
                    self.board.push_uci(move)
            except Exception as e:
                winsound.MessageBeep()
                print(f"OmiX Error: Movement '{move}' is invalid! {e}")

        # --- تنظیمات رندر (همان تنظیمات عالی خودت) ---
        square_size = 80
        padding = 30
        board_size = 8 * square_size
        total_size = board_size + (padding * 2)

        image = Image.new("RGB", (total_size, total_size), "#2b2b2b")
        draw = ImageDraw.Draw(image)

        try:
            coord_font = ImageFont.truetype("C:/Windows/Fonts/tahoma.ttf", 20)
            font = ImageFont.truetype("C:/Windows/Fonts/seguisym.ttf", int(square_size * 0.7))
        except:
            coord_font = ImageFont.load_default()
            font = ImageFont.load_default()

        # رسم مختصات
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i, letter in enumerate(letters):
            x_pos = padding + (i * square_size) + (square_size // 2) - 5
            draw.text((x_pos, total_size - padding + 5), letter, fill="white", font=coord_font)
            draw.text((x_pos, 5), letter, fill="white", font=coord_font)

        for i in range(8):
            number = str(8 - i)
            y_pos = padding + (i * square_size) + (square_size // 2) - 10
            draw.text((10, y_pos), number, fill="white", font=coord_font)
            draw.text((total_size - padding + 10, y_pos), number, fill="white", font=coord_font)

        # رسم صفحه و مهره‌ها
        colors = ["#F0D9B5", "#B58863"]
        for r in range(8):
            for c in range(8):
                x0, y0 = padding + (c * square_size), padding + (r * square_size)
                x1, y1 = x0 + square_size, y0 + square_size
                draw.rectangle([x0, y0, x1, y1], fill=colors[(r + c) % 2])

                square = chess.square(c, 7 - r)
                piece = self.board.piece_at(square)
                if piece:
                    char = self.PIECE_CHARS.get(piece.piece_type, "?")
                    # تنظیم رنگ مهره‌های سفید و سیاه بر اساس کد خودت
                    text_color = "white" if piece.color == chess.WHITE else "#666666"

                    bbox = draw.textbbox((0, 0), char, font=font)
                    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
                    piece_x = x0 + (square_size - w) / 2
                    piece_y = y0 + (square_size - h) / 2 - (h * 0.1)

                    draw.text((piece_x, piece_y), char, fill=text_color, font=font, stroke_width=2, stroke_fill="black")

        # خروجی نهایی
        np_image = np.array(image).astype(np.float32) / 255.0
        tensor_image = torch.from_numpy(np_image).unsqueeze(0)

        return (tensor_image, self.board.fen())


# ثبت نود
NODE_CLASS_MAPPINGS = {"ChessBoardNode": ChessBoardNode}
NODE_DISPLAY_NAME_MAPPINGS = {"ChessBoardNode": "👾 OmiX Chess Board ♟"}