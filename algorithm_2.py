from grammar import Grammar


def remove_unreachable_symbols(grammar):
    reachable_symbols = grammar.get_all_reachable_symbols(grammar.S)
    unreachable_symbols = grammar.N.union(grammar.T).difference(reachable_symbols)

    p = dict()
    for key in grammar.P:
        if key not in unreachable_symbols:
            p[key] = grammar.P[key]

    return Grammar(reachable_symbols.intersection(grammar.N), reachable_symbols.intersection(grammar.T), p, grammar.S)
