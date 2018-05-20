from RegexTree import *
from Automaton import *

root = Concat(Star(Or(Letter('a'), Letter('b'))),
              Concat(Letter('a'), Or(Letter('a'), Letter('b'))))

leafs = root.leaf_nodes()

graph = Automaton()
graph.states.append(State(-1))
for leaf in leafs:
    graph.states.append(State(leaf.id))

graph.set_start_state(-1)

for node in root.last():
    graph.set_end_state(node.id)

if root.empty():
    graph.set_end_state(-1)

for node in root.first():
    graph.add_transition(-1, node.character, node.id)

for leaf in leafs:
    for node in leaf.next():
        graph.add_transition(leaf.id, node.character, node.id)

graph.generate_dot()
