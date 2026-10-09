import unittest
from scanner.port_scanner import validate_port_range


class TestPortScanner(unittest.TestCase):

    def test_valid_range(self):
        validate_port_range(1, 1024)

    def test_invalid_range(self):
        with self.assertRaises(ValueError):
            validate_port_range(1000, 100)

    def test_invalid_port(self):
        with self.assertRaises(ValueError):
            validate_port_range(0, 65536)


if __name__ == "__main__":
    unittest.main()