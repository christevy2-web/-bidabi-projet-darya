import os
import sys
from pathlib import Path

# Cette ligne est CRUCIALRE pour Python 3.14 : elle ajoute la racine au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Maintenant, utilise les imports avec "src."
from src.config import DATA_DIR, OUTPUT_DIR
from src.loaders.loader_factory import LoaderFactory
from src.processors.data_processor import DataProcessor
from src.translators.translator import Translator
from src.evaluators.evaluator import Evaluator

class Orchestrator:
    """
    High-level orchestrator for the full translation pipeline.
    """

    def __init__(
        self, data_path: str, output_dir: str, translation_model: str, metric: str
    ):
        # Build full input path
        self.input_path = os.path.join(DATA_DIR, data_path)

        # Store parameters
        self.output_dir = Path(output_dir)
        self.model_name = translation_model
        self.metric = metric

        # Validate input file
        if not os.path.isfile(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")

        # Validate output directory
        if not os.path.isdir(self.output_dir):
            raise RuntimeError(f"Output directory does not exist: {self.output_dir}")

    def run(self):
        # --- 1. Load ---
        loader = LoaderFactory.create(self.input_path)
        df = loader.to_dataframe()
        df.to_csv(self.output_dir / "01_loaded.csv", index=False)

        # --- 2. Clean ---
        processor = DataProcessor(df)
        df = processor.clean()
        df.to_csv(self.output_dir / "02_cleaned.csv", index=False)

        # --- 3. Translate ---
        translator = Translator(self.model_name)
        df = translator.translate(df, column="source", new_column="translation")
        df.to_csv(self.output_dir / "03_translated.csv", index=False)

        # --- 4. Evaluate ---
        evaluator = Evaluator(df)
        scores = evaluator.evaluate()

        print("\n📊 Translation quality metrics:")
        for metric, value in scores.items():
            print(f"  {metric}: {value:.2f}")

        print("\nPipeline completed.")


if __name__ == "__main__":
    orch = Orchestrator(
        data_path="big.csv",
        output_dir="output",
        translation_model="Helsinki-NLP/opus-mt-fr-en",
        metric="bleu",
    )
    orch.run()