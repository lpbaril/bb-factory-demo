import unittest

from tip import tip


class TipTest(unittest.TestCase):
    def test_default_percent(self):
        self.assertAlmostEqual(tip(100, 15), 15.0)

    def test_custom_percent(self):
        self.assertAlmostEqual(tip(80, 20), 16.0)


if __name__ == "__main__":
    unittest.main()
