from rpg_game.game_logic.character import Character
from rpg_game.game_logic.combat import start_combat

def main():
    # Initialize a player character
    player = Character(name="Hero", hp=100, attack_power=20, defense=10)

    # Initialize an enemy character
    enemy = Character(name="Goblin", hp=50, attack_power=15, defense=5)

    # Start combat
    start_combat(player, enemy)

if __name__ == "__main__":
    main()
