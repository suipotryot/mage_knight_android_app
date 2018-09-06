from main import Dummy
import unittest


class TestDummyScreen(unittest.TestCase):

    """"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_should_create_deck_of_16_cards(self):
        ds = Dummy("", "ARYTHEA")

        deck = ds.deck

        self.assertEqual(len(deck), 16)

    def test_deck_contains_mage_special_cards_after_init(self):
        ds = Dummy("", "ARYTHEA")

        deck = ds.deck
        
        self.assertEqual(deck[0], ("Battle Versatility", "Red"))
        self.assertEqual(deck[13], ("Mana Pull", "White"))

    def test_play_card_should_pick_a_random_card(self):
        ds = Dummy("", "ARYTHEA")

        deck = ds.deck
        ds.play_card()

        self.assertEqual(len(deck), 15)

    def test_play_card_should_play_multiple_cards_if_times_given(self):
        ds = Dummy("", "ARYTHEA")
        
        deck = ds.deck
        ds.play_card(times=5)

        self.assertEqual(len(deck), 16-5)

    def test_play_card_should_return_played_cards(self):
        ds = Dummy("", "ARYTHEA")

        deck = ds.deck
        played_cards = ds.play_card(times=3)

        self.assertEqual(len(played_cards), 3)

    def test_play_turn_should_play_only_3_cards_if_no_crystal_of_3rd_one_color(self):
        ds = Dummy("", "ARYTHEA")
        def play_card_stub(times):
            for i in range(times):
                ds.deck.pop(0)
            return [("Determination", "Blue")]
        ds.play_card = play_card_stub

        deck = ds.deck
        ds.play_turn()

        self.assertEqual(len(deck), 16-3)

    def test_play_turn_should_play_5_cards_if_2_crystals_of_3rd_one_color(self):
        ds = Dummy("", "ARYTHEA")
        def play_card_stub(times):
            for i in range(times):
                ds.deck.pop(0)
            return [("Rage", "Red")]
        ds.play_card = play_card_stub

        deck = ds.deck
        ds.play_turn()

        self.assertEqual(len(deck), 16-5)
