from grammar import Grammar
import unittest
import algorithm_2


class U(unittest.TestCase):
    def setUp(self):
        self.needed_grammar = Grammar({"E", "T", "F"}, {"a", "+"},
                             {"E": ["E+T", "TF"], "T": ["T", "F"], "F": ["F", "a"]}, "E")

    def test_1_no_changes(self):
        tested_grammar = Grammar({"E", "T", "F"}, {"a", "+"},
                     {"E": ["E+T", "TF"], "T": ["T", "F"], "F": ["F", "a"]}, "E")

        self.assertEqual(algorithm_2.remove_unreachable_symbols(tested_grammar), self.needed_grammar)

    def test_2_unreachable_non_terminals(self):
        g1 = Grammar({"E", "T", "J", "F"}, {"a", "+"},
                     {"E": ["E+T", "TF"], "T": ["T", "F"], "F": ["F", "a"], "J":["J"]}, "E")

        self.assertEqual(algorithm_2.remove_unreachable_symbols(g1), self.needed_grammar)

    def test_3_unreachable_terminals(self):
        g2 = Grammar({"E", "T", "F"}, {"a", "+", "d"},
                     {"E": ["E"], "T": ["T", "F"], "F": ["F", "a"]}, "E")

        g_needed2 = Grammar({"E"}, set(),
                     {"E": ["E"]}, "E")

        self.assertEqual(algorithm_2.remove_unreachable_symbols(g2), g_needed2)
