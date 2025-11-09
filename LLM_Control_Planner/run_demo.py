from llm_planner.planner import generate_plan
from simulator.esp32_sim import ESP32Sim

def main():
    # Simulated ESP32 hardware
    esp32 = ESP32Sim()

    # Example goal and context
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

    # Generate plan (mocked LLM)
    plan = generate_plan(goal, context)

    # Execute plan on simulated ESP32
    for action in plan["actions"]:
        func = getattr(esp32, action["function"])
        func(**action["args"])

if __name__ == "__main__":
    main()