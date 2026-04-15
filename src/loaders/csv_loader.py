from pathlib import Path
from typing import Union, List

import pandas as pd

from src.loaders.base_loader import BaseLoader


class CSVLoader(BaseLoader):
    """
    Charge un ou plusieurs fichiers CSV depuis un répertoire
    et les combine en un DataFrame unique.
    """

    def __init__(self, directory: Union[str, Path], pattern: str = "*.csv"):
        """
        Initialise le chargeur avec un répertoire et un motif de sélection.

        Paramètres
        ----------
        directory : str ou Path
            Chemin vers le dossier contenant les fichiers CSV.
        pattern : str
            Motif permettant de filtrer les fichiers (ex: '*.csv', 'train_*.csv').
        """
        self.directory = Path(directory)
        self.pattern = pattern

    def _list_csv_files(self) -> List[Path]:
        """
        Retourne la liste des fichiers CSV correspondant au motif.
        """
        return list(self.directory.glob(self.pattern))

    def to_dataframe(self) -> pd.DataFrame:
        """
        Charge tous les fichiers CSV sélectionnés et les concatène
        en un seul DataFrame. Ajoute une colonne 'filename' pour
        indiquer la provenance de chaque ligne.
        """
        files = self._list_csv_files()

        if not files:
            raise FileNotFoundError(
                f"Aucun fichier CSV trouvé dans {self.directory} avec le motif {self.pattern}"
            )

        dataframes = []

        for file in files:
            df = pd.read_csv(file)
            df["filename"] = file.name
            dataframes.append(df)

        return pd.concat(dataframes, ignore_index=True)
