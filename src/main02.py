import os
from src.config import DATA_DIR, OUTPUT_DIR
from src.loaders.json_loader import JsonLoader
from src.processors.data_processor import DataProcessor


def main():
    """
    Intermediate pipeline:
      1. Load a specific JSON file
      2. Clean/process the data
      3. Save the cleaned intermediate result
    """

    # --- 1. Resolve input directory ---
    input_dir = DATA_DIR

    if not os.path.isdir(input_dir):
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    # --- 2. Load only the target JSON file ---
    # JsonLoader supports filtering via pattern
    loader = JsonLoader(input_dir, pattern="sample02.json")
    df = loader.to_dataframe()

    print("After loading:")
    print(df.head(20))

    # --- 3. Clean/process data ---
    processor = DataProcessor(df)
    df = processor.clean()

    print("After cleaning:")
    print(df.head(20))

    # --- 4. Prepare output path ---
    if not os.path.isdir(OUTPUT_DIR):
        raise RuntimeError(f"Output directory does not exist: {OUTPUT_DIR}")

    output_path = os.path.join(OUTPUT_DIR, "02_cleaned.csv")

    # --- 5. Save cleaned result ---
    df.to_csv(output_path, index=False)
    print(f"File saved to: {output_path}")


if __name__ == "__main__":
    main()
