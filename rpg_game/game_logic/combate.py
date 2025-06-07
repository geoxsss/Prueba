from .personaje import Personaje # Asegúrate de importar Personaje

def iniciar_combate(jugador: Personaje, enemigo: Personaje): # Renamed parameters for clarity in Spanish
    print(f"--- ¡Comienza el Combate! ---")
    print(f"{jugador.nombre} (PV: {jugador.pv}) vs {enemigo.nombre} (PV: {enemigo.pv})")

    turno = 1 # Renamed 'turn' to 'turno'
    while jugador.esta_vivo() and enemigo.esta_vivo():
        print(f"\n--- Turno {turno} ---")

        # Turno del Jugador
        jugador.atacar(enemigo)
        print(f"{enemigo.nombre} PV: {enemigo.pv}/{enemigo.pv_max}")
        if not enemigo.esta_vivo():
            print(f"\n¡{enemigo.nombre} ha sido derrotado!")
            print(f"¡{jugador.nombre} gana!")
            break

        # Turno del Enemigo
        enemigo.atacar(jugador)
        print(f"{jugador.nombre} PV: {jugador.pv}/{jugador.pv_max}")
        if not jugador.esta_vivo():
            print(f"\n¡{jugador.nombre} ha sido derrotado!")
            print(f"¡{enemigo.nombre} gana!")
            break

        turno += 1

    print(f"\n--- Fin del Combate ---")
