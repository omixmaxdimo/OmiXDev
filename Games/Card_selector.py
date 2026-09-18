# =========================================================
# Node: CardGame Presets
# Description: Select color from dropdown or enter HEX manually (Strict HSB Hidden)
# Author: OmiX.IR
# Category: Tools
# =========================================================

class OmiX_Cardselector:
    """
    Select a cardgame from preset list
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "suit_selection": (
                    [
                        "♠ Spade",
                        "♣ Club",
                        "♥ Heart",
                        "♦ Dimond",
                    ],
                    {"default": "♠ Spade"}
                ),
                "rank_selection": (
                    [
                        "Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2",
                    ],
                    {"default": "Ace"}
                ),
            }
        }

    RETURN_TYPES = ("STRING","STRING","INT")
    RETURN_NAMES = ("Str Card","Str Suit","Int Rank")

    FUNCTION = "execute_card_selection"
    CATEGORY = "👾 OmiXDev/Games"

    def execute_card_selection(self, suit_selection, rank_selection):

        preset_map = {
            "♠ Spade": "♠",
            "♣ Club": "♣",
            "♥ Heart": "♥",
            "♦ Dimond": "♦",
          }
        rank_map = {
            "Joker": 15,
            "Ace": 14,
            "King": 13,
            "Queen": 12,
            "Jack":11,
            "10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,
           }
        card_str = str(rank_selection)+" "+str(preset_map[suit_selection])
        rank_int = int(rank_map[rank_selection])
        print(card_str)
        return (card_str,suit_selection,rank_int)


NODE_CLASS_MAPPINGS = {
    "OmiX_Cardselector": OmiX_Cardselector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OmiX_Cardselector": "👾 Card Selector 🃏"
}