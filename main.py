import kivy
kivy.require('1.0.6')
import sys

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ListProperty

mages = {
    "BASE": {
        "cards": {
            0: ("Rage", "Red"),
            1: ("Rage", "Red"),
            2: ("Determination", "Blue"),
            3: ("Swiftness", "White"),
            4: ("Swiftness", "White"),
            5: ("March", "Green"),
            6: ("March", "Green"),
            7: ("Stamina", "Blue"),
            8: ("Stamina", "Blue"),
            9: ("Tranquility", "Green"),
            10: ("Promise", "White"),
            11: ("Threaten", "Red"),
            12: ("Crystallize", "Blue"),
            13: ("Mana Draw", "White"),
            14: ("Concentration", "Green"),
            15: ("Improvisation" , "Red"),
            }
    },
    "ARYTHEA": {
        "cards": {
                0: ("Battle Versatility", "Red"),
                13: ("Mana Pull", "White"),
            },
        "crystals": ["Red", "Red", "White"]
    },
    "GOLDYX": {
        "cards": {
                12: ("Crystal Joy", "Blue"),
                14: ("Will Focus", "Green"),
            },
        "crystals": ["Blue", "Green", "Green"]
    },
    "NOROWAS": {
        "cards": {
                9: ("Rejuvenate", "Green"),
                10: ("Noble Manners", "White"),
            },
        "crystals": ["Green", "White", "White"]
    },
    "TOVAK": {
        "cards": {
                2: ("Cold Toughness", "Blue"),
                15: ("Instinct", "Red"),
            },
        "crystals": ["Red", "Blue", "Blue"]
    },
    "WOLFHAWK": {
        "cards": {
                3: ("Swift Reflexes", "White"),
                7: ("Tirelessness", "Blue"),
            },
        "crystals": ["Blue", "White", "White"]
    },
    "KRANG": {
        "cards": {
                5: ("Savage Harvesting", "Green"),
                11: ("Ruthless Coercion", "Red"),
            },
        "crystals": ["Red", "Red", "Green"]
    },
    "BRAEVALAR": {
        "cards": {
                6: ("One With the Land", "Green"),
                8: ("Druidic Paths", "Blue"),
            },
        "crystals": ["Blue", "Blue", "Green"]
    }
}

sm = ScreenManager()

def select_mage_callback(mage_name):
    def set_dummy_screen():
        screen = Dummy('dummy_name', mage_name)
        sm.switch_to(screen)
    return set_dummy_screen

# Declare both screens
class MenuScreen(Screen):
    pass


class DummySelectionScreen(Screen):

    def on_pre_enter(self, *args):
        mage_list = {k for k, v in mages.items() if k != 'BASE'}
        for mage in mage_list:
            button = Button(text=mage)
            button.on_press = select_mage_callback(mage)
            self.ids.dummy_selection_grid.add_widget(button, index=1)


class Dummy(Screen):

    deck = ListProperty()
    deed_deck = ListProperty()
    crystals = ListProperty()
        
    def __init__(self, name, dummy_name):
        super().__init__()
        self.deck = {**(mages['BASE']['cards']), **(mages[dummy_name]['cards'])}.values()
        self.crystals = mages[dummy_name]['crystals']
        self.deed_deck = {}

    def play_turn(self):
        played_cards = self.play_card(3)
        crystal_count = self.crystals.count(played_cards[-1][1])
        self.play_card(times=crystal_count)

    def play_card(self, times=1):
        import random
        played_cards = []
        for t in range(times):
            random_index = random.randrange(len(self.deck))
            played_card = self.deck.pop(random_index)
            played_cards.append(played_card)
        return played_cards



class DummyApp(App):

    def build(self):
        # Create the screen manager
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(DummySelectionScreen(name='dummy_selection'))

        return sm

if __name__ == '__main__':
    DummyApp().run()
