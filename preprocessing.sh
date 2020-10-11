#!/bin/bash

echo "Preprocessing Star Wars Data into Edgelist!"
python3 preprocessing.py

echo " "

echo "Done preprocessing data!"

mv interaction_link_with_weight.edgelist ./node2vec/dataset/
mv mentions_link_with_weight.edgelist ./node2vec/dataset/

cd ./node2vec