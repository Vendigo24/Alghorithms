from unittest import TestCase
from grammar import Grammar


class GetNTTFromRule(TestCase):
    def test_1(self):
        self.assertEqual(Grammar.get_ntt_from_rule("<error>TN+DF")[0], {"<error>", "T", "N", "+", "D", "F"})

    def test_2(self):
        self.assertEqual(Grammar.get_ntt_from_rule("error")[0], {"e", "r", "o"})

    def test_3(self):
        self.assertEqual(Grammar.get_ntt_from_rule(" ")[0], {" "})
