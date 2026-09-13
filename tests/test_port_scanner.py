from scanner.port_scanner import validate_port_range


def test_valid_port_range():
    validate_port_range(1, 1024)


def test_invalid_start_port():
    try:
        validate_port_range(0, 1024)
        assert False
    except ValueError:
        pass


def test_invalid_end_port():
    try:
        validate_port_range(1, 70000)
        assert False
    except ValueError:
        pass


def test_reversed_port_range():
    try:
        validate_port_range(1000, 100)
        assert False
    except ValueError:
        pass