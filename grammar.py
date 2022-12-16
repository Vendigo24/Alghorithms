from copy import deepcopy


class Grammar:
    def __init__(self, n: set, t: set, p: dict[str, list[str]], s: str):
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
                    if not Grammar.get_ntt_from_rule(a)[0].difference(temp_good_value) and a != '':
                        good_value.add(key)

        if self.S in good_value:
            new_grammar = Grammar(self.N, self.T, deepcopy(self.P), self.S)
            # нетерминалы составлены из нетерминалов множества "good_value"
            new_grammar.N = good_value.intersection(new_grammar.N)

            # правила, которые состоят из символов нетерминалов и терминалов
            bad_keys = set()
            for key, value in new_grammar.P.items():
                if key not in good_value:
                    bad_keys.add(key)

            # Удаляю ненужные привила
            for key in bad_keys:
                new_grammar.P.pop(key)

            copy_new_grammar = new_grammar.P.copy()

            for key, value in copy_new_grammar.items():
                for a in value:
                    if Grammar.get_ntt_from_rule(a)[0].intersection(bad_keys):
                        new_grammar.P[key].remove(a)

            return self.S in good_value, new_grammar
        else:
            return False, None

    def get_all_reachable_symbols(self, start_symbol):
        """ Get all symbols reachable from start_symbol in that grammar. """
        all_reachable_symbols = set(start_symbol)
        reachable_symbols = list(start_symbol)

        i = 0
        while i < len(reachable_symbols):
            if reachable_symbols[i] in self.P:
                symbols_reachable_from_rule = set()
                for rule in self.P[reachable_symbols[i]]:
                    symbols_reachable_from_rule = symbols_reachable_from_rule.union(Grammar.get_ntt_from_rule(rule)[0])

                raw_symbols = symbols_reachable_from_rule.difference(all_reachable_symbols)
                if len(raw_symbols) > 0:
                    reachable_symbols.extend(raw_symbols)
                    all_reachable_symbols = all_reachable_symbols.union(raw_symbols)
            i += 1

        return all_reachable_symbols

    @staticmethod
    def get_ntt_from_rule(rule):
        """ Return set and list with all non-terminals and terminals from rule, include non-terminals like X' """
        non_terminals_terminals_from_rule = list()

        i = 0
        rule_len = len(rule)
        while i < rule_len:
            if rule[i] == "<":
                j = i + 1
                while rule[j] != ">":
                    j += 1
                    if j == rule_len:
                        raise NameError('No ">" character closing the "<" character in rule')
                non_terminals_terminals_from_rule.append(rule[i:j + 1])
                i = j + 1
            else:
                # Считаем запись вида X' - корректной
                if i + 1 < rule_len and rule[i + 1] == "'":
                    non_terminals_terminals_from_rule.append(rule[i] + rule[i + 1])
                    i += 1
                else:
                    non_terminals_terminals_from_rule.append(rule[i])
                i += 1
        return set(non_terminals_terminals_from_rule), non_terminals_terminals_from_rule
