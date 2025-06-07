import unittest
from rpg_game.game_logic.personaje import Personaje
from rpg_game.game_logic.combate import iniciar_combate
from io import StringIO # Para capturar la salida de print
import sys # Para redirigir stdout

class TestCombate(unittest.TestCase):

    def setUp(self):
        # Redirigir stdout para capturar las declaraciones print
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restaurar stdout
        sys.stdout = self.held_stdout

    def test_combate_jugador_gana(self):
        # El jugador es mucho más fuerte
        jugador = Personaje(nombre="Jugador Fuerte", pv=100, poder_ataque=50, defensa=10)
        enemigo = Personaje(nombre="Enemigo Débil", pv=30, poder_ataque=5, defensa=5)

        iniciar_combate(jugador, enemigo)

        self.assertTrue(jugador.esta_vivo())
        self.assertFalse(enemigo.esta_vivo())

        output = sys.stdout.getvalue() # Obtener la salida de print
        self.assertIn("¡Jugador Fuerte gana!", output)

    def test_combate_enemigo_gana(self):
        # El enemigo es mucho más fuerte
        jugador = Personaje(nombre="Jugador Débil", pv=30, poder_ataque=5, defensa=5)
        enemigo = Personaje(nombre="Enemigo Fuerte", pv=100, poder_ataque=50, defensa=10)

        iniciar_combate(jugador, enemigo)

        self.assertFalse(jugador.esta_vivo())
        self.assertTrue(enemigo.esta_vivo())

        output = sys.stdout.getvalue() # Obtener la salida de print
        self.assertIn("¡Enemigo Fuerte gana!", output)

    def test_combate_escenario_similar_termina(self):
        # Estadísticas iguales, esperando que el combate termine y alguien gane.
        # En este sistema simple, el primer atacante tiene ventaja.
        jugador = Personaje(nombre="Jugador", pv=50, poder_ataque=10, defensa=5)
        enemigo = Personaje(nombre="Enemigo", pv=50, poder_ataque=10, defensa=5)

        iniciar_combate(jugador, enemigo)

        # Uno de ellos debe ser derrotado
        self.assertTrue(not jugador.esta_vivo() or not enemigo.esta_vivo())
        # Asegurar que se declara un ganador
        output = sys.stdout.getvalue()
        mensaje_victoria_jugador = f"¡{jugador.nombre} gana!" # Espera "¡Jugador gana!"
        mensaje_victoria_enemigo = f"¡{enemigo.nombre} gana!" # Espera "¡Enemigo gana!"

        self.assertTrue(mensaje_victoria_jugador in output or \
                        mensaje_victoria_enemigo in output,
                        msg=f"No se encontró el mensaje de victoria esperado. Output fue:\n{output}")


if __name__ == '__main__':
    unittest.main()
