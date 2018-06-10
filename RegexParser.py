from RegexTree import *

class RegexParser:
    def __init__(self):
        self.word = ""
        self.position = 0
        self.next = ""

    def parse(self, word):
        self.word = word + "$"
        self.position = 0
        self.next = self.word[0]

        tree = self.parseOr()

        if self.next != "$":
            raise Exception()

        return tree

    def check(self, word):
        try:
            self.parse(word)
        except:
            return False
        return True

    def parseOr(self):
        left = self.parseConcat()

        while self.next == "|":
            self.consume()
            right = self.parseConcat()
            left = Or(left, right)

        return left

    def parseConcat(self):
        left = self.parseStar()

        while self.next.isalnum() or self.next == "(":
            right = self.parseStar()
            left = Concat(left, right)

        return left

    def parseStar(self):
        inner = self.parseTerm()

        while self.next == "*":
            self.consume()
            inner = Star(inner)

        return inner

    def parseTerm(self):
        if self.next == "(":
            self.consume()
            inner = self.parseOr()
            if self.next == ")":
                self.consume()
            else:
                raise Exception()
            return inner
        elif self.next.isalnum():
            return self.consume()
        else:
            raise Exception()

    def consume(self):
        letter = Letter(self.next)
        self.position += 1
        self.next = self.word[self.position]
        return letter