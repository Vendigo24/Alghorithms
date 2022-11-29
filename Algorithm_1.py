from grammar import Grammar

#TODO вернуть новую грамматику, которая
# 1. нетерминалы составлены из нетерминалов множества "good_value"
# 2. терминалы старой грамматики
# 3. правила, которые состоят из символов нетерминалов и терминалов
# 4. аксиома старой грамматики
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
