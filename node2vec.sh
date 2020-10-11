#!/bin/bash

echo "Training Node2Vec Graph!"

cd ./node2vec/src

python3 main.py --input ../dataset/interaction_link_with_weight.edgelist --output ../output/starwars_linkfeat2.txt --dimensions 30 --walk-length 5 --weighted

echo " "

echo "Done Creating feature vector by .emb file!"


