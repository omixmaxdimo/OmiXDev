# =========================================================
# Node: CardGame Random Deal
# Description: Dealing any kind of cardgames max for 6 person poker , black jack , sentence
# Author: OmiX.IR
# Category: Tools
# =========================================================
import os
import torch
import random
import winsound
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class Card:

    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank

    def __str__(self):

        return self.rank + self.suit

class Player:

    def __init__(self, name, position,stack):

        self.name = name
        self.position = position
        self.stack = stack
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(f"Hand {self.name}: { [str(card) for card in self.hand]}") # تغییر این خط


class DealGame:

    def __init__(self):
        #self.deck=[]

        self.deck = self.create_deck(0) # 0 : joker in preset
        self.players = []
        self.table_hand = []
        self.bet_flop = 0
        self.bet_turn = 0
        self.bet_river = 0
        self.table_balance = 0

    def create_deck(self,joker_num):

        deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                deck.append(Card(suit, rank))
        print(">>> Total card before joker:",len(deck))
        if joker_num>0:
            print("!!!! PRESET Adding Jokers",joker_num)
            for i in range(joker_num):
                deck.append(Card(str(i+1),"Joker"))
                print("JOKER ",i)
        random.shuffle(deck)
        print("Total card after jokers:", len(deck))
        return deck

    def add_player(self, player):

        self.players.append(player)

    def deal(self, n):
        for _ in range(n):
            for player in self.players:
                if len(self.deck)>0:
                    card = self.deck.pop()
                    player.add_card(card)
                else:
                    print("Deck is Empty")
                    return

    def deal_table_hand(self, n):

        for _ in range(n):
            if self.deck:
                card = self.deck.pop()
                self.table_hand.append(card)
            else:
                print("Deck Is Empty")
                return
        print("Table Hand : ", [str(card) for card in self.table_hand])

