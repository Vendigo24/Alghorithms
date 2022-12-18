from grammar import Grammar


def algorithm(g: Grammar) -> Grammar:
    reachable_symbols = g.get_all_reachable_symbols(g.S)
    unreachable_symbols = g.N.union(g.T).difference(reachable_symbols)

    p = dict()
    for key in g.P:
        if key not in unreachable_symbols:
            p[key] = g.P[key]

    return Grammar(reachable_symbols.intersection(g.N), reachable_symbols.intersection(g.T), p, g.S)
