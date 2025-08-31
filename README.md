# 🚀 PitchGenAI — AI Startup Pitch Generator

**PitchGenAI** is a local AI-powered tool that generates structured startup pitch scripts based on your input. Designed for educational and assignment purposes, it runs fully offline using the **Phi-3-mini-4k-instruct-q4.gguf** local model.

---

## Features

* Generate investor-ready startup pitches.
* Fully offline using a local GPT4All model.
* Customizable pitch tone: *formal, persuasive, storytelling*.
* Auto-save generated pitches with timestamps.
* Streamlit interface for easy interaction.
* Download generated pitches as `.txt` files.

---

## Input Fields

1. **Startup Name**
2. **Problem** — the main challenge your startup solves
3. **Solution** — how your startup addresses the problem
4. **Target Market** — who your startup serves
5. **Business Model** — how your startup earns revenue
6. **Pitch Tone** — tone of the generated pitch

---

## Tech Stack

* **Python 3.10+**
* **Streamlit** — for UI
* **GPT4All Python package** — for local LLM inference
* **Phi-3-mini-4k-instruct-q4.gguf** — instruction-tuned local model

---

## Folder Structure

```
PitchGenAI/
├─ app.py                  # Streamlit application
├─ requirements.txt        # Python dependencies
├─ models/
│  └─ Phi-3-mini-4k-instruct-q4.gguf  # Local GPT4All model
├─ generators/
│  └─ pitch_generator.py   # Script to generate pitches
├─ utils/
│  ├─ prompt_templates.py  # Pitch templates
│  └─ helpers.py           # Save/download functions
├─ outputs/                # Auto-saved pitch scripts
└─ test/
   └─ test_generator.py    # Unit tests (optional)
```

---

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the **Phi-3-mini-4k-instruct-q4.gguf** model and place it in the `models/` folder.

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

1. Fill in the startup information.
2. Select a pitch tone.
3. Click **Generate Pitch**.
4. View the generated pitch and download it if desired.

---

## Example Input

* Startup Name: GreenSpark Energy
* Problem: Small businesses struggle to adopt renewable energy due to high upfront costs.
* Solution: Subscription-based platform offering tailored solar & wind energy plans.
* Target Market: SMEs aiming to reduce energy costs and carbon footprint.
* Business Model: Subscription fees + commission on installations.
* Pitch Tone: Persuasive

---

## Notes

* Works fully offline — no API keys required.
* Max tokens can be increased in `pitch_generator.py` for longer pitches.
* Recommended for assignments or local MVP demos.

