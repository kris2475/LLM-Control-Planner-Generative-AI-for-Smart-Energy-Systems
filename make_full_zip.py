import zipfile

files = {
    "llm_planner/__init__.py": "",
    "llm_planner/planner.py": """
# LLM-based Planner (Free version)
import json

def generate_plan(goal, context):
    # Simulate LLM output as JSON plan
    plan = {
        "actions": [
            {"function": "set_target_temp", "args": {"value": 22}},
            {"function": "set_heater_power", "args": {"value": 0.6}},
            {"function": "preheat_floor", "args": {"use_solar": True}},
            {"function": "log_event", "args": {"message": "Preheating using solar surplus, avoiding overshoot"}}
        ]
    }
    return plan
""",
    "simulator/__init__.py": "",
    "simulator/esp32_sim.py": """
# Simulated ESP32 controller
class ESP32Sim:
    def set_target_temp(self, value):
        print(f"Target temperature set to {value}°C")

    def set_heater_power(self, value):
        print(f"Heater power set to {int(value*100)}%")

    def preheat_floor(self, use_solar=True):
        source = "solar energy" if use_solar else "grid energy"
        print(f"Preheating floor using {source}")

    def log_event(self, message):
        print(f"[LOG]: {message}")
""",
    "run_demo.py": """
from llm_planner.planner import generate_plan
from simulator.esp32_sim import ESP32Sim

def main():
    esp32 = ESP32Sim()
    goal = ("Keep the living room around 22°C when people are home, "
            "but reduce to 19°C if the house is empty for more than an hour. "
            "If the sun is shining and solar generation exceeds 1.5 kW, "
            "use the excess energy to preheat the floor. "
            "Avoid overshooting the comfort range.")
    context = {
        "temperature": 21.3,
        "occupancy": True,
        "solar_generation": 1.8,
        "energy_price": 0.24,
        "time_since_empty": 0.5
    }

    plan = generate_plan(goal, context)

    for action in plan["actions"]:
        func = getattr(esp32, action["function"])
        func(**action["args"])

if __name__ == "__main__":
    main()
""",
    "README.md": "# LLM-Control-Planner-Full\n\nThis is the full working demo zip with LLM planner and simulated ESP32."
}

zip_name = "LLM-Control-Planner-Full.zip"

with zipfile.ZipFile(zip_name, "w") as zf:
    for path, content in files.items():
        zf.writestr(path, content)

print(f"{zip_name} created successfully!")

