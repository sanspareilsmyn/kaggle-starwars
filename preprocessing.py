import snap
import json

#Graph = snap.PNGraph.new() # Undirected Network
id_map = dict()
inv_id_map = dict()
link_map = dict()
id_count = 0
link_count = 0

print("Reading json")
with open('dataset/starwars-episode-1-interactions.json', 'r') as f:
    json_data = json.load(f)
#print(json.dumps(json_data))
#print(json.dumps(json_data, indent="\t"))

#a = json_data["nodes"][0]["name"]
#print(len(json_data["nodes"])) #37
#print(len(json_data["links"])) #129

print("Creating name map")
json_node = json_data["nodes"]
for character in json_node:
    id_map[character["name"]] = id_count
    inv_id_map[id_count] = character["name"]
    id_count += 1

#print(id_map)
#print(inv_id_map)

print("Creating link map")
json_link = json_data["links"]
line = open('interaction_link_with_weight.edgelist', 'w')
for character in json_link:
    #print(character) #{'source': 1, 'target': 0, 'value': 1}
    start = character["source"]
    end = character["target"]
    weight = float(character["value"])
    line.write('{} {} {}\n'.format(start, end, weight))
    line.write('{} {} {}\n'.format(end, start, weight))


line.close()

