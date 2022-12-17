from grammar import Grammar
import unittest
import remove_unreachable_symbols
import chomsky_normal_form

class RemoveUnreachableSymbols(unittest.TestCase):
    def setUp(self):
        self.needed_grammar = Grammar({"E", "T", "F"},
                                      {"a", "+"},
                                      {
                                          "E": ["E+T", "TF"],
                                          "T": ["T", "F"],
                                          "F": ["F", "a"]
                                      },
                                      "E")

    def test_1_no_changes(self):
        tested_grammar = Grammar({"E", "T", "F"},
                                 {"a", "+"},
                                 {
                                     "E": ["E+T", "TF"],
                                     "T": ["T", "F"],
                                     "F": ["F", "a"]
                                 },
                                 "E")

        self.assertEqual(remove_unreachable_symbols.algorithm(tested_grammar), self.needed_grammar)

    def test_2_unreachable_non_terminals(self):
        g1 = Grammar({"E", "T", "J", "F"},
                     {"a", "+"},
                     {
                         "E": ["E+T", "TF"],
                         "T": ["T", "F"],
                         "F": ["F", "a"],
                         "J": ["J"]
                     },
                     "E")

        self.assertEqual(remove_unreachable_symbols.algorithm(g1), self.needed_grammar)

    def test_3_unreachable_terminals(self):
        g2 = Grammar({"E", "T", "F"},
                     {"a", "+", "d"},
                     {
                         "E": ["E"],
                         "T": ["T", "F"],
                         "F": ["F", "a"]
                     },
                     "E")

        g_needed2 = Grammar({"E"},
                            set(),
                            {"E": ["E"]},
                            "E")

        self.assertEqual(remove_unreachable_symbols.algorithm(g2), g_needed2)

class ChomskyNormalForm(unittest.TestCase):
    def test_1(self):
        g1 = Grammar({"E", "T", "F"},
                     {"a", "+", "d"},
                     {
                         "E": ["T"],
                         "T": ["dF", "FF"],
                         "F": ["d", "aa"]
                     },
                     "E")
        print(chomsky_normal_form.algorithm(g1))

    def test_2(self):
        g1 = Grammar({"E", "T", "F", "a'", "d'"},
                     {"a", "d"},
                     {
                         "E": ["T"],
                         "d'": ['d'],
                         'T': ["d'F", 'FF'],
                         'F': ['d', "a'a'"],
                         "a'": ['a']
                     },
                     "E")
        print(chomsky_normal_form.algorithm(g1))