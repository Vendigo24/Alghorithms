class Grammar:
    def __init__(self, n, t, p, s):
        self.N = n
        self.T = t
        self.P = p
        self.S = s

    def __str__(self):
        return "N: " + str(self.N) + "\nT: " + str(self.T) + "\nP: " + str(self.P) + "\nS: " + str(self.S)
