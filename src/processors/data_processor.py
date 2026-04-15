import pandas as pd


class DataProcessor:
    """
    Effectue des opérations de nettoyage et de prétraitement sur les données.
    """

    def __init__(self, df: pd.DataFrame):
        """
        Initialise le processeur avec un DataFrame.
        """
        self.df = df

    def clean(self) -> pd.DataFrame:
        """
        Nettoie les colonnes principales :
        - suppression des lignes incomplètes
        - suppression des espaces superflus
        """
        df = self.df.copy()
        df = df.dropna(subset=["source", "reference"])
        df["source"] = df["source"].str.strip()
        df["reference"] = df["reference"].str.strip()
        return df
