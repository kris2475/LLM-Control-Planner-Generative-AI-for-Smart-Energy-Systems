class ESP32Sim:
    def __init__(self):
        self.temperature = 21.0
        self.occupancy = True
        self.heater_power = 0.0

    def set_target_temp(self, value: float):
        print(f"Target temperature set to {value}°C")

    def set_heater_power(self, value: float):
        self.heater_power = value
        print(f"Heater power set to {value*100:.0f}%")

    def preheat_floor(self, use_solar: bool = False):
        print(f"Preheating floor using {'solar' if use_solar else 'grid'} energy")

    def log_event(self, message: str):
        print(f"[LOG]: {message}")