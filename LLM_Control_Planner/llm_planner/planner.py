import json

def generate_plan(goal: str, context: dict):
    """
    Mock LLM planner for demonstration.
    Returns a deterministic JSON plan simulating LLM output.
    """
    print(f"Generating plan for goal: {goal}")

    # Example plan based on complex LLM use-case
    plan = {
        "actions": [
            {"function": "set_target_temp", "args": {"value": 22 if context["occupancy"] else 19}},
            {"function": "set_heater_power", "args": {"value": 0.6}},
            {"function": "preheat_floor", "args": {"use_solar": context.get("solar_generation", 0) > 1.5}},
            {"function": "log_event", "args": {"message": "Preheating using solar surplus, avoiding overshoot"}}
        ]
    }
    return plan