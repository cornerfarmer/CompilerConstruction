from RegexEvaluator import RegexEvaluator
from RegexTree import *

root = Concat(Star(Or(Letter('a'), Letter('b'))),
              Concat(Letter('a'), Or(Letter('a'), Letter('b'))))

evaluator = RegexEvaluator(root)
evaluator.draw_nfa()

words = ["a", "aa", "bbb", "bbbabab"]

for key, word in enumerate(words):
    print(word, evaluator.evaluate(word))
    evaluator.draw_dfa("_" + str(key))