from pathlib import Path

from src.loaders.json_loader import JsonLoader
from src.loaders.csv_loader import CSVLoader


class LoaderFactory:
    """
    Fabrique orientée objet permettant de sélectionner
    dynamiquement le chargeur approprié.
    """

    @classmethod
    def create(cls, path: str, pattern: str = None):
        """
        Crée un chargeur en fonction du chemin fourni.

        Paramètres
        ----------
        path : str
            Chemin vers un fichier ou un dossier.
        pattern : str
            Motif optionnel pour filtrer les fichiers.

        Retourne
        --------
        BaseLoader
            Une instance du chargeur approprié.
        """
        p = Path(path)

        # --- Cas 1 : chemin vers un fichier ---
        if p.is_file():
            ext = p.suffix.lower()
            if ext == ".json":
                return JsonLoader(p.parent, pattern=p.name)
            if ext == ".csv":
                return CSVLoader(p.parent, pattern=p.name)
            raise ValueError(f"Extension non supportée : {ext}")

        # --- Cas 2 : chemin vers un dossier ---
        if p.is_dir():
            json_files = list(p.glob("*.json"))
            csv_files = list(p.glob("*.csv"))

            if pattern:
                if pattern.endswith(".json"):
                    return JsonLoader(p, pattern)
                if pattern.endswith(".csv"):
                    return CSVLoader(p, pattern)
                raise ValueError(f"Motif non supporté : {pattern}")

            if json_files and not csv_files:
                return JsonLoader(p)
            if csv_files and not json_files:
                return CSVLoader(p)

            raise ValueError(
                "Impossible de choisir automatiquement : "
                "le dossier contient plusieurs types de fichiers."
            )

        raise FileNotFoundError(f"Chemin introuvable : {path}")
