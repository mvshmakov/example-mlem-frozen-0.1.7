import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from mlem.api import save


def main():
    data: pd.DataFrame
    data, y = load_iris(return_X_y=True, as_frame=True)
    data["target"] = y
    train_data, test_data = train_test_split(data, random_state=42)
    save(train_data, "data/train", external=True)
    save(test_data.drop("target", axis=1), "data/test_x", external=True)
    save(test_data[["target"]], "data/test_y", external=True)


if __name__ == "__main__":
    main()
