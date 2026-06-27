import joblib
from pathlib import Path

def save_model(model):
    save_dir = Path("models/trained")
    file_name = "best_model.pkl"
    save_dir.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        model,
        save_dir / file_name
    )

    print(f"Model Saved: {save_dir}\{file_name}")