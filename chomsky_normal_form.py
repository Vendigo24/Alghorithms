from grammar import Grammar
import eliminate_chain_rules
import algorithm_3
import algorithm_4


def algorithm(g: Grammar):
    def add_rule(p: dict, key, rule):
        if key in p and rule not in p[key]:
            p[key].append(rule)
        else:
            p[key] = list()
            p[key].append(rule)

    g = algorithm_3.remove_useless_symbols(g)
    g = eliminate_chain_rules.algorithm(g)

    if g is None:
        return None

    g = algorithm_4.remove_lambda_rules(g)

    new_rules = dict()

    for key, rules in g.P.items():
        for rule in rules:
            # Получаем составные части правила (это нетерминалы + терминалы)
            rule_parts = Grammar.get_ntt_from_rule(rule)

            if len(rule_parts[1]) == 1:
                add_rule(new_rules, key, rule)
            else:
                n_count = 0
                no_terminals = True

                for part in rule_parts[1]:
                    if part in g.N:
                        n_count += 1
                    else:
                        no_terminals = False
                        break

                if n_count == 2 and no_terminals:
                    add_rule(new_rules, key, rule)
                else:
                    # начинается веселье
                    parts = rule_parts[1]
                    old_key = key
                    i = 0
                    while i < len(parts) - 1:
                        if (len(parts) - i) > 2:
                            new_rule = str(parts[i])
                            # Если это терминал, то штрихуем его
                            if parts[i] in g.T:
                                new_rule += "'"
                                add_rule(new_rules, new_rule, parts[i])

                            # Берем оставшееся как один нетерминал
                            second_part = f"<{''.join(parts[i+1:])}>"
                            new_rule += second_part

                            add_rule(new_rules, old_key, new_rule)

                            old_key = second_part
                        else:
                            new_rule = str()
                            # У нас осталось два "символа"
                            for temp_part in parts[i:]:
                                if temp_part in g.T:
                                    new_rule += temp_part + "'"
                                    add_rule(new_rules, temp_part + "'", temp_part)
                                else:
                                    new_rule += temp_part
                            add_rule(new_rules, old_key, new_rule)
                        i += 1

    return Grammar(g.N.union(new_rules.keys()), g.T, new_rules, g.S)
