class Character:
    def __init__(self, name: str, hp: int, attack_power: int, defense: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp  # max_hp is initialized to the starting hp
        self.attack_power = attack_power
        self.defense = defense

    def take_damage(self, amount: int):
        # For now, a simple damage calculation. Defense will be factored in later.
        # Ensure HP doesn't go below 0.
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, target: 'Character'):
        # For now, attack directly applies damage.
        # Later, this might involve more complex logic like critical hits, misses, etc.
        # The damage calculation will be simple: attacker's attack_power.
        # The target's defense will be handled in take_damage or here.
        # For this step, let's make it simple: damage = self.attack_power
        # We will refine how defense is applied in the take_damage method or here later.
        # For now, let's assume attack_power is the raw damage dealt.
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)

    def is_alive(self) -> bool:
        return self.hp > 0
