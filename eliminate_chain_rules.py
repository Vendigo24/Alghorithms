from grammar import Grammar
from algorithm_3 import remove_useless_symbols


def algorithm(g: Grammar):
    c_gr = remove_useless_symbols(g)

    if c_gr is None:
        return None

    new_rule = dict()

    for m_key, m_value in c_gr.P.items():
        chain_rule = set()
        chain_rule.add(m_key)
        temp_chain_rule = set()

        new_rule[m_key] = list()

        while chain_rule != temp_chain_rule:
            temp_chain_rule = chain_rule.copy()
            cop_key = m_key

            for sub1_key, sub1_value in c_gr.P.items():
                for a in sub1_value:
                    if (a in c_gr.N) and (sub1_key == cop_key):
                        cop_key = a
                        chain_rule.add(a)

        check_key = m_key
        temp_check_key = list()
        while check_key != temp_check_key:
            temp_check_key = check_key

            for a in c_gr.P[check_key]:
                if a in chain_rule:
                    check_key = a
                else:
                    new_rule[m_key].append(a)

    new_grammar = Grammar(c_gr.N, c_gr.T, new_rule, c_gr.S)

    return remove_useless_symbols(new_grammar)
