# Assure-toi d'être dans C:\Users\Moi\Desktop\bidabi-clone-adapt-translate
import os
from pathlib import Path

# Chemin vers la racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")