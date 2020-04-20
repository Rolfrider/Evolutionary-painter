import pytest
from rgba_rect import RGBARect
from unittest import mock


@pytest.fixture
def sut() -> RGBARect:
    return RGBARect(100, 100, 100, 100, 10, 10, 300, 300)


def test_weanWith(sut):
    otherRect = RGBARect(100, 100, 100, 100, 10, 10, 300, 300)
    result = sut.meanWith(otherRect)
    expected = RGBARect(100, 100, 100, 100, 10, 10, 300, 300)
    assert result.__dict__ == expected.__dict__


def test_mutateDeviation(sut):
    otherRect = RGBARect(2, 2, 2, 2, 2, 2, 2, 2)
    sut.mutateDeviation(otherRect)
    expected = RGBARect(200, 200, 200, 200, 20, 20, 600, 600)
    assert sut.__dict__ == expected.__dict__


def test_mutateRect(sut):
    with mock.patch("numpy.random.normal", return_value=1) as mock_numpy:
        otherRect = RGBARect(100, 100, 100, 100, 10, 10, 300, 300)
        sut.mutateRect(otherRect)
        expected = RGBARect(200, 200, 200, 200, 20, 20, 600, 600)
        assert sut.__dict__ == expected.__dict__


def test_interpolate(sut):
    otherRect = RGBARect(100, 100, 100, 100, 10, 10, 300, 300)
    result = sut.interpolate(otherRect, 0.5)
    expected = RGBARect(100, 100, 100, 100, 10, 10, 300, 300)
    assert result.__dict__ == expected.__dict__
