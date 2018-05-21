
from Automaton import *

class RegexEvaluator:

    def __init__(self, regex_tree):
        self._nfa = self._automaton_from_regex(regex_tree)

        self._dfa = Automaton()
        self._dfa.states.append(State({-1}))
        self._dfa.set_start_state({-1})

    def _automaton_from_regex(self, root):
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

        return graph

    def evaluate(self, word):
        current_state = self._dfa.state_by_id({-1})
        for char in word:
            if self._dfa.follow_once(current_state, char) is None:
                following = set()
                for nfa_id in current_state.id:
                    following |= self._nfa.follow_all(self._nfa.state_by_id(nfa_id), char)
                following = self._nfa.ids_from_states(following)

                if self._dfa.state_by_id(following, True) is None:
                    self._dfa.states.append(State(following))
                    for id in following:
                        if self._nfa.is_end_state(id):
                            self._dfa.set_end_state(following)
                            break
                self._dfa.add_transition(current_state.id, char, following)

            current_state = self._dfa.follow_once(current_state, char)

        return current_state in self._dfa.end_states

    def draw_nfa(self, suffix=""):
        self._nfa.generate_dot('graph_nfa' + suffix + '.png')

    def draw_dfa(self,  suffix=""):
        self._dfa.generate_dot('graph_dfa' + suffix + '.png')