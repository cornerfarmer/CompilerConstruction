import pydot

class Transition:
    def __init__(self, start, character, end):
        self.start = start
        self.character = character
        self.end = end

class State:
    def __init__(self, id):
        self.id = id

class Automaton:
    def __init__(self):
        self.states = []
        self.start_states = []
        self.end_states = []
        self.transitions = []

    def set_start_state(self, id):
        self.start_states.append(self.state_by_id(id))

    def set_end_state(self, id):
        self.end_states.append(self.state_by_id(id))

    def state_by_id(self, id):
        for state in self.states:
            if state.id == id:
                return state
        raise IndexError()

    def add_transition(self, start_id, character, end_id):
        self.transitions.append(Transition(self.state_by_id(start_id), character, self.state_by_id(end_id)))

    def generate_dot(self):
        graph = pydot.Dot(graph_type='digraph', rankdir="LR")

        graph.add_node(pydot.Node("start", shape="none", width=0, height=0, margin=0, label=""))

        for state in self.states:
            graph.add_node(pydot.Node(state.id, shape="doublecircle" if state in self.end_states else "circle", label=state.id + 1))

        for state in self.start_states:
            graph.add_edge(pydot.Edge("start", state.id))
        for transition in self.transitions:
            graph.add_edge(pydot.Edge(transition.start.id, transition.end.id, label=transition.character))

        graph.write_png('graph.png')
