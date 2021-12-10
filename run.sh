#!/bin/sh
set -exu

echo Create .mlem dir in the current folder
mlem init

echo Generating data
python src/generate_data.py

echo Training
python src/train.py data/train models/iris-classifier

echo Linking
mlem link models/iris-classifier latest

echo Listing models
mlem ls model

echo Predicting
mlem apply latest data/test_x -m predict_proba -o data/pred

echo Scoring
python src/score.py data/pred data/test_y scores.json

echo "Completed!"
