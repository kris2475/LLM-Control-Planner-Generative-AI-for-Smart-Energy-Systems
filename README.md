# 🤖 LLM-Control-Planner: Generative AI for Smart Energy Systems

## 🚨 Executive Summary

**LLM-Control-Planner** shows how a **Large Language Model (LLM)** can act as a *high-level controller* for smart home or IoT systems.  

In simple terms:

1. You give the system a **natural-language goal** like:  
   *“Keep the living room at 22°C when occupied, reduce to 19°C when empty, and use extra solar energy to preheat the floor.”*

2. The LLM **converts that goal into a step-by-step plan** in JSON format, deciding **what functions to call and with which values**.  

3. The Python demo **executes the plan** on a simulated ESP32, printing results like:

```
Target temperature set to 22°C
Heater power set to 60%
Preheating floor using solar energy
[LOG]: Preheating using solar surplus, avoiding overshoot
```

✅ This immediately shows **how high-level goals become deterministic actions**, balancing comfort, efficiency, and energy use—all without needing real hardware.

---

## 🔍 Overview

Traditional control systems struggle with **multi-variable, context-dependent goals**, such as balancing comfort, occupancy, solar energy use, and thermal inertia.  

This project demonstrates how an **LLM can act as a semantic control bridge**:

1. **Input:** Natural-language goals + contextual sensor data  
2. **Processing:** The LLM interprets intent and generates a deterministic JSON plan  
3. **Output:** The plan calls pre-defined control functions like `set_heater_power(x)` or `set_target_temp(y)`  

The Python demo executes the plan directly, showing the target temperature, heater power, and any energy-saving actions in the console.

---

## ⚡ Example Input & Output

**User Goal:**

> “Keep the living room around 22°C when people are home, but reduce to 19°C if the house is empty for more than an hour.  
> If the sun is shining and solar generation exceeds 1.5 kW, use the excess energy to preheat the floor.  
> Avoid overshooting the comfort range.”

**Context:**
```json
{
  "temperature": 21.3,
  "occupancy": true,
  "solar_generation": 1.8,
  "energy_price": 0.24,
  "time_since_empty": 0.5
}
```

**Generated JSON Plan (executed by demo):**
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

**Console Output:**
```
Target temperature set to 22°C
Heater power set to 60%
Preheating floor using solar energy
[LOG]: Preheating using solar surplus, avoiding overshoot
```

---

## 🖥️ How to Read the Output

| Console Line                                  | Meaning                                                                 |
|-----------------------------------------------|-------------------------------------------------------------------------|
| `Target temperature set to 22°C`              | The system will maintain 22°C in the living room.                       |
| `Heater power set to 60%`                      | Heater output is set to 60% to efficiently reach the target temperature.|
| `Preheating floor using solar energy`          | Extra solar energy is being used to heat the floor, saving electricity. |
| `[LOG]: Preheating using solar surplus...`     | Informational message from the system explaining its decision.          |

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

## 🧠 Key Features

- Translate **natural language instructions** into deterministic, executable actions  
- Simulate hardware safely with Python stubs  
- Use energy-aware reasoning for occupancy, solar, and comfort constraints  
- Plans can later be run on real embedded controllers  

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

Combining **LightGBM precision control** with **LLM high-level planning** for energy-efficient smart systems.
https://github.com/kris2475/AI-Informed-Underfloor-Heating-Control-with-ESP32

---

## 🏷️ Tags

`#GenAI` `#LLM` `#IoT` `#EdgeAI` `#EnergyEfficiency` `#ControlSystems`  

---

*Author: K Seunarine*  
*License: MIT*
