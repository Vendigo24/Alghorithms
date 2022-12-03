from unittest import TestCase
from grammar import Grammar
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
            {},
            {
                "S": [""]
            },
            "S"
        )

        necessary_grammar = Grammar(
            {"S"},
            {},
            {
                "S": [""]
            },
            "S"
        )

        new_grammar = algorithm_4.remove_lambda_rules(g)

        self.assertEqual(new_grammar, necessary_grammar)


