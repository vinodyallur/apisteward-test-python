import unittest
from billing import bill


class TestBilling(unittest.TestCase):
    def test_uses_payment_method(self):
        self.assertEqual(bill(1000).get("payment_method"), "tok_visa")

    def test_old_source_removed(self):
        self.assertIsNone(bill(1000).get("source"))

    def test_amount(self):
        self.assertEqual(bill(2500)["amount"], 2500)

    def test_currency(self):
        self.assertEqual(bill(1000)["currency"], "usd")


if __name__ == "__main__":
    unittest.main()
