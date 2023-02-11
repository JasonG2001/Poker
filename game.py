from typing import Dict, Set
import random

class Game:

    def __init__(self) -> None:

        self.lowest_num: int = 2
        self.highest_num: int = 14
        self.SUITS: Set[str] = set(["C", "D", "H", "S"])
        self.CONVERSION: Dict[int,str] = {
            "11": "J",
            "12": "Q",
            "13": "K",
            "14": "A"
        }
        
        self.deck: Set[str] = set() 
        self.add_cards_to_deck()


    def play(self):
        pass

    def get_preflop(self):
        pass

    def draw_card(self, leftover_cards: Set[str]):
        return random.choice(leftover_cards)


    def add_cards_to_deck(self) -> None:

        num: int
        for num in range(self.lowest_num, self.highest_num + 1):
            num: str = str(num)
            if num in self.CONVERSION:
                num: str = self.CONVERSION[num]
            suit: str
            for suit in self.SUITS:
                self.deck.add(suit + num)
