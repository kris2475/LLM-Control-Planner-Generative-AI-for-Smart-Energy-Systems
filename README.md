# 🤖 LLM-Control-Planner: Generative AI for Smart Energy Systems

**LLM-Control-Planner** is a demonstration of using a **Large Language Model (LLM)** as a *high-level control planner* for embedded or IoT systems.  
It translates natural-language goals (e.g. “Keep the room comfortable but save energy when solar power is high”) into a **deterministic JSON control plan** that can be executed by a lower-level controller such as an ESP32 running a LightGBM or PID-based kernel.

This repository focuses on the *Generative AI orchestration layer* — not the physical hardware.  
The hardware is **simulated**, allowing experimentation and demonstration of the control logic without needing an actual underfloor heating setup.

---

## 🔍 Overview

Traditional control systems are rule-based or model-driven, optimised for efficiency within fixed boundaries.  
However, they struggle to interpret **human intent** or adapt dynamically to contextual conditions (like sunlight, occupancy, or energy price forecasts).

This project demonstrates how an **LLM can act as a semantic control bridge**:

1. **Input:** Natural-language goals + contextual sensor data.  
2. **Processing:** The LLM converts intent into a deterministic, machine-readable control plan (JSON).  
3. **Output:** The plan calls pre-defined control functions such as `set_heater_power(x)` or `adjust_target_temp(y)`.

---

## 🧩 Architecture

```text
+--------------------------+
|   User / External Agent  |
| "Keep the room at 22°C   |
|  but save energy if sunny"|
+------------+-------------+
             |
             v
+--------------------------+
|       LLM Planner        |
| (Function-calling API)   |
| • Parses natural language|
| • Interprets context     |
| • Outputs JSON plan      |
+------------+-------------+
             |
             v
+--------------------------+
|  Control Execution Layer |
| (Simulated ESP32 Kernel) |
| • Executes commands      |
| • Feeds back telemetry   |
+--------------------------+
```

---

## ⚙️ Example Interaction

**Input:**
```json
{
  "goal": "Keep the living room around 22°C when occupied, reduce to 19°C if empty, and use solar excess for preheating.",
  "context": {
    "temperature": 21.3,
    "occupancy": true,
    "solar_generation": 1.8,
    "energy_price": 0.24
  }
}
```

**LLM Output:**
```json
{
  "actions": [
    { "function": "set_target_temp", "args": { "value": 22 } },
    { "function": "set_heater_power", "args": { "value": 0.6 } },
    { "function": "log_event", "args": { "message": "Preheating using solar surplus" } }
  ]
}
```

---

## 🧠 Key Features

- **Natural-language control:** Translate user intent into actionable control logic.
- **Function-calling LLM API:** Deterministic JSON plans ensure reproducibility and safety.
- **Hardware simulation:** Mocked ESP32 environment for development and testing.
- **Modular design:** Swap in real hardware control interfaces later.
- **Energy-awareness:** Context-driven reasoning (temperature, solar, occupancy, cost).

---

## 🧰 Tech Stack

- **Python** (main control logic)
- **OpenAI / Llama function calling** (LLM orchestration)
- **FastAPI** (optional REST interface)
- **Simulated hardware layer** (Python mock of ESP32 control)
- **JSON schema validation** (for deterministic plan execution)

---

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/LLM-Control-Planner.git
cd LLM-Control-Planner
pip install -r requirements.txt
python run_demo.py
```

---

## 📄 Example: Generated Control Plan

Run the demo and see how the LLM converts intent into deterministic commands:

```bash
python run_demo.py --goal "Keep the house warm when occupied, reduce power when unoccupied, use solar gain when available."
```

---

## 🧩 Future Extensions

- Integrate with real ESP32 MQTT control nodes.  
- Add reinforcement feedback (auto-tuning of setpoints).  
- Include weather forecasts and price signals for predictive planning.  
- Explore smaller local LLMs for on-edge reasoning.  

---

## 📚 Inspiration

This project extends the ideas explored in my **AI Climate Control (log(1 + PWMTarget) Bridge)** series — combining **LightGBM precision control** with **LLM-based high-level planning** for energy-efficient systems.

---

## 🏷️ Tags

`#GenAI` `#LLM` `#IoT` `#EdgeAI` `#EnergyEfficiency` `#ControlSystems`

---

*Author: K Seunarine*  
*License: MIT*
