from treelib import Node, Tree

class Valve:
    def __init__(self, name,flow_rate, neighbors):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors
        self.is_open = False
    def add_neighbor(self,neighbor):
        self.neighbors += [neighbor]
        return None
    def open_valve(self):
        self.is_open = True

# input parsing
input_file = 'day17\input.txt'
with open(input_file) as infile:
    lines = [line.strip() for line in infile]

tree = Tree()
valves = {}
lines = [line.replace('Valve ','').replace(' has flow rate=',',').split(';') for line in lines]
lines = [[line[0].split(','),line[1].split(',')] for line in lines]
for idx in range(len(lines)):
    lines[idx][1][0] = lines[idx][1][0].split(' ')[5]
    name = lines[idx][0][0]
    flow_rate = int(lines[idx][0][1])
    neighbors = [elem.replace(' ','') for elem in lines[idx][1] if len(elem) == 2]
    valves[name] = Valve(name,flow_rate,neighbors)
    tree.create_node("name",)
# replace valve neighbors with the real valves
for name in valves:
    valves[name].neighbors = [valves[neighbor_name] for neighbor_name in valves[name].neighbors]
print(valves)




tree.create_node("Harry", "harry")  # No parent means its the root node
tree.create_node("Jane",  "jane"   , parent="harry")
tree.create_node("Bill",  "bill"   , parent="harry")
tree.create_node("Diane", "diane"  , parent="jane")
tree.create_node("Mary",  "mary"   , parent="diane")
tree.create_node("Mark",  "mark"   , parent="jane")
tree.show()