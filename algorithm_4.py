from grammar import Grammar


def remove_lambda_rules(old_grammar):
    def find_non_terminals(grammar):

        def find_lambda_non_terminals(sym, _set, path):
            for rule in grammar.P[sym]:
                set_of_sym = grammar.get_ntt_from_rule(rule)[0]
                if not set_of_sym or set_of_sym.issubset(_set):
                    _set.add(sym)
                    return
                set_of_n_in_rule = set_of_sym.intersection(grammar.N)
                for symbol in set_of_n_in_rule.difference(path[sym]):
                    path[sym].add(symbol)
                    find_lambda_non_terminals(symbol, _set, path)
                else:
                    continue

        def find_non_terminals_with_terminals(sym, _set, path):
            for rule in grammar.P[sym]:
                set_of_sym = grammar.get_ntt_from_rule(rule)[0]
                if set_of_sym.intersection(grammar.T.union(_set)):
                    _set.add(sym)
                    return
                set_of_n_in_rule = set_of_sym.intersection(grammar.N)
                for symbol in set_of_n_in_rule.difference(path[sym]):
                    path[sym].add(symbol)
                    find_lambda_non_terminals(symbol, _set, path)
                else:
                    if set_of_sym:
                        _set.add(sym)
                        return

        l_non_terminals = set()
        non_terminals = set()
        rules_path = {key: set() for key in grammar.P.keys()}
        for el in grammar.P:
            find_lambda_non_terminals(el, l_non_terminals, rules_path)
            find_non_terminals_with_terminals(el, non_terminals, rules_path)

        return l_non_terminals, non_terminals

    def find_rules_with_lambda_non_terminals(grammar, set_of_non_terminals):
        return (zip([i_key], [rule]) for i_key, i_value in grammar.P.items() for rule in i_value
                if grammar.get_ntt_from_rule(rule)[0].intersection(set_of_non_terminals))

    def find_rules_without_lambda_non_terminals(grammar, set_of_non_terminals):
        rules = dict()
        for i_key, i_value in grammar.P.items():
            value = [rule for rule in i_value
                     if not grammar.get_ntt_from_rule(rule)[0].intersection(set_of_non_terminals) and set(rule)]
            if len(value) != 0:
                rules[i_key] = value
        return rules

    (non_terminals_l, new_non_terminals) = find_non_terminals(old_grammar)
    rules_with_lambda_non_terminals = find_rules_with_lambda_non_terminals(old_grammar, non_terminals_l)
    rules_without_lambda_non_terminals = find_rules_without_lambda_non_terminals(old_grammar, non_terminals_l)

    for lambda_rule in rules_with_lambda_non_terminals:
        for start, end in lambda_rule:
            symbols = old_grammar.get_ntt_from_rule(end)[0]
            if symbols.issubset(non_terminals_l) and not(symbols.intersection(new_non_terminals)):
                continue
            for elem in symbols.intersection(non_terminals_l.difference(new_non_terminals)):
                end = end.replace(elem, '')
            temp = list()
            if symbols.intersection(new_non_terminals.intersection(non_terminals_l)):
                temp = list({end.replace(elem, '', count)
                             if len(end) != 1 and symbols.intersection(new_non_terminals.intersection(non_terminals_l))
                             else end
                            for elem in symbols.intersection(new_non_terminals.intersection(non_terminals_l))
                            for count in range(end.count(elem) + 1)})
            else:
                temp.append(end)
            if len(temp) != 0:
                if start in rules_without_lambda_non_terminals:
                    rules_without_lambda_non_terminals[start].extend(temp)
                else:
                    rules_without_lambda_non_terminals[start] = temp

    if len(rules_without_lambda_non_terminals) == 0:
        rules_without_lambda_non_terminals[old_grammar.S] = ['']
        new_non_terminals.add(old_grammar.S)
        return Grammar(new_non_terminals, old_grammar.T, rules_without_lambda_non_terminals, old_grammar.S)

    new_axiom = 'S\'' if old_grammar.S in non_terminals_l else old_grammar.S

    if new_axiom not in new_non_terminals:
        rules_without_lambda_non_terminals[new_axiom] = ['', old_grammar.S]
        new_non_terminals.add(new_axiom)

    return Grammar(new_non_terminals.union(non_terminals_l),
                   old_grammar.T,
                   rules_without_lambda_non_terminals,
                   new_axiom)
