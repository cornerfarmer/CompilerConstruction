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

    def state_by_id(self, id, allow_none=False):
        for state in self.states:
            if state.id == id:
                return state
        if allow_none:
            return None
        else:
            raise IndexError(id)

    def follow_once(self, start_state, character):
        for transition in self.transitions:
            if transition.start == start_state and transition.character == character:
                return transition.end
        return None

    def follow_all(self, start_state, character):
        following = set()
        for transition in self.transitions:
            if transition.start == start_state and transition.character == character:
                following.add(transition.end)
        return following

    def ids_from_states(self, states):
        ids = set()
        for state in states:
            ids.add(state.id)
        return ids

    def is_end_state(self, id):
        return self.state_by_id(id) in self.end_states

    def add_transition(self, start_id, character, end_id):
        self.transitions.append(Transition(self.state_by_id(start_id), character, self.state_by_id(end_id)))

    def generate_dot(self, path):
        graph = pydot.Dot(graph_type='digraph', rankdir="LR")

        graph.add_node(pydot.Node("start", shape="none", width=0, height=0, margin=0, label=""))

        for state in self.states:
            if type(state.id) == set:
                label = str({(id + 1) for id in state.id})
            else:
                label = str(state.id + 1)
            graph.add_node(pydot.Node(str(state.id), shape="doublecircle" if state in self.end_states else "circle", label=label))

        for state in self.start_states:
            graph.add_edge(pydot.Edge("start", str(state.id)))
        for transition in self.transitions:
            graph.add_edge(pydot.Edge(str(transition.start.id), str(transition.end.id), label=transition.character))

        graph.write_png(path)
