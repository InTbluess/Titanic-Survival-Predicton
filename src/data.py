import seaborn as sns

from src.utils import save_dataset


def load_data():
    df = sns.load_dataset("titanic")

    save_dataset(
        df,
        "raw/titanic_raw.csv"
    )
    return df