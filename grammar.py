from copy import deepcopy


class Grammar:
    def __init__(self, n, t, p, s):
        self.N = n
        self.T = t
        self.P = p
        self.S = s

    def __eq__(self, other):
        def compare_rules(rules1, rules2):
            for key, value in rules1.items():
                if rules2.get(key) is None:
                    return False
                if sorted(rules1[key]) != sorted(rules2[key]):
                    return False
            return True

        return self.N == other.N \
            and self.T == other.T \
            and compare_rules(self.P, other.P) \
            and self.S == other.S

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
            new_grammar = Grammar(self.N, self.T, deepcopy(self.P), self.S)
            # нетерминалы составлены из нетерминалов множества "good_value"
            new_grammar.N = good_value.intersection(new_grammar.N)

            # правила, которые состоят из символов нетерминалов и терминалов
            bad_keys = set()
            for key, value in new_grammar.P.items():
                if not key in good_value:
                    bad_keys.add(key)

            # Удаляю ненужные привила
            for key in bad_keys:
                new_grammar.P.pop(key)

            copy_new_grammar = new_grammar.P.copy()

            for key, value in copy_new_grammar.items():
                for a in value:
                    if set(a).intersection(bad_keys):
                        new_grammar.P[key].remove(a)

            return self.S in good_value, new_grammar
        else:
            return False
