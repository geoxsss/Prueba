class Personaje:
    def __init__(self, nombre: str, pv: int, poder_ataque: int, defensa: int):
        self.nombre = nombre
        self.pv = pv
        self.pv_max = pv  # pv_max se inicializa con los pv iniciales
        self.poder_ataque = poder_ataque
        self.defensa = defensa

    def recibir_danio(self, cantidad: int): # 'amount' parameter also translated to 'cantidad' for consistency
        # Por ahora, un cálculo de daño simple. La defensa se tendrá en cuenta más adelante.
        # Asegura que los PV no bajen de 0.
        self.pv -= cantidad
        if self.pv < 0:
            self.pv = 0

    def atacar(self, objetivo: 'Personaje'): # 'target' parameter also translated to 'objetivo' for consistency
        # Por ahora, el ataque aplica daño directamente.
        # Más adelante, esto podría involucrar lógica más compleja como golpes críticos, fallos, etc.
        # El cálculo de daño será simple: el poder_ataque del atacante.
        # La defensa del objetivo se manejará en recibir_danio o aquí.
        # Para este paso, hagámoslo simple: daño = self.poder_ataque
        # Refinaremos cómo se aplica la defensa en el método recibir_danio o aquí más adelante.
        # Por ahora, asumamos que poder_ataque es el daño bruto infligido.
        print(f"¡{self.nombre} ataca a {objetivo.nombre}!")
        objetivo.recibir_danio(self.poder_ataque)

    def esta_vivo(self) -> bool:
        return self.pv > 0
