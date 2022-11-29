class Grammar:
    def __init__(self, n, t, p, s):
        self.N = n
        self.T = t
        self.P = p
        self.S = s

    def __str__(self):
        return "N: " + str(self.N) + "\nT: " + str(self.T) + "\nP: " + str(self.P) + "\nS: " + str(self.S)

    def is_empty(self):
        good_value = set(self.T)
        temp_good_value = set()
        while good_value != temp_good_value:
            temp_good_value = good_value.copy()
            for key, value in self.P.items():
                for a in value:
                    if not set(a).difference(temp_good_value):
                        good_value.add(key)

        if self.S in good_value:

            # нетерминалы составлены из нетерминалов множества "good_value"
            self.N = good_value.intersection(self.N)

            # правила, которые состоят из символов нетерминалов и терминалов
            bad_keys = set()
            for key, value in self.P.items():
                if not key in good_value:
                        bad_keys.add(key)

            # Удаляю ненужные привила
            for key in bad_keys:
                self.P.pop(key)

            return self