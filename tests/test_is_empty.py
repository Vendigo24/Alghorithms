import unittest
import grammar as gr


class MyTestCase(unittest.TestCase):
    def test_non_empty_language_created_by_grammar_with_no_change(self):
        grammar = gr.Grammar({'S', 'A', 'B'},
                             {'a', 'b'},
                             {'S': ['ABA', 'BAB'], 'A': ['aba'], 'B': ['bb']},
                             'S')
        self.assertEqual(grammar.is_empty(), (True, grammar))

    def test_non_empty_language_created_by_grammar_with_change(self):
        grammar = gr.Grammar({'S', 'A', 'B'},
                             {'a', 'b'},
                             {'S': ['ab', 'B'], 'A': ['aA'], 'B': ['bb']},
                             'S')
        self.assertEqual(grammar.is_empty(), (True, gr.Grammar({'S', 'B'},
                                                               {'a', 'b'},
                                                               {'S': ['ab', 'B'], 'B': ['bb']},
                                                               'S')))

    def test_non_empty_language_created_by_grammar(self):
        grammar = gr.Grammar({'S', 'A', 'B'},
                             {'a', 'b'},
                             {'S': ['A'], 'A': ['AA'], 'B': ['bB']},
                             'S')
        self.assertEqual(grammar.is_empty(), False)


if __name__ == '__main__':
    unittest.main()
