import unittest
from rpg_game.game_logic.character import Character

class TestCharacter(unittest.TestCase):

    def test_character_creation(self):
        char = Character(name="TestDummy", hp=100, attack_power=10, defense=5)
        self.assertEqual(char.name, "TestDummy")
        self.assertEqual(char.hp, 100)
        self.assertEqual(char.max_hp, 100)
        self.assertEqual(char.attack_power, 10)
        self.assertEqual(char.defense, 5)

    def test_take_damage_reduces_hp(self):
        char = Character(name="TestDummy", hp=100, attack_power=10, defense=5)
        char.take_damage(30)
        self.assertEqual(char.hp, 70)

    def test_take_damage_hp_does_not_go_below_zero(self):
        char = Character(name="TestDummy", hp=20, attack_power=10, defense=5)
        char.take_damage(30)
        self.assertEqual(char.hp, 0)

    def test_is_alive_true(self):
        char = Character(name="TestDummy", hp=100, attack_power=10, defense=5)
        self.assertTrue(char.is_alive())

    def test_is_alive_false(self):
        char = Character(name="TestDummy", hp=0, attack_power=10, defense=5)
        self.assertFalse(char.is_alive())

    def test_attack_deals_damage(self):
        attacker = Character(name="Attacker", hp=100, attack_power=25, defense=5)
        defender = Character(name="Defender", hp=100, attack_power=10, defense=5)
        
        initial_defender_hp = defender.hp
        attacker.attack(defender)
        
        expected_damage = attacker.attack_power
        self.assertEqual(defender.hp, initial_defender_hp - expected_damage)

if __name__ == '__main__':
    unittest.main()
