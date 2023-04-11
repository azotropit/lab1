import numpy as np

f = open("l1_2.txt")

graph = []
nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
tree = []
for line in f:
    graph.append(line.split())
f.close()

graph.pop(0)
x = np.array(graph)
for i in range(1, 100):
    smallest_index = list(zip(*np.where(x == str(i))))
    if smallest_index:
        line = []
        for t in range(2):
            line.append(nodes[smallest_index[0][t]])
 # discover how many times each element is already in array (should be less than 2 to append)
        if sum([i.count(line[0]) for i in tree]) < 2 and sum([i.count(line[1])
for i in tree]) < 2:
            tree.append(line)
print("Мінімальне остове дерево включає в себе наступні дуги:\n", tree)