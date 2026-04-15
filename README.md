# Machine Translation Pipeline Project

This repository contains a modular machine translation pipeline designed to translate text
from French to English using a HuggingFace model and to evaluate translation quality using
standard NLP metrics such as BLEU. The project is structured to be clear, extensible, and
aligned with good software engineering practices.

---
## À propos du projet

Ce dépôt fait partie du cours **Big Data and Business Intelligence (BIDABI)**.  
Il a pour objectif d’initier les étudiants au travail avec du code open‑source et à l’adaptation de projets
existants dans une structure professionnelle.

Dans ce projet, les étudiants intègrent un pipeline de traduction automatique (NLP) basé sur un modèle
HuggingFace, comprenant le chargement des données, la traduction, le post‑traitement et l’évaluation
(BLEU). Ils apprennent à :

- analyser et comprendre un projet open‑source existant,
- réorganiser et intégrer ce code dans un template Cookiecutter,
- structurer un pipeline de traitement de données selon les bonnes pratiques,
- préparer un environnement reproductible et adapté aux workflows Big Data.

Ce projet constitue une première immersion dans l’ingénierie des pipelines de données et dans les
méthodologies utilisées dans les systèmes Big Data modernes.

---
## 📌 Project Overview

The goal of this project is to implement a complete translation workflow, including:

- loading input data,
- applying a machine translation model,
- processing translated outputs,
- evaluating translation quality,
- saving results to an output directory.

The pipeline is orchestrated by a central `Orchestrator` class that coordinates all steps.

---

## 📁 Project Structure
```
project/
│
├── data/                # Input data (CSV, JSON, etc.)
│   ├── sample.json
│   ├── sample02.json
│   └── big.csv
│
├── output/              # Generated outputs
│
├── src/
│   ├── loaders/         # Data loading modules
│   ├── translators/     # HuggingFace translation models
│   ├── processors/      # Optional text processing steps
│   ├── evaluators/      # Evaluation metrics (BLEU, etc.)
│   └── orchestrator/    # Main pipeline controller
│       └── orchestrator.py
│
├── tests/               # unit tests
└── main.py              # Entry point for running the pipeline
└── main01.py            # For test
└── main02.py            # For test
└── config.py 
```

---

## ⚙️ How the Pipeline Works

The `Orchestrator` class performs the following steps:

1. **Load data** from the specified file (CSV or JSON).
2. **Translate text** using the model  
   `Helsinki-NLP/opus-mt-fr-en`.
3. **Process results** (optional transformations).
4. **Evaluate translations** using BLEU or another metric.
5. **Save outputs** to the `output/` directory.
6. **Print evaluation scores** and completion status.

Example execution:

```python
if __name__ == "__main__":
    orch = Orchestrator(
        data_path="big.csv",
        output_dir="output",
        translation_model="Helsinki-NLP/opus-mt-fr-en",
        metric="bleu"
    )
    orch.run()
```
## 🎯 Learning Objectives
By working with this project, students will practice:

- structuring a Python project using modular architecture,
- working with HuggingFace translation models,
- handling text datasets,
- computing translation quality metrics,
- managing a complete NLP pipeline from input to evaluation.

## 🧩 Assignment Instructions
You must use this repository as the source code for your assignment:

👉 https://github.com/delnouty/bidabi-clone-adapt-translate.git (github.com in Bing)

Your task is to:

- Generate a new project using the provided template.
- Clone this repository.
- Transfer the code from this repository into the structure created by your template.
- Adapt the code where necessary to match the template’s conventions.
- Ensure the pipeline runs correctly inside the new project.

You are expected to demonstrate initiative and independent problem‑solving while integrating the code.

📅 Your results will be reviewed during the next session.

## 🚀 Running the Project
After integrating the code into your template:
```Bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
python src/orchestrator/orchestrator.py
```
## 📄 License
This project is provided for educational purposes.  
