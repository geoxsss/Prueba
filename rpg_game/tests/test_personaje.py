import unittest
from rpg_game.game_logic.personaje import Personaje

class TestPersonaje(unittest.TestCase):

    def test_creacion_personaje(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=100, poder_ataque=10, defensa=5)
        self.assertEqual(personaje.nombre, "MuñecoDePruebas")
        self.assertEqual(personaje.pv, 100)
        self.assertEqual(personaje.pv_max, 100)
        self.assertEqual(personaje.poder_ataque, 10)
        self.assertEqual(personaje.defensa, 5)

    def test_recibir_danio_reduce_pv(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=100, poder_ataque=10, defensa=5)
        personaje.recibir_danio(30)
        self.assertEqual(personaje.pv, 70)

    def test_recibir_danio_pv_no_baja_de_cero(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=20, poder_ataque=10, defensa=5)
        personaje.recibir_danio(30)
        self.assertEqual(personaje.pv, 0)

    def test_esta_vivo_verdadero(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=100, poder_ataque=10, defensa=5)
        self.assertTrue(personaje.esta_vivo())

    def test_esta_vivo_falso(self):
        personaje = Personaje(nombre="MuñecoDePruebas", pv=0, poder_ataque=10, defensa=5)
        self.assertFalse(personaje.esta_vivo())

    def test_atacar_inflige_danio(self):
        atacante = Personaje(nombre="Atacante", pv=100, poder_ataque=25, defensa=5)
        defensor = Personaje(nombre="Defensor", pv=100, poder_ataque=10, defensa=5)

        pv_inicial_defensor = defensor.pv
        atacante.atacar(defensor) # Assumes Personaje.atacar takes Personaje as argument

        # The attack method in Personaje directly uses self.poder_ataque as damage
        # The recibir_danio method then subtracts this from pv
        danio_esperado = atacante.poder_ataque
        self.assertEqual(defensor.pv, pv_inicial_defensor - danio_esperado)

if __name__ == '__main__':
    unittest.main()
