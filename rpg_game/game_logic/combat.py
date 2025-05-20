from .character import Character # Make sure to import Character

def start_combat(player: Character, enemy: Character):
    print(f"--- Combat Starts! ---")
    print(f"{player.name} (HP: {player.hp}) vs {enemy.name} (HP: {enemy.hp})")

    turn = 1
    while player.is_alive() and enemy.is_alive():
        print(f"\n--- Turn {turn} ---")

        # Player's turn
        player.attack(enemy)
        print(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}")
        if not enemy.is_alive():
            print(f"\n{enemy.name} has been defeated!")
            print(f"{player.name} wins!")
            break

        # Enemy's turn
        enemy.attack(player)
        print(f"{player.name} HP: {player.hp}/{player.max_hp}")
        if not player.is_alive():
            print(f"\n{player.name} has been defeated!")
            print(f"{enemy.name} wins!")
            break
        
        turn += 1
    
    print(f"\n--- Combat Ends ---")
