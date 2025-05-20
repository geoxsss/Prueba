import unittest
from rpg_game.game_logic.character import Character
from rpg_game.game_logic.combat import start_combat
from io import StringIO # To capture print output
import sys # To redirect stdout

class TestCombat(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.held_stdout

    def test_combat_player_wins(self):
        # Player is much stronger
        player = Character(name="Strong Player", hp=100, attack_power=50, defense=10)
        enemy = Character(name="Weak Enemy", hp=30, attack_power=5, defense=5)
        
        start_combat(player, enemy)
        
        self.assertTrue(player.is_alive())
        self.assertFalse(enemy.is_alive())
        
        output = sys.stdout.getvalue() # Get print output
        self.assertIn("Strong Player wins!", output)

    def test_combat_enemy_wins(self):
        # Enemy is much stronger
        player = Character(name="Weak Player", hp=30, attack_power=5, defense=5)
        enemy = Character(name="Strong Enemy", hp=100, attack_power=50, defense=10)
        
        start_combat(player, enemy)
        
        self.assertFalse(player.is_alive())
        self.assertTrue(enemy.is_alive())

        output = sys.stdout.getvalue() # Get print output
        self.assertIn("Strong Enemy wins!", output)

    def test_combat_draw_scenario_eventual_win(self):
        # Equal stats, expecting player to win due to attacking first or more turns
        # For this simple system, the first attacker has an advantage.
        # Let's ensure combat ends and someone wins.
        player = Character(name="Player", hp=50, attack_power=10, defense=5)
        enemy = Character(name="Enemy", hp=50, attack_power=10, defense=5)
        
        start_combat(player, enemy)
        
        # One of them must be defeated
        self.assertTrue(not player.is_alive() or not enemy.is_alive())
        # Ensure a winner is declared
        output = sys.stdout.getvalue()
        self.assertTrue("wins!" in output)


if __name__ == '__main__':
    unittest.main()
