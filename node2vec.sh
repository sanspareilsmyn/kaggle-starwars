#!/bin/bash

echo "Training Node2Vec Graph!"

cd ./node2vec/src

python3 main.py --input ../dataset/interaction_link_with_weight.edgelist --output ../output/interaction_feat.txt --dimensions 15 --walk-length 5 --weighted
python3 main.py --input ../dataset/mentions_link_with_weight.edgelist --output ../output/mentions_feat.txt --dimensions 15 --walk-length 5 --weighted
echo " "

echo "Done Creating feature vector by .emb file!"

python3 aggregation.py

echo "Interaction Features and Mentions Features are combined!"

