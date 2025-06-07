from rpg_game.game_logic.personaje import Personaje
from rpg_game.game_logic.combate import iniciar_combate

def main():
    # Inicializa un personaje jugador
    jugador = Personaje(nombre="Héroe", pv=100, poder_ataque=20, defensa=10)

    # Inicializa un personaje enemigo
    enemigo = Personaje(nombre="Trasgo", pv=50, poder_ataque=15, defensa=5)

    # Iniciar combate
    iniciar_combate(jugador, enemigo)

if __name__ == "__main__":
    main()
