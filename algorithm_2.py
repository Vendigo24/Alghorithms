from grammar import Grammar


def remove_unreachable_symbols(grammar):
    def get_all_reachable_symbols(s, vv):
        vt = set()

        if not (s in grammar.P):
            return vv

        for rule in grammar.P[s]:
            vt = vt.union(set(rule))

        vt = vt.difference(vv)

        if len(vt) == 0:
            return vv

        vtt = vv.union(vt)
        for symbol in vt:
            vv = vv.union(get_all_reachable_symbols(symbol, vtt))

        return vv

    p = dict()

    reachable_symbols = get_all_reachable_symbols(grammar.S, {grammar.S})
    unreachable_n = grammar.N.difference(reachable_symbols.intersection(grammar.N))
    unreachable_t = grammar.T.difference(reachable_symbols.intersection(grammar.T))
    unreachable_symbols = unreachable_n.union(unreachable_t)

    for key in grammar.P:
        if key in unreachable_symbols:
            continue

        p[key] = grammar.P[key]

    return Grammar(grammar.N.difference(unreachable_n), grammar.T.difference(unreachable_t), p, grammar.S)


def demo():
    g1 = Grammar({"E", "T", "F"}, {"a", "+", "*"}, {"E": ["E+T", "F"], "F": ["(E)", "a"]}, "E")
    g2 = remove_unreachable_symbols(g1)

    print(g1)
    print()
    print(g2)
