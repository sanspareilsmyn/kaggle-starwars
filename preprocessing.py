import json

id_map = dict()
inv_id_map = dict()
id_count = 0

print("Reading json")
with open('dataset/starwars-full-interactions.json', 'r') as f:
    json_data = json.load(f)

print("----- Creating Interaction Edgelist -----")
print("Creating name map")
json_node = json_data["nodes"]
for character in json_node:
    id_map[character["name"]] = id_count
    inv_id_map[id_count] = character["name"]
    id_count += 1

print("Creating edges with weight")
json_link = json_data["links"]
line = open('interaction_link_with_weight.edgelist', 'w')
for character in json_link:
    start = character["source"]
    end = character["target"]
    weight = float(character["value"])
    line.write('{} {} {}\n'.format(start, end, weight))
line.close()
print('Interaction Edgelist is created!')

#######################################################################
print("----- Creating Mentions Edgelist -----")

id_map_m_unordered = dict()
inv_id_map_m_unordered = dict()
id_map_m = dict()
inv_id_map_m = dict()
id_count_m = 0

with open('dataset/starwars-full-mentions.json', 'r') as f:
    json_data_m = json.load(f)
print("Creating name map")
json_node_m = json_data_m["nodes"]
for character in json_node_m:
    if character["name"] in id_map:
        id_map_m[character["name"]] = id_map[character["name"]]
        inv_id_map_m[id_map[character["name"]]] = character["name"]

        id_map_m_unordered[character["name"]] = id_count_m
        inv_id_map_m_unordered[id_count_m] = character["name"]
        id_count_m += 1

print("Creating edges with weight")
json_link_m = json_data_m["links"]
line = open('mentions_link_with_weight.edgelist', 'w')

for character in json_link_m:
    if character["source"] < len(id_map) and character["target"] < len(id_map):
        start = id_map[inv_id_map_m_unordered[character["source"]]]
        end = id_map[inv_id_map_m_unordered[character["target"]]]
        weight = float(character["value"])
        line.write('{} {} {}\n'.format(start, end, weight))
line.close()

print('Mentions Edgelist is created!')
# Create id_map.json, inv_id_map.json
json_file = json.dumps(id_map)
f = open("id_map.json","w")
f.write(json_file)
f.close()
print('ID Map is Created!')

json_file = json.dumps(inv_id_map)
f = open("inv_id_map.json","w")
f.write(json_file)
f.close()
print('Inv Map is Created!')
