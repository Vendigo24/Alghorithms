# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from grammar import Grammar

g1 = Grammar({"E", "T", "J", "F"}, {"a", "+", "*", "d"}, {"E": ["E+T", "TF"], "T": ["T", "F"], "F": ["F", "a"], "J":["J+J"]}, "E")
print(g1)
print("###################################")
g2 = g1.is_empty()
print(g2)
print("###################################")
print(g1)