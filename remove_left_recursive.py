from grammar import Grammar
from grammar_misc import add_rule
from copy import deepcopy
import eliminate_chain_rules
import algorithm_3
import algorithm_4


def algorithm(g: Grammar) -> Grammar | None:
    # TODO Дождаться других алгоритмов и поправить с 17 по 23 строки
    g = algorithm_3.remove_useless_symbols(g)

    if g is None:
        return None

    g = eliminate_chain_rules.algorithm(g)
    # g = algorithm_4.remove_lambda_rules(g)

    nt = list(g.P.keys())
    i = 0

    new_rules = deepcopy(g.P)

    while True:
        # Проверяем наличие непосредственной левой рекурсии
        left_recurse = list()
        temp_rules = new_rules[nt[i]].copy()
        new_rules[nt[i]] = list()

        for rule in temp_rules:
            temp = Grammar.get_ntt_from_rule(rule)
            if temp[1][0] == nt[i]:
                left_recurse.append(rule)
            else:
                add_rule(new_rules, nt[i], rule)

        if len(left_recurse) > 0:
            temp_rules = new_rules[nt[i]].copy()
            for normal_rule in temp_rules:
                add_rule(new_rules, nt[i], normal_rule + nt[i] + "'")
            for left_rule in left_recurse:
                temp = Grammar.get_ntt_from_rule(left_rule)
                add_rule(new_rules, nt[i] + "'", ''.join(temp[1][1:]))
                add_rule(new_rules, nt[i] + "'", ''.join(temp[1][1:]) + nt[i] + "'")
            pass

        if i == len(nt) - 1:
            break

        i += 1
        # Для цикла с постусловием j = -1
        j = -1

        while j != i - 1:
            j += 1

            temp_rules = new_rules[nt[i]].copy()
            new_rules[nt[i]] = list()

            # Проверяем наличие сквозной левой рекурсии
            for rule in temp_rules:
                temp = Grammar.get_ntt_from_rule(rule)
                if temp[1][0] == nt[j]:
                    for rule_temp in new_rules[nt[j]]:
                        new_rule = rule_temp
                        if len(temp[1]) > 1:
                            new_rule += ''.join(temp[1][1:])
                        add_rule(new_rules, nt[i], new_rule)
                else:
                    add_rule(new_rules, nt[i], rule)
    return Grammar(g.N.union(new_rules.keys()), g.T, new_rules, g.S)
