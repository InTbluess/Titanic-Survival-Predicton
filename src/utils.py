from pathlib import Path

# Save Dataset before & after processes
def save_dataset(df, filepath):

    filepath = Path("data") / filepath

    filepath.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        filepath,
        index=False
    )

    print(f"Saved: {filepath}")

