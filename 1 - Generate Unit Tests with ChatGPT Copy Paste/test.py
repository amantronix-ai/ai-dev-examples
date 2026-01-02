import pytest

from calculator import add, divide
# Replace `your_module` with the actual filename (without .py)


# --------------------
# Tests for add()
# --------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (-5, -7, -12),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
        (1e10, 1e10, 2e10),
        ("foo", "bar", "foobar"),  # valid behavior for +
    ],
)
def test_add_valid_inputs(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        (1, "2"),
        (None, 3),
        ([1, 2], 3),
    ],
)
def test_add_invalid_inputs(a, b):
    with pytest.raises(TypeError):
        add(a, b)


# --------------------
# Tests for divide()
# --------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2),
        (-6, 3, -2),
        (5, 2, 2.5),
        (0, 5, 0),
        (1e10, 2, 5e9),
    ],
)
def test_divide_valid_inputs(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize(
    "a, b",
    [
        ("6", 3),
        (None, 1),
        (5, None),
    ],
)
def test_divide_invalid_inputs(a, b):
    with pytest.raises(TypeError):
        divide(a, b)
