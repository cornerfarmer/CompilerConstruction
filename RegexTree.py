class RegexTree:

    def __init__(self):
        self.parent = None
        pass

    def leaf_nodes(self):
        raise NotImplementedError

    def empty(self):
        raise NotImplementedError

    def first(self):
        raise NotImplementedError

    def last(self):
        raise NotImplementedError

    def next_for_child(self, child):
        raise NotImplementedError

    def next(self):
        return set() if self.parent is None else self.parent.next_for_child(self)

class Epsilon(RegexTree):

    def empty(self):
        return True

    def first(self):
        raise set()

    def last(self):
        raise set()

class Letter(RegexTree):
    next_id = 0

    def __init__(self, character):
        super().__init__()
        self.character = character
        self.id = Letter.next_id
        Letter.next_id += 1

    def leaf_nodes(self):
        return [self]

    def empty(self):
        return False

    def first(self):
        return {self}

    def last(self):
        return {self}

class Concat(RegexTree):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        left.parent = self
        self.right = right
        right.parent = self

    def leaf_nodes(self):
        return self.left.leaf_nodes() + self.right.leaf_nodes()

    def empty(self):
        return self.left.empty() and self.right.empty()

    def first(self):
        return self.left.first() | self.right.first() if self.left.empty() else self.left.first()

    def last(self):
        return self.left.last() | self.right.last() if self.right.empty() else self.right.last()

    def next_for_child(self, child):
        if child is self.left:
            return self.right.first() | self.next() if self.right.empty() else self.right.first()
        else:
            return self.next()

class Or(RegexTree):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        left.parent = self
        self.right = right
        right.parent = self

    def leaf_nodes(self):
        return self.left.leaf_nodes() + self.right.leaf_nodes()

    def empty(self):
        return self.left.empty() or self.right.empty()

    def first(self):
        return self.left.first() | self.right.first()

    def last(self):
        return self.left.last() | self.right.last()

    def next_for_child(self, child):
        return self.next()

class Star(RegexTree):
    def __init__(self, r):
        super().__init__()
        self.r = r
        r.parent = self

    def leaf_nodes(self):
        return self.r.leaf_nodes()

    def empty(self):
        return True

    def first(self):
        return self.r.first()

    def last(self):
        return self.r.last()

    def next_for_child(self, child):
        return self.r.first() | self.next()
