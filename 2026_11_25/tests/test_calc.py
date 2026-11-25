import unittest

from calc import divide


class TestCalcDivide(unittest.TestCase):
    def test_divide_positive_numbers(self) -> None:
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_negative_and_float(self) -> None:
        self.assertEqual(divide(-9, 3), -3.0)
        self.assertAlmostEqual(divide(1.5, 0.5), 3.0)

    def test_divide_by_zero_raises_value_error(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertEqual(str(ctx.exception), "除數不可為零")

    def test_divide_by_zero_float_raises_value_error(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0.0)
        self.assertEqual(str(ctx.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
