import pytest
from week01.stats import mean

def test_mean() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0

def test_mean_decimals() -> None:
    assert mean([0.1, 0.2]) == pytest.approx(0.15)

def test_negative_mean() -> None:
    assert mean([-0.1, -0.2]) == pytest.approx(-0.15)

def test_mean_empty_list() -> None:
    with pytest.raises(ValueError):
        mean([])