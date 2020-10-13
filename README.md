# Friends Recommendation System with Star Wars Social Network

[Kaggle Link](https://www.kaggle.com/sangminyoon/friend-recommendation-system-with-starwars-dataset)

## 1. Project Intro  

Star Wars series is awesome! It is one of the most greatest fictional worlds existing in our culture.  
What if characters in Star Wars used Facebook? What if characters in Star Wars series would be recommended each other?  
Let's make this happen by programming awesome codes!  

I've used Star Wars Social Network dataset on [Kaggle](https://www.kaggle.com/ruchi798/star-wars?select=starwars-episode-2-interactions.json)!  
![image](https://user-images.githubusercontent.com/52681837/95673535-3d127180-0be4-11eb-8edd-01336771077d.png)

## 2. How can we make the system?  
### 1) Preprocessing Data
If you want to preprocess data without reading how it works, just execute preprocessing.sh file like below.

    ./preprocessing.sh


First, we have to consider how data is distributed. There are two files we should deal with.
1) starwars-full-interactions.json.  

This file contains information of the mutual scene.  

  a. Nodes. 
  
    name: Name of the character. 
    value: Number of scenes the character appeared in. 
    colour: Colour in the visualization  
    
  b. Links. 
  
    source: zero-based index of the character that is one end of the link, the order of nodes is the order in which they are listed in the “nodes” element. 
    target: zero-based index of the character that is the the other end of the link.  
    value: Number of scenes where the “source character” and “target character” of the link appeared together.  
2) starwars-full-mentions.json.  

This file contains information of the mention in the scene. Schema is same as above.  

***We make interaction_link_with_weight.edgelist in ./node2vec/dataset/.
After preprocessing, the result will come out like this.***

interaction_link_with_weight.edgelist  
// Start node, end node, # of scenes appearing together  
1 7 1.0  
9 8 3.0  
8 10 1.0  
9 10 3.0  
11 0 22.0  
11 4 12.0  
11 12 2.0  

mention_link_with_weight.edgelist  
// Start node, end node, # of scenes mention from start node to end node  
11 10 1.0  
9 11 7.0  
0 10 2.0  
9 0 9.0  
9 14 7.0  
14 0 16.0  

### 2) Feature Extraction with node2vec  
If you want to extract feature vector without reading how it works, just execute node2vec.sh file like below.

    ./node2vec.sh

Now we can make a graph with .edgelist file. We use this as a input file and push it to the graph using [networkx](https://networkx.github.io/documentation/stable/tutorial.html). 
<img width="328" alt="스크린샷 2020-10-11 오후 7 15 15" src="https://user-images.githubusercontent.com/52681837/95676024-2543e900-0bf6-11eb-94da-e17b5e0e996c.png">

How can we represent Graph as a feature vector? We will use [node2vec](https://cs.stanford.edu/~jure/pubs/node2vec-kdd16.pdf) algorithm.  
We seek to optimize the following objective function, which maximizes the log-probability of observing a network neighborhood NS(u) for a node u conditioned on its feature representation, given by f.  

<img width="197" alt="스크린샷 2020-10-11 오후 7 23 03" src="https://user-images.githubusercontent.com/52681837/95676183-3e996500-0bf7-11eb-8d18-7e5a2c95464b.png">

By setting p, q, we can set return-parameter and in-out parameter.  

<img width="334" alt="스크린샷 2020-10-11 오후 7 24 19" src="https://user-images.githubusercontent.com/52681837/95676201-6092e780-0bf7-11eb-85bf-8612f1020568.png">


### 3) Link Prediction
Please execute network_analysis.ipynb!  

<img width="495" alt="스크린샷 2020-10-13 오후 8 22 55" src="https://user-images.githubusercontent.com/52681837/95854527-0da16780-0d92-11eb-980f-9c09e5a4ac2d.png">

