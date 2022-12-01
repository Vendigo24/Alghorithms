from unittest import TestCase


class PrintCase(TestCase):
    def test_1(self):
        self.assertEqual(True, False)

    def test_2(self):
        self.assertEqual(True, True)

    def test_3(self):
        self.assertEqual(False, False)

    def test_4(self):
        self.assertEqual(False, True)
