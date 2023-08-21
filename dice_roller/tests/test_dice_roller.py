import unittest
import random
from dice_roller import dice_roll


class DiceRollerTest(unittest.TestCase):
    def test_dice_has_allowed_number_of_sides(self):
        self.assertEqual(
            dice_roll.DICE_TYPES,
            ("d4", "d6", "d8", "d10", "d12", "d20", "d100")
        )

    def test_roll(self):
        for dice in dice_roll.DICE_TYPES:
            sides = int(dice[1:])
            result = dice_roll.dice_roll(1, dice)
            numeric_result = int(result.split()[-1])
            self.assertTrue(1 <= numeric_result <= sides) 

    def test_total_roll(self):
        result = dice_roll.dice_roll(2, "d4")
        total_roll_str = result.split(":")[-1].strip()
        total_roll = int(total_roll_str.split()[-1])
        self.assertTrue(2 <= total_roll <= 8)
