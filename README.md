# 🤖 LLM-Control-Planner: Generative AI for Smart Energy Systems

**LLM-Control-Planner** demonstrates using a **Large Language Model (LLM)** as a *high-level control planner* for embedded or IoT systems.  
It converts natural-language goals into **deterministic JSON control plans** that are executed by a lower-level controller (simulated ESP32 in this repository).  

The focus is on **Generative AI orchestration**, allowing you to showcase complex, intent-driven control without needing real hardware.

---

## 🔍 Overview

Traditional control systems struggle with **multi-variable, context-dependent goals**, such as balancing comfort, occupancy, solar energy use, and thermal inertia.  

This project demonstrates how an **LLM can act as a semantic control bridge**:

1. **Input:** Natural-language goals + contextual sensor data  
2. **Processing:** The LLM interprets intent and generates a deterministic JSON plan  
3. **Output:** The plan calls pre-defined control functions like `set_heater_power(x)` or `set_target_temp(y)`  

The Python demo executes the plan directly, showing the target temperature, heater power, and any energy-saving actions in the console.

---

## 🧩 Example User Goal

A realistic user intent might be:  

> “Keep the living room around 22°C when people are home, but reduce to 19°C if the house is empty for more than an hour.  
> If the sun is shining and solar generation exceeds 1.5 kW, use the excess energy to preheat the floor.  
> However, avoid overshooting the comfort range to prevent wasted heat later in the evening.”  

The **LLM planner** interprets these instructions and generates a deterministic plan that respects all constraints, balancing **comfort, efficiency, and energy availability**.

---

## ⚙️ Architecture

```text
+--------------------------+
|   User / External Agent  |
| Natural language intent  |
+------------+-------------+
             |
             v
+--------------------------+
|       LLM Planner        |
| (Function-calling API)   |
| • Parses intent          |
| • Interprets context     |
| • Outputs JSON plan      |
+------------+-------------+
             |
             v
+--------------------------+
|  Control Execution Layer |
| (Simulated ESP32 Kernel) |
| • Executes commands      |
| • Prints console output  |
+--------------------------+
```

---

## ⚡ Example Input & Output

**Input to the LLM:**
```json
{
  "goal": "Keep the living room around 22°C when people are home, but reduce to 19°C if the house is empty for more than an hour. If the sun is shining and solar generation exceeds 1.5 kW, use the excess energy to preheat the floor. Avoid overshooting the comfort range.",
  "context": {
    "temperature": 21.3,
    "occupancy": true,
    "solar_generation": 1.8,
    "energy_price": 0.24,
    "time_since_empty": 0.5
  }
}
```

**LLM Output (executed by the Python demo):**
```json
{
  "actions": [
    { "function": "set_target_temp", "args": { "value": 22 } },
    { "function": "set_heater_power", "args": { "value": 0.6 } },
    { "function": "preheat_floor", "args": { "use_solar": true } },
    { "function": "log_event", "args": { "message": "Preheating using solar surplus, avoiding overshoot" } }
  ]
}
```

The demo prints:

```
Target temperature set to 22°C
Heater power set to 60%
Preheating floor using solar energy
[LOG]: Preheating using solar surplus, avoiding overshoot
```

---

## 🧠 Key Features

- **Natural-language control:** Translate complex, flexible instructions into deterministic commands  
- **Function-calling LLM API:** Ensures reproducibility, safety, and interpretable plans  
- **Hardware simulation:** Python stubs simulate ESP32 for testing without devices  
- **Energy-aware reasoning:** Accounts for occupancy, solar generation, and comfort constraints  
- **Modular design:** Plans can be executed on real embedded controllers later  

---

## 🧰 Tech Stack

- **Python** (main control logic)  
- **Transformers / Hugging Face models** (free LLM for plan generation)  
- **Simulated ESP32 hardware layer** (Python mock)  
- **JSON schema validation** (deterministic plan verification)  

---

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/LLM-Control-Planner.git
cd LLM-Control-Planner
pip install -r requirements.txt
python run_demo.py
```

---

## 🧩 Future Extensions

- Connect to real ESP32 MQTT nodes for live testing  
- Add reinforcement learning for plan optimisation  
- Include weather forecasts and energy price data for predictive control  
- Explore local LLMs for edge deployment  

---

## 📚 Inspiration

Based on the **AI Climate Control (log(1 + PWMTarget) Bridge)** project, combining **LightGBM precision control** with **LLM high-level planning** for energy-efficient smart systems.

---

## 🏷️ Tags

`#GenAI` `#LLM` `#IoT` `#EdgeAI` `#EnergyEfficiency` `#ControlSystems`  

---

*Author: K Seunarine*  
*License: MIT*
