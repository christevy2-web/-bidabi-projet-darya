import os
from src.config import DATA_DIR, OUTPUT_DIR
from src.loaders.loader_factory import LoaderFactory
from src.processors.data_processor import DataProcessor
from src.translators.translator import Translator
from src.evaluators.evaluator import Evaluator


def main():
    """
    Main orchestration function for the translation pipeline.
    Steps:
      1. Load input data
      2. Clean/process it
      3. Translate selected column
      4. Save results
      5. Evaluate translation quality
    """

    # --- 1. Resolve input file path ---
    # We explicitly construct the path using the centralized config.
    file_path = os.path.join(DATA_DIR, "sample02.json")

    # Ensure the input file exists before proceeding.
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")

    # --- 2. Load data ---
    loader = LoaderFactory.create(file_path)
    df = loader.to_dataframe()
    print(f"Loaded {len(df)} rows.")

    # --- 3. Clean/process data ---
    processor = DataProcessor(df)
    df = processor.clean()

    # --- 4. Translate ---
    # Using a specific HuggingFace model for FR → EN translation.
    translator = Translator("Helsinki-NLP/opus-mt-fr-en")
    df = translator.translate(df, column="source", new_column="translation")

    # --- 5. Prepare output path ---
    # We do NOT create directories automatically — strict pipeline.
    if not os.path.isdir(OUTPUT_DIR):
        raise RuntimeError(f"Output directory does not exist: {OUTPUT_DIR}")

    output_path = os.path.join(OUTPUT_DIR, "translated.csv")

    # --- 6. Save results ---
    df.to_csv(output_path, index=False)
    print(f"Saved translated file to: {output_path}")

    # --- 7. Evaluate translation quality ---
    evaluator = Evaluator(df)
    scores = evaluator.evaluate()

    print("\n📊 Translation quality metrics:")
    for metric, value in scores.items():
        print(f"  {metric}: {value:.2f}")


if __name__ == "__main__":
    main()
