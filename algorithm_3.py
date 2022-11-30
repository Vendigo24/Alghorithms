from algorithm_2 import remove_unreachable_symbols


def remove_useless_symbols(old_grammar):
    (is_empty, grammar) = old_grammar.is_empty()
    if is_empty:
        return remove_unreachable_symbols(grammar)