class DealRandom:
    """"
    👾 OmiX Deal random cards in ComfyUI
    Manages poker logic, renders cards
    """


    def __init__(self):
        self.jk = 0
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "SEED": ("INT", {"default": 2005520646546}),
                "Game_Name": ("STRING", {"default": "Holdem Poker"}),
                "Deal_Num": ("INT", {"default":2}),
                "Deal_table_Num": ("INT", {"default": 5}),
                "Deal_Jokers_Num": ("INT", {"default": 0}),
                "Suit_colors": (
                    [
                        "2",
                        "4",
                    ],
                    {"default": "4"}
                ),
                "Sort_Hand_method": (
                    [
                        "rank",
                        "suit",
                    ],
                    {"default": "suit"}
                ),
                "Player_1_name": ("STRING", {"default": "OmiX"}),
                "Player_1_Sited": ("BOOLEAN", {"default": True}),
                "Player_2_name": ("STRING", {"default": "MahPsy"}),
                "Player_2_Sited": ("BOOLEAN", {"default": True}),
                "Player_3_name": ("STRING", {"default": "PC 1"}),
                "Player_3_Sited": ("BOOLEAN", {"default": True}),
                "Player_4_name": ("STRING", {"default": "PC 2"}),
                "Player_4_Sited": ("BOOLEAN", {"default": False}),
                "Player_5_name": ("STRING", {"default": "PC 3"}),
                "Player_5_Sited": ("BOOLEAN", {"default": False}),
                "Player_6_name": ("STRING", {"default": "PC 4"}),
                "Player_6_Sited": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("image", "Player hand 1", "Player hand 2", "Player hand 3", "Player hand 4", "Player hand 5", "Player hand 6", "Table hand","Remain Deck")

    FUNCTION = "Deal"
    CATEGORY = "👾 OmiXDev/Games"

    def Deal(self,SEED,Game_Name,Suit_colors,Sort_Hand_method,Deal_Num,Deal_table_Num,Deal_Jokers_Num,Player_1_name,Player_2_name,Player_3_name,Player_4_name,Player_5_name,Player_6_name,Player_1_Sited,Player_2_Sited,Player_3_Sited,Player_4_Sited,Player_5_Sited,Player_6_Sited):
        random.seed = SEED

        game = DealGame()
        # Define Players
        player1 = Player(Player_1_name, 1, 300)
        player2 = Player(Player_2_name, 2, 200)
        player3 = Player(Player_3_name, 3, 332)
        player4 = Player(Player_4_name, 4, 300)
        player5 = Player(Player_5_name, 5, 200)
        player6 = Player(Player_6_name, 6, 332)
        #player_fold_cards = Player("fold card", 0, 0)

        # Add Players to Game
        if Player_1_Sited : game.add_player(player1)
        if Player_2_Sited : game.add_player(player2)
        if Player_3_Sited : game.add_player(player3)
        if Player_4_Sited : game.add_player(player4)
        if Player_5_Sited : game.add_player(player5)
        if Player_6_Sited : game.add_player(player6)

        player_names = [Player_1_name, Player_2_name, Player_3_name, Player_4_name, Player_5_name, Player_6_name]
        player_hands = [player1.hand,player2.hand,player3.hand,player4.hand,player5.hand,player6.hand]
        table_hand = [] #tested
        for card in game.table_hand:
            table_hand.append(str(card))

        def render(player_names,suit_n,player_hands,table_hand,Game_Name):

            green_background = Image.new("RGB", (800, 600), (0, 64, 0))
            draw = ImageDraw.Draw(green_background)

            try:
                card_image = Image.open("card_logo.png")
            except FileNotFoundError:
                print("Error: card_logo.png not found.")
                card_image = None  # Assign None to card_image in case of error
            except Exception as e:
                print(f"An error occurred: {e}")
                card_image = None  # Assign None to card_image in case of error

            try:
                font = ImageFont.truetype("arial.ttf", 30)  # فونت مناسب را انتخاب کنید
            except IOError:
                font = ImageFont.load_default()
            try:
                font1 = ImageFont.truetype("arial.ttf", 15)  # فونت مناسب را انتخاب کنید
            except IOError:
                font1 = ImageFont.load_default()

            try:
                font2 = ImageFont.truetype("Webdings.ttf", 40)  # فونت مناسب را انتخاب کنید
            except IOError:
                font2 = ImageFont.load_default()


            draw.rectangle([(0,230),(800,350)],fill="#1c3f35")
            draw.text((10, 240), f"{Game_Name}", fill="white",font=font)
            card_width, card_height = 75, 75
            x0, y0 = 250, 240
            y_ofset = 5
            x_ofset = 35
            radius = 8
            jj=0
            for cards in ex_table_hand:
                jj+=1
                draw.rounded_rectangle([(x0, y0), (x0 + card_width, y0 + card_height)], fill="white", outline="black",
                                           width=1, radius=radius)
                draw.text((x0 + 25, y0 + 30), f"w", fill="black", font=font2)
                if "♠" in cards: draw.text((x0+5,y0+5),f"{cards}",fill="black",font=font1)
                elif "♥" in cards: draw.text((x0+5,y0+5),f"{cards}",fill="red",font=font1)
                elif "♣" in cards and suit_n=="2" : draw.text((x0+5,y0+5),f"{cards}",fill="black",font=font1)
                elif "♣" in cards and suit_n == "4": draw.text((x0 + 5, y0 + 5), f"{cards}", fill="green", font=font1)
                elif "Jo" in str(cards): draw.text((x0 + 5, y0 + 5), f"{cards}", fill="black", font=font1)
                elif "♦" in cards and suit_n=="2": draw.text((x0+5,y0+5),f"{cards}",fill="red",font=font1)
                elif "♦" in cards and suit_n=="4": draw.text((x0+5,y0+5),f"{cards}",fill="blue",font=font1)
                #green_background.paste(card_image,[(x0+15,y0+15),(x0+65,y0+65)])
                if jj % 3 == 0 :
                    x0, y0 = x0 + x_ofset + 20, 240
                else:
                    x0, y0 = x0 + x_ofset, y0 + y_ofset

            card_width,card_height=75,100
            x0,y0=10,30
            y_ofset = 20
            x_ofset = 15
            for i in range(len(player_hands)):
                j=0
                if i==1 : x0,y0=300,30
                if i==2 : x0,y0=550,30
                if i==3 : x0,y0=10,380
                if i==4 : x0,y0=300,380
                if i==5 : x0, y0 = 550, 380
                draw.text((x0, y0-20), f"{player_names[i]} Hand", fill="white", font=font1)
                for cards in player_hands[i]:
                    j+=1
                    draw.rounded_rectangle([(x0, y0), (x0 + card_width, y0 + card_height)], fill="white", outline="black",
                                           width=1, radius=radius)

                    draw.text((x0 + 25, y0 + 30), f"®", fill="black", font=font2)

                    if "♥" in str(cards) : draw.text((x0+5,y0+5),f"{cards}",fill="red",font=font1)
                    elif "♣" in str(cards) and suit_n=="2"  :draw.text((x0+5,y0+5),f"{cards}",fill="black",font=font1)
                    elif "♣" in str(cards) and suit_n=="4":draw.text((x0+5,y0+5),f"{cards}",fill="green",font=font1)
                    elif "♠" in str(cards): draw.text((x0 + 5, y0 + 5), f"{cards}", fill="black", font=font1)
                    elif "Jo" in str(cards): draw.text((x0 + 5, y0 + 5), f"{cards}", fill="black", font=font1)
                    elif "♦" in str(cards) and suit_n=="2":draw.text((x0+5,y0+5),f"{cards}",fill="red",font=font1)
                    elif "♦" in str(cards) and suit_n=="4": draw.text((x0+5,y0+5),f"{cards}",fill="blue",font=font1)
                    #green_background.paste(card_image, (x0 + 35, y0 + 35))

                    if j%5==0 and i<3 :x0,y0=x0+x_ofset+20,35
                    elif j%5==0 and i>=3 : x0,y0=x0+x_ofset+10,385
                    else:x0,y0 = x0+x_ofset , y0+y_ofset

            np_image = np.array(green_background).astype(np.float32) / 255.0
            tensor_image = torch.from_numpy(np_image).unsqueeze(0)
            return tensor_image


        """
        player_sited_flags = [Player_1_Sited, Player_2_Sited, Player_3_Sited, Player_4_Sited, Player_5_Sited,Player_6_Sited]
        for i in range(len(player_names)):
            if player_sited_flags[i]:
                player = Player(player_names[i], i + 1, 300)  # Assuming player number is i + 1
                game.add_player(player)
        """
        # Deal to on sited players

        game.create_deck(Deal_Jokers_Num)
        print("jokers in desk :",Deal_Jokers_Num)

        if Deal_Jokers_Num>0:
            print("!!!! Adding Jokers",Deal_Jokers_Num)
            for i in range(Deal_Jokers_Num):
                game.deck.append(Card(str(i+1),"Joker"))
                print("JOKER ",i+1)
        random.shuffle(game.deck)
        print("Total Cards in deck :",len(game.deck))
        game.deal(Deal_Num)
        print("Deal Card Numebers to pleayers :", Deal_Num)
        # Deal to table
        if Deal_table_Num>0 : game.deal_table_hand(Deal_table_Num)

        # Show Players Hands in consul
        player1.show_hand()
        player2.show_hand()
        player3.show_hand()
        player4.show_hand()
        player5.show_hand()
        player6.show_hand()
        print(table_hand)


        def replace_unicode_suit(card_string):
            """replace char code to show in ComfyUI."""
            card_string = card_string.replace("♠", " Spade")
            card_string = card_string.replace("♥", " Heart")
            card_string = card_string.replace("♦", " Dimond")
            card_string = card_string.replace("♣", " Club")
            return card_string

        def sort_hand(hand, Sort_Hand_method):
            """مرتب سازی دست کارت ها بر اساس خال یا رتبه."""
            if Sort_Hand_method == "suit":
                hand.sort(key=lambda card: card.suit)  # مرتب سازی بر اساس خال
            elif Sort_Hand_method == "rank":
                hand.sort(key=lambda card: card.rank)  # مرتب سازی بر اساس رتبه
            else:
                print("Invalid sorting state. Use 'suit' or 'rank'.")
            return hand


        player1.hand=sort_hand(player1.hand, Sort_Hand_method)
        player2.hand=sort_hand(player2.hand, Sort_Hand_method)
        player3.hand=sort_hand(player3.hand, Sort_Hand_method)
        player4.hand=sort_hand(player4.hand, Sort_Hand_method)
        player5.hand=sort_hand(player5.hand, Sort_Hand_method)
        player6.hand=sort_hand(player6.hand, Sort_Hand_method)
        game.table_hand=sort_hand(game.table_hand,Sort_Hand_method)

        #ex_pl1_hand = str(player1.name) + " hands : " + [f"{card}" for card in player1.hand]
        ex_pl1_hand = str(player1.name) + " hands : "+str([replace_unicode_suit(str(card)) for card in player1.hand])
        ex_pl2_hand = str(player2.name) + " hands : "+str([replace_unicode_suit(str(card)) for card in player2.hand])
        ex_pl3_hand = str(player3.name) + " hands : "+str([replace_unicode_suit(str(card)) for card in player3.hand])
        ex_pl4_hand = str(player4.name) + " hands : "+str([replace_unicode_suit(str(card)) for card in player4.hand])
        ex_pl5_hand = str(player5.name) + " hands : "+str([replace_unicode_suit(str(card)) for card in player5.hand])
        ex_pl6_hand = str(player6.name) + " hands : "+str([replace_unicode_suit(str(card)) for card in player6.hand])

        ex_table_hand1 =str([replace_unicode_suit(str(card)) for card in game.table_hand])
        ex_table_hand =[str(card) for card in game.table_hand]

        ex_image = render(player_names,Suit_colors, player_hands, table_hand,Game_Name)
        ex_deck = [replace_unicode_suit(str(card)) for card in game.deck]

        winsound.Beep(1000, 500)
        return (ex_image,ex_pl1_hand,ex_pl2_hand,ex_pl3_hand,ex_pl4_hand,ex_pl5_hand,ex_pl6_hand,ex_table_hand1,ex_deck)

NODE_CLASS_MAPPINGS = {"DealRandom": DealRandom}
NODE_DISPLAY_NAME_MAPPINGS = {"DealRandom": "👾 Deal Random Cards 🃏🃏"}
