class Personaje:
    def __init__(self, nombre: str, pv: int, poder_ataque: int, defensa: int):
        self.nombre = nombre
        self.pv = pv
        self.pv_max = pv  # pv_max se inicializa con los pv iniciales
        self.poder_ataque = poder_ataque
        self.defensa = defensa

    def recibir_danio(self, cantidad: int):
        # La defensa reduce el daño recibido. El daño no puede ser negativo.
        danio_real = max(0, cantidad - self.defensa)
        print(f"{self.nombre} recibe {danio_real} puntos de daño.")
        # Asegura que los PV no bajen de 0.
        self.pv -= danio_real
        if self.pv < 0:
            self.pv = 0

    def atacar(self, objetivo: 'Personaje'):
        # El ataque inflige daño basado en el poder_ataque.
        # La lógica de reducción de daño por defensa se maneja en el método recibir_danio del objetivo.
        # Futuras mejoras podrían incluir golpes críticos, fallos, etc.
        print(f"¡{self.nombre} ataca a {objetivo.nombre}!")
        objetivo.recibir_danio(self.poder_ataque)

    def esta_vivo(self) -> bool:
        return self.pv > 0
