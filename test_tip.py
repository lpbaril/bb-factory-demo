import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from tip import main, tip


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = main(["tip.py", *args])
    return code, out.getvalue(), err.getvalue()


class TipTest(unittest.TestCase):
    def test_default_percent(self):
        self.assertAlmostEqual(tip(100, 15), 15.0)

    def test_custom_percent(self):
        self.assertAlmostEqual(tip(80, 20), 16.0)


class MainTest(unittest.TestCase):
    def test_no_split(self):
        self.assertEqual(run("100"), (0, "15.00\n", ""))
        self.assertEqual(run("80", "20"), (0, "16.00\n", ""))

    def test_split_default_percent(self):
        self.assertEqual(run("100", "--split", "4"), (0, "3.75\n", ""))

    def test_split_custom_percent_rounds_to_cents(self):
        self.assertEqual(run("80", "20", "--split", "3"), (0, "5.33\n", ""))

    def test_split_one(self):
        self.assertEqual(run("100", "--split", "1"), (0, "15.00\n", ""))

    def test_invalid_split(self):
        for args in (["0"], ["-2"], ["2.5"], ["abc"], []):
            with self.subTest(split=args):
                code, out, err = run("100", "--split", *args)
                self.assertEqual(code, 1)
                self.assertEqual(out, "")
                self.assertIn("--split needs a positive integer", err)


if __name__ == "__main__":
    unittest.main()
