import json
from pathlib import Path
from typing import Any, Dict, List, Union

import pandas as pd

from src.loaders.base_loader import BaseLoader


class JsonLoader(BaseLoader):
    """
    Charge des fichiers JSON depuis un répertoire et les convertit en DataFrame.
    Gère aussi bien les objets JSON uniques que les listes d'objets.
    """

    def __init__(self, directory, pattern="*.json"):
        """
        Initialise le chargeur avec un chemin vers un répertoire contenant des fichiers JSON.
        """
        self.directory = Path(directory)
        self.pattern = pattern

    def load_json_files(self) -> List[Path]:
        """
        Retourne la liste des fichiers JSON présents dans le répertoire.
        """
        return list(self.directory.glob(self.pattern))

    def _flatten(
        self, obj: Any, prefix: str = "", out: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Aplati récursivement une structure JSON (dictionnaires et listes)
        en un dictionnaire à clés simples.

        Exemple de clés générées :
        - meta.id
        - meta.tags[0]
        """
        if out is None:
            out = {}

        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{prefix}.{key}" if prefix else key
                self._flatten(value, new_key, out)

        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                new_key = f"{prefix}[{index}]"
                self._flatten(item, new_key, out)

        else:
            out[prefix] = obj

        return out

    def to_dataframe(self) -> pd.DataFrame:
        """
        Charge tous les fichiers JSON du répertoire, aplatit leur contenu
        et retourne un DataFrame consolidé.
        """
        rows = []

        for file in self.load_json_files():
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Si le fichier contient une liste d’objets
            if isinstance(data, list):
                for item in data:
                    flat = self._flatten(item)
                    flat["filename"] = file.name
                    rows.append(flat)

            # Si le fichier contient un seul objet JSON
            elif isinstance(data, dict):
                flat = self._flatten(data)
                flat["filename"] = file.name
                rows.append(flat)

        return pd.DataFrame(rows)
