from abc import ABC, abstractmethod
import pandas as pd


class BaseLoader(ABC):
    """
    Classe abstraite définissant l'interface commune à tous les chargeurs de données.
    Chaque sous-classe doit implémenter la méthode `to_dataframe`.
    """

    @abstractmethod
    def to_dataframe(self) -> pd.DataFrame:
        """
        Charge les données et retourne un objet pandas.DataFrame.
        """
        pass
