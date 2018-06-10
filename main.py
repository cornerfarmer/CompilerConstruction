from RegexEvaluator import RegexEvaluator
from RegexParser import RegexParser

parser = RegexParser()

regexs = ["a*", "ab", "a||b", "(a|b)*asdb(a|b)"]
for regex in regexs:
    print(regex, parser.check(regex))

root = parser.parse("(a|b)*a(a|b)")

evaluator = RegexEvaluator(root)
evaluator.draw_nfa()

words = ["a", "aa", "bbb", "bbbabab"]

for key, word in enumerate(words):
    print(word, evaluator.evaluate(word))
    evaluator.draw_dfa("_" + str(key))