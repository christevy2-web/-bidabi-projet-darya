import os
from src.config import DATA_DIR, OUTPUT_DIR
from src.loaders.json_loader import JsonLoader


def main():
    """
    Simple data-loading pipeline.
    Steps:
      1. Initialize JSON loader
      2. Load data into a DataFrame
      3. Preview the first rows
      4. Save the loaded data to the output directory
    """

    # --- 1. Resolve input directory ---
    # We explicitly construct the path using centralized config.
    input_dir = DATA_DIR

    if not os.path.isdir(input_dir):
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    # --- 2. Create loader and load data ---
    loader = JsonLoader(input_dir)
    df = loader.to_dataframe()

    print("Preview of the loaded DataFrame:")
    print(df.head())

    # --- 3. Prepare output path ---
    if not os.path.isdir(OUTPUT_DIR):
        raise RuntimeError(f"Output directory does not exist: {OUTPUT_DIR}")

    output_path = os.path.join(OUTPUT_DIR, "01_loaded.csv")

    # --- 4. Save result ---
    df.to_csv(output_path, index=False)
    print(f"File saved to: {output_path}")


if __name__ == "__main__":
    main()
