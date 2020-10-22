# Aufgabe:  Binärbaum implementieren

class Baum:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_right(self):
        return self.right

    def set_left(self, new_left):
        self.left = new_left
        return new_left

    def get_left(self):
        return self.left

    def set_right(self, new_right):
        self.right = new_right
        return new_right


    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


def create_tree() -> Baum:
    root = Baum(15)
    l = root.set_left(Baum(5))
    r = root.set_right(Baum(16))

    ll = l.set_left(Baum(3))
    lr = l.set_right(Baum(12))
    rr = r.set_right(Baum(20))

    lrl = lr.set_left(Baum(10))
    lrr = lr.set_right(Baum(13))
    rrl = rr.set_left(Baum(18))
    rrr = rr.set_right(Baum(23))

    lrll = lrl.set_left(Baum(6))

    lrllr = lrll.set_right(Baum(7))