from grammar import Grammar


def is_empty(grammar):
    good_value = set(grammar.T)
    temp_good_value = set()
    while good_value != temp_good_value:
        temp_good_value = good_value.copy()
        for key, value in grammar.P.items():
            for a in value:
                if not set(a).difference(temp_good_value):
                    good_value.add(key)

    if grammar.S in good_value:
        return grammar


def demo():
    g1 = Grammar({"E", "T", "J", "F"}, {"a", "+", "*", "d"}, {"E": ["E+T", "TF"], "T": ["T", "F"], "F": ["F", "a"]}, "E")
    print(is_empty(g1))
