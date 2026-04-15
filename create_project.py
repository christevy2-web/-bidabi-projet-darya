import os
from pathlib import Path


PROJECT_STRUCTURE = {
    "src": [
        "loaders",
        "processors",
        "translators",
        "evaluators",
        "orchestrator"
    ],
    "data": [],
    "output": [],
    "tests": []
}


def create_project_structure(base_path: str = "."):
    base = Path(base_path)

    for folder, subfolders in PROJECT_STRUCTURE.items():
        folder_path = base / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        for sub in subfolders:
            sub_path = folder_path / sub
            sub_path.mkdir(parents=True, exist_ok=True)

    # создаём пустые __init__.py
    for root, dirs, files in os.walk(base / "src"):
        for d in dirs:
            init_file = Path(root) / d / "__init__.py"
            init_file.touch()

    print("Структура проекта создана.")


if __name__ == "__main__":
    create_project_structure()
