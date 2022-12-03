from unittest import TestCase
from grammar import Grammar
import algorithm_3
import algorithm_4


class RemoveLambdaRulesCase(TestCase):
    def test_1(self):
        g = Grammar(
            {"A", "B", "M", "N", "K", "S"},
            {"a", "b", "c", "p"},
            {
                "A": ["c", ""],
                "B": ["p", ""],
                "M": ["AB"],
                "N": ["Ab"],
                "K": ["ab"],
                "S": ["KNM"]
            },
            "S"
        )

        necessary_grammar = Grammar(
            {"A", "B", "M", "N", "K", "S"},
            {"a", "b", "c", "p"},
            {
                "A": ["c"],
                "B": ["p"],
                "M": ["AB", "A", "B"],
                "N": ["Ab", "b"],
                "K": ["ab"],
                "S": ["KNM", "KN"]
            },
            "S"
        )

        new_grammar = algorithm_4.remove_lambda_rules(g)

        self.assertEqual(new_grammar, necessary_grammar)

    def test_2(self):
        g = Grammar(
            {"S"},
            set(),
            {
                "S": [""]
            },
            "S"
        )

        necessary_grammar = Grammar(
            {"S"},
            set(),
            {
                "S": [""]
            },
            "S"
        )

        new_grammar = algorithm_4.remove_lambda_rules(g)

        self.assertEqual(new_grammar, necessary_grammar)

    def test_3(self):
        g = Grammar(
            {"S", "A"},
            {"a"},
            {
                "S": ["A"],
                "A": ["", "a"]
            },
            "S"
        )

        necessary_grammar = Grammar(
            {"S", "A", "S'"},
            {"a"},
            {
                "S'": ["", "S"],
                "S": ["A"],
                "A": ["a"]
            },
            "S'"
        )

        new_grammar = algorithm_4.remove_lambda_rules(g)

        self.assertEqual(new_grammar, necessary_grammar)


class RemoveUselessSymbols(TestCase):
    def test_1(self):
        g = Grammar(
            {"S", "A"},
            {"a"},
            {
                "S": ["A"],
                "A": ["", "a"]
            },
            "S"
        )

        necessary_grammar = Grammar(
            {"S", "A"},
            {"a"},
            {
                "S": ["A"],
                "A": ["", "a"]
            },
            "S"
        )

        new_grammar = algorithm_3.remove_useless_symbols(g)

        self.assertEqual(new_grammar, necessary_grammar)

    def test_2(self):
        g = Grammar(
            {"S"},
            set(),
            {
                "S": [""]
            },
            "S"
        )

        new_grammar = algorithm_3.remove_useless_symbols(g)

        self.assertEqual(new_grammar, None)

    def test_3(self):
        g = Grammar(
            {"E", "T", "F"},
            {"a", "+", "d"},
            {
                "E": ["E"],
                "T": ["T", "F"],
                "F": ["F", "a+"]
            },
            "E"
        )

        new_grammar = algorithm_3.remove_useless_symbols(g)

        self.assertEqual(new_grammar, None)
