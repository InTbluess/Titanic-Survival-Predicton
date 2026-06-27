def engineer_features(df):
    df = df.copy()
    df["family_size"] = (
        df["sibsp"] +
        df["parch"] +
        1
    )

    df["is_alone"] = (
        df["family_size"] == 1
    ).astype(int)

    df["fare_per_person"] = (
        df["fare"] /
        df["family_size"]
    )

    # print("AFTER: ")
    # print(df.head())

    # print(df.info())

    # print(df.isnull().sum())
    # print(df.types)

    return df