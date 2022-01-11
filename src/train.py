import sys

import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from mlem.api import load, save


def main():
    params = yaml.safe_load(open("params.yaml"))["train"]

    if len(sys.argv) != 4:
        sys.stderr.write("Arguments error. Usage:\n")
        sys.stderr.write("\tpython train.py features model\n")
        sys.exit(1)

    input = sys.argv[1]
    output1 = sys.argv[2]
    output2 = sys.argv[3]
    seed = params["seed"]
    n_est = params["n_est"]
    min_split = params["min_split"]

    df: pd.DataFrame = load(input)
    x = df.drop("target", axis=1)
    labels = df.target

    sys.stderr.write("Input matrix size {}\n".format(df.shape))
    sys.stderr.write("X matrix size {}\n".format(x.shape))
    sys.stderr.write("Y matrix size {}\n".format(labels.shape))

    clf = RandomForestClassifier(
        n_estimators=n_est,
        min_samples_split=min_split,
        n_jobs=2,
        random_state=seed,
    )
    clf.fit(x, labels)

    clf2 = LogisticRegression()
    clf2.fit(x, labels)

    save(clf, output1, tmp_sample_data=x, external=True, tags=["random-forest", "classifier"])
    save(clf2, output2, tmp_sample_data=x, external=True, tags=["logistic-regression", "classifier"])


if __name__ == "__main__":
    main()
