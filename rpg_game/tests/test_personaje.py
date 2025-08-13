import unittest
from rpg_game.game_logic.personaje import Personaje
from io import StringIO
import sys

class TestPersonaje(unittest.TestCase):

    def setUp(self):
        # Redirigir stdout para no mostrar los print durante las pruebas
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Restaurar stdout
        sys.stdout = self.held_stdout

    def test_creacion_personaje(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=100, poder_ataque=10, defensa=5)
        self.assertEqual(personaje.nombre, "MuñecoDePruebas")
        self.assertEqual(personaje.pv, 100)
        self.assertEqual(personaje.pv_max, 100)
        self.assertEqual(personaje.poder_ataque, 10)
        self.assertEqual(personaje.defensa, 5)

    def test_recibir_danio_reduce_pv_con_defensa(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=100, poder_ataque=10, defensa=5)
        personaje.recibir_danio(30)
        # Daño real = 30 (daño bruto) - 5 (defensa) = 25
        # PV restantes = 100 - 25 = 75
        self.assertEqual(personaje.pv, 75)

    def test_recibir_danio_pv_no_baja_de_cero(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=20, poder_ataque=10, defensa=5)
        # Daño real = 30 (daño bruto) - 5 (defensa) = 25
        # PV restantes = 20 - 25 = -5, que debe ser 0
        personaje.recibir_danio(30)
        self.assertEqual(personaje.pv, 0)

    def test_esta_vivo_verdadero(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=100, poder_ataque=10, defensa=5)
        self.assertTrue(personaje.esta_vivo())

    def test_esta_vivo_falso(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=0, poder_ataque=10, defensa=5)
        self.assertFalse(personaje.esta_vivo())

    def test_atacar_inflige_danio_considerando_defensa(self):
        atacante = Personaje(nombre="Atacante", pv=100, poder_ataque=25, defensa=5)
        defensor = Personaje(nombre="Defensor", pv=100, poder_ataque=10, defensa=10)

        pv_inicial_defensor = defensor.pv
        atacante.atacar(defensor)

        # Daño esperado = 25 (poder_ataque) - 10 (defensa) = 15
        danio_esperado = atacante.poder_ataque - defensor.defensa
        self.assertEqual(defensor.pv, pv_inicial_defensor - danio_esperado)

    def test_defensa_alta_reduce_danio_a_cero(self):
        atacante = Personaje(nombre="Atacante Débil", pv=100, poder_ataque=10, defensa=5)
        defensor = Personaje(nombre="Defensor Fuerte", pv=100, poder_ataque=10, defensa=20)

        pv_inicial_defensor = defensor.pv
        atacante.atacar(defensor)

        # Como defensa (20) > poder_ataque (10), el daño debe ser 0
        self.assertEqual(defensor.pv, pv_inicial_defensor)

if __name__ == '__main__':
    unittest.main()
