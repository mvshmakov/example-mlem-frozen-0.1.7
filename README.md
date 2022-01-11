# Getting Started

This is Getting Started example to showcase MLEM usage.

Repo has three branches:
- `main`: produced by `dvc repro`, models artifacts are stored with DVC
- `small-forest`: we make an experiment with `dvc exp` on the `main` branch and create this branch
- `no-dvc`: produced by `bash run.sh`, this branch has model artifacts pushed straight to Git

You can examine [run.sh](run.sh) for pipeline commands or run `dvc repro` on [dvc.yaml](dvc.yaml), which has the same outcome as `run.sh`, except that with `dvc repro` artifacts are stored with DVC.

If you want to reproduce the example from clean state, remove `data/`, `.mlem/` and `scores.json` first.

# Installation

**1. Fork / Clone this repository**

```bash
git clone git@github.com:iterative/example-mlem.git
cd example-mlem
```

**2. Create virtual environment named `venv`**
```bash
python3 -m venv venv
source venv/bin/activate
```
Install python libraries

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

**3. Run**

```bash
dvc repro
```

or:

```bash
chmod +x run.sh
./run.sh
```
